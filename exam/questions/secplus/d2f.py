"""Security+ SY0-701 practice questions — Domain 2 (Threats, Vulnerabilities,
and Mitigations), batch F.

43 scenario-driven questions (39 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 2 in
``_topic_labels.json``.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Threat actors (2.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A cloud data engineer, frustrated that the approved data-warehouse "
            "request has been stuck in procurement for six weeks, signs up for a "
            "third-party analytics SaaS platform on a personal credit card and "
            "loads a full export of customer records into it to meet a quarterly "
            "deadline. Months later, a researcher discovers the SaaS vendor left "
            "the dataset in a publicly readable storage bucket. The engineer had "
            "no intent to harm the company and believed they were solving a "
            "business problem. Which threat actor classification BEST describes "
            "the engineer's role in this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Shadow IT",
                "correct": True,
                "rationale": (
                    "Correct. An employee provisioning and using an unsanctioned, "
                    "unapproved technology platform outside IT's visibility and "
                    "governance — even with good intentions — is the definition of "
                    "shadow IT, and it is exactly this kind of ungoverned system "
                    "that produced the exposure."
                ),
            },
            {
                "id": "b",
                "text": "Malicious insider threat",
                "correct": False,
                "rationale": (
                    "Incorrect. Insider threat implies intent to harm the "
                    "organization or knowingly abuse authorized access; the "
                    "engineer acted without malicious intent and was trying to "
                    "meet a legitimate deadline."
                ),
            },
            {
                "id": "c",
                "text": "Organized crime",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no financially motivated criminal "
                    "enterprise here — the exposure resulted from an employee's "
                    "unauthorized tooling choice, not an external profit-seeking "
                    "group."
                ),
            },
            {
                "id": "d",
                "text": "Unskilled attacker",
                "correct": False,
                "rationale": (
                    "Incorrect. This term describes an external, low-skill "
                    "individual using off-the-shelf tools to attack a target; it "
                    "does not describe an internal employee's use of unsanctioned "
                    "business software."
                ),
            },
        ],
        "explanation": (
            "Provisioning and using technology outside IT's knowledge, approval, "
            "and security controls — regardless of intent — is shadow IT, and it "
            "is a recognized threat actor category because it creates ungoverned "
            "risk exactly like this exposure."
        ),
    },
    {
        "id": "nd2f-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "In the week before a multinational climate summit, several thousand "
            "internal emails from a chemical manufacturer are leaked to "
            "journalists, revealing that the company knowingly under-reported "
            "emissions data for years. The leak is timed to maximize media "
            "coverage during the summit, accompanied by a public statement "
            "condemning the company's 'corporate greenwashing.' No ransom is "
            "demanded, and no data is offered for sale. Which threat actor is "
            "MOST likely responsible?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hacktivist",
                "correct": True,
                "rationale": (
                    "Correct. An ideologically motivated leak, deliberately timed "
                    "to a public event to maximize reputational damage and "
                    "advance an environmental cause, with no financial demand, is "
                    "the defining signature of hacktivism."
                ),
            },
            {
                "id": "b",
                "text": "Organized crime",
                "correct": False,
                "rationale": (
                    "Incorrect. Organized crime groups monetize stolen data "
                    "through ransom or sale; this actor released the data for "
                    "free specifically to embarrass the company on ideological "
                    "grounds."
                ),
            },
            {
                "id": "c",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. Nation-state operations typically pursue "
                    "espionage or strategic advantage covertly; a public leak "
                    "timed to a climate summit with an explicit cause-driven "
                    "statement is inconsistent with that stealthy, strategic "
                    "profile."
                ),
            },
            {
                "id": "d",
                "text": "Insider threat acting for financial gain",
                "correct": False,
                "rationale": (
                    "Incorrect. The stem specifies no ransom or sale occurred and "
                    "the motive was explicitly a public environmental cause, not "
                    "personal profit — this points to ideology rather than "
                    "insider financial gain."
                ),
            },
        ],
        "explanation": (
            "A data leak released for free, timed to a public event, and framed "
            "around an explicit ideological cause with no financial demand is the "
            "hallmark of hacktivism."
        ),
    },
    # ------------------------------------------------------------------ #
    # Social engineering (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-003",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "An accounts-payable clerk receives a phone call that sounds exactly "
            "like the company's CFO, including the CFO's characteristic speech "
            "cadence and a background office noise the clerk recognizes. The "
            "caller urgently instructs the clerk to wire funds to a new vendor "
            "account before a board meeting. The clerk later learns the CFO was "
            "on a flight with no phone service at the stated call time. Security "
            "researchers confirm the audio was synthesized from publicly posted "
            "earnings-call recordings of the CFO's voice. Which technique BEST "
            "describes this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Vishing using AI-generated deepfake audio",
                "correct": True,
                "rationale": (
                    "Correct. This is a voice phone call (vishing) in which the "
                    "attacker used AI voice-cloning technology trained on public "
                    "recordings to synthesize a convincing deepfake of the CFO's "
                    "voice to pressure an urgent wire transfer."
                ),
            },
            {
                "id": "b",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. No email was used at any stage of this attack — "
                    "the entire interaction occurred over a synthesized phone "
                    "call."
                ),
            },
            {
                "id": "c",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting relies on a lookalike misspelled "
                    "domain name to lure victims to a fake website; no domain or "
                    "website was involved in this voice-based attack."
                ),
            },
            {
                "id": "d",
                "text": "Watering hole attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A watering hole attack compromises a website "
                    "frequently visited by the target to deliver malware; this "
                    "incident involved a synthesized voice call, not a "
                    "compromised website."
                ),
            },
        ],
        "explanation": (
            "A phone-based social engineering attack that uses AI-synthesized "
            "audio cloned from a real executive's voice to pressure an urgent "
            "financial action is vishing enhanced with deepfake technology, "
            "distinct from email-based BEC, domain-based typosquatting, or "
            "website-based watering hole attacks."
        ),
    },
    {
        "id": "nd2f-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "Customers report receiving an email that uses Amazon's exact logo, "
            "color scheme, and email footer formatting, claiming an order could "
            "not be delivered. The email links to \"amaz0n-support-center.net,\" "
            "a domain registered two days earlier that hosts a pixel-perfect "
            "clone of Amazon's login page. Which TWO techniques does this attack "
            "combine? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Typosquatting",
                "correct": True,
                "rationale": (
                    "Correct. Registering \"amaz0n-support-center.net\" — a "
                    "character-substituted lookalike of a real brand's domain — "
                    "to catch users who misread or misclick is typosquatting."
                ),
            },
            {
                "id": "b",
                "text": "Brand impersonation",
                "correct": True,
                "rationale": (
                    "Correct. Copying Amazon's exact logo, color scheme, and "
                    "formatting to make the email and login page appear to "
                    "genuinely originate from Amazon is brand impersonation."
                ),
            },
            {
                "id": "c",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. Pretexting involves a fabricated persona or "
                    "invented backstory used interactively against a specific "
                    "target; this is a mass, templated phishing email with no "
                    "personalized fabricated scenario."
                ),
            },
            {
                "id": "d",
                "text": "Watering hole attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No legitimate, frequently visited website was "
                    "compromised — the attacker built an entirely new, "
                    "attacker-controlled lookalike domain."
                ),
            },
            {
                "id": "e",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling targets specific senior executives; this "
                    "campaign was broadly sent to ordinary retail customers, not "
                    "narrowly targeted at high-value individuals."
                ),
            },
        ],
        "explanation": (
            "A lookalike misspelled domain paired with a pixel-perfect copy of a "
            "real brand's visual identity combines typosquatting (the domain "
            "trick) with brand impersonation (the visual deception) — it is not "
            "pretexting, a watering hole attack, or whaling."
        ),
    },
    # ------------------------------------------------------------------ #
    # Threat vectors and attack surfaces (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A regional chain of dental offices outsources printer fleet "
            "management to a single vendor that installs a remote-support agent "
            "on one workstation at each office for toner and maintenance alerts. "
            "An attacker compromises the vendor's central management portal and "
            "uses that single foothold to push ransomware simultaneously to "
            "every office in the chain through the same remote-support agent. "
            "Which attack surface was primarily exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A third-party vendor/supply chain relationship",
                "correct": True,
                "rationale": (
                    "Correct. The attacker never directly targeted any dental "
                    "office; instead they compromised a shared third-party "
                    "vendor management tool trusted across all client sites, "
                    "which is a supply chain attack surface."
                ),
            },
            {
                "id": "b",
                "text": "Removable media",
                "correct": False,
                "rationale": (
                    "Incorrect. No USB drive or removable storage device was "
                    "involved — the compromise propagated entirely through a "
                    "remote software agent."
                ),
            },
            {
                "id": "c",
                "text": "An unpatched public-facing web application",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a management portal "
                    "compromise that abused an existing trust relationship, not "
                    "an exploited web application vulnerability at the dental "
                    "offices themselves."
                ),
            },
            {
                "id": "d",
                "text": "Social engineering of front-desk staff",
                "correct": False,
                "rationale": (
                    "Incorrect. No employee at any office was tricked, phished, "
                    "or manipulated — the attack path went entirely through the "
                    "vendor's remote-management infrastructure."
                ),
            },
        ],
        "explanation": (
            "Compromising one shared, trusted third-party vendor tool to reach "
            "many otherwise-unrelated client organizations at once is a "
            "supply chain / vendor attack surface, not removable media, an "
            "application flaw at the victim sites, or social engineering."
        ),
    },
    {
        "id": "nd2f-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A researcher sits in an open-plan office lobby with a software-"
            "defined radio and captures the unencrypted 2.4 GHz signal between "
            "an executive's wireless keyboard/mouse USB receiver and the "
            "receiver dongle. The researcher demonstrates that crafted RF "
            "packets can be injected directly into the receiver, causing the "
            "target laptop to type attacker-chosen keystrokes without ever "
            "touching the keyboard. Which attack surface enabled this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An unencrypted wireless peripheral (keyboard/mouse RF) link",
                "correct": True,
                "rationale": (
                    "Correct. The wireless keyboard/mouse dongle communicates "
                    "over an unauthenticated, unencrypted proprietary RF "
                    "protocol, allowing nearby attackers to inject spoofed "
                    "keystroke packets directly into the receiver — an "
                    "often-overlooked wireless peripheral attack surface."
                ),
            },
            {
                "id": "b",
                "text": "A Bluetooth pairing vulnerability",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly describes a proprietary "
                    "2.4 GHz USB receiver dongle, not a Bluetooth pairing "
                    "session."
                ),
            },
            {
                "id": "c",
                "text": "A supply chain compromise of the laptop's firmware",
                "correct": False,
                "rationale": (
                    "Incorrect. No firmware was altered before or during "
                    "manufacturing or shipping; the attack exploited live radio "
                    "communication captured and injected in real time."
                ),
            },
            {
                "id": "d",
                "text": "Removable media autorun",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media was inserted into the "
                    "laptop — the entire attack occurred wirelessly over the "
                    "keyboard/mouse RF channel."
                ),
            },
        ],
        "explanation": (
            "Unencrypted, unauthenticated proprietary RF protocols used by "
            "wireless keyboard/mouse dongles are a real and exploitable "
            "wireless peripheral attack surface, distinct from Bluetooth, "
            "firmware supply chain, or removable media vectors."
        ),
    },
    # ------------------------------------------------------------------ #
    # Application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-007",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A gift-card redemption service first reads a card's remaining "
            "balance, then, in a separate later step, subtracts the requested "
            "amount and writes the new balance back to the database. A tester "
            "fires 200 simultaneous redemption requests against a single "
            "$50 gift card and successfully redeems over $4,000 in merchandise "
            "before the balance ever reaches zero. Which vulnerability was "
            "exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A race condition (time-of-check to time-of-use)",
                "correct": True,
                "rationale": (
                    "Correct. Because the balance check and the balance "
                    "deduction happen as two separate, non-atomic steps, "
                    "concurrent requests can all read the same 'sufficient "
                    "balance' state before any of them writes back a deduction — "
                    "a classic TOCTOU race condition."
                ),
            },
            {
                "id": "b",
                "text": "Integer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no evidence the balance value wrapped "
                    "around a numeric boundary; the issue is the timing gap "
                    "between checking and updating the balance under "
                    "concurrency."
                ),
            },
            {
                "id": "c",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. No serialized object or untrusted data structure "
                    "is being reconstructed by the application here — the flaw "
                    "is purely in the non-atomic check-then-act sequence."
                ),
            },
            {
                "id": "d",
                "text": "Memory leak",
                "correct": False,
                "rationale": (
                    "Incorrect. A memory leak causes gradual resource "
                    "exhaustion over time, not a logic flaw that lets a "
                    "financial balance be over-spent through concurrent "
                    "requests."
                ),
            },
        ],
        "explanation": (
            "Splitting a balance check and a balance deduction into two "
            "non-atomic operations creates a window that concurrent requests can "
            "exploit to redeem far more value than actually exists — a "
            "time-of-check to time-of-use race condition."
        ),
    },
    {
        "id": "nd2f-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A video-transcoding service reads a user-supplied 32-bit field from "
            "an uploaded file header that specifies frame width times height, "
            "then allocates a buffer sized to that value. A tester crafts a file "
            "with width and height values whose product exceeds the maximum "
            "value a 32-bit unsigned integer can hold, causing the calculation "
            "to wrap around to a very small number. The undersized buffer is "
            "then allocated, and the subsequent frame-copy routine writes far "
            "past its end, corrupting adjacent memory and achieving code "
            "execution. Which vulnerability chain does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Integer overflow leading to a buffer overflow",
                "correct": True,
                "rationale": (
                    "Correct. The width-by-height multiplication wraps around "
                    "(integer overflow) to a small value, causing an "
                    "undersized buffer to be allocated; the later copy routine "
                    "then writes beyond that buffer's bounds, producing a "
                    "classic overflow-driven memory corruption chain."
                ),
            },
            {
                "id": "b",
                "text": "A race condition between the allocation and the write",
                "correct": False,
                "rationale": (
                    "Incorrect. Timing and concurrency play no role here; the "
                    "flaw is a single-threaded arithmetic wraparound that "
                    "mis-sizes a buffer, not competing simultaneous requests."
                ),
            },
            {
                "id": "c",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. No serialized object graph is being "
                    "reconstructed from untrusted input; this is a numeric "
                    "calculation and memory-allocation flaw."
                ),
            },
            {
                "id": "d",
                "text": "A resource exhaustion (denial-of-service) flaw",
                "correct": False,
                "rationale": (
                    "Incorrect. The outcome described is memory corruption and "
                    "code execution from an undersized buffer, not gradual "
                    "resource depletion or service unavailability."
                ),
            },
        ],
        "explanation": (
            "An unchecked arithmetic calculation that wraps around to a small "
            "value, followed by a copy routine that overruns the resulting "
            "undersized buffer, is the textbook integer-overflow-to-"
            "buffer-overflow chain."
        ),
    },
    {
        "id": "nd2f-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "An internal reporting tool caches expensive query results using a "
            "Python object cache: results are serialized with the pickle module "
            "and stored, keyed by a hash the client supplies in a request "
            "header. A researcher discovers that submitting a crafted, "
            "attacker-built pickle byte stream under a guessed cache key causes "
            "the server to execute arbitrary shell commands the moment the "
            "cached object is loaded and deserialized on a later request. Which "
            "vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Insecure deserialization",
                "correct": True,
                "rationale": (
                    "Correct. Loading an attacker-supplied pickle byte stream "
                    "without validating or restricting what object types can be "
                    "reconstructed lets the attacker embed executable code that "
                    "runs automatically during deserialization — the defining "
                    "risk of insecure deserialization."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF tricks an authenticated user's browser "
                    "into submitting unwanted requests; this attack directly "
                    "supplies a malicious serialized payload to a server-side "
                    "cache, with no browser or victim session involved."
                ),
            },
            {
                "id": "c",
                "text": "Server-side request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF tricks a server into making unintended "
                    "outbound requests on the attacker's behalf; this attack "
                    "instead abuses object reconstruction from untrusted "
                    "serialized data to achieve code execution."
                ),
            },
            {
                "id": "d",
                "text": "Directory traversal",
                "correct": False,
                "rationale": (
                    "Incorrect. No file-path manipulation or attempt to escape "
                    "an intended directory is involved — the exploit is entirely "
                    "in how the untrusted cached object is reconstructed."
                ),
            },
        ],
        "explanation": (
            "Deserializing an attacker-controlled byte stream (such as a "
            "crafted Python pickle payload) without restricting object types "
            "allows embedded code to execute automatically on load — this is "
            "insecure deserialization, not CSRF, SSRF, or path traversal."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mobile vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A corporate mobile app stores the OAuth access and refresh tokens "
            "it receives from the SSO provider in a local SQLite database file "
            "in plaintext, with no operating-system keystore protection. A "
            "researcher connects the phone over USB, pulls an unencrypted "
            "application backup with a standard debugging tool, and extracts "
            "both tokens without ever unlocking the device or seeing the app's "
            "UI. Which mobile vulnerability does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Insecure local data storage",
                "correct": True,
                "rationale": (
                    "Correct. Persisting sensitive authentication tokens in "
                    "plaintext within an app's local database, unprotected by "
                    "the platform's secure keystore/keychain, allows them to be "
                    "recovered directly from a device backup — the definition of "
                    "insecure local data storage."
                ),
            },
            {
                "id": "b",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping involves an attacker fraudulently "
                    "porting a victim's phone number to a new SIM to intercept "
                    "calls and SMS; no carrier account or SIM was involved in "
                    "this local file extraction."
                ),
            },
            {
                "id": "c",
                "text": "Jailbreak/root detection bypass",
                "correct": False,
                "rationale": (
                    "Incorrect. The device was never jailbroken or rooted, and "
                    "no detection mechanism was bypassed — the tokens were "
                    "recoverable simply because the app itself stored them "
                    "insecurely."
                ),
            },
            {
                "id": "d",
                "text": "Bluetooth object exchange (OBEX) exploitation",
                "correct": False,
                "rationale": (
                    "Incorrect. No Bluetooth file-transfer protocol was used; "
                    "extraction occurred through a wired USB debugging backup of "
                    "the app's own local storage."
                ),
            },
        ],
        "explanation": (
            "Storing authentication tokens in plaintext in an app's local "
            "database instead of the platform's protected keystore lets them be "
            "recovered from a routine device backup — an insecure local data "
            "storage vulnerability, not SIM swapping, jailbreak bypass, or "
            "Bluetooth exploitation."
        ),
    },
    {
        "id": "nd2f-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A sales representative sideloads a free third-party keyboard app "
            "from outside the corporate MDM's approved catalog and grants it "
            "\"full access,\" including network permissions, to enable custom "
            "themes. Weeks later, security discovers the keyboard app has been "
            "silently transmitting every string typed on the device — including "
            "one-time MFA codes and corporate passwords — to a remote server. "
            "Which mobile vulnerability MOST directly enabled this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sideloading an application with excessive, unmanaged permissions",
                "correct": True,
                "rationale": (
                    "Correct. Installing an app from outside the MDM-approved "
                    "catalog and granting it broad, unreviewed permissions "
                    "(full keyboard access plus network access) allowed it to "
                    "capture and exfiltrate every keystroke, including MFA "
                    "codes."
                ),
            },
            {
                "id": "b",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. No carrier port-out or SIM reassignment "
                    "occurred; the data was captured directly by a "
                    "permission-abusing application already installed on the "
                    "device."
                ),
            },
            {
                "id": "c",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluesnarfing is unauthorized data theft over an "
                    "active Bluetooth connection; the exfiltration here occurred "
                    "through the keyboard app's own network permission, not a "
                    "Bluetooth exploit."
                ),
            },
            {
                "id": "d",
                "text": "A malicious QR code",
                "correct": False,
                "rationale": (
                    "Incorrect. The stem describes a deliberately sideloaded "
                    "app with granted permissions, not a scanned QR code "
                    "triggering an unwanted install or configuration."
                ),
            },
        ],
        "explanation": (
            "Bypassing the MDM-managed app catalog to sideload an app and "
            "grant it broad, unreviewed permissions is what let a malicious "
            "keyboard capture and exfiltrate keystrokes, including MFA codes — "
            "a sideloading/excessive-permission mobile vulnerability, not SIM "
            "swapping, Bluesnarfing, or a QR code attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A hypervisor administrator leaves a legacy shared-clipboard and "
            "drag-and-drop guest-integration feature enabled on a production "
            "host to make VM console troubleshooting more convenient. "
            "Researchers demonstrate that a crafted clipboard payload sent from "
            "within one guest VM triggers a flaw in the guest-tools driver, "
            "allowing arbitrary code to execute directly on the underlying "
            "hypervisor host, outside of any guest VM. Which vulnerability does "
            "this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VM escape",
                "correct": True,
                "rationale": (
                    "Correct. Code executing inside a guest VM breaking out to "
                    "run directly on the host hypervisor, by abusing a "
                    "guest-integration feature like shared clipboard, is the "
                    "definition of a VM escape."
                ),
            },
            {
                "id": "b",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. VM sprawl refers to unmanaged, forgotten virtual "
                    "machines accumulating without oversight; this scenario "
                    "describes an active code-execution exploit breaking guest "
                    "isolation, not an inventory management problem."
                ),
            },
            {
                "id": "c",
                "text": "Resource reuse (data remanence)",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource reuse involves recovering leftover data "
                    "from storage or memory reassigned to another tenant "
                    "without sanitization; here the attacker achieved active "
                    "code execution on the host, not passive data recovery."
                ),
            },
            {
                "id": "d",
                "text": "Live migration interception",
                "correct": False,
                "rationale": (
                    "Incorrect. No VM migration event or network capture is "
                    "described — the exploit occurred through a guest-tools "
                    "clipboard feature while the VM was running normally."
                ),
            },
        ],
        "explanation": (
            "Exploiting a hypervisor guest-integration feature to break out of "
            "a VM's isolation boundary and execute code directly on the host is "
            "a VM escape, distinct from VM sprawl, data remanence, or migration "
            "interception."
        ),
    },
    {
        "id": "nd2f-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A developer runs a container with the Docker daemon's Unix socket "
            "(/var/run/docker.sock) mounted inside it for a CI/CD build step. A "
            "penetration tester who compromises the containerized application "
            "uses that mounted socket to instruct the Docker daemon on the "
            "underlying host to launch a brand-new, fully privileged container "
            "with the host's root filesystem mounted inside it, giving the "
            "tester unrestricted control of the host itself. Which "
            "vulnerability does this scenario illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Container breakout via an exposed container-management interface",
                "correct": True,
                "rationale": (
                    "Correct. Mounting the host's Docker socket inside a "
                    "container hands that container the ability to control the "
                    "host's container engine directly; an attacker who "
                    "compromises the container can use that socket to spawn a "
                    "privileged container and escape to full host control."
                ),
            },
            {
                "id": "b",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not about unmanaged, forgotten "
                    "instances accumulating over time — it is an active "
                    "privilege-escalation exploit using an intentionally "
                    "mounted management interface."
                ),
            },
            {
                "id": "c",
                "text": "Resource reuse (data remanence)",
                "correct": False,
                "rationale": (
                    "Incorrect. No leftover data from a prior tenant or "
                    "workload was recovered; the attacker actively commanded "
                    "the host's container engine to create a new privileged "
                    "container."
                ),
            },
            {
                "id": "d",
                "text": "A side-channel timing attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No indirect measurement of shared hardware "
                    "resources (cache timing, power draw, etc.) was used — the "
                    "attacker directly issued commands to the exposed Docker "
                    "socket."
                ),
            },
        ],
        "explanation": (
            "Mounting a host's container-management socket inside a container "
            "gives any process that compromises that container a direct path "
            "to command the host's container engine and escalate to full host "
            "compromise — a container breakout, not VM sprawl, data remanence, "
            "or a side-channel attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Vulnerability scan and assessment result classification (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A vulnerability scanner flags a Linux mail server as critically "
            "vulnerable to a known remote code execution flaw, based entirely "
            "on the version string reported in the service's banner. The "
            "system administrator confirms that the distribution's maintainers "
            "backported the security fix into that exact package version "
            "without incrementing the version number displayed in the banner, "
            "and manual exploitation attempts against the live server fail. How "
            "should this finding be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False positive",
                "correct": True,
                "rationale": (
                    "Correct. The scanner flagged a vulnerability based solely "
                    "on an outdated version string, but the underlying flaw was "
                    "actually already patched (backported); since the server is "
                    "not actually exploitable, the finding is a false positive."
                ),
            },
            {
                "id": "b",
                "text": "True positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A true positive requires the reported "
                    "vulnerability to actually exist; manual exploitation "
                    "attempts failed, confirming the server was not actually "
                    "vulnerable despite the version banner."
                ),
            },
            {
                "id": "c",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative describes a real vulnerability "
                    "that the scanner failed to detect; here the scanner did "
                    "flag something, and that flag turned out to be inaccurate — "
                    "the opposite situation."
                ),
            },
            {
                "id": "d",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative means the scanner correctly "
                    "reported no vulnerability; here the scanner did report a "
                    "vulnerability, which was then disproven through manual "
                    "verification."
                ),
            },
        ],
        "explanation": (
            "Banner-based version detection can be misled when a vendor "
            "backports a security fix without changing the displayed version "
            "string; manual verification disproving exploitability confirms the "
            "scanner's flag was a false positive."
        ),
    },
    {
        "id": "nd2f-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A scan reports a CVSS v3.1 base score of 9.8 (Critical) for an "
            "unauthenticated remote code execution flaw on an internal "
            "application server. The analyst calculates the environmental "
            "score after accounting for the organization's actual deployment: "
            "the server sits on a physically air-gapped lab network with no "
            "route to the corporate network or internet, and only two "
            "authorized engineers have physical access to that lab. Which "
            "action reflects the BEST use of this environmental context?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Re-prioritize remediation using the environmentally "
                    "adjusted score while still tracking the finding for "
                    "eventual patching"
                ),
                "correct": True,
                "rationale": (
                    "Correct. CVSS environmental scoring exists precisely to "
                    "reflect real-world exposure and compensating controls; "
                    "since the server is air-gapped with severely restricted "
                    "access, the effective risk is far lower than the base "
                    "score suggests, so remediation can be reprioritized "
                    "behind more exposed findings without dropping it "
                    "entirely."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Dismiss the finding as a false positive since the base "
                    "score does not match observed risk"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The vulnerability itself is real and confirmed; "
                    "the environmental score adjusts prioritization based on "
                    "exposure, it does not mean the flaw doesn't actually "
                    "exist."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Treat it as an emergency requiring immediate off-hours "
                    "patching identical to an internet-facing critical finding"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Applying the same urgency as an internet-facing "
                    "critical vulnerability ignores the compensating "
                    "controls (air gap, restricted physical access) that "
                    "substantially reduce real-world exploitability."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ignore the finding entirely since it is on an internal "
                    "network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Internal placement reduces but does not "
                    "eliminate risk (insider threat, physical access); the "
                    "finding should be reprioritized and eventually remediated, "
                    "not ignored outright."
                ),
            },
        ],
        "explanation": (
            "CVSS environmental scoring is designed to adjust the base score "
            "using real deployment context such as network exposure and "
            "compensating controls; the correct response is to reprioritize — "
            "not dismiss, over-escalate, or ignore — the finding based on that "
            "adjusted risk."
        ),
    },
    # ------------------------------------------------------------------ #
    # Web application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A profile-update API accepts a JSON body and binds every field in "
            "the request directly to the corresponding column in the user's "
            "database record without an explicit allow-list of editable "
            "fields. A tester who is logged in as an ordinary user adds "
            "\"\\\"role\\\": \\\"admin\\\"\" to their own profile-update JSON "
            "payload — a field never exposed in the UI — and their account is "
            "immediately elevated to administrator. Which vulnerability does "
            "this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mass assignment",
                "correct": True,
                "rationale": (
                    "Correct. The API blindly binds every client-supplied JSON "
                    "field to the underlying data model instead of restricting "
                    "which fields a client may set, letting the tester set an "
                    "unexposed, sensitive field (role) on their own record — the "
                    "definition of a mass assignment vulnerability."
                ),
            },
            {
                "id": "b",
                "text": "Insecure direct object reference (IDOR)",
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR involves accessing or modifying a "
                    "different user's object by manipulating a referenced "
                    "identifier; here the tester modified fields on their own "
                    "account, not another user's record."
                ),
            },
            {
                "id": "c",
                "text": "Cross-site request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF tricks a victim's browser into submitting "
                    "an unwanted request using their existing session; here the "
                    "tester deliberately and directly crafted their own "
                    "request."
                ),
            },
            {
                "id": "d",
                "text": "SQL injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No malformed SQL syntax or database query "
                    "manipulation is involved — the API's own binding logic "
                    "legitimately wrote the attacker-supplied field to the "
                    "database exactly as designed, just without restriction."
                ),
            },
        ],
        "explanation": (
            "Automatically binding every client-supplied field to a data model "
            "without an allow-list lets an attacker set fields the UI never "
            "exposes, such as a role field — mass assignment, distinct from "
            "IDOR (which targets another user's object), CSRF (which forges a "
            "victim's request), or SQL injection (which manipulates a query)."
        ),
    },
    {
        "id": "nd2f-017",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A single-page application's API responds to cross-origin requests "
            "with the header \"Access-Control-Allow-Origin: *\" alongside "
            "\"Access-Control-Allow-Credentials: true.\" A researcher hosts a "
            "malicious page on an unrelated domain that issues a background "
            "request to the API using a victim's existing authenticated "
            "session cookie and successfully reads the JSON response — "
            "including the victim's account balance — directly in JavaScript "
            "running on the attacker's page. Which vulnerability allowed this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Insecure CORS configuration (wildcard origin with credentials)",
                "correct": True,
                "rationale": (
                    "Correct. Combining a wildcard \"Allow-Origin: *\" with "
                    "\"Allow-Credentials: true\" lets any external site read the "
                    "authenticated API response in JavaScript on behalf of a "
                    "logged-in victim — a misconfigured, overly permissive CORS "
                    "policy."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF causes an unwanted state-changing action to "
                    "be submitted; here the attacker's page directly read the "
                    "response body of the request, which CSRF alone does not "
                    "permit — that read access came from the permissive CORS "
                    "headers."
                ),
            },
            {
                "id": "c",
                "text": "Reflected cross-site scripting",
                "correct": False,
                "rationale": (
                    "Incorrect. No unsanitized input was reflected back into the "
                    "API's own page and executed; the malicious script ran "
                    "entirely on the attacker's own separate domain."
                ),
            },
            {
                "id": "d",
                "text": "Clickjacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Clickjacking tricks a user into clicking a "
                    "hidden, overlaid element; this attack involved a background "
                    "script reading cross-origin API data, with no user "
                    "interaction or invisible overlay involved."
                ),
            },
        ],
        "explanation": (
            "A wildcard CORS origin combined with credentialed requests allows "
            "any external site's JavaScript to read an authenticated user's "
            "API responses — an insecure CORS configuration, distinct from "
            "CSRF (which cannot read responses), reflected XSS (no injected "
            "script on the vulnerable site), or clickjacking (no UI overlay)."
        ),
    },
    {
        "id": "nd2f-018",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A front-end reverse proxy enforces a web application firewall "
            "policy before forwarding requests to a back-end application "
            "server. A researcher submits a single HTTP request containing "
            "both a \"Content-Length\" header and a conflicting "
            "\"Transfer-Encoding: chunked\" header. The front-end proxy and the "
            "back-end server parse the conflicting headers differently, "
            "causing part of the request body to be interpreted by the back "
            "end as the start of an entirely separate, second request that "
            "bypasses the WAF's inspection and reaches an internal-only admin "
            "endpoint. Which vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "HTTP request smuggling",
                "correct": True,
                "rationale": (
                    "Correct. Exploiting inconsistent parsing of conflicting "
                    "Content-Length and Transfer-Encoding headers between a "
                    "front-end proxy and back-end server to smuggle a hidden "
                    "second request past inspection is the defining mechanism "
                    "of HTTP request smuggling."
                ),
            },
            {
                "id": "b",
                "text": "Server-side request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF tricks a server into making an unintended "
                    "outbound request on the attacker's behalf; here the "
                    "attacker's single crafted request is being split and "
                    "misparsed to smuggle a hidden inbound request, not to "
                    "trigger an outbound one."
                ),
            },
            {
                "id": "c",
                "text": "XML external entity (XXE) injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No XML document or external entity declaration "
                    "is involved; the exploit abuses conflicting HTTP header "
                    "parsing behavior between two different servers."
                ),
            },
            {
                "id": "d",
                "text": "Cross-site request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF relies on a victim's browser submitting an "
                    "unwanted authenticated request; this attack is a "
                    "server-to-server HTTP parsing discrepancy with no victim "
                    "browser or session involved."
                ),
            },
        ],
        "explanation": (
            "Ambiguous, conflicting Content-Length and Transfer-Encoding "
            "headers parsed differently by a front-end proxy and a back-end "
            "server allow an attacker to smuggle a hidden request past "
            "security controls — HTTP request smuggling, not SSRF, XXE, or "
            "CSRF."
        ),
    },
    # ------------------------------------------------------------------ #
    # Authentication factors and protocols (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-019",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "A network team wants junior administrators to be able to run "
            "read-only \"show\" commands on core switches but be blocked from "
            "running any \"configure\" commands, with every individual command "
            "attempt logged to a central AAA server for audit. Which "
            "authentication protocol BEST supports this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TACACS+",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ separates authentication, authorization, "
                    "and accounting and can authorize (or deny) individual "
                    "commands on network devices, logging each command attempt "
                    "centrally — exactly the granular, per-command control "
                    "required here."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS combines authentication and "
                    "authorization into a single response and encrypts only the "
                    "password in transit; it does not natively support "
                    "per-command authorization on network devices."
                ),
            },
            {
                "id": "c",
                "text": "Kerberos",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos provides ticket-based single sign-on "
                    "authentication for a domain environment; it is not designed "
                    "for granular, per-command authorization on network device "
                    "CLIs."
                ),
            },
            {
                "id": "d",
                "text": "CHAP",
                "correct": False,
                "rationale": (
                    "Incorrect. CHAP is a challenge-response authentication "
                    "protocol used to verify identity over a link, such as PPP; "
                    "it has no concept of command-level authorization or "
                    "centralized command auditing."
                ),
            },
        ],
        "explanation": (
            "TACACS+'s separation of authentication, authorization, and "
            "accounting, along with its support for per-command authorization "
            "on network devices, makes it the standard choice for granular "
            "administrative command control — unlike RADIUS, Kerberos, or "
            "CHAP."
        ),
    },
    {
        "id": "nd2f-020",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "A phone's screen-unlock is configured to use two-dimensional "
            "facial recognition with liveness detection disabled for faster "
            "unlocking. A colleague holds up a high-resolution printed photo "
            "of the phone's owner in front of the camera, and the device "
            "unlocks immediately. Which authentication weakness does this "
            "demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A biometric (\"something you are\") factor being spoofed "
                    "due to missing liveness detection"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Facial recognition is a biometric factor, and "
                    "without liveness detection (checks for blinking, depth, or "
                    "motion), a static two-dimensional photo can successfully "
                    "impersonate the legitimate user's face."
                ),
            },
            {
                "id": "b",
                "text": "MFA fatigue (push bombing)",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA fatigue involves flooding a user with "
                    "repeated push notifications until one is approved; no "
                    "push prompts or a second authenticated party approving "
                    "requests is involved here — a single biometric check was "
                    "spoofed directly."
                ),
            },
            {
                "id": "c",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing reuses previously breached "
                    "username/password pairs against other services; no "
                    "password or credential database was involved in this "
                    "photo-based unlock."
                ),
            },
            {
                "id": "d",
                "text": "Token replay",
                "correct": False,
                "rationale": (
                    "Incorrect. Token replay involves capturing and reusing a "
                    "previously issued authentication token or session "
                    "artifact; this attack directly spoofed the biometric "
                    "sensor itself with a photograph, not a captured token."
                ),
            },
        ],
        "explanation": (
            "Disabling liveness detection on a facial-recognition unlock lets "
            "a static photo satisfy a \"something you are\" biometric factor — "
            "a spoofing weakness distinct from MFA fatigue, credential "
            "stuffing, or token replay."
        ),
    },
    {
        "id": "nd2f-021",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "A corporate intranet login form builds an LDAP search filter by "
            "directly concatenating the submitted username into a query "
            "string: \"(&(uid=<input>)(userPassword=<input>))\". A tester "
            "submits a username of \"*)(uid=*))(|(uid=*\" with any password "
            "and is authenticated as the first account returned by the "
            "directory, without knowing any valid credentials. Which "
            "vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "LDAP injection",
                "correct": True,
                "rationale": (
                    "Correct. Concatenating unsanitized user input directly "
                    "into an LDAP search filter allows an attacker to inject "
                    "wildcard and logical operators that rewrite the query's "
                    "meaning, bypassing the intended authentication check — "
                    "LDAP injection."
                ),
            },
            {
                "id": "b",
                "text": "Pass-the-hash",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash reuses a captured password hash "
                    "to authenticate without knowing the plaintext password; "
                    "this attack instead manipulates the syntax of the LDAP "
                    "query itself, with no hash captured or reused."
                ),
            },
            {
                "id": "c",
                "text": "Kerberoasting",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberoasting extracts and offline-cracks "
                    "service account password hashes from Kerberos service "
                    "tickets; no Kerberos ticket request or offline cracking is "
                    "involved in this LDAP filter manipulation."
                ),
            },
            {
                "id": "d",
                "text": "A brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Brute forcing involves systematically guessing "
                    "many credential combinations; the tester succeeded on the "
                    "first attempt by exploiting query syntax, not by guessing "
                    "a password."
                ),
            },
        ],
        "explanation": (
            "Unsanitized input concatenated directly into an LDAP filter lets "
            "an attacker inject wildcard/logical operators to bypass the "
            "authentication check entirely — LDAP injection, not "
            "pass-the-hash, Kerberoasting, or brute forcing."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cryptographic attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-022",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A developer encrypts a bitmap image using AES in ECB mode, where "
            "each identical 16-byte plaintext block always produces the "
            "identical ciphertext block. When the resulting ciphertext is "
            "rendered as an image, the original picture's outline and shapes "
            "remain clearly visible, even though the pixel values themselves "
            "are encrypted. Which weakness explains this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "ECB mode's lack of diffusion between identical plaintext "
                    "blocks"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because ECB mode encrypts each block "
                    "independently with no chaining or randomization, "
                    "identical plaintext blocks always map to identical "
                    "ciphertext blocks, preserving visible patterns in the "
                    "underlying data — the well-known ECB weakness."
                ),
            },
            {
                "id": "b",
                "text": "A birthday attack against the encryption key",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack exploits hash collision "
                    "probability, not a block cipher's mode of operation; no "
                    "hash function or collision search is involved here."
                ),
            },
            {
                "id": "c",
                "text": "A downgrade attack forcing a weaker cipher suite",
                "correct": False,
                "rationale": (
                    "Incorrect. AES itself is a strong cipher and was not "
                    "downgraded to anything weaker; the flaw lies entirely in "
                    "the chosen mode of operation (ECB), not the algorithm's "
                    "strength."
                ),
            },
            {
                "id": "d",
                "text": "A padding oracle attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A padding oracle attack abuses distinguishable "
                    "error responses during decryption to recover plaintext "
                    "incrementally; no decryption error behavior is described "
                    "here — the issue is pattern leakage from encrypting "
                    "identical blocks identically."
                ),
            },
        ],
        "explanation": (
            "ECB mode encrypts identical plaintext blocks into identical "
            "ciphertext blocks with no diffusion, which is why encrypted "
            "images in ECB mode still visibly reveal the original picture's "
            "structure — a mode-of-operation weakness distinct from birthday, "
            "downgrade, or padding oracle attacks."
        ),
    },
    {
        "id": "nd2f-023",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A researcher captures traffic on a legacy WEP-protected wireless "
            "network and observes that its 24-bit initialization vector (IV) "
            "space is small enough that IVs begin repeating after collecting "
            "roughly five thousand packets on a busy access point. By "
            "collecting frames that reuse the same IV (and therefore the same "
            "RC4 keystream), the researcher XORs pairs of ciphertexts together "
            "to recover portions of the plaintext without ever learning the "
            "shared key. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A keystream-reuse (IV collision) attack against RC4",
                "correct": True,
                "rationale": (
                    "Correct. WEP's short 24-bit IV space causes IV reuse on "
                    "busy networks, which causes the RC4 keystream to repeat; "
                    "XORing two ciphertexts encrypted with the same keystream "
                    "cancels the keystream out and recovers a XOR of the two "
                    "plaintexts, exposing message content without recovering "
                    "the key directly."
                ),
            },
            {
                "id": "b",
                "text": "A birthday attack against the WEP key",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack targets hash collisions "
                    "based on probability across a large search space; this "
                    "attack instead exploits WEP's IV field being too small to "
                    "avoid keystream reuse, a design flaw rather than a "
                    "probabilistic hash collision search."
                ),
            },
            {
                "id": "c",
                "text": "A downgrade attack forcing a weaker protocol version",
                "correct": False,
                "rationale": (
                    "Incorrect. No protocol negotiation or forced fallback to "
                    "an older standard occurred; WEP was already the protocol "
                    "in use, and the flaw exploited is IV/keystream reuse "
                    "inherent to WEP itself."
                ),
            },
            {
                "id": "d",
                "text": "A padding oracle attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Padding oracle attacks rely on distinguishable "
                    "decryption error messages to recover plaintext block by "
                    "block; this attack instead directly XORs captured "
                    "ciphertexts that share a reused RC4 keystream."
                ),
            },
        ],
        "explanation": (
            "WEP's short IV space causes RC4 keystream reuse, and XORing "
            "ciphertexts that share a keystream cancels it out to reveal "
            "plaintext — a keystream-reuse attack, distinct from a birthday "
            "attack, a downgrade attack, or a padding oracle attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Indicators of malicious activity (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-024",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A DNS server's query logs show a single internal workstation "
            "issuing thousands of DNS TXT record queries per hour to "
            "subdomains of a single external domain, with each subdomain label "
            "consisting of 60+ characters of seemingly random alphanumeric "
            "text. No other workstation queries that domain, and the "
            "workstation's normal web browsing traffic looks unremarkable. "
            "Which indicator of compromise is MOST consistent with this "
            "activity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DNS tunneling used for covert data exfiltration",
                "correct": True,
                "rationale": (
                    "Correct. A high volume of TXT queries to long, "
                    "high-entropy, randomly generated subdomain labels under a "
                    "single attacker-controlled domain is the classic signature "
                    "of DNS tunneling, which encodes stolen data into DNS query "
                    "traffic to slip past controls that don't inspect DNS "
                    "closely."
                ),
            },
            {
                "id": "b",
                "text": "A distributed denial-of-service amplification attack",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS amplification abuses open resolvers to "
                    "flood a victim with large response traffic from many "
                    "sources; this scenario shows one internal host generating "
                    "outbound queries to one external domain, not inbound flood "
                    "traffic from many resolvers."
                ),
            },
            {
                "id": "c",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting relies on a lookalike misspelled "
                    "domain name to trick a user visually; the domain names "
                    "here are random, high-entropy subdomain labels used to "
                    "encode data, not a deceptive lookalike brand name."
                ),
            },
            {
                "id": "d",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. Impossible travel refers to authentication "
                    "events from geographically implausible locations in too "
                    "short a time; this scenario involves DNS query patterns "
                    "from a single workstation, with no login or geolocation "
                    "data described."
                ),
            },
        ],
        "explanation": (
            "A high volume of high-entropy TXT queries to a single external "
            "domain from one host is the classic pattern of DNS tunneling used "
            "for covert exfiltration, not amplification DDoS, typosquatting, "
            "or impossible travel."
        ),
    },
    {
        "id": "nd2f-025",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A forensic timeline reconstruction of a compromised domain "
            "controller shows the following, all within a nine-minute window: "
            "(1) Windows Security event ID 1102 — \"The audit log was "
            "cleared\" — logged under a service account that has never "
            "interactively logged on before; (2) PowerShell's console history "
            "file (ConsoleHost_history.txt) for that same session was deleted "
            "immediately afterward; (3) no other suspicious authentication "
            "events appear before or after in the surviving logs. Which TWO "
            "conclusions are BEST supported by this evidence? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The attacker performed anti-forensic log tampering to cover their tracks",
                "correct": True,
                "rationale": (
                    "Correct. Deliberately clearing the security audit log "
                    "(event ID 1102) is a direct, well-documented anti-forensic "
                    "technique used to erase evidence of prior malicious "
                    "activity."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The command history was intentionally destroyed to hide "
                    "the specific commands the attacker executed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Deleting the PowerShell console history "
                    "immediately after clearing the audit log indicates a "
                    "deliberate effort to prevent investigators from "
                    "reconstructing exactly which commands were run during the "
                    "session."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The absence of other suspicious events proves no earlier "
                    "compromise occurred"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The absence of other suspicious events is "
                    "explained by the log clearing itself — evidence of an "
                    "earlier compromise may simply have been erased, not "
                    "proven absent."
                ),
            },
            {
                "id": "d",
                "text": "This activity indicates normal scheduled log rotation",
                "correct": False,
                "rationale": (
                    "Incorrect. Routine log rotation does not generate event ID "
                    "1102 (a manual/explicit clear action) paired with targeted "
                    "deletion of one session's command history — this is "
                    "deliberate tampering, not automated maintenance."
                ),
            },
            {
                "id": "e",
                "text": "The service account credentials were definitely phished via email",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the evidence describes how the "
                    "credentials were originally obtained; the timeline only "
                    "shows post-compromise log-clearing behavior, not the "
                    "initial access vector."
                ),
            },
        ],
        "explanation": (
            "A cleared audit log paired with deleted command history in the "
            "same session is textbook anti-forensic evidence tampering meant "
            "to erase both the record of the event and the specific commands "
            "run — it does not prove no earlier compromise occurred, does not "
            "reflect routine log rotation, and says nothing about how "
            "credentials were originally obtained."
        ),
    },
    {
        "id": "nd2f-026",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Firewall logs from an infected workstation show DNS queries for "
            "several hundred distinct, algorithmically generated domain names "
            "per day — strings such as \"xqzplv4k.net\" and \"vbhtmn9r.com\" — "
            "the overwhelming majority of which fail to resolve (NXDOMAIN). "
            "Roughly once every few days, one of these domains does resolve, "
            "and the workstation immediately establishes an outbound HTTPS "
            "connection to it. Which indicator does this activity MOST "
            "strongly suggest?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A domain generation algorithm (DGA) being used for "
                    "command-and-control"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Malware that generates a large number of "
                    "pseudo-random candidate domains and queries them daily, "
                    "expecting most to fail until the operator registers one to "
                    "activate, is the defining behavior of a domain generation "
                    "algorithm used for resilient C2 infrastructure."
                ),
            },
            {
                "id": "b",
                "text": "A DNS amplification attack originating from the workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS amplification abuses open resolvers to "
                    "flood a third-party victim with large responses; this "
                    "workstation is issuing lookups for itself, not spoofing "
                    "requests to flood another target."
                ),
            },
            {
                "id": "c",
                "text": "Legitimate content delivery network (CDN) load balancing",
                "correct": False,
                "rationale": (
                    "Incorrect. CDN load balancing does not produce hundreds of "
                    "daily lookups to random alphanumeric domains that "
                    "overwhelmingly fail to resolve — that pattern is "
                    "consistent with malware probing for an active C2 domain, "
                    "not normal content delivery."
                ),
            },
            {
                "id": "d",
                "text": "A typosquatting campaign targeting the organization",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting uses a small number of deliberate "
                    "lookalike domains aimed at tricking users, not hundreds of "
                    "random, algorithmically generated candidate domains "
                    "queried automatically by infected software."
                ),
            },
        ],
        "explanation": (
            "A high volume of random-looking candidate domains that mostly "
            "fail to resolve, with occasional successful resolutions "
            "triggering an outbound connection, is the classic fingerprint of "
            "a domain generation algorithm used for resilient malware C2, not "
            "amplification DDoS, CDN behavior, or typosquatting."
        ),
    },
    # ------------------------------------------------------------------ #
    # Log sources and investigative questions (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-027",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "An executive suspects a competitor obtained a confidential "
            "product roadmap. The organization's email gateway logs show no "
            "large attachments were sent externally, and the web proxy logs "
            "show only routine browsing from the executive's workstation. "
            "Investigators need to determine whether the roadmap document "
            "actually left the network by any channel and, if so, how much "
            "data was transferred. Which log source is BEST suited to answer "
            "this specific question?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Firewall/DLP traffic logs showing outbound connection "
                    "volume and destination"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Firewall and DLP traffic logs record the volume "
                    "and destination of outbound data across all channels "
                    "(not just email or standard web browsing), making them the "
                    "right source to confirm whether — and how much — data left "
                    "the network, including through less obvious channels like "
                    "personal cloud storage or non-standard ports."
                ),
            },
            {
                "id": "b",
                "text": "Email gateway logs alone",
                "correct": False,
                "rationale": (
                    "Incorrect. Email logs only cover data sent through the "
                    "corporate mail system; they have already been checked and "
                    "cannot reveal exfiltration through other channels like "
                    "cloud storage uploads or USB transfer."
                ),
            },
            {
                "id": "c",
                "text": "DHCP lease logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs record IP address assignments to "
                    "devices on the network; they contain no information about "
                    "data volume or destination of outbound transfers."
                ),
            },
            {
                "id": "d",
                "text": "Print spooler logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Print logs would only be relevant if physical "
                    "printing were suspected; the investigative question here "
                    "is specifically about digital exfiltration of data leaving "
                    "the network."
                ),
            },
        ],
        "explanation": (
            "Because email and standard web-browsing logs already came back "
            "clean, the question of whether data left through any channel and "
            "how much requires firewall/DLP traffic logs, which capture "
            "outbound volume and destination across all channels — not DHCP "
            "or print logs, which don't address exfiltration at all."
        ),
    },
    {
        "id": "nd2f-028",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "A shared kiosk workstation in a warehouse is used by rotating "
            "shift employees who each log in with individual domain "
            "accounts. Malware was launched from that workstation at 2:47 "
            "p.m. Investigators need to determine exactly which employee's "
            "account was logged on to the workstation at that specific "
            "timestamp. Which log source will answer this question?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The domain controller's security event log (logon/logoff "
                    "events)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Security event logs on the domain controller "
                    "(and locally on the workstation) record which account "
                    "logon and logoff events occurred and when, directly "
                    "answering which user was authenticated to the machine at "
                    "the time in question."
                ),
            },
            {
                "id": "b",
                "text": "The malware's own file-creation timestamp metadata",
                "correct": False,
                "rationale": (
                    "Incorrect. File timestamps can indicate when a file was "
                    "created or modified but do not by themselves identify "
                    "which user account was actively logged on to the machine "
                    "at that moment."
                ),
            },
            {
                "id": "c",
                "text": "DNS resolver cache logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs record name resolution requests, not "
                    "user authentication or session activity on a specific "
                    "workstation."
                ),
            },
            {
                "id": "d",
                "text": "Switch port VLAN assignment logs",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN assignment logs describe network "
                    "segmentation configuration for a switch port, not which "
                    "user account was logged on to a device at a given time."
                ),
            },
        ],
        "explanation": (
            "Identifying which specific user account was active on a shared "
            "workstation at a precise timestamp is exactly what authentication "
            "(logon/logoff) security event logs are designed to answer — file "
            "metadata, DNS logs, and VLAN logs do not capture that "
            "information."
        ),
    },
    {
        "id": "nd2f-029",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "An EDR alert confirms a malicious PowerShell process ran on an "
            "endpoint but does not display the full command that was "
            "executed. Investigators need to recover the exact, complete "
            "command-line arguments — including any Base64-encoded payload — "
            "that were passed when the process was launched. Which log "
            "source is BEST suited to provide this detail?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Endpoint process-creation telemetry (such as Sysmon "
                    "Event ID 1 or EDR process logs) with command-line "
                    "logging enabled"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Process-creation telemetry sources like Sysmon "
                    "Event ID 1 or full EDR process logs specifically capture "
                    "the complete command line used to launch a process, "
                    "including any encoded or obfuscated arguments."
                ),
            },
            {
                "id": "b",
                "text": "Firewall connection logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs record network connection "
                    "metadata such as source/destination IP and port, not the "
                    "command-line arguments used to launch a local process."
                ),
            },
            {
                "id": "c",
                "text": "DHCP lease logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs track IP address assignment and have "
                    "no visibility into process execution details on an "
                    "endpoint."
                ),
            },
            {
                "id": "d",
                "text": "Print spooler logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Print logs are unrelated to process execution "
                    "and would not contain PowerShell command-line data."
                ),
            },
        ],
        "explanation": (
            "Recovering the exact command-line arguments (including encoded "
            "payloads) used to launch a malicious process requires endpoint "
            "process-creation telemetry such as Sysmon or EDR process logs — "
            "network, DHCP, and print logs do not capture that level of "
            "process detail."
        ),
    },
    # ------------------------------------------------------------------ #
    # Malware types (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-030",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "A software vendor embeds hidden code in its dealership management "
            "platform that checks, once daily, whether the client's account is "
            "current on its licensing subscription against the vendor's "
            "activation server. During a payment dispute, the vendor disables "
            "the account server-side; the very next scheduled check causes the "
            "embedded code to lock every workstation running the platform "
            "across all of the client's locations simultaneously. Which type "
            "of malicious code does this embedded check represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Logic bomb",
                "correct": True,
                "rationale": (
                    "Correct. Code that lies dormant within legitimate software "
                    "until a specific condition is met — here, the licensing "
                    "check failing — and then triggers a damaging action "
                    "(locking every workstation) is the definition of a logic "
                    "bomb."
                ),
            },
            {
                "id": "b",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm self-propagates across systems by "
                    "exploiting vulnerabilities or network shares; this code "
                    "was already deployed everywhere as part of the legitimate "
                    "software and simply activated on a triggering condition, "
                    "without spreading anywhere new."
                ),
            },
            {
                "id": "c",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit is designed to hide its presence and "
                    "maintain stealthy, privileged access; this code operated "
                    "openly as part of the vendor's own software with no "
                    "concealment involved."
                ),
            },
            {
                "id": "d",
                "text": "Potentially unwanted program (PUP)",
                "correct": False,
                "rationale": (
                    "Incorrect. A PUP is unwanted but generally non-destructive "
                    "bundled software (adware, toolbars); this code was "
                    "deliberately destructive, locking production systems the "
                    "moment its trigger condition was met."
                ),
            },
        ],
        "explanation": (
            "Dormant code embedded in legitimate software that activates a "
            "damaging action only when a specific condition (a failed "
            "licensing check) is met is a logic bomb, not a self-propagating "
            "worm, a stealth-focused rootkit, or a merely unwanted PUP."
        ),
    },
    {
        "id": "nd2f-031",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Malware types",
        "stem": (
            "Forensic analysis of a compromised server finds that the attacker "
            "achieved persistence entirely through a WMI (Windows Management "
            "Instrumentation) event subscription that re-launches a malicious "
            "PowerShell command block on every system startup. No new "
            "executable file was ever written to disk at any point in the "
            "intrusion, and every tool the attacker used — PowerShell, "
            "WMIC, and certutil — was a legitimate, digitally signed Windows "
            "binary already present on the system. Which TWO techniques does "
            "this intrusion demonstrate? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fileless malware",
                "correct": True,
                "rationale": (
                    "Correct. Persisting entirely through a WMI event "
                    "subscription and in-memory PowerShell execution, with no "
                    "malicious executable ever written to disk, is the "
                    "defining characteristic of fileless malware."
                ),
            },
            {
                "id": "b",
                "text": "Living-off-the-land (LOLBin) technique",
                "correct": True,
                "rationale": (
                    "Correct. Exclusively using pre-installed, legitimately "
                    "signed system tools such as PowerShell, WMIC, and "
                    "certutil to carry out the attack — rather than deploying "
                    "custom malware binaries — is a living-off-the-land "
                    "technique."
                ),
            },
            {
                "id": "c",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit specifically hooks or modifies OS "
                    "components to actively hide files, processes, or "
                    "registry keys from view; the scenario describes "
                    "persistence and execution mechanics, not a concealment "
                    "mechanism hiding artifacts from the OS's own utilities."
                ),
            },
            {
                "id": "d",
                "text": "Trojan horse",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan disguises a malicious executable as "
                    "legitimate software the user is tricked into running; no "
                    "new file or disguised installer was ever introduced here "
                    "at all."
                ),
            },
            {
                "id": "e",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm self-propagates to other hosts over a "
                    "network; this scenario describes persistence and stealthy "
                    "execution on a single already-compromised server, with no "
                    "mention of spreading to additional systems."
                ),
            },
        ],
        "explanation": (
            "Persisting without ever writing a file to disk is fileless "
            "malware, and relying exclusively on legitimate, pre-installed "
            "system binaries to execute the attack is a living-off-the-land "
            "technique — neither a rootkit's concealment mechanics, a "
            "trojan's disguised-installer delivery, nor a worm's "
            "network propagation apply here."
        ),
    },
    {
        "id": "nd2f-032",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "An incident responder observes real-time activity on a "
            "compromised workstation: the mouse cursor moves independently, "
            "folders are manually browsed one at a time, and a text editor is "
            "opened to search file contents for the word \"password,\" all "
            "while the legitimate user is away from their desk. This differs "
            "from an earlier incident on the same network in which infected "
            "hosts simply executed the same automated, queued command from a "
            "control server without any live human interaction. Which "
            "malware classification BEST describes the tool used in the "
            "CURRENT incident?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Remote access trojan (RAT)",
                "correct": True,
                "rationale": (
                    "Correct. Real-time, hands-on-keyboard control — moving the "
                    "cursor, manually browsing folders, and interactively "
                    "searching files — indicates an attacker is actively "
                    "operating the compromised machine live through a remote "
                    "access trojan, rather than issuing automated batch "
                    "commands."
                ),
            },
            {
                "id": "b",
                "text": "Bot performing automated command-and-control tasks",
                "correct": False,
                "rationale": (
                    "Incorrect. The comparison scenario (automated, queued "
                    "commands with no live interaction) describes classic "
                    "botnet behavior; the current incident instead shows live, "
                    "interactive human control, which distinguishes it from an "
                    "automated bot."
                ),
            },
            {
                "id": "c",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm's defining trait is autonomous "
                    "self-propagation across systems; nothing in this scenario "
                    "describes the malware spreading to other hosts, only "
                    "interactive control of one already-compromised machine."
                ),
            },
            {
                "id": "d",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb triggers a predefined destructive "
                    "action once a condition is met; this scenario describes "
                    "ongoing, live, hands-on-keyboard exploration by an "
                    "attacker, not a dormant conditional trigger."
                ),
            },
        ],
        "explanation": (
            "Live, hands-on-keyboard interaction with a compromised host — as "
            "opposed to an automated, pre-queued command executed without a "
            "human actively directing it — is the distinguishing sign of a "
            "remote access trojan rather than a bot, worm, or logic bomb."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-033",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "An attacker connects a laptop to an access port on a switch that "
            "belongs to an untrusted guest VLAN. The attacker crafts Ethernet "
            "frames with two stacked 802.1Q VLAN tags: an outer tag matching "
            "the guest VLAN and an inner tag matching a restricted finance "
            "VLAN. The access port strips only the outer tag before "
            "forwarding, causing the switch to treat the frame as if it "
            "originated on the finance VLAN, allowing the attacker's traffic "
            "to reach hosts it should never be able to reach. Which attack "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN hopping via double tagging",
                "correct": True,
                "rationale": (
                    "Correct. Nesting a second 802.1Q tag inside a frame so "
                    "that after the outer tag is stripped by the access port, "
                    "the switch forwards the frame based on the hidden inner "
                    "tag, is the defining mechanism of a double-tagging VLAN "
                    "hopping attack."
                ),
            },
            {
                "id": "b",
                "text": "MAC flooding",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC flooding overwhelms a switch's CAM table "
                    "with bogus MAC addresses to force it into a hub-like "
                    "flooding mode; this attack instead crafts nested VLAN tags "
                    "to cross a segmentation boundary, with no CAM table "
                    "exhaustion involved."
                ),
            },
            {
                "id": "c",
                "text": "ARP spoofing",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP spoofing poisons a host's IP-to-MAC "
                    "mapping to intercept traffic at layer 2/3; this attack "
                    "instead abuses VLAN tag processing on a switch port to "
                    "cross a VLAN boundary, with no ARP cache manipulation "
                    "described."
                ),
            },
            {
                "id": "d",
                "text": "A rogue DHCP server attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A rogue DHCP server hands out malicious IP "
                    "configuration to clients; no DHCP server or IP "
                    "configuration is involved here — the attack manipulates "
                    "VLAN tag stacking to reach a restricted segment directly."
                ),
            },
        ],
        "explanation": (
            "Stacking two VLAN tags so a switch forwards a frame based on the "
            "hidden inner tag after stripping the outer one is VLAN hopping "
            "via double tagging, distinct from MAC flooding, ARP spoofing, or "
            "a rogue DHCP server attack."
        ),
    },
    {
        "id": "nd2f-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "For roughly 40 minutes, global internet traffic destined for a "
            "company's public IP address range is unexpectedly routed through "
            "an unfamiliar autonomous system in another country before "
            "reaching the company's actual data center, adding significant "
            "latency and allowing the traffic to be passively captured along "
            "the way. Network engineers determine that a more specific route "
            "for the company's IP block was announced from that foreign "
            "autonomous system during the incident window. Which attack does "
            "this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "BGP route hijacking",
                "correct": True,
                "rationale": (
                    "Correct. Announcing a more specific, unauthorized route "
                    "for a victim's IP address block from a different "
                    "autonomous system causes global internet routers to "
                    "prefer that route and redirect traffic through the "
                    "attacker's network — the definition of a BGP route "
                    "hijack."
                ),
            },
            {
                "id": "b",
                "text": "DNS cache poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS cache poisoning corrupts a resolver's "
                    "name-to-IP mappings; this incident involves routing "
                    "tables directing traffic to the correct IP address block "
                    "through the wrong network path, not falsified DNS "
                    "responses."
                ),
            },
            {
                "id": "c",
                "text": "ARP spoofing",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP spoofing operates only within a single "
                    "local layer-2 broadcast domain; this incident affected "
                    "global internet routing across autonomous systems, far "
                    "beyond the scope of ARP."
                ),
            },
            {
                "id": "d",
                "text": "An evil twin access point attack",
                "correct": False,
                "rationale": (
                    "Incorrect. An evil twin is a rogue wireless access point "
                    "mimicking a legitimate SSID to lure nearby wireless "
                    "clients; this incident involves internet-wide routing "
                    "table manipulation, unrelated to Wi-Fi."
                ),
            },
        ],
        "explanation": (
            "Announcing a more specific BGP route from an unauthorized "
            "autonomous system to redirect global traffic for a victim's IP "
            "block through the attacker's network — enabling interception — "
            "is a BGP route hijack, not DNS poisoning, ARP spoofing, or an "
            "evil twin attack."
        ),
    },
    {
        "id": "nd2f-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "An attacker connects a laptop to an unused switch port and begins "
            "sending crafted Bridge Protocol Data Units (BPDUs) advertising an "
            "artificially low bridge priority. Within seconds, the Spanning "
            "Tree Protocol topology recalculates, and the attacker's laptop is "
            "elected the new root bridge for the VLAN, causing legitimate "
            "inter-switch traffic to reroute through the attacker's laptop, "
            "where it can be captured. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spanning Tree Protocol (STP) manipulation / root bridge takeover",
                "correct": True,
                "rationale": (
                    "Correct. Injecting BPDUs advertising a lower bridge "
                    "priority to force an election as the new root bridge, "
                    "redirecting inter-switch traffic through the attacker's "
                    "device, is a Spanning Tree Protocol manipulation attack."
                ),
            },
            {
                "id": "b",
                "text": "MAC flooding",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC flooding exhausts a switch's CAM table "
                    "with bogus addresses to force flooding behavior; this "
                    "attack instead manipulates the layer-2 spanning tree "
                    "topology election process directly with crafted BPDUs."
                ),
            },
            {
                "id": "c",
                "text": "A rogue DHCP server attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A rogue DHCP server issues malicious IP "
                    "configuration to clients; no DHCP activity or IP "
                    "configuration manipulation is described — the attacker "
                    "instead manipulated switch topology via BPDUs."
                ),
            },
            {
                "id": "d",
                "text": "VLAN hopping via double tagging",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN hopping uses nested 802.1Q tags to cross a "
                    "VLAN boundary; this attack instead manipulates Spanning "
                    "Tree Protocol root bridge election, an entirely different "
                    "layer-2 mechanism."
                ),
            },
        ],
        "explanation": (
            "Forging BPDUs to win the Spanning Tree Protocol root bridge "
            "election and redirect inter-switch traffic through an attacker's "
            "device is STP manipulation, distinct from MAC flooding, a rogue "
            "DHCP server, or VLAN hopping via double tagging."
        ),
    },
    # ------------------------------------------------------------------ #
    # Physical attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-036",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A security review of an employee turnstile finds a thin, "
            "battery-powered device wedged inside the badge-swipe reader "
            "housing that copies the magnetic stripe data from every employee "
            "badge swiped through it, storing the captured data for later "
            "retrieval. Cloned badges created from the captured data are later "
            "used to enter the building after hours. Which physical attack "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Card skimming",
                "correct": True,
                "rationale": (
                    "Correct. A concealed device that captures magnetic "
                    "stripe data as legitimate badges are swiped through it, "
                    "for later cloning and unauthorized use, is the definition "
                    "of a skimming attack."
                ),
            },
            {
                "id": "b",
                "text": "RFID proximity capture",
                "correct": False,
                "rationale": (
                    "Incorrect. RFID proximity capture reads contactless card "
                    "data wirelessly from a distance using a handheld reader; "
                    "this scenario describes a physical device embedded in the "
                    "swipe reader that copies magnetic stripe data during "
                    "actual card swipes, a different mechanism."
                ),
            },
            {
                "id": "c",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating involves an unauthorized person "
                    "following an authorized person through a door without "
                    "using their own credential; this scenario instead "
                    "involves cloned badge credentials being used "
                    "independently to enter after hours."
                ),
            },
            {
                "id": "d",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving recovers discarded physical "
                    "documents or media from trash; no discarded materials are "
                    "involved — the data was captured directly from a "
                    "compromised badge reader."
                ),
            },
        ],
        "explanation": (
            "A concealed device embedded in a physical badge reader that "
            "captures magnetic stripe data from swiped cards for later cloning "
            "is card skimming, distinct from wireless RFID capture, "
            "tailgating, or dumpster diving."
        ),
    },
    {
        "id": "nd2f-037",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Physical attacks",
        "stem": (
            "During a scheduled corporate espionage sweep, a security "
            "consultant uses an RF spectrum analyzer to detect a covert "
            "transmission originating from inside a boardroom's wall-mounted "
            "clock. The device is found to contain a small microphone and "
            "radio transmitter that continuously broadcasts ambient audio to "
            "a receiver parked in a vehicle outside the building. Which "
            "physical attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Covert eavesdropping via a hidden listening device (bugging)",
                "correct": True,
                "rationale": (
                    "Correct. Planting a concealed microphone and transmitter "
                    "inside an everyday object to continuously capture and "
                    "relay private conversations to a nearby receiver is the "
                    "definition of bugging — a covert physical eavesdropping "
                    "attack."
                ),
            },
            {
                "id": "b",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing involves an attacker directly "
                    "observing a target's screen, keypad entry, or documents in "
                    "person; this scenario involves a hidden electronic device "
                    "continuously transmitting audio, not direct visual "
                    "observation."
                ),
            },
            {
                "id": "c",
                "text": "Badge cloning",
                "correct": False,
                "rationale": (
                    "Incorrect. Badge cloning involves duplicating access "
                    "credential data to gain physical entry; nothing in this "
                    "scenario involves access badges — the device instead "
                    "captures audio from meetings."
                ),
            },
            {
                "id": "d",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving recovers information from "
                    "discarded physical materials; this attack instead uses an "
                    "active, hidden electronic transmitter to capture live "
                    "audio in real time."
                ),
            },
        ],
        "explanation": (
            "A concealed microphone and transmitter hidden inside an object to "
            "continuously relay private conversations to an outside receiver "
            "is covert eavesdropping (bugging), distinct from shoulder "
            "surfing, badge cloning, or dumpster diving."
        ),
    },
    # ------------------------------------------------------------------ #
    # Hardening (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A CIS benchmark scan of a server fleet that was originally "
            "deployed from a single hardened golden image six months ago now "
            "shows that 60 of the 500 servers have drifted from that baseline: "
            "several have re-enabled a disabled service, one has a locally "
            "created administrator account not present in the original image, "
            "and several are missing a registry setting that disables a "
            "legacy protocol. No malicious activity is confirmed — the "
            "changes appear to have accumulated gradually through ad hoc "
            "manual administration. Which TWO actions BEST remediate this "
            "situation going forward? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Reapply the approved baseline configuration to the "
                    "drifted servers using a configuration management tool"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Automatically reapplying the golden-image "
                    "baseline directly remediates the drifted settings across "
                    "the affected servers, restoring the intended hardened "
                    "state."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Implement continuous configuration compliance monitoring "
                    "to detect future drift automatically"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ongoing compliance monitoring compares live "
                    "configuration against the baseline continuously, so future "
                    "drift is detected and can be corrected quickly rather than "
                    "accumulating unnoticed for months."
                ),
            },
            {
                "id": "c",
                "text": "Install endpoint antivirus software on the drifted servers",
                "correct": False,
                "rationale": (
                    "Incorrect. Antivirus software addresses malware "
                    "detection, not configuration baseline drift caused by "
                    "gradual manual administrative changes."
                ),
            },
            {
                "id": "d",
                "text": "Disable all USB ports on the drifted servers",
                "correct": False,
                "rationale": (
                    "Incorrect. USB port control addresses removable-media "
                    "risk, which is unrelated to the re-enabled services, "
                    "unauthorized local accounts, and missing registry "
                    "hardening settings described in this scenario."
                ),
            },
            {
                "id": "e",
                "text": "Increase the password expiration interval fleet-wide",
                "correct": False,
                "rationale": (
                    "Incorrect. Password expiration policy has no bearing on "
                    "re-enabled services, unauthorized local accounts, or "
                    "missing protocol-disabling registry settings drifting "
                    "from the baseline."
                ),
            },
        ],
        "explanation": (
            "Configuration drift accumulated through ad hoc manual changes is "
            "best remediated by reapplying the approved baseline through "
            "configuration management and by implementing continuous "
            "compliance monitoring to catch future drift early — antivirus, "
            "USB port controls, and password expiration policy do not address "
            "baseline drift."
        ),
    },
    {
        "id": "nd2f-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hardening",
        "stem": (
            "A penetration test finds that when a workstation cannot resolve a "
            "hostname through standard DNS, it falls back to broadcasting a "
            "Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name "
            "Service (NBT-NS) request to the entire local subnet. The tester "
            "runs a credential-relay tool that responds to these broadcast "
            "requests, tricking workstations into sending their NTLM "
            "authentication hashes directly to the tester's machine. Which "
            "hardening action would MOST directly close this attack path?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable LLMNR and NBT-NS fallback name resolution via policy",
                "correct": True,
                "rationale": (
                    "Correct. Disabling LLMNR and NBT-NS removes the "
                    "broadcast-based fallback name resolution mechanism that "
                    "an attacker's rogue responder tool exploits to capture "
                    "NTLM hashes, directly closing this credential-relay attack "
                    "path."
                ),
            },
            {
                "id": "b",
                "text": "Disable SMBv1 on all workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the older SMBv1 protocol addresses a "
                    "different, unrelated set of legacy file-sharing "
                    "vulnerabilities; it does nothing to stop broadcast-based "
                    "LLMNR/NBT-NS name resolution poisoning."
                ),
            },
            {
                "id": "c",
                "text": "Enforce a longer minimum password length",
                "correct": False,
                "rationale": (
                    "Incorrect. Password length policy does not prevent the "
                    "underlying protocol weakness that lets a rogue responder "
                    "capture and relay NTLM hashes in the first place."
                ),
            },
            {
                "id": "d",
                "text": "Enable Secure Boot on all workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. Secure Boot protects the boot process against "
                    "unauthorized firmware or bootloader tampering; it has no "
                    "effect on local-subnet name resolution broadcasts or NTLM "
                    "hash relay attacks."
                ),
            },
        ],
        "explanation": (
            "Disabling the broadcast-based LLMNR/NBT-NS fallback name "
            "resolution protocols directly removes the mechanism a rogue "
            "responder abuses to harvest NTLM hashes — SMBv1 disabling, "
            "password policy, and Secure Boot each address unrelated risks."
        ),
    },
    {
        "id": "nd2f-040",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Hardening",
        "stem": (
            "An internal audit finds that employees across several departments "
            "have repeatedly copied confidential design files onto personal "
            "USB flash drives to work from home, bypassing the approved "
            "remote-access VPN entirely. No malware infection has occurred, "
            "but the security team wants to prevent this specific behavior "
            "fleet-wide going forward. Which hardening control would MOST "
            "directly address this risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Enforce endpoint device-control policy to block or "
                    "restrict USB mass-storage devices"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A device-control policy that blocks or restricts "
                    "USB mass-storage functionality directly prevents "
                    "employees from copying confidential files onto personal "
                    "flash drives, addressing the exact behavior observed."
                ),
            },
            {
                "id": "b",
                "text": "Require a longer minimum password length",
                "correct": False,
                "rationale": (
                    "Incorrect. Password length policy has no effect on "
                    "whether a workstation allows files to be copied to an "
                    "attached USB storage device."
                ),
            },
            {
                "id": "c",
                "text": "Disable unused inbound firewall ports on the VPN concentrator",
                "correct": False,
                "rationale": (
                    "Incorrect. This audit finding is about employees "
                    "bypassing the VPN by using USB drives instead, not about "
                    "inbound firewall exposure on the VPN concentrator itself."
                ),
            },
            {
                "id": "d",
                "text": "Enable full-disk encryption on all workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. Full-disk encryption protects data at rest if "
                    "a device is lost or stolen; it does not prevent an "
                    "authorized, logged-in user from copying files onto a "
                    "USB drive in the first place."
                ),
            },
        ],
        "explanation": (
            "Blocking or restricting USB mass-storage functionality through "
            "endpoint device-control policy directly stops the observed "
            "behavior of copying confidential files to personal flash "
            "drives — password policy, VPN firewall rules, and full-disk "
            "encryption do not address removable-media data movement."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mitigation techniques (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2f-041",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "A critical remote code execution vulnerability is disclosed in a "
            "public-facing application, but the vendor states an official "
            "patch will not be available for at least three weeks. The "
            "application cannot be taken offline, as it processes live "
            "customer orders. The security team writes and deploys a custom "
            "rule on the web application firewall in front of the application "
            "that specifically blocks the request pattern used to trigger the "
            "vulnerability. Which mitigation technique does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Compensating control (virtual patching)",
                "correct": True,
                "rationale": (
                    "Correct. Deploying a WAF rule to block the specific "
                    "exploitation pattern for a known vulnerability while the "
                    "official vendor patch is unavailable is a compensating "
                    "control, commonly called virtual patching."
                ),
            },
            {
                "id": "b",
                "text": "Decommissioning",
                "correct": False,
                "rationale": (
                    "Incorrect. Decommissioning means permanently retiring a "
                    "system; the stem explicitly states the application must "
                    "remain online to process live orders, ruling out "
                    "decommissioning."
                ),
            },
            {
                "id": "c",
                "text": "Least privilege enforcement",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege restricts account and process "
                    "permissions to the minimum necessary; it does not address "
                    "blocking a specific exploit request pattern at the "
                    "network edge."
                ),
            },
            {
                "id": "d",
                "text": "Application allow listing",
                "correct": False,
                "rationale": (
                    "Incorrect. Application allow listing restricts which "
                    "executables are permitted to run on an endpoint; it has no "
                    "relevance to filtering malicious HTTP request patterns "
                    "targeting a web application vulnerability."
                ),
            },
        ],
        "explanation": (
            "Blocking the specific exploit request pattern at the WAF while "
            "waiting for an official patch is a compensating control (virtual "
            "patching), not decommissioning, least privilege, or application "
            "allow listing."
        ),
    },
    {
        "id": "nd2f-042",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "An access review finds that 85% of the organization's standard "
            "user accounts have been granted permanent local administrator "
            "rights on their own workstations, a practice that began years "
            "ago to reduce help-desk tickets. A recent malware infection was "
            "able to install a kernel-mode driver only because the logged-in "
            "user had those standing admin rights. Which mitigation strategy "
            "would MOST effectively reduce the impact of future similar "
            "infections?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Remove standing local administrator rights and enforce "
                    "least privilege, using just-in-time elevation for "
                    "approved tasks"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing permanent local admin rights and "
                    "granting elevated privileges only temporarily and only "
                    "when justified directly reduces the ability of malware "
                    "running in a standard user's context to install "
                    "kernel-mode drivers or make other privileged changes."
                ),
            },
            {
                "id": "b",
                "text": "Increase the frequency of full-disk antivirus scans",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent scanning may detect malware "
                    "faster after the fact but does nothing to reduce the "
                    "privilege level that allowed the malware to install a "
                    "kernel-mode driver in the first place."
                ),
            },
            {
                "id": "c",
                "text": "Require longer, more complex user passwords",
                "correct": False,
                "rationale": (
                    "Incorrect. Password complexity does not limit what an "
                    "already-authenticated, privileged local session is "
                    "capable of installing — the root cause here is excessive "
                    "standing privilege, not weak credentials."
                ),
            },
            {
                "id": "d",
                "text": "Segment the network into additional VLANs",
                "correct": False,
                "rationale": (
                    "Incorrect. Network segmentation limits lateral movement "
                    "between hosts; it does not address the excessive local "
                    "privilege on the individual workstation that allowed the "
                    "kernel-mode driver installation to succeed."
                ),
            },
        ],
        "explanation": (
            "Removing unnecessary standing administrator rights and enforcing "
            "least privilege with just-in-time elevation directly limits what "
            "malware running under a compromised standard user's session can "
            "do — antivirus scan frequency, password complexity, and network "
            "segmentation don't address the excessive privilege itself."
        ),
    },
    {
        "id": "nd2f-043",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "During a large-scale phishing campaign, thousands of employees "
            "across the organization click links leading to a rotating set of "
            "newly registered, malicious credential-harvesting domains before "
            "the email security gateway can update its block list for each new "
            "domain. The security team wants a single control that prevents "
            "any employee's workstation from resolving or connecting to known "
            "malicious domains network-wide, regardless of which application "
            "or channel a user was tricked into clicking through. Which "
            "mitigation technique BEST meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "DNS filtering/sinkholing of known-malicious domains at "
                    "the resolver level"
                ),
                "correct": True,
                "rationale": (
                    "Correct. DNS filtering blocks or redirects resolution "
                    "requests for known-malicious domains at the network's "
                    "DNS resolver, stopping the connection before it is ever "
                    "established, regardless of which application or link a "
                    "user clicked."
                ),
            },
            {
                "id": "b",
                "text": "Increasing email attachment size scanning limits",
                "correct": False,
                "rationale": (
                    "Incorrect. This campaign relies on malicious links, not "
                    "attachments, and attachment scanning limits would not "
                    "prevent a workstation from reaching a credential-"
                    "harvesting domain."
                ),
            },
            {
                "id": "c",
                "text": "Enforcing longer password rotation intervals",
                "correct": False,
                "rationale": (
                    "Incorrect. Password rotation policy does not prevent "
                    "workstations from connecting to malicious domains and "
                    "does not address the network-wide blocking requirement "
                    "described."
                ),
            },
            {
                "id": "d",
                "text": "Disabling USB mass-storage device access",
                "correct": False,
                "rationale": (
                    "Incorrect. USB device control addresses removable-media "
                    "risk, which is unrelated to blocking network connections "
                    "to malicious phishing domains."
                ),
            },
        ],
        "explanation": (
            "Filtering or sinkholing DNS resolution for known-malicious "
            "domains at the network level provides a single, application-"
            "agnostic control that blocks connections to credential-"
            "harvesting sites regardless of the delivery channel — "
            "attachment scanning, password rotation, and USB controls do not "
            "meet that requirement."
        ),
    },
]

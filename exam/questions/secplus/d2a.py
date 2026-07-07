"""Security+ SY0-701 practice questions — Domain 2 (Threats, Vulnerabilities,
and Mitigations), batch A.

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
        "id": "nd2a-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A security team detects an intrusion that has been present in the network "
            "for 14 months. The attacker used custom, previously unseen tooling, moved "
            "slowly between systems to avoid detection, and exfiltrated small amounts of "
            "proprietary R&D data over encrypted channels timed to blend with normal "
            "traffic. No ransom demand or public disclosure ever occurred. Which threat "
            "actor is MOST likely responsible?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Advanced persistent threat / nation-state actor",
                "correct": True,
                "rationale": (
                    "Correct. Custom tooling, extreme patience, low operational noise, "
                    "and a data-theft motive without extortion or exposure align with a "
                    "well-resourced, disciplined nation-state APT."
                ),
            },
            {
                "id": "b",
                "text": "Organized crime group",
                "correct": False,
                "rationale": (
                    "Incorrect. Organized crime is financially motivated and typically "
                    "seeks fast monetization (ransom, resale of data) rather than a "
                    "14-month quiet campaign focused on stealing R&D."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. Hacktivists want public attention for an ideological "
                    "cause; this is inconsistent with over a year of stealth and no "
                    "public disclosure."
                ),
            },
            {
                "id": "d",
                "text": "Unskilled attacker (script kiddie)",
                "correct": False,
                "rationale": (
                    "Incorrect. Script kiddies rely on existing, off-the-shelf tools "
                    "and lack the discipline and custom-tooling capability for a "
                    "prolonged, low-profile campaign."
                ),
            },
        ],
        "explanation": (
            "Patience, custom tooling, low noise, and a pure intelligence/IP-theft "
            "motive without extortion or public exposure are the classic fingerprints "
            "of a nation-state-sponsored APT, distinguishing it from financially driven "
            "organized crime, attention-seeking hacktivism, and low-skill opportunists."
        ),
    },
    {
        "id": "nd2a-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "Two weeks after a systems administrator was terminated for cause, unusual "
            "after-hours logins occur using their still-active service account, and "
            "configuration backups are quietly deleted from the only offsite repository "
            "the admin was known to have set up. Which threat actor classification BEST "
            "describes this activity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Insider threat",
                "correct": True,
                "rationale": (
                    "Correct. A former employee using unique insider knowledge (a "
                    "specific, otherwise-obscure backup repository) and a still-active "
                    "account to sabotage systems after termination is a textbook "
                    "insider-threat scenario."
                ),
            },
            {
                "id": "b",
                "text": "Shadow IT",
                "correct": False,
                "rationale": (
                    "Incorrect. Shadow IT describes unauthorized but not necessarily "
                    "malicious use of technology by legitimate staff, not deliberate "
                    "sabotage carried out by a terminated employee."
                ),
            },
            {
                "id": "c",
                "text": "Organized crime",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no financial extortion or monetization angle "
                    "here; the motive and method both point to personal, insider-driven "
                    "retaliation rather than profit-seeking crime."
                ),
            },
            {
                "id": "d",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ideological message or public leak; the "
                    "targeted destruction of a specific, obscure backup path is a "
                    "signature of insider knowledge, not ideology."
                ),
            },
        ],
        "explanation": (
            "Knowledge of a specific, non-obvious asset (the offsite backup repository) "
            "combined with reuse of still-valid access after termination is the "
            "defining pattern of an insider threat."
        ),
    },
    {
        "id": "nd2a-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A group defaces a company's public website, replacing the homepage with a "
            "political statement about the company's environmental record, and "
            "simultaneously leaks internal emails to a news outlet. The tools used are "
            "publicly available website-defacement kits requiring minimal technical "
            "skill. Which threat actor MOST likely carried out this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hacktivist",
                "correct": True,
                "rationale": (
                    "Correct. An ideological motive (environmental criticism), public "
                    "messaging, and leaking material to the press are hallmark "
                    "hacktivist behaviors, even when the technical sophistication used "
                    "is low."
                ),
            },
            {
                "id": "b",
                "text": "Unskilled attacker (script kiddie)",
                "correct": False,
                "rationale": (
                    "Incorrect. A script kiddie uses available tools for disruption or "
                    "bragging rights without a coherent ideological agenda; the "
                    "political messaging and press leak here point to hacktivism, not "
                    "just low skill."
                ),
            },
            {
                "id": "c",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. Nation-states favor stealth and long-term access over "
                    "noisy public defacement, and rarely take this kind of visible "
                    "action over a private company's environmental record."
                ),
            },
            {
                "id": "d",
                "text": "Organized crime group",
                "correct": False,
                "rationale": (
                    "Incorrect. Organized crime is financially driven; there is no "
                    "ransom or monetization angle, only ideological messaging and "
                    "public disclosure."
                ),
            },
        ],
        "explanation": (
            "Low technical sophistication does not rule out hacktivism — the deciding "
            "factor is the ideological, publicity-seeking motive (defacement message "
            "plus press leak), which distinguishes it from a skill-only script kiddie."
        ),
    },
    # ------------------------------------------------------------------ #
    # Threat vectors and attack surfaces (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "An analyst determines that a manufacturing plant's control network was "
            "compromised through a firmware update package delivered by a trusted "
            "industrial equipment vendor; the update contained a backdoor inserted "
            "before it ever reached the vendor's distribution servers. Which attack "
            "vector does this scenario describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Supply chain",
                "correct": True,
                "rationale": (
                    "Correct. The compromise originated upstream, inside a trusted "
                    "vendor's software delivery pipeline, before it ever reached the "
                    "victim — the defining trait of a supply chain attack."
                ),
            },
            {
                "id": "b",
                "text": "Direct access",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no evidence of an attacker physically or "
                    "locally connecting to plant equipment; the vector was a remotely "
                    "delivered, trusted vendor update."
                ),
            },
            {
                "id": "c",
                "text": "Removable media",
                "correct": False,
                "rationale": (
                    "Incorrect. No USB drive or other portable media was used; the "
                    "payload arrived through an official vendor firmware-update "
                    "channel."
                ),
            },
            {
                "id": "d",
                "text": "Wireless",
                "correct": False,
                "rationale": (
                    "Incorrect. The compromise is tied to a firmware distribution "
                    "channel, not to interception or exploitation of a wireless "
                    "network."
                ),
            },
        ],
        "explanation": (
            "When a trusted vendor's update or build pipeline is the point of "
            "compromise, before the product ever reaches the customer, that is a "
            "supply chain attack vector."
        ),
    },
    {
        "id": "nd2a-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "An employee plugs a USB drive found in the parking lot into a workstation "
            "to identify its owner, unknowingly triggering an autorun script that "
            "installs a remote access tool. Which attack vector was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Removable media",
                "correct": True,
                "rationale": (
                    "Correct. The initial infection vector was a portable USB device "
                    "introduced into the environment — a classic removable-media "
                    "attack vector."
                ),
            },
            {
                "id": "b",
                "text": "Message-based",
                "correct": False,
                "rationale": (
                    "Incorrect. No email, SMS, or messaging platform delivered the "
                    "payload; the vector was physical media, not a message."
                ),
            },
            {
                "id": "c",
                "text": "Image-based",
                "correct": False,
                "rationale": (
                    "Incorrect. Image-based vectors hide malicious code inside image "
                    "files or their metadata; this scenario describes an autorun "
                    "executable on a USB device, not a crafted image file."
                ),
            },
            {
                "id": "d",
                "text": "Default credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. No credential reuse or default password was involved "
                    "in gaining initial access; the compromise happened purely through "
                    "plugging in the found media."
                ),
            },
        ],
        "explanation": (
            "A found or planted USB drive that executes code when connected is the "
            "removable-media attack vector — a common baiting technique for gaining an "
            "initial foothold."
        ),
    },
    # ------------------------------------------------------------------ #
    # Social engineering (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "A caller identifies themselves as a member of the help desk and tells an "
            "employee that their account will be locked in five minutes unless they "
            "read back the one-time passcode just texted to their phone. Which social "
            "engineering technique is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Vishing",
                "correct": True,
                "rationale": (
                    "Correct. The attack is carried out over a live voice phone call "
                    "impersonating a trusted party (the help desk) to extract a "
                    "one-time passcode — the channel-defining trait of vishing."
                ),
            },
            {
                "id": "b",
                "text": "Smishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Smishing is phishing delivered via SMS text as the "
                    "attack channel; here the attack itself is conducted over a phone "
                    "call, with the text message only incidentally carrying the OTP."
                ),
            },
            {
                "id": "c",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. No email is used at any point in this scenario; the "
                    "entire interaction happens over a phone call."
                ),
            },
            {
                "id": "d",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. A false identity and urgency are indeed used to build "
                    "the scenario, but the exam classifies attacks by their delivery "
                    "channel when one is explicit; since this specific attack is "
                    "conducted live over the phone, vishing is the more precise "
                    "classification for this channel-based technique."
                ),
            },
        ],
        "explanation": (
            "When social engineering is conducted over a live voice call, the "
            "channel-specific term vishing is the best classification, even though the "
            "underlying trick (a fabricated help-desk identity and urgency) is a form "
            "of pretexting."
        ),
    },
    {
        "id": "nd2a-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "An attacker registers the domain \"micros0ft-support.com\" and emails "
            "employees a link to a fake login portal, after researching the company's "
            "org chart on LinkedIn so the message can reference their actual manager's "
            "name to appear legitimate. Which combination of techniques BEST describes "
            "this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Typosquatting combined with pretexting",
                "correct": True,
                "rationale": (
                    "Correct. The lookalike domain with a substituted character is "
                    "typosquatting, and inventing a false but plausible scenario "
                    "(referencing the real manager) to gain trust is pretexting."
                ),
            },
            {
                "id": "b",
                "text": "Watering hole combined with vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. No compromised third-party website employees regularly "
                    "visit was used (watering hole), and no phone call occurred "
                    "(vishing); the attack was delivered by email with a crafted link."
                ),
            },
            {
                "id": "c",
                "text": "Business email compromise combined with whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. No legitimate email account was actually compromised "
                    "or spoofed as an executive (BEC), and the message targets the "
                    "general employee population rather than a single high-value "
                    "executive (whaling)."
                ),
            },
            {
                "id": "d",
                "text": "Smishing combined with brand impersonation only",
                "correct": False,
                "rationale": (
                    "Incorrect. The message was delivered by email, not SMS, so "
                    "smishing does not apply; brand impersonation alone also omits the "
                    "personalized pretext referencing the real manager's name."
                ),
            },
        ],
        "explanation": (
            "The lookalike domain is typosquatting, and researching and inserting a "
            "real manager's name to fabricate legitimacy is pretexting — together they "
            "describe a personalized phishing email, not BEC, whaling, or a watering "
            "hole attack."
        ),
    },
    {
        "id": "nd2a-008",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "Review the phishing email excerpt below, sent to the finance department:\n\n"
            "\"URGENT — Wire Transfer Required Today. This is the CEO. I am in "
            "back-to-back board meetings and unreachable by phone until tomorrow. "
            "Process the attached wire instructions immediately and reply only to this "
            "address to confirm — do not loop in anyone else or wait for my "
            "callback.\"\n\n"
            "Which TWO social engineering principles are being leveraged in this "
            "message? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Urgency",
                "correct": True,
                "rationale": (
                    "Correct. Phrases like \"Required Today\" and \"immediately\" "
                    "pressure the recipient into acting fast, before they have time to "
                    "verify the request through normal channels."
                ),
            },
            {
                "id": "b",
                "text": "Authority",
                "correct": True,
                "rationale": (
                    "Correct. Impersonating the CEO leverages the target's deference "
                    "to senior leadership to discourage questioning or escalation of "
                    "the request."
                ),
            },
            {
                "id": "c",
                "text": "Scarcity",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no claim of a limited-availability resource "
                    "or offer running out; the pressure in this message comes purely "
                    "from a deadline and rank, not from scarcity of something the "
                    "target wants."
                ),
            },
            {
                "id": "d",
                "text": "Social proof (consensus)",
                "correct": False,
                "rationale": (
                    "Incorrect. The message never references other employees, peers, "
                    "or vendors already having complied; there is no bandwagon or "
                    "consensus cue present."
                ),
            },
            {
                "id": "e",
                "text": "Likability",
                "correct": False,
                "rationale": (
                    "Incorrect. The tone is a cold, secretive command rather than an "
                    "attempt to build friendliness or rapport with the target."
                ),
            },
        ],
        "explanation": (
            "This message combines a false authority figure (the CEO) with manufactured "
            "time pressure (urgency) and explicit secrecy instructions, both classic "
            "BEC/social-engineering principles — no scarcity, consensus, or likability "
            "cues are present."
        ),
    },
    # ------------------------------------------------------------------ #
    # Application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A web application crashes with a segmentation fault whenever a form field "
            "that normally accepts a 10-character ZIP code is submitted with several "
            "thousand characters, and crash dumps show the return address on the stack "
            "has been overwritten. Which vulnerability class does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Buffer overflow",
                "correct": True,
                "rationale": (
                    "Correct. Unbounded input overwriting the stack — including the "
                    "return address — is the signature of a classic buffer overflow."
                ),
            },
            {
                "id": "b",
                "text": "Race condition (TOCTOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. A TOCTOU flaw involves a timing gap between checking "
                    "and using a resource, not oversized input overwriting memory."
                ),
            },
            {
                "id": "c",
                "text": "Integer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. An integer overflow results from arithmetic exceeding "
                    "a variable's storage capacity and wrapping around; it is not "
                    "primarily caused by a raw oversized string overrunning a "
                    "fixed-size buffer as described here."
                ),
            },
            {
                "id": "d",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. Deserialization flaws involve reconstructing objects "
                    "from untrusted serialized data; this scenario shows a fixed-size "
                    "input field being overrun, not object deserialization."
                ),
            },
        ],
        "explanation": (
            "Oversized input overwriting the stack and corrupting the saved return "
            "address is the classic mechanism of a buffer overflow vulnerability."
        ),
    },
    {
        "id": "nd2a-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A file-upload service checks whether a filename already exists and, if "
            "not, reserves the name; a moment later, in a separate step, it writes the "
            "uploaded content and permission metadata to that filename. A tester "
            "uploads two files with the same name in rapid succession and finds one "
            "file's contents overwrite the other's permission metadata, enabling "
            "privilege escalation. Which vulnerability is being exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Time-of-check to time-of-use (TOCTOU) race condition",
                "correct": True,
                "rationale": (
                    "Correct. The gap between checking whether the name exists and "
                    "actually writing to it allows a second, concurrent request to "
                    "interleave and manipulate the resource before the first operation "
                    "completes."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No oversized input or stack/heap memory corruption is "
                    "described; the flaw is a timing gap between a check and a "
                    "subsequent use."
                ),
            },
            {
                "id": "c",
                "text": "Server-side request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF tricks a server into making unintended requests "
                    "to internal or external resources; it does not describe a "
                    "check/write timing gap on file uploads."
                ),
            },
            {
                "id": "d",
                "text": "Insecure direct object reference",
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR involves accessing another user's object via a "
                    "predictable identifier with no timing dependency; here the flaw "
                    "specifically depends on the interleaving of two near-simultaneous "
                    "upload requests."
                ),
            },
        ],
        "explanation": (
            "A vulnerability that depends on the sequence and timing between checking "
            "a condition and acting on it is a time-of-check to time-of-use race "
            "condition."
        ),
    },
    # ------------------------------------------------------------------ #
    # Web application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A vulnerability scan flags a web form that reflects unsanitized user "
            "input back into the page's HTML. A researcher confirms this by submitting "
            "a comment containing a \"<script>\" tag that executes in the browser of "
            "every other user who later views that comment. Which vulnerability is "
            "confirmed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Stored cross-site scripting (XSS)",
                "correct": True,
                "rationale": (
                    "Correct. The malicious script persists (is stored) in the "
                    "comment and executes in the browsers of any user who later views "
                    "the page, which is the definition of stored XSS."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF forces an already-authenticated user's browser to "
                    "submit an unwanted request; it does not involve injecting a "
                    "script that runs in other users' sessions."
                ),
            },
            {
                "id": "c",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF causes the server itself to make attacker-"
                    "controlled requests to other systems; here the payload executes "
                    "client-side, in victims' browsers, not on the server."
                ),
            },
            {
                "id": "d",
                "text": "Reflected cross-site scripting",
                "correct": False,
                "rationale": (
                    "Incorrect. Reflected XSS requires the victim to click a "
                    "crafted link so the payload is echoed back in a single response; "
                    "here the payload persists in stored comments and affects any "
                    "viewer, which is stored XSS, not reflected."
                ),
            },
        ],
        "explanation": (
            "Because the injected script is saved server-side and executes for every "
            "subsequent viewer rather than only for a victim who clicks a crafted "
            "link, this is stored XSS."
        ),
    },
    {
        "id": "nd2a-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "An internal application lets users enter a URL that the server fetches "
            "and returns a thumbnail of. A tester submits "
            "\"http://169.254.169.254/latest/meta-data/iam/security-credentials/\" as "
            "the URL and receives cloud instance credentials back in the thumbnail "
            "response. Which vulnerability was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Server-side request forgery (SSRF)",
                "correct": True,
                "rationale": (
                    "Correct. The server itself was tricked into making a request to "
                    "an internal cloud metadata endpoint on the attacker's behalf, "
                    "disclosing sensitive credentials — the defining trait of SSRF."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF abuses an authenticated victim's browser to "
                    "perform actions on a site; it does not involve the target server "
                    "itself issuing an outbound request to an internal resource."
                ),
            },
            {
                "id": "c",
                "text": "Cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. No script was injected or executed in a victim's "
                    "browser; the server-side URL fetch itself was abused."
                ),
            },
            {
                "id": "d",
                "text": "Directory traversal",
                "correct": False,
                "rationale": (
                    "Incorrect. Directory traversal manipulates file paths to access "
                    "files outside a restricted directory; it does not involve URLs "
                    "that cause the server to issue outbound network requests."
                ),
            },
        ],
        "explanation": (
            "A vulnerable server-side fetch feature that can be pointed at internal-"
            "only resources like the cloud metadata service is a textbook SSRF."
        ),
    },
    {
        "id": "nd2a-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A tester submits the request below to a banking application's password-"
            "reset endpoint:\n\n"
            "POST /reset-password HTTP/1.1\n"
            "Host: internal-api.bank.local\n"
            "Cookie: session=abc123 (the tester's own valid session)\n"
            "Content-Type: application/json\n\n"
            "{\"account_id\": 55892, \"new_password\": \"Test1234!\"}\n\n"
            "The tester changes account_id to a value belonging to another customer "
            "and resubmits, still using their own valid session cookie; the other "
            "customer's password is successfully reset. Which TWO characteristics of "
            "this attack point to it being an insecure direct object reference (IDOR) "
            "rather than CSRF or SSRF? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The request succeeds using the attacker's own valid, unmodified "
                    "session/authentication"
                ),
                "correct": True,
                "rationale": (
                    "Correct. IDOR occurs when an authenticated user can access or "
                    "modify another user's object simply by changing a reference "
                    "(account_id); no forged cross-user request or hijacked session "
                    "was needed."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The server fails to verify that account_id belongs to the "
                    "authenticated session owner"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This missing authorization/ownership check on the "
                    "object being modified is the defining flaw behind IDOR."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The attacker's browser was forced to submit the request without "
                    "the attacker's knowledge"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF requires an unwitting victim's browser to submit "
                    "a forged request; here the tester deliberately and knowingly "
                    "crafted and sent the request themselves."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The target server made an outbound request to another internal "
                    "system on the attacker's behalf"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes SSRF; no server-side outbound request "
                    "to another system occurred, only a direct manipulation of a "
                    "parameter referencing the target resource."
                ),
            },
        ],
        "explanation": (
            "Because the tester used their own legitimate, unforced session and the "
            "only flaw was a missing ownership check on the account_id parameter, this "
            "is an insecure direct object reference, not CSRF (which needs an unwitting "
            "victim) or SSRF (which needs the server to make its own outbound request)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mobile vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A mobile device management (MDM) console shows that a managed device "
            "recently gained the ability to install applications outside the vendor's "
            "official app store, and that MDM policy-enforcement APIs on the device no "
            "longer respond. Which mobile vulnerability MOST likely explains these "
            "findings?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Jailbreaking (or rooting)",
                "correct": True,
                "rationale": (
                    "Correct. Removing OS-level restrictions disables vendor "
                    "sandboxing and MDM enforcement hooks, enabling sideloading from "
                    "unofficial sources — exactly what is observed here."
                ),
            },
            {
                "id": "b",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping transfers a victim's phone number to an "
                    "attacker-controlled SIM to intercept calls and SMS; it does not "
                    "alter the device's OS restrictions or app installation controls."
                ),
            },
            {
                "id": "c",
                "text": "Insecure app permissions",
                "correct": False,
                "rationale": (
                    "Incorrect. Overly broad app permissions are a configuration "
                    "weakness within the OS's normal sandbox, not the wholesale "
                    "removal of OS-level restrictions and loss of MDM control "
                    "described here."
                ),
            },
            {
                "id": "d",
                "text": "Bluejacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluejacking is sending unsolicited messages or data "
                    "to nearby devices over Bluetooth; it has no effect on MDM "
                    "enforcement or the device's OS restrictions."
                ),
            },
        ],
        "explanation": (
            "Loss of MDM enforcement combined with the ability to install apps from "
            "outside the official store is the signature of a jailbroken/rooted "
            "device."
        ),
    },
    {
        "id": "nd2a-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A user reports their phone suddenly stopped receiving calls and texts. "
            "Shortly after, their email and banking accounts receive password-reset "
            "SMS codes the legitimate user never requested, and the accounts are "
            "compromised. Which attack MOST likely occurred?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SIM swapping",
                "correct": True,
                "rationale": (
                    "Correct. The attacker convinced or bribed the carrier to port "
                    "the victim's number to a new SIM, intercepting SMS-based MFA "
                    "codes and enabling account takeover — explaining why the victim's "
                    "own phone lost service."
                ),
            },
            {
                "id": "b",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluesnarfing is unauthorized access to data over a "
                    "close-range Bluetooth connection, not a carrier-level number port "
                    "that redirects SMS traffic."
                ),
            },
            {
                "id": "c",
                "text": "Malicious app sideloading",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no indication of a malicious app installed "
                    "on the device; the loss of cellular service on the legitimate "
                    "device is the key clue pointing to a carrier-side number change."
                ),
            },
            {
                "id": "d",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreaking removes OS restrictions on the device "
                    "itself; it would not cause the victim's own phone to suddenly "
                    "lose cellular service."
                ),
            },
        ],
        "explanation": (
            "Sudden loss of cellular service followed by unauthorized SMS-based "
            "password resets is the classic pattern of SIM swapping."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A cloud tenant's forensic team discovers that a process running inside "
            "their VM was able to read memory belonging to a different customer's VM "
            "hosted on the same physical server by exploiting a flaw in the "
            "hypervisor's memory isolation. Which vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VM escape",
                "correct": True,
                "rationale": (
                    "Correct. Breaking out of a VM's isolation boundary to access the "
                    "hypervisor or co-resident VMs is the definition of a VM escape."
                ),
            },
            {
                "id": "b",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. VM sprawl refers to unmanaged proliferation of "
                    "forgotten or unpatched VMs — an operational hygiene issue, not a "
                    "hypervisor isolation breach between running VMs."
                ),
            },
            {
                "id": "c",
                "text": "Resource reuse (data remnants)",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource reuse issues involve residual data left in "
                    "shared physical resources reassigned to a new VM after "
                    "deallocation, not an active exploit breaching isolation between "
                    "two currently running VMs."
                ),
            },
            {
                "id": "d",
                "text": "Live migration hijacking",
                "correct": False,
                "rationale": (
                    "Incorrect. This targets the process of moving a running VM "
                    "between physical hosts, not a memory-isolation exploit between "
                    "VMs already running on the same host."
                ),
            },
        ],
        "explanation": (
            "Breaching the hypervisor's isolation to read another tenant's VM memory "
            "while both VMs are actively running is the definition of VM escape."
        ),
    },
    {
        "id": "nd2a-017",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "An organization decommissions a VM and reassigns its freed storage blocks "
            "to a new VM without a sanitization step. The new VM's administrator later "
            "finds fragments of the previous tenant's database files recoverable from "
            "unallocated space. Which vulnerability does this MOST closely describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Resource reuse (data remnants)",
                "correct": True,
                "rationale": (
                    "Correct. Failing to sanitize storage before reallocation leaves "
                    "recoverable remnants of the prior tenant's data — a classic "
                    "resource-reuse/data-remanence issue in shared virtualized "
                    "storage."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. No isolation boundary between a running hypervisor "
                    "and a guest was broken; the issue is leftover data in reassigned "
                    "storage, not an active exploit."
                ),
            },
            {
                "id": "c",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. Sprawl describes accumulation of unmanaged, forgotten "
                    "VMs, not leftover data on storage blocks that were properly "
                    "decommissioned and reassigned."
                ),
            },
            {
                "id": "d",
                "text": "Hypervisor jackpotting",
                "correct": False,
                "rationale": (
                    "Incorrect. Hypervisor jackpotting (hyperjacking) involves "
                    "installing a rogue hypervisor to control guest VMs, unrelated to "
                    "leftover data on recycled storage blocks."
                ),
            },
        ],
        "explanation": (
            "Recoverable fragments of a prior tenant's data on reassigned storage, due "
            "to missing sanitization, is a resource reuse (data remanence) "
            "vulnerability specific to shared/virtualized environments."
        ),
    },
    # ------------------------------------------------------------------ #
    # Vulnerability scan and assessment result classification (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-018",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A vulnerability scanner flags a Linux server as running an outdated, "
            "vulnerable version of OpenSSL based on its banner response. Manual "
            "verification shows the vendor backported the security patch into the "
            "existing version string without changing the displayed version number, "
            "and the server is not actually vulnerable. How should this finding be "
            "classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False positive",
                "correct": True,
                "rationale": (
                    "Correct. The scanner reported a vulnerability that does not "
                    "actually exist once manual verification confirmed the patch had "
                    "been backported, despite the unchanged version banner."
                ),
            },
            {
                "id": "b",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative would mean the scanner failed to "
                    "flag a real vulnerability; here the scanner did flag something, "
                    "it was simply inaccurate."
                ),
            },
            {
                "id": "c",
                "text": "True positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A true positive requires the flagged condition to be "
                    "verified as actually present and exploitable, which manual "
                    "verification disproved here."
                ),
            },
            {
                "id": "d",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative means no vulnerability was reported "
                    "and none exists; here the scanner did report a vulnerability, it "
                    "was simply wrong."
                ),
            },
        ],
        "explanation": (
            "A reported vulnerability that manual verification disproves is a false "
            "positive, a common issue with banner-based/version-based scanning against "
            "backported patches."
        ),
    },
    {
        "id": "nd2a-019",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "During a credentialed scan, a critical remote code execution "
            "vulnerability on a database server was not reported by the scanner. "
            "Three weeks later, that exact vulnerability is used to compromise the "
            "server. How should the scanner's original result for that host be "
            "classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False negative",
                "correct": True,
                "rationale": (
                    "Correct. A real, exploitable vulnerability existed but the scan "
                    "failed to detect and report it — the definition of a false "
                    "negative."
                ),
            },
            {
                "id": "b",
                "text": "False positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A false positive is an incorrectly reported "
                    "vulnerability that isn't real; here the problem is the opposite "
                    "— a real vulnerability went unreported."
                ),
            },
            {
                "id": "c",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative applies when no vulnerability is "
                    "present and none is reported; here a vulnerability genuinely "
                    "existed, so the silence about it was an error, not an accurate "
                    "negative result."
                ),
            },
            {
                "id": "d",
                "text": "Indicator of compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. An IoC is forensic evidence that a breach occurred; "
                    "the question asks how to classify the earlier scan result itself, "
                    "not the later breach evidence."
                ),
            },
        ],
        "explanation": (
            "A real vulnerability that a scan fails to detect and report, later "
            "confirmed by exploitation, is a false negative."
        ),
    },
    # ------------------------------------------------------------------ #
    # Indicators of malicious activity (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-020",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Endpoint telemetry shows \"powershell.exe\" launched with a Base64-"
            "encoded command-line argument that decodes to a script downloading "
            "additional code from a remote IP directly into memory, with no file ever "
            "written to disk. Which indicator/technique does this MOST closely "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Living-off-the-land attack using a LOLBin (fileless execution)",
                "correct": True,
                "rationale": (
                    "Correct. Abusing a trusted, built-in administrative binary "
                    "(PowerShell) to execute obfuscated, memory-resident code without "
                    "dropping a file to disk is the hallmark of living-off-the-land/"
                    "fileless activity."
                ),
            },
            {
                "id": "b",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is dormant code embedded in existing "
                    "software that triggers on a specific condition or date; this "
                    "scenario shows an actively launched encoded command downloading "
                    "a remote payload right now."
                ),
            },
            {
                "id": "c",
                "text": "Rootkit installation",
                "correct": False,
                "rationale": (
                    "Incorrect. Rootkits modify the OS or kernel to hide a persistent "
                    "presence on disk; this scenario explicitly shows no file written "
                    "to disk and does not describe kernel-level concealment."
                ),
            },
            {
                "id": "d",
                "text": "Command injection",
                "correct": False,
                "rationale": (
                    "Incorrect. Command injection is a web application vulnerability "
                    "where attacker input is passed to a system shell via a "
                    "vulnerable application; this scenario describes endpoint "
                    "execution of an encoded PowerShell command, not an injected web "
                    "parameter."
                ),
            },
        ],
        "explanation": (
            "Encoded, memory-resident execution via a trusted administrative binary "
            "with no file dropped to disk is the classic signature of a living-off-"
            "the-land/fileless technique."
        ),
    },
    {
        "id": "nd2a-021",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A SIEM alert shows an employee's account authenticating successfully "
            "from Chicago at 9:02 a.m. and again from a location 6,000 miles away at "
            "9:14 a.m., with no VPN egress point that would explain the discrepancy. "
            "Which indicator does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Impossible travel",
                "correct": True,
                "rationale": (
                    "Correct. Two successful logins from geographically distant "
                    "locations within a timeframe that makes physical travel "
                    "impossible is the definition of the impossible-travel indicator "
                    "of account compromise."
                ),
            },
            {
                "id": "b",
                "text": "Brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Brute force is characterized by many failed "
                    "authentication attempts, not two successful logins from "
                    "disparate locations."
                ),
            },
            {
                "id": "c",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing involves automated login "
                    "attempts using breached username/password pairs across many "
                    "accounts, typically producing many failed attempts across "
                    "multiple accounts, not two successful logins on one account from "
                    "impossible locations."
                ),
            },
            {
                "id": "d",
                "text": "Session replay attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Session replay reuses a previously captured valid "
                    "session token to impersonate a user without a new authentication "
                    "event; here two distinct successful authentications occurred, "
                    "pointing to credential compromise and impossible travel rather "
                    "than token reuse."
                ),
            },
        ],
        "explanation": (
            "Two successful authentications from locations that could not both be "
            "reached within the elapsed time is the impossible-travel indicator, a "
            "strong sign the account's credentials are compromised."
        ),
    },
    {
        "id": "nd2a-022",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "An incident responder investigating a suspected ransomware outbreak "
            "finds the following on an affected file server: thousands of user "
            "documents renamed with a new \".lockxyz\" extension within a 90-second "
            "window, and PowerShell command history showing "
            "\"vssadmin delete shadows /all /quiet\" executed moments before the mass "
            "renaming began. Which TWO findings are the strongest indicators that this "
            "is an active ransomware attack rather than routine backup maintenance? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Mass renaming of unrelated user files to a uniform, unfamiliar "
                    "extension within a very short time window"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Rapid, bulk encryption/renaming of unrelated user files "
                    "to a single new extension is a classic ransomware behavioral "
                    "indicator that routine maintenance does not produce."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deletion of volume shadow copies immediately before the mass "
                    "file changes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ransomware routinely deletes shadow copies/backups "
                    "first to prevent easy recovery; paired with mass encryption, this "
                    "strongly indicates malicious intent rather than legitimate "
                    "administration."
                ),
            },
            {
                "id": "c",
                "text": "The activity was performed using PowerShell, a legitimate administrative tool",
                "correct": False,
                "rationale": (
                    "Incorrect. PowerShell is used constantly for legitimate "
                    "administration; its mere use is not itself an indicator of "
                    "malicious activity without the surrounding destructive context."
                ),
            },
            {
                "id": "d",
                "text": "The events occurred during normal business hours",
                "correct": False,
                "rationale": (
                    "Incorrect. Timing alone (business hours versus after hours) is "
                    "not a reliable indicator of ransomware; both legitimate "
                    "maintenance and real ransomware detonations occur at various "
                    "times, so this fact alone doesn't distinguish malicious from "
                    "routine activity."
                ),
            },
        ],
        "explanation": (
            "Bulk file renaming to a uniform new extension plus deliberate shadow-copy "
            "deletion right before it are the strongest ransomware indicators here; the "
            "tool used and the time of day are not, by themselves, distinguishing "
            "factors."
        ),
    },
    # ------------------------------------------------------------------ #
    # Malware types (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-023",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "Antivirus telemetry shows a file replicating itself across every host on "
            "a subnet by exploiting an unpatched SMB service, with no user opening an "
            "attachment or executing a file on any destination host required. Which "
            "malware type is described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Worm",
                "correct": True,
                "rationale": (
                    "Correct. Self-propagation across a network by exploiting a "
                    "vulnerability, without requiring a user to open or execute "
                    "anything, is the defining trait of a worm."
                ),
            },
            {
                "id": "b",
                "text": "Virus",
                "correct": False,
                "rationale": (
                    "Incorrect. A virus requires a host file and typically needs "
                    "user action, such as opening an infected file, to execute and "
                    "spread; this scenario shows autonomous network propagation with "
                    "no user interaction."
                ),
            },
            {
                "id": "c",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan disguises itself as legitimate software and "
                    "relies on a user being tricked into installing or running it; "
                    "there is no deceptive installation described here, only "
                    "autonomous exploitation of a vulnerable service."
                ),
            },
            {
                "id": "d",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is dormant malicious code embedded in "
                    "existing software that activates on a trigger condition; it does "
                    "not self-propagate across a network as described here."
                ),
            },
        ],
        "explanation": (
            "Autonomous, network-based self-replication through an exploited service, "
            "with no user interaction, is the defining behavior of a worm."
        ),
    },
    {
        "id": "nd2a-024",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "Three weeks after an IT administrator is terminated, a script embedded "
            "in a scheduled task silently deletes all entries in the accounting "
            "database at 2 a.m. on the first day of the fiscal quarter — a date and "
            "time hardcoded into the script months earlier. Which malware type is "
            "this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Logic bomb",
                "correct": True,
                "rationale": (
                    "Correct. Malicious code that lies dormant until a specific "
                    "pre-set condition, such as a hardcoded date and time, triggers "
                    "it is the definition of a logic bomb."
                ),
            },
            {
                "id": "b",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan's defining trait is disguising itself as "
                    "legitimate software to trick a user into running it; this "
                    "scenario centers on a dormant, condition-triggered payload "
                    "already embedded in a scheduled task, not deceptive packaging."
                ),
            },
            {
                "id": "c",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. Worms self-propagate across systems and networks; "
                    "this payload sits dormant on one system waiting for a specific "
                    "date, with no described network-spreading behavior."
                ),
            },
            {
                "id": "d",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit's purpose is to conceal ongoing "
                    "unauthorized access or presence at the OS or kernel level; this "
                    "scenario describes a one-time destructive action triggered by a "
                    "date, not stealthy persistent concealment."
                ),
            },
        ],
        "explanation": (
            "Dormant, condition-triggered destructive code hidden inside an existing "
            "scheduled task is a logic bomb, a common insider-threat payload."
        ),
    },
    {
        "id": "nd2a-025",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types",
        "stem": (
            "A forensic examiner images a compromised server's disk and finds "
            "malicious code embedded in the Master Boot Record that loads a hidden "
            "kernel driver before the operating system itself finishes initializing. "
            "The malware survives a full reinstall of the OS onto the same disk "
            "because the MBR itself is never wiped. Which malware type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bootkit",
                "correct": True,
                "rationale": (
                    "Correct. Malware that infects the boot process, such as the MBR "
                    "or UEFI firmware, to load before and persist beneath the OS, "
                    "surviving OS reinstalls unless the boot sector is wiped, is a "
                    "bootkit."
                ),
            },
            {
                "id": "b",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A standard rootkit typically operates at the OS or "
                    "kernel level after the OS has already loaded, to hide processes "
                    "or files; it doesn't specifically infect the boot record and "
                    "generally would not survive a full OS reinstall the way this "
                    "scenario describes."
                ),
            },
            {
                "id": "c",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is condition-triggered destructive code "
                    "within existing software, not persistent boot-level malware "
                    "providing stealthy concealment."
                ),
            },
            {
                "id": "d",
                "text": "Fileless malware",
                "correct": False,
                "rationale": (
                    "Incorrect. Fileless malware resides and executes in memory or "
                    "the registry rather than as files, but this scenario specifically "
                    "describes persistence in the disk's boot sector, which survives "
                    "reboots and OS reinstalls, unlike typical fileless techniques."
                ),
            },
        ],
        "explanation": (
            "Persistence in the Master Boot Record that loads before the OS and "
            "survives a full OS reinstall on the same disk is the defining trait of a "
            "bootkit, distinct from a standard OS/kernel-level rootkit."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-026",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "A network analyst reviewing switch logs notices that the MAC address "
            "associated with the default gateway's IP address changed three times "
            "within one minute, and multiple hosts on the segment begin sending "
            "internet-bound traffic to an unauthorized workstation instead. Which "
            "attack is MOST likely occurring?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ARP poisoning (on-path attack)",
                "correct": True,
                "rationale": (
                    "Correct. Rapidly shifting MAC-to-IP bindings for the gateway "
                    "address, causing hosts to redirect traffic to an attacker's "
                    "machine, is the signature of ARP cache poisoning enabling an "
                    "on-path/MITM position."
                ),
            },
            {
                "id": "b",
                "text": "DNS poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS poisoning corrupts name-to-IP resolution records, "
                    "not the Layer 2 MAC-to-IP ARP bindings for the gateway itself."
                ),
            },
            {
                "id": "c",
                "text": "DHCP spoofing",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP spoofing involves a rogue DHCP server handing "
                    "out malicious lease configurations to new clients; it would not "
                    "cause an already-configured gateway's MAC binding to rapidly "
                    "change for hosts already on the network."
                ),
            },
            {
                "id": "d",
                "text": "MAC flooding",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC flooding overwhelms a switch's CAM table with "
                    "bogus addresses to force it into hub-like broadcast behavior; it "
                    "doesn't specifically cause the gateway's IP to become bound to a "
                    "new MAC address for redirecting traffic to a chosen host."
                ),
            },
        ],
        "explanation": (
            "Repeated changes to the gateway's ARP binding that redirect traffic to an "
            "attacker-controlled host is the classic pattern of ARP poisoning used to "
            "establish an on-path position."
        ),
    },
    {
        "id": "nd2a-027",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "Packet captures from a compromised segment show gratuitous ARP replies "
            "broadcast every two seconds, each mapping the default gateway's IP "
            "address to the MAC address of a workstation that is not the actual "
            "router; every host on the VLAN subsequently updates its ARP cache to "
            "that MAC address. Which TWO facts from this capture best confirm an ARP "
            "poisoning/on-path attack rather than simple network noise? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The gratuitous ARP replies map the gateway's IP to a MAC address "
                    "that does not belong to the real router"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Binding the legitimate gateway IP to an illegitimate "
                    "MAC address is the core mechanism used to hijack traffic in ARP "
                    "poisoning."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The ARP replies are broadcast repeatedly and unsolicited "
                    "(gratuitous) rather than sent in response to a request"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Legitimate ARP resolution is normally request/"
                    "response; a flood of unsolicited gratuitous replies forcing cache "
                    "updates across the VLAN is a strong indicator of deliberate "
                    "poisoning rather than normal ARP chatter."
                ),
            },
            {
                "id": "c",
                "text": "The traffic was observed on a VLAN, which is inherently insecure",
                "correct": False,
                "rationale": (
                    "Incorrect. VLANs are a standard, generally security-positive "
                    "segmentation mechanism; merely operating on a VLAN is not "
                    "evidence of an attack."
                ),
            },
            {
                "id": "d",
                "text": "ARP is a Layer 2 protocol",
                "correct": False,
                "rationale": (
                    "Incorrect. This is simply a true, general fact about ARP's "
                    "function in the OSI model and has no bearing on whether this "
                    "specific traffic pattern indicates an attack."
                ),
            },
        ],
        "explanation": (
            "The malicious MAC-to-IP binding and the unsolicited, repeated nature of "
            "the gratuitous ARP replies are what distinguish this from benign network "
            "activity — the fact that ARP operates at Layer 2 or that a VLAN is in use "
            "proves nothing on its own."
        ),
    },
    {
        "id": "nd2a-028",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "A DDoS mitigation appliance logs a massive spike of inbound UDP "
            "responses from thousands of distinct public NTP and DNS servers, each "
            "response far larger than the packet that supposedly requested it, all "
            "destined for a single web server's IP address that never sent those "
            "requests. Which attack does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Amplification/reflection attack",
                "correct": True,
                "rationale": (
                    "Correct. Attackers spoof the victim's IP as the source of small "
                    "requests to third-party UDP services like NTP and DNS, which "
                    "send disproportionately large responses to the victim, "
                    "amplifying and reflecting traffic to overwhelm it."
                ),
            },
            {
                "id": "b",
                "text": "SYN flood",
                "correct": False,
                "rationale": (
                    "Incorrect. A SYN flood abuses the TCP three-way handshake with "
                    "half-open connections; this scenario describes UDP responses "
                    "from third-party servers, not TCP SYN packets."
                ),
            },
            {
                "id": "c",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing is an authentication attack "
                    "using stolen credentials against login endpoints, unrelated to "
                    "volumetric UDP traffic flooding a server."
                ),
            },
            {
                "id": "d",
                "text": "ARP poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning operates at Layer 2 within a local "
                    "segment to redirect traffic via false MAC bindings; this "
                    "scenario describes internet-sourced UDP flooding from many "
                    "distinct external servers, not local ARP cache manipulation."
                ),
            },
        ],
        "explanation": (
            "Spoofed small requests to open UDP services that generate large "
            "responses directed at a victim who never sent the requests is the "
            "hallmark of an amplification/reflection DDoS attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Physical attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-029",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A security guard reviewing badge-reader logs and lobby camera footage "
            "notices that a single valid badge swipe by an employee was immediately "
            "followed by two people entering through the same door before it closed, "
            "with no second badge swipe recorded. Which physical attack does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tailgating",
                "correct": True,
                "rationale": (
                    "Correct. An unauthorized person following an authorized badge "
                    "holder through a secured door without presenting their own "
                    "credential is the definition of tailgating (piggybacking)."
                ),
            },
            {
                "id": "b",
                "text": "Badge cloning",
                "correct": False,
                "rationale": (
                    "Incorrect. Badge cloning involves duplicating the RFID/"
                    "proximity credential itself to produce a working fake badge; the "
                    "logs here show only one legitimate swipe, with the second person "
                    "using no badge at all."
                ),
            },
            {
                "id": "c",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing is covertly observing someone "
                    "entering a PIN, password, or other sensitive information, not "
                    "physically following them through a door."
                ),
            },
            {
                "id": "d",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving involves retrieving sensitive "
                    "information from discarded materials or trash, unrelated to "
                    "bypassing a badge-controlled door."
                ),
            },
        ],
        "explanation": (
            "A second person entering on a single valid badge swipe, with no "
            "credential of their own, is the definition of tailgating/piggybacking."
        ),
    },
    {
        "id": "nd2a-030",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A penetration tester uses a handheld device to capture the radio signal "
            "from an employee's proximity access card from a few feet away in a "
            "coffee shop, then uses that captured data to program a blank card that "
            "unlocks the company's front door. Which attack was performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Badge cloning (RFID cloning)",
                "correct": True,
                "rationale": (
                    "Correct. Capturing and duplicating a legitimate proximity/RFID "
                    "credential's signal onto a new physical card to gain "
                    "unauthorized access is badge cloning."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating relies on following an authorized person "
                    "through a door without any credential at all; here the tester "
                    "created and used a working duplicate credential, not physical "
                    "following."
                ),
            },
            {
                "id": "c",
                "text": "Skimming",
                "correct": False,
                "rationale": (
                    "Incorrect. Skimming specifically refers to capturing payment "
                    "card (magnetic stripe/chip) data at a point-of-sale or ATM to "
                    "commit financial fraud, not cloning a building access badge."
                ),
            },
            {
                "id": "d",
                "text": "Environmental attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Environmental attacks target HVAC, power, or other "
                    "facility systems to cause disruption or damage, unrelated to "
                    "duplicating an access credential."
                ),
            },
        ],
        "explanation": (
            "Wirelessly capturing an RFID/proximity credential and duplicating it "
            "onto a blank card is badge cloning, distinct from tailgating (which uses "
            "no credential) or payment-card skimming."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cryptographic attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-031",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A cryptography researcher finds that two completely different input "
            "files, hashed with a legacy algorithm, produce an identical output "
            "digest, allowing a malicious file to be substituted for a trusted one "
            "without detection by hash comparison. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Collision attack",
                "correct": True,
                "rationale": (
                    "Correct. Finding two different inputs that produce the same "
                    "hash output is the definition of a hash collision attack, "
                    "undermining the hash's use for integrity verification."
                ),
            },
            {
                "id": "b",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack is the probabilistic method used "
                    "to find collisions more efficiently than brute force; the "
                    "scenario describes the resulting collision itself being "
                    "exploited, and \"collision attack\" is the precise term for that "
                    "outcome, while \"birthday attack\" names the underlying search "
                    "technique, not what was found and used."
                ),
            },
            {
                "id": "c",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A downgrade attack forces a system to use a weaker, "
                    "older protocol or cipher suite; it doesn't involve finding two "
                    "inputs with matching hash digests."
                ),
            },
            {
                "id": "d",
                "text": "Rainbow table attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Rainbow tables are precomputed hash-to-plaintext "
                    "lookup tables used to reverse a hash back to a likely password, "
                    "not a technique for finding two different inputs that collide to "
                    "the same output."
                ),
            },
        ],
        "explanation": (
            "Two different inputs producing an identical hash digest, exploited to "
            "substitute a malicious file undetected, is a collision attack — the "
            "birthday attack is the statistical method sometimes used to find such "
            "collisions faster, not the outcome being described."
        ),
    },
    {
        "id": "nd2a-032",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A penetration tester intercepts a TLS handshake and forces the client "
            "and server to negotiate SSLv3 instead of TLS 1.2, then exploits a known "
            "weakness in the older protocol to recover plaintext from the encrypted "
            "session. Which attack technique enabled this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Downgrade attack",
                "correct": True,
                "rationale": (
                    "Correct. Forcing a negotiation to fall back to an older, "
                    "weaker protocol or cipher version so a known weakness can be "
                    "exploited is the definition of a downgrade attack."
                ),
            },
            {
                "id": "b",
                "text": "On-path (man-in-the-middle) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. While the attacker is positioned between client and "
                    "server, simply intercepting traffic (on-path) is not what "
                    "enabled the plaintext recovery; the specific technique used was "
                    "forcing weaker protocol negotiation, which is the downgrade "
                    "attack."
                ),
            },
            {
                "id": "c",
                "text": "Replay attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A replay attack involves capturing and resending "
                    "valid data or authentication messages later; this scenario "
                    "involves manipulating protocol version negotiation in real time, "
                    "not resending a captured message."
                ),
            },
            {
                "id": "d",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack targets hash collision "
                    "probability, not protocol version negotiation during a TLS "
                    "handshake."
                ),
            },
        ],
        "explanation": (
            "Forcing a weaker protocol version during negotiation so a known flaw can "
            "be exploited is a downgrade attack; an on-path position enabled it, but "
            "the specific attack technique is the forced downgrade."
        ),
    },
    # ------------------------------------------------------------------ #
    # Log sources and investigative questions (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-033",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "An analyst confirms that malware executed on a workstation and needs to "
            "determine which external command-and-control domain the malware "
            "attempted to contact before the firewall blocked the connection. Which "
            "log source will MOST directly answer this investigative question?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DNS query logs",
                "correct": True,
                "rationale": (
                    "Correct. DNS logs record the domain names a host attempted to "
                    "resolve, directly revealing which C2 domain the malware tried to "
                    "contact even if the connection itself was later blocked."
                ),
            },
            {
                "id": "b",
                "text": "Firewall deny logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs confirm that a connection to an IP and "
                    "port was blocked but typically record IP addresses and ports "
                    "rather than the domain name the malware originally attempted to "
                    "resolve, making DNS logs the more direct source for the domain "
                    "itself."
                ),
            },
            {
                "id": "c",
                "text": "Windows Security Event logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Security Event logs primarily capture "
                    "authentication, account, and local system events; they do not "
                    "record external DNS resolution attempts made by a process."
                ),
            },
            {
                "id": "d",
                "text": "Antivirus quarantine logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine logs show what file was detected and "
                    "blocked and when, but do not typically capture the network "
                    "domain the malware attempted to reach."
                ),
            },
        ],
        "explanation": (
            "To identify a specific C2 domain name a host attempted to resolve, DNS "
            "query logs are the most direct log source, ahead of firewall, security "
            "event, or antivirus logs."
        ),
    },
    {
        "id": "nd2a-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "An incident response team confirms a workstation was compromised and "
            "now needs to determine whether the attacker used the stolen credentials "
            "to authenticate to other systems on the domain. Which log source will "
            "BEST answer this \"where else\" investigative question?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Authentication/domain controller logon logs",
                "correct": True,
                "rationale": (
                    "Correct. Logon event logs on the domain controller directly "
                    "show every system the credential was used to authenticate to, "
                    "answering the lateral-movement question."
                ),
            },
            {
                "id": "b",
                "text": "Web proxy logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Web proxy logs capture outbound HTTP/HTTPS browsing "
                    "activity, not internal Windows domain authentication events "
                    "between hosts."
                ),
            },
            {
                "id": "c",
                "text": "Firewall allow logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs can show that traffic passed between "
                    "hosts on certain ports, but they do not confirm whether an "
                    "authentication event with the stolen credential actually "
                    "succeeded on the destination system."
                ),
            },
            {
                "id": "d",
                "text": "Antivirus logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Antivirus logs report detected malicious files or "
                    "behaviors, not credential-based authentication activity across "
                    "systems."
                ),
            },
        ],
        "explanation": (
            "Confirming where stolen credentials were used to authenticate is best "
            "answered by domain controller/authentication logon logs, which directly "
            "record every successful and failed logon across the domain."
        ),
    },
    # ------------------------------------------------------------------ #
    # Authentication factors and protocols (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "An analyst reviewing Kerberos ticket-granting service (TGS) requests "
            "notices one workstation account requested tickets for an unusually high "
            "number of high-privilege service principal names over a short period, "
            "with no corresponding failed logon attempts anywhere in the environment. "
            "Offline cracking attempts against the captured ticket encryption later "
            "succeed. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Kerberoasting",
                "correct": True,
                "rationale": (
                    "Correct. Requesting TGS tickets for service accounts, which are "
                    "encrypted with the service account's password hash, and cracking "
                    "them offline to recover the plaintext password is the defining "
                    "pattern of Kerberoasting, and it produces no failed logons since "
                    "only ordinary ticket requests occur."
                ),
            },
            {
                "id": "b",
                "text": "Pass-the-hash",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash reuses a captured NTLM hash directly "
                    "to authenticate without knowing the plaintext password; it does "
                    "not involve requesting and offline-cracking Kerberos TGS "
                    "tickets."
                ),
            },
            {
                "id": "c",
                "text": "Golden ticket attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A golden ticket attack forges a Kerberos "
                    "ticket-granting ticket using a compromised krbtgt account hash "
                    "to impersonate any user indefinitely; this scenario describes "
                    "normal TGS ticket requests being harvested and cracked, not a "
                    "forged TGT."
                ),
            },
            {
                "id": "d",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing involves submitting large "
                    "numbers of breached username/password pairs against login "
                    "interfaces, which would typically generate many failed "
                    "authentication attempts — the opposite of what's observed here."
                ),
            },
        ],
        "explanation": (
            "Harvesting TGS tickets for service accounts and cracking them offline, "
            "with no failed logons generated, is the signature of Kerberoasting, "
            "distinct from pass-the-hash, golden tickets, or credential stuffing."
        ),
    },
    {
        "id": "nd2a-036",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "Months after a domain compromise was believed fully remediated, an "
            "attacker is found to still have unrestricted domain administrator access "
            "to any system at any time, without needing to re-authenticate or trigger "
            "any password-related alert, because they possess a forged ticket-"
            "granting ticket signed with the domain's krbtgt account hash. Which "
            "attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Golden ticket attack",
                "correct": True,
                "rationale": (
                    "Correct. Forging a TGT using the compromised krbtgt hash grants "
                    "persistent, unrestricted domain access that survives password "
                    "resets of individual accounts and doesn't require "
                    "re-authentication, which is the defining characteristic of a "
                    "golden ticket attack."
                ),
            },
            {
                "id": "b",
                "text": "Kerberoasting",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberoasting targets individual service account TGS "
                    "tickets to crack their passwords offline; it does not involve "
                    "forging a TGT with the krbtgt hash for persistent, universal "
                    "access."
                ),
            },
            {
                "id": "c",
                "text": "Pass-the-hash",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash reuses an NTLM hash for a specific "
                    "account to authenticate to specific services; it does not "
                    "create a forged, universally trusted Kerberos ticket independent "
                    "of any single account's credentials."
                ),
            },
            {
                "id": "d",
                "text": "Session replay",
                "correct": False,
                "rationale": (
                    "Incorrect. Session replay reuses a previously captured valid "
                    "session token or transaction; this scenario describes a "
                    "cryptographically forged Kerberos ticket built from the domain's "
                    "master key, not a replayed prior session."
                ),
            },
        ],
        "explanation": (
            "A forged TGT built from the krbtgt account's hash, granting persistent, "
            "universal domain access that survives normal remediation, is the "
            "definition of a golden ticket attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Hardening (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "An external scan of a newly deployed server reveals FTP, Telnet, and an "
            "old SNMP service listening and reachable from the internet, none of "
            "which are used by the application the server was built to run. Which "
            "hardening action should be taken FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable or remove the unnecessary services and close their corresponding ports",
                "correct": True,
                "rationale": (
                    "Correct. Eliminating unused services and ports directly "
                    "reduces the attack surface created by exposing unneeded, often "
                    "legacy-insecure protocols with no business need."
                ),
            },
            {
                "id": "b",
                "text": "Apply the latest security patches to the services",
                "correct": False,
                "rationale": (
                    "Incorrect. Patching FTP, Telnet, and SNMP would still leave "
                    "inherently unnecessary services exposed; since the application "
                    "doesn't need them at all, removal or disabling is the more "
                    "direct and complete first hardening step rather than maintaining "
                    "and patching services that shouldn't be running."
                ),
            },
            {
                "id": "c",
                "text": "Move the server behind a web application firewall",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF protects HTTP/HTTPS application traffic and "
                    "would not address unrelated, unnecessary FTP, Telnet, or SNMP "
                    "services still directly listening and exposed."
                ),
            },
            {
                "id": "d",
                "text": "Enable full-disk encryption on the server",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data at rest if the "
                    "physical disk is stolen; it does nothing to reduce the "
                    "network-facing attack surface created by unnecessary running "
                    "services."
                ),
            },
        ],
        "explanation": (
            "The first and most direct hardening step for unused, unnecessary "
            "services is to disable them and close their ports, reducing the attack "
            "surface rather than maintaining, patching, or shielding services that "
            "shouldn't be running at all."
        ),
    },
    {
        "id": "nd2a-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A security team wants every new server deployed with a known, tested, "
            "minimal set of installed software, disabled default accounts, and "
            "consistent configuration settings before it ever reaches production. "
            "Which hardening concept BEST describes this practice?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Secure/golden configuration baseline",
                "correct": True,
                "rationale": (
                    "Correct. Building and deploying systems from a standardized, "
                    "hardened baseline image ensures consistent minimal installation, "
                    "disabled defaults, and known-good configuration across every new "
                    "server."
                ),
            },
            {
                "id": "b",
                "text": "Patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. Patch management addresses applying updates to "
                    "already-deployed systems over time; it doesn't by itself define "
                    "the initial minimal, standardized configuration a server is "
                    "built from."
                ),
            },
            {
                "id": "c",
                "text": "Sandboxing",
                "correct": False,
                "rationale": (
                    "Incorrect. Sandboxing isolates the execution of untrusted code "
                    "or applications from the rest of the system; it doesn't describe "
                    "a standardized initial deployment configuration for new servers."
                ),
            },
            {
                "id": "d",
                "text": "Application allow listing",
                "correct": False,
                "rationale": (
                    "Incorrect. Allow listing restricts which executables are "
                    "permitted to run on an already-running system; it's a runtime "
                    "control, not the initial baseline configuration/build process "
                    "itself."
                ),
            },
        ],
        "explanation": (
            "Deploying every new system from a standardized, minimal, hardened image "
            "is the definition of a secure/golden configuration baseline, distinct "
            "from ongoing patching, runtime sandboxing, or allow listing."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mitigation techniques (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2a-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "A hospital operates a legacy imaging system running an unsupported OS "
            "that cannot be patched without voiding the FDA-certified device "
            "warranty, yet the device must remain connected for clinical use. Which "
            "mitigation technique BEST reduces risk from this unpatchable device?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Network segmentation/isolation",
                "correct": True,
                "rationale": (
                    "Correct. Placing the device on an isolated VLAN with tightly "
                    "controlled access limits its exposure and the blast radius of "
                    "any exploit, compensating for the inability to patch the device "
                    "directly."
                ),
            },
            {
                "id": "b",
                "text": "Patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. Patching is explicitly not possible here without "
                    "voiding the device's regulatory certification, so it isn't a "
                    "viable mitigation for this specific device."
                ),
            },
            {
                "id": "c",
                "text": "Full-disk encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data if the physical media "
                    "is stolen but does nothing to reduce the network-based "
                    "exploitation risk of an unpatched, reachable service."
                ),
            },
            {
                "id": "d",
                "text": "Multifactor authentication on the device",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding MFA to the legacy device is unlikely to be "
                    "supported by its unsupported OS/software and would not address "
                    "the underlying unpatched vulnerability being reachable over the "
                    "network; segmentation addresses the actual exposure."
                ),
            },
        ],
        "explanation": (
            "When a vulnerable system genuinely cannot be patched, isolating/"
            "segmenting it is the standard compensating control to reduce its "
            "exposure and limit the impact of any exploit."
        ),
    },
    {
        "id": "nd2a-040",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "After a malware outbreak was traced to employees downloading and running "
            "unauthorized executables from personal cloud storage links, which "
            "mitigation technique would MOST effectively prevent a recurrence?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Application allow listing",
                "correct": True,
                "rationale": (
                    "Correct. Allow listing permits only pre-approved, known-good "
                    "executables to run, directly blocking unauthorized downloaded "
                    "executables regardless of their source."
                ),
            },
            {
                "id": "b",
                "text": "Full-disk encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data confidentiality if a "
                    "device is lost or stolen; it has no effect on preventing an "
                    "unauthorized executable from running."
                ),
            },
            {
                "id": "c",
                "text": "Patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. Patching addresses known vulnerabilities in "
                    "existing software; it wouldn't stop a user from intentionally "
                    "downloading and executing an entirely new, unauthorized program."
                ),
            },
            {
                "id": "d",
                "text": "Network segmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation limits lateral movement and blast "
                    "radius after compromise but doesn't directly prevent a user "
                    "from executing an unauthorized downloaded file on their own "
                    "endpoint in the first place."
                ),
            },
        ],
        "explanation": (
            "To directly prevent unauthorized executables from running regardless of "
            "how they arrive on an endpoint, application allow listing is the most "
            "effective mitigation."
        ),
    },
]

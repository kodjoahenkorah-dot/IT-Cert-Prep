"""
CompTIA A+ Core 1 (220-1201) — Domain 1: Mobile Devices
30 practice questions at hard/expert difficulty (v3 set).
"""

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # 1 — Laptop hardware
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician opens a laptop to install a second SODIMM module and notices "
            "the existing module is installed in Slot B while Slot A is empty. The "
            "system has been running with only one module. After installing an identical "
            "DDR4-3200 SODIMM in Slot A, the BIOS still reports single-channel mode. "
            "The technician verifies both modules are fully seated. What is the MOST "
            "likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The two SODIMMs are from different manufacturers, which prevents dual-channel operation on all platforms.",
                "correct": False,
                "rationale": (
                    "Incorrect. Dual-channel operation does not require identical "
                    "manufacturer; it requires compatible speed, capacity, and correct "
                    "slot placement. Different manufacturers alone do not prevent "
                    "dual-channel mode."
                ),
            },
            {
                "id": "b",
                "text": "Some laptop platforms require the first module to be installed in Slot A (the primary slot), and installing in Slot B first can cause the firmware to map both modules to the same channel.",
                "correct": True,
                "rationale": (
                    "Correct. Certain laptop platforms (particularly Intel-based systems) "
                    "require the primary SODIMM slot (often labeled Slot 0 or Slot A) to "
                    "be populated first. If the original module was in Slot B and the "
                    "firmware maps both slots to channel 0 in that configuration, moving "
                    "the original module to Slot A and placing the new module in Slot B "
                    "is necessary to achieve dual-channel operation. The technician should "
                    "consult the service manual for correct dual-channel slot pairing."
                ),
            },
            {
                "id": "c",
                "text": "DDR4-3200 SODIMMs cannot run in dual-channel mode because DDR4 supports only single-channel in the mobile form factor.",
                "correct": False,
                "rationale": (
                    "Incorrect. DDR4 SODIMM absolutely supports dual-channel mode. The "
                    "form factor does not restrict channel capability; the memory "
                    "controller and slot wiring determine channel configuration."
                ),
            },
            {
                "id": "d",
                "text": "The new SODIMM needs to be formatted with a disk utility before the memory controller will recognize it as dual-channel.",
                "correct": False,
                "rationale": (
                    "Incorrect. RAM cannot be 'formatted.' Memory modules are recognized "
                    "and configured by the memory controller at POST; no disk utility "
                    "operation is applicable or required."
                ),
            },
        ],
        "explanation": (
            "Most dual-channel laptop platforms require the primary slot (Slot A / Slot 0) "
            "to be populated. When only one module is installed, placing it in the secondary "
            "slot can cause the memory controller to reference incorrect channel assignments. "
            "The correct configuration for dual-channel is one module in each channel's "
            "designated slot. Always refer to the OEM service manual for slot population "
            "rules before purchasing and installing additional memory."
        ),
    },
    # ------------------------------------------------------------------ #
    # 2 — Mobile display components
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-002",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile display components",
        "stem": (
            "A technician is replacing a cracked display assembly on a laptop. The OEM "
            "part number specifies an IPS panel with 400 nits brightness and 100% sRGB "
            "color gamut. The supplier offers a compatible-fit TN panel at half the price "
            "with 250 nits and 45% NTSC color gamut. The laptop owner is a professional "
            "photographer who edits images on-screen. Which statement BEST advises the "
            "technician?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Install the TN panel; color accuracy differences are imperceptible in practice and the cost saving is significant.",
                "correct": False,
                "rationale": (
                    "Incorrect. TN panels exhibit severe color shift at off-axis viewing "
                    "angles, lower color gamut coverage (~45% NTSC ≈ ~67% sRGB), and "
                    "reduced brightness. For a professional photographer these differences "
                    "are absolutely perceptible and professionally consequential."
                ),
            },
            {
                "id": "b",
                "text": "The TN panel's 45% NTSC gamut covers more colors than 100% sRGB, so it is actually a superior choice for color work.",
                "correct": False,
                "rationale": (
                    "Incorrect. 45% NTSC is approximately 67% sRGB — it covers fewer "
                    "colors, not more. 100% sRGB coverage is the professional minimum for "
                    "photo editing. This is a common unit-confusion trap."
                ),
            },
            {
                "id": "c",
                "text": "The OEM IPS panel should be sourced; the reduced color gamut, lower brightness, and poor viewing angles of the TN panel are unacceptable for professional photo editing.",
                "correct": True,
                "rationale": (
                    "Correct. Professional photographers require accurate color reproduction "
                    "(wide gamut, high accuracy), sufficient brightness for shadow detail, "
                    "and consistent color at various viewing angles. IPS panels provide all "
                    "three; TN panels do not. The technician should source the correct OEM "
                    "or equivalent-spec IPS replacement, not the TN alternative."
                ),
            },
            {
                "id": "d",
                "text": "Either panel is acceptable because the GPU outputs the same signal regardless of which panel is installed.",
                "correct": False,
                "rationale": (
                    "Incorrect. While the GPU signal is panel-agnostic, the physical "
                    "characteristics of the panel — color gamut, viewing angles, brightness "
                    "— directly determine what the user sees. An inferior panel will "
                    "produce inferior results regardless of GPU output quality."
                ),
            },
        ],
        "explanation": (
            "Display panel comparison for professional use: IPS offers wide viewing angles "
            "(near 178°), high color accuracy, and broader gamut coverage — suitable for "
            "color-critical work. TN offers fast response times but narrow viewing angles, "
            "poor color reproduction, and limited gamut. 45% NTSC ≈ 67% sRGB, well below the "
            "100% sRGB minimum for photo editing. When replacing displays, matching panel "
            "technology is important when the user's workflow depends on accurate color."
        ),
    },
    # ------------------------------------------------------------------ #
    # 3 — Mobile connection types & ports
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-003",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A technician needs to connect a modern laptop (USB-C only, no legacy ports) "
            "to an older projector that accepts only a VGA signal. The technician has a "
            "USB-C to HDMI adapter and a separate HDMI to VGA converter in her toolkit. "
            "She chains them together: Laptop USB-C → USB-C-to-HDMI adapter → HDMI-to-VGA "
            "converter → projector. The projector receives no signal. She confirms the "
            "USB-C port supports DisplayPort Alt Mode. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "HDMI and VGA use the same signaling; chaining the adapters doubles the signal level and overdrives the projector's input.",
                "correct": False,
                "rationale": (
                    "Incorrect. HDMI is a digital signal; VGA is an analog signal. They do "
                    "not use the same signaling and cannot be passively combined. There is "
                    "no 'double signal' effect from chaining adapters."
                ),
            },
            {
                "id": "b",
                "text": "The HDMI-to-VGA converter is passive and cannot convert a digital HDMI signal to analog VGA without an active conversion chip; a powered (active) HDMI-to-VGA adapter is required.",
                "correct": True,
                "rationale": (
                    "Correct. HDMI carries a digital (TMDS) signal. VGA is an analog signal. "
                    "Converting between them requires active digital-to-analog conversion "
                    "circuitry with a DAC. A passive cable or passive adapter cannot perform "
                    "this conversion. The technician needs an active HDMI-to-VGA adapter "
                    "with an internal DAC (and often requires USB bus power or a separate "
                    "power source)."
                ),
            },
            {
                "id": "c",
                "text": "USB-C Alt Mode supports DisplayPort but not HDMI, so the USB-C-to-HDMI adapter produces no output.",
                "correct": False,
                "rationale": (
                    "Incorrect. USB-C Alt Mode supports HDMI output via an HDMI Alt Mode "
                    "adapter or a DisplayPort-to-HDMI active adapter. USB-C to HDMI adapters "
                    "are widely available and functional. The problem is not at the USB-C–to-"
                    "HDMI step."
                ),
            },
            {
                "id": "d",
                "text": "VGA projectors require a DVI-to-VGA adapter as an intermediate step; HDMI-to-VGA direct conversion is not supported by any adapter.",
                "correct": False,
                "rationale": (
                    "Incorrect. Active HDMI-to-VGA adapters do exist and work correctly when "
                    "they contain an internal DAC. DVI-to-VGA adapters (passive) work because "
                    "DVI-A and DVI-I carry an analog signal on the same connector; HDMI does "
                    "not carry an analog signal natively."
                ),
            },
        ],
        "explanation": (
            "HDMI outputs a digital TMDS (Transition-Minimized Differential Signaling) signal. "
            "VGA inputs require an analog RGB signal. Converting HDMI to VGA requires an active "
            "adapter containing a digital-to-analog converter (DAC) chip. Passive HDMI-to-VGA "
            "'cables' or simple passive adapters do not work. Active HDMI-to-VGA adapters are "
            "commonly powered via USB Micro-B or USB-C. This is a common field troubleshooting "
            "trap; always verify whether an adapter is active (contains a DAC/converter chip) "
            "or passive before purchasing."
        ),
    },
    # ------------------------------------------------------------------ #
    # 4 — Laptop hardware
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-004",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is tasked with replacing the thermal paste on an overheating "
            "laptop CPU. After removing the heat sink, the technician applies a large "
            "bead of paste in the center of the IHS (Integrated Heat Spreader) and "
            "reinstalls the heat sink tightly. After reassembly, CPU temperatures are "
            "even higher than before the repair. Which application error MOST likely "
            "explains the worsened thermal performance?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Thermal paste was applied too thinly; a thick application is required to fill all air gaps between the CPU and heat sink.",
                "correct": False,
                "rationale": (
                    "Incorrect. Thermal paste is designed to fill microscopic surface "
                    "imperfections, not to serve as a thick thermal pad. Excess paste "
                    "actually increases thermal resistance because paste conducts heat "
                    "worse than direct metal-to-metal contact. Thick application worsens, "
                    "not improves, heat transfer."
                ),
            },
            {
                "id": "b",
                "text": "A large bead of paste likely pushed air bubbles to the edges but left a void in the center under pressure, creating insulating air pockets.",
                "correct": False,
                "rationale": (
                    "Incorrect. A single bead in the center is actually a common recommended "
                    "application method (the 'pea method') that spreads evenly under heat "
                    "sink pressure. While poor spreading can leave voids, this is less likely "
                    "to cause dramatically higher temperatures than excessive paste volume."
                ),
            },
            {
                "id": "c",
                "text": "Excess paste squeezed out from under the heat sink and contacted adjacent capacitors or inductors, potentially causing electrical shorts that increase power dissipation.",
                "correct": True,
                "rationale": (
                    "Correct. Applying too large a bead causes paste to squeeze out under "
                    "the heat sink when it is tightened. If electrically conductive or semi-"
                    "conductive paste contacts nearby SMD components (capacitors, inductors, "
                    "MOSFETs) it can create partial shorts or leakage paths that increase "
                    "current draw and power dissipation, causing higher temperatures. Even "
                    "non-conductive paste can thermally insulate components that are supposed "
                    "to dissipate heat through the PCB. Excess paste should be cleaned up "
                    "with isopropyl alcohol before reassembly."
                ),
            },
            {
                "id": "d",
                "text": "The heat sink screws were overtightened, cracking the CPU die, which reduced thermal conductivity through the IHS.",
                "correct": False,
                "rationale": (
                    "Incorrect. Overtightening heat sink screws can bow the heat sink or "
                    "crack a bare die (on delidded CPUs), but laptop CPUs have an IHS that "
                    "distributes pressure. Cracking a laptop CPU die from normal heat sink "
                    "reinstallation is extremely rare. The excess paste scenario is far more "
                    "probable given the described application method."
                ),
            },
        ],
        "explanation": (
            "Thermal paste application: the goal is the thinnest possible uniform layer to "
            "fill microscopic surface imperfections. Excess paste increases thermal resistance "
            "(paste conducts worse than metal) and risks contaminating adjacent components. "
            "If electrically conductive paste (e.g., silver-based) contacts SMD components, "
            "it can cause partial shorts. Best practices: clean both surfaces with IPA, apply "
            "a pea-sized bead for the 'spread-under-pressure' method, or pre-spread a thin "
            "uniform layer. Wipe away any squeeze-out before closing the chassis."
        ),
    },
    # ------------------------------------------------------------------ #
    # 5 — Mobile email configuration
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-005",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile email configuration",
        "stem": (
            "A user configures a new Android phone to access corporate email using "
            "Microsoft Exchange ActiveSync. The phone successfully receives new email "
            "but cannot send messages; outgoing mail fails with 'Authentication required'. "
            "Incoming IMAP settings are confirmed correct. Which configuration is MOST "
            "likely missing or incorrect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The Exchange ActiveSync URL is pointing to the wrong autodiscover endpoint.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the ActiveSync URL were wrong, both sending and receiving "
                    "would fail. The scenario states receiving works, ruling out an incorrect "
                    "server address as the cause of the send-only failure."
                ),
            },
            {
                "id": "b",
                "text": "The outgoing SMTP server settings require authentication (username and password or OAuth token) that have not been configured for the send account.",
                "correct": True,
                "rationale": (
                    "Correct. 'Authentication required' on outgoing mail means the SMTP "
                    "server is rejecting the connection because valid credentials were not "
                    "presented. Microsoft Exchange requires SMTP AUTH to be enabled and "
                    "the correct account credentials (or a modern auth token) must be "
                    "provided for outgoing mail. The technician must configure the SMTP "
                    "authentication settings in the email account's outgoing server setup."
                ),
            },
            {
                "id": "c",
                "text": "The Exchange server requires a client-side S/MIME certificate to encrypt all outgoing messages before they are accepted.",
                "correct": False,
                "rationale": (
                    "Incorrect. S/MIME certificates are optional and are used for message "
                    "signing and encryption, not for SMTP authentication. Lack of an S/MIME "
                    "certificate produces a different error than 'Authentication required'."
                ),
            },
            {
                "id": "d",
                "text": "The device OS version is too old to support Exchange ActiveSync for outgoing mail and must be updated.",
                "correct": False,
                "rationale": (
                    "Incorrect. Exchange ActiveSync has been supported on Android since early "
                    "versions. An OS version issue would typically prevent all Exchange "
                    "functionality, not just outgoing mail. The specific 'Authentication "
                    "required' error points to a credentials or auth configuration issue, "
                    "not an OS compatibility problem."
                ),
            },
        ],
        "explanation": (
            "SMTP servers at corporate Exchange deployments require authenticated connections "
            "to prevent open relay. If outgoing mail settings lack proper authentication "
            "credentials (username/password for basic auth, or OAuth 2.0 token for modern "
            "auth), the server returns an authentication error. IMAP (incoming) and SMTP "
            "(outgoing) have separate authentication configurations in mobile email clients; "
            "correct incoming settings do not automatically configure outgoing authentication. "
            "Exchange Online (Office 365) requires modern auth (OAuth 2.0) or SMTP AUTH "
            "explicitly enabled per-mailbox."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6 — Mobile network connectivity
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-006",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile network connectivity",
        "stem": (
            "A user's Android smartphone can browse the web on Wi-Fi and make phone calls "
            "on cellular, but mobile data (internet over cellular) does not work at all. "
            "The carrier confirms the account is active with a data plan. The SIM is "
            "recognized and cellular signal is strong. Which configuration element should "
            "the technician check FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The Wi-Fi frequency band; 5 GHz Wi-Fi can interfere with LTE Band 41 and block cellular data.",
                "correct": False,
                "rationale": (
                    "Incorrect. Wi-Fi at 5 GHz and LTE Band 41 (2,500 MHz) operate at "
                    "different frequencies and power levels; consumer Wi-Fi does not "
                    "meaningfully interfere with cellular data reception. This is not a "
                    "valid troubleshooting path."
                ),
            },
            {
                "id": "b",
                "text": "The APN (Access Point Name) settings; an incorrect or missing APN prevents the device from establishing a data bearer to the carrier's network.",
                "correct": True,
                "rationale": (
                    "Correct. The APN tells the device how to connect to the carrier's "
                    "packet data gateway. If the APN is missing, corrupted, or incorrect "
                    "(wrong APN name, MCC/MNC, or authentication type), the device can "
                    "register for voice and SMS on the cellular network but cannot "
                    "establish a data connection. Resetting to carrier defaults or "
                    "manually entering the carrier's APN resolves this."
                ),
            },
            {
                "id": "c",
                "text": "The device's Bluetooth is enabled; Bluetooth shares the 2.4 GHz spectrum with LTE and must be disabled for cellular data to work.",
                "correct": False,
                "rationale": (
                    "Incorrect. While Bluetooth and Wi-Fi share the 2.4 GHz ISM band, they "
                    "use different protocols from LTE, which operates on licensed spectrum "
                    "(700 MHz, 1700 MHz, 2100 MHz, etc. depending on band). Bluetooth state "
                    "does not affect cellular data connectivity."
                ),
            },
            {
                "id": "d",
                "text": "The screen timeout setting; if the screen locks too quickly it disconnects the cellular data session.",
                "correct": False,
                "rationale": (
                    "Incorrect. Screen timeout affects the display and may suspend some "
                    "app background activity, but it does not disconnect the cellular data "
                    "registration or prevent mobile data from functioning. This is not a "
                    "cause of cellular data failure."
                ),
            },
        ],
        "explanation": (
            "The APN (Access Point Name) is the gateway between the cellular network and the "
            "internet. Every cellular carrier requires a correctly configured APN for data "
            "services. Voice calls and SMS use circuit-switched or IMS channels that don't "
            "require the APN, so a device with a wrong APN can still make calls but not use "
            "mobile data. APN settings are usually auto-provisioned when the SIM is inserted, "
            "but can become corrupted or may need manual entry after a factory reset, OS "
            "update, or carrier migration."
        ),
    },
    # ------------------------------------------------------------------ #
    # 7 — Bluetooth pairing
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-007",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Bluetooth pairing",
        "stem": (
            "A user's Bluetooth keyboard was paired to a tablet and worked correctly for "
            "months. After the tablet received an OS update, the keyboard stopped "
            "responding. The keyboard appears in the device's Bluetooth settings as "
            "'Paired' but not 'Connected'. Turning the keyboard off and on does not help. "
            "Which action should the technician take FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace the keyboard batteries; low battery voltage is the most common cause of Bluetooth pairing loss after OS updates.",
                "correct": False,
                "rationale": (
                    "Incorrect. While low batteries can cause disconnections, the scenario "
                    "states the keyboard appears as 'Paired' in Bluetooth settings — "
                    "indicating the radio is functioning. Battery replacement is a reasonable "
                    "step but not the most targeted first action for an OS-update-correlated "
                    "pairing issue where the device is visible."
                ),
            },
            {
                "id": "b",
                "text": "Remove (unpair/forget) the keyboard from the tablet's Bluetooth settings, then re-pair it from scratch.",
                "correct": True,
                "rationale": (
                    "Correct. OS updates can invalidate stored Bluetooth link keys or change "
                    "the Bluetooth stack configuration in ways that leave an old pairing "
                    "record in place but non-functional. Removing the pairing from both the "
                    "tablet and keyboard (entering pairing mode on the keyboard) and performing "
                    "a fresh Secure Simple Pairing clears any stale cryptographic state and "
                    "re-establishes a clean connection."
                ),
            },
            {
                "id": "c",
                "text": "Downgrade the tablet OS to the previous version to restore Bluetooth compatibility with the keyboard.",
                "correct": False,
                "rationale": (
                    "Incorrect. Downgrading an OS is a drastic, potentially unsupported "
                    "action with security implications. A stale pairing record is far more "
                    "likely to cause this symptom and is resolved by re-pairing — a simple "
                    "non-destructive step that should be tried first."
                ),
            },
            {
                "id": "d",
                "text": "Place both devices in airplane mode simultaneously for 60 seconds to force a Bluetooth controller reset on both.",
                "correct": False,
                "rationale": (
                    "Incorrect. Airplane mode disables radios including Bluetooth but does "
                    "not clear pairing records or cryptographic link keys. Re-enabling "
                    "Bluetooth after airplane mode would restore the same broken pairing "
                    "state. This does not address the root cause."
                ),
            },
        ],
        "explanation": (
            "Bluetooth pairings store a shared link key for authentication. OS updates can "
            "alter the Bluetooth host controller interface (HCI) stack, invalidate stored keys, "
            "or change profile priorities. When a previously working device appears 'Paired' "
            "but not 'Connected' after an update, the established fix is to remove the pairing "
            "on the host device, reset the peripheral to pairing mode (clearing its stored key), "
            "and perform a fresh pairing. This re-establishes a valid shared key under the "
            "updated Bluetooth stack."
        ),
    },
    # ------------------------------------------------------------------ #
    # 8 — MDM/MAM
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-008",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "MDM/MAM",
        "stem": (
            "A healthcare organization issues company-owned iPhones to nurses. Regulations "
            "require that all protected health information (PHI) stored on devices must be "
            "encrypted at rest, devices must auto-lock after 2 minutes of inactivity, and "
            "the organization must be able to wipe any device instantly if lost. Which MDM "
            "capability combination BEST satisfies all three requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable iCloud Backup for all devices; iCloud encrypts backup data at rest, provides device management, and allows remote erase via Find My.",
                "correct": False,
                "rationale": (
                    "Incorrect. iCloud Backup is a consumer service controlled by the "
                    "individual Apple ID, not by the organization. It does not enforce "
                    "auto-lock policies, does not provide enterprise-grade PHI encryption "
                    "controls, and remote erase via Find My is tied to the user's personal "
                    "Apple ID, not the organization's MDM. iCloud Backup of PHI may also "
                    "violate HIPAA data residency requirements."
                ),
            },
            {
                "id": "b",
                "text": "Enroll devices in an MDM solution (e.g., Apple Business Manager with Jamf or Intune) and push a configuration profile enforcing: device encryption, a 2-minute auto-lock policy, and remote wipe capability.",
                "correct": True,
                "rationale": (
                    "Correct. Enterprise MDM with Apple Business Manager (ABM) / Automated "
                    "Device Enrollment (ADE) allows the organization to enforce iOS "
                    "configuration profiles that mandate encryption (native on all iPhones "
                    "with a passcode), auto-lock intervals, and provides the MDM admin with "
                    "remote wipe (selective or full) capability independent of the user's "
                    "Apple ID. This satisfies all three regulatory requirements."
                ),
            },
            {
                "id": "c",
                "text": "Install a VPN app on each device; VPN encryption protects data at rest and in transit, and the VPN server can remotely disable device access.",
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN encrypts data in transit between the device and the "
                    "VPN server; it does not encrypt data at rest on the device's storage. "
                    "A VPN server cannot enforce auto-lock policies or remotely wipe a "
                    "device. VPN access revocation is not equivalent to a device wipe."
                ),
            },
            {
                "id": "d",
                "text": "Deploy S/MIME certificates via email to each nurse; S/MIME encrypts data at rest and allows the server to revoke certificates to disable all device access.",
                "correct": False,
                "rationale": (
                    "Incorrect. S/MIME encrypts email message content in transit and at "
                    "rest within the mail client, but it does not encrypt the device's "
                    "entire storage, enforce auto-lock, or provide remote wipe capability. "
                    "Certificate revocation prevents future S/MIME-signed messages from "
                    "being trusted but does not wipe the device or block device access."
                ),
            },
        ],
        "explanation": (
            "For healthcare device management, enterprise MDM (Apple Business Manager + MDM "
            "solution like Microsoft Intune or Jamf) enrolled via Automated Device Enrollment "
            "(ADE/DEP) provides: enforced passcode/encryption (iOS encrypts storage when a "
            "passcode is set, satisfying HIPAA data-at-rest requirements); configuration "
            "profiles that mandate auto-lock timeout; and MDM-initiated remote wipe independent "
            "of the user's Apple ID. Consumer solutions (iCloud, VPN, S/MIME alone) do not "
            "satisfy enterprise compliance requirements."
        ),
    },
    # ------------------------------------------------------------------ #
    # 9 — Mobile synchronization
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-009",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile synchronization",
        "stem": (
            "A user's Android phone synchronizes Gmail contacts to the phone's native "
            "Contacts app. She installs a new third-party CRM app that creates local "
            "contacts on the device. Two weeks later, she notices none of the CRM app "
            "contacts appear in Gmail Contacts on the web. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gmail synchronization requires a paid Google Workspace account; contacts sync is not available on free accounts.",
                "correct": False,
                "rationale": (
                    "Incorrect. Gmail contact synchronization is available on free Google "
                    "accounts. Google Contacts syncs via the Google account sync framework "
                    "regardless of Workspace subscription status."
                ),
            },
            {
                "id": "b",
                "text": "The CRM app is saving contacts to the device's local storage account rather than to the user's Google account, so they are not synchronized to Google Contacts.",
                "correct": True,
                "rationale": (
                    "Correct. Android supports multiple contact storage accounts: the "
                    "Google account (synced to cloud), the device/local account (stored only "
                    "on-device), and third-party accounts (CRM, Exchange, etc.). If the CRM "
                    "app creates contacts under a local or app-specific account rather than "
                    "the Google account, those contacts never enter the Google sync framework "
                    "and do not appear in Gmail Contacts. The solution is to move or import "
                    "contacts into the Google account, or configure the CRM to sync via "
                    "Google Contacts API."
                ),
            },
            {
                "id": "c",
                "text": "Google contact sync is disabled during the first 30 days after a new app installation for privacy reasons.",
                "correct": False,
                "rationale": (
                    "Incorrect. Google does not impose a 30-day sync delay for newly installed "
                    "apps. Contact synchronization is continuous and not gated by app "
                    "installation timing."
                ),
            },
            {
                "id": "d",
                "text": "The phone's background data restriction is enabled, preventing all contact sync until Wi-Fi is connected.",
                "correct": False,
                "rationale": (
                    "Incorrect. Background data restriction would affect all sync equally — "
                    "including Gmail contacts that already sync correctly. The scenario states "
                    "Gmail contacts sync works; only CRM contacts are missing, pointing to an "
                    "account storage issue rather than a background data restriction."
                ),
            },
        ],
        "explanation": (
            "Android stores contacts in 'accounts' within its Contacts content provider: the "
            "Google account (cloud-synced), the device/phone account (local-only), and any "
            "third-party accounts (Exchange, Facebook, CRM apps). Only contacts stored under "
            "the Google account are synced to Google Contacts on the web. When a third-party "
            "app creates contacts in its own account or the local device account, they appear "
            "in the native Contacts app (if merged view is enabled) but never sync to Google. "
            "The user must configure the CRM to use the Google account as the target store, "
            "or copy/export contacts from the local account to Google."
        ),
    },
    # ------------------------------------------------------------------ #
    # 10 — Location services
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-010",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Location services",
        "stem": (
            "A company deploys field service smartphones and wants to track technician "
            "locations in real time for dispatch purposes. The IT manager suggests enabling "
            "GPS only in the location settings to maximize battery life. A field tech "
            "reports the dispatch app can't get a location lock when working inside large "
            "metal warehouses. Which BEST explains the issue and recommends a solution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "GPS is blocked by metal roofs; enabling 'High accuracy' mode (GPS + Wi-Fi + cellular) allows the device to use Wi-Fi positioning as a fallback when GPS is unavailable indoors.",
                "correct": True,
                "rationale": (
                    "Correct. GPS signals (L1: 1575.42 MHz) are attenuated by metal "
                    "structures and cannot penetrate metal-roofed warehouses reliably. "
                    "'High accuracy' (or 'Google Location Services') mode uses GPS when "
                    "available and automatically falls back to Wi-Fi positioning (using "
                    "nearby AP BSSIDs) and cellular tower estimates when GPS is unavailable. "
                    "This provides location data indoors at the cost of slightly higher "
                    "battery usage."
                ),
            },
            {
                "id": "b",
                "text": "The smartphones need an external GNSS antenna connected via USB-C to penetrate the metal structure.",
                "correct": False,
                "rationale": (
                    "Incorrect. External GNSS antennas can improve GPS sensitivity outdoors "
                    "but will not penetrate a metal-shielded environment where GPS signals "
                    "are fundamentally blocked regardless of antenna gain. Wi-Fi or cellular "
                    "positioning is the correct solution for indoor tracking."
                ),
            },
            {
                "id": "c",
                "text": "Enabling Bluetooth on the device allows it to triangulate position from nearby Bluetooth MAC addresses with the same accuracy as GPS.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth-based positioning (using device MAC addresses) "
                    "does exist as part of location fusion on some platforms, but it provides "
                    "very coarse location data and is far less accurate than Wi-Fi positioning. "
                    "It does not match GPS accuracy and is not equivalent to it."
                ),
            },
            {
                "id": "d",
                "text": "Location services should be disabled entirely for field devices as they create a privacy liability; dispatch should use manual check-in instead.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling location services eliminates real-time tracking "
                    "entirely, which directly contradicts the business requirement. Privacy "
                    "considerations for company-owned dispatch devices are addressed through "
                    "policy (e.g., location data only during work hours) — not by disabling "
                    "location tracking altogether."
                ),
            },
        ],
        "explanation": (
            "GPS satellite signals (L-band, ~1.5 GHz) are blocked or severely attenuated by "
            "metal roofs and dense building materials. 'GPS only' mode will fail indoors. "
            "'High accuracy' mode (Android) / 'Precise location' (iOS) combines GPS, Wi-Fi "
            "positioning (BSSID-based), and cellular tower data. When inside a warehouse, "
            "the OS automatically falls back to Wi-Fi positioning, which can achieve 15–40 m "
            "accuracy — sufficient for dispatch purposes — without GPS satellite visibility. "
            "The trade-off is slightly higher battery consumption from Wi-Fi radio scanning."
        ),
    },
    # ------------------------------------------------------------------ #
    # 11 — Laptop hardware
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-011",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is asked to expand storage in a corporate laptop that has a "
            "single occupied 2.5-inch SATA III bay and an unused M.2 slot. The M.2 slot "
            "is documented as 'PCIe Gen 3 x4, NVMe only' in the service manual. The "
            "technician sources an M.2 2280 drive that supports both SATA and NVMe "
            "(B+M key notch). After installation, the BIOS does not detect the new drive. "
            "What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The M.2 2280 form factor is incompatible with this laptop's M.2 slot; a 2242 drive is required.",
                "correct": False,
                "rationale": (
                    "Incorrect. The form factor designation (2280 = 22 mm × 80 mm) describes "
                    "physical dimensions and is independent of interface. If the slot is a "
                    "standard M.2 slot, it typically accommodates 2280 drives. Form factor "
                    "mismatch alone would not prevent detection; the drive simply would not "
                    "fit physically."
                ),
            },
            {
                "id": "b",
                "text": "The drive defaulted to SATA mode at startup; the BIOS cannot detect it because the M.2 slot provides only PCIe/NVMe signals with no SATA lanes.",
                "correct": True,
                "rationale": (
                    "Correct. Dual-mode B+M key drives typically boot in SATA mode unless "
                    "the host system drives them into NVMe mode via PCIe signals. If the "
                    "slot is wired exclusively for PCIe NVMe (no SATA M.2 support), and the "
                    "drive powers up in SATA mode (which many do by default), the BIOS will "
                    "not detect it because no SATA signaling exists on those pins. The "
                    "technician needs a single-mode NVMe-only M.2 drive for this slot."
                ),
            },
            {
                "id": "c",
                "text": "Both storage devices cannot coexist; the laptop supports only one storage device and disables the M.2 slot when the SATA bay is occupied.",
                "correct": False,
                "rationale": (
                    "Incorrect. Most laptops with both a 2.5-inch SATA bay and an M.2 slot "
                    "support both devices simultaneously with independent controllers. Some "
                    "budget platforms share bandwidth but do not disable the slot entirely "
                    "when both are populated."
                ),
            },
            {
                "id": "d",
                "text": "NVMe drives require a driver to be pre-installed in the OS before the BIOS can detect them during POST.",
                "correct": False,
                "rationale": (
                    "Incorrect. BIOS detection of NVMe drives happens at the hardware level "
                    "during POST, before any OS driver is loaded. NVMe is supported natively "
                    "by UEFI firmware via the NVMe UEFI driver. OS drivers are only needed "
                    "for OS-level access (e.g., legacy BIOS environments needing an NVMe "
                    "option ROM, but that is not the issue here)."
                ),
            },
        ],
        "explanation": (
            "M.2 drives with a B+M key notch are physically compatible with both B-key (SATA) "
            "and M-key (PCIe/NVMe) slots, but the underlying electrical interface still matters. "
            "Many B+M key combo drives initialize in SATA mode by default, requiring the host "
            "to supply PCIe signals to engage NVMe mode. An M.2 slot documented as 'PCIe Gen 3 "
            "x4, NVMe only' supplies PCIe signals but no SATA — so a drive stuck in SATA init "
            "mode will not be detected. For NVMe-only slots, always use a single-mode NVMe M.2 "
            "drive to avoid this initialization ambiguity."
        ),
    },
    # ------------------------------------------------------------------ #
    # 12 — Mobile display components
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-012",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile display components",
        "stem": (
            "A user reports that their OLED laptop display develops a persistent ghost "
            "image of the taskbar after the laptop is used for 8 hours a day with the "
            "taskbar always visible. The image is only visible on dark backgrounds and "
            "disappears after the display shows a bright white screen for several minutes. "
            "Which condition is described and what is the BEST long-term mitigation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "This is image retention (temporary burn-in); the BEST mitigation is to set a screen timeout of 2 minutes and enable a screen saver to prevent static elements from dwelling on the screen.",
                "correct": True,
                "rationale": (
                    "Correct. OLED pixels degrade at different rates depending on usage "
                    "intensity. Static UI elements (taskbar, menu bars) cause uneven pixel "
                    "wear, leading to image retention (temporary) or permanent burn-in "
                    "over time. A short screen timeout and screen saver (or moving taskbar "
                    "auto-hide) reduce the amount of time static content dwells on any "
                    "individual pixel, mitigating the differential aging effect."
                ),
            },
            {
                "id": "b",
                "text": "This is a GPU artifact caused by a failing discrete graphics card; replacing the GPU eliminates the ghost image.",
                "correct": False,
                "rationale": (
                    "Incorrect. GPU artifacts typically manifest as corruption, colored "
                    "blocks, or flickering across the entire display — not as a persistent "
                    "faint outline of a specific static UI element only visible on dark "
                    "backgrounds. The described symptom is characteristic of OLED image "
                    "retention, not GPU failure."
                ),
            },
            {
                "id": "c",
                "text": "This is backlight bleed from the OLED panel's LED backlight; replacing the backlight assembly resolves the issue.",
                "correct": False,
                "rationale": (
                    "Incorrect. OLED displays have no backlight. Each pixel emits its own "
                    "light independently. The concept of 'backlight bleed' does not apply "
                    "to OLED technology. Backlight bleed is an LCD/IPS phenomenon."
                ),
            },
            {
                "id": "d",
                "text": "This is a driver incompatibility between the OS display driver and the OLED panel; a driver update from the GPU vendor resolves it.",
                "correct": False,
                "rationale": (
                    "Incorrect. GPU driver updates address rendering and compatibility issues "
                    "but cannot reverse or prevent physical pixel degradation from uneven "
                    "usage — which is what image retention represents. A driver update would "
                    "not resolve differential pixel wear on an OLED panel."
                ),
            },
        ],
        "explanation": (
            "OLED image retention occurs because organic pixels degrade slightly each time "
            "they emit light. Static UI elements displayed for extended periods cause the "
            "pixels beneath them to age faster than surrounding pixels, leaving a faint "
            "phantom image. The effect is temporary in early stages (fades with bright "
            "content) and becomes permanent burn-in with prolonged exposure. Mitigation "
            "strategies: short screen timeout, screen saver, auto-hide taskbar, periodic "
            "pixel refresh utilities (built into many OLED-equipped laptops), and avoiding "
            "maximum brightness for extended use."
        ),
    },
    # ------------------------------------------------------------------ #
    # 13 — Mobile email configuration
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-013",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile email configuration",
        "stem": (
            "A user sets up email on an iPhone using the manual Exchange account type. "
            "She enters her corporate email address and password. The phone prompts for "
            "a server address. She enters 'mail.company.com' but receives 'Cannot Connect "
            "Using SSL'. The corporate IT team confirms the Exchange server uses a "
            "self-signed certificate not trusted by iOS. Which is the BEST resolution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Toggle off SSL in the Exchange account settings; plaintext connections are equally secure when used on the corporate Wi-Fi network.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling SSL transmits credentials and email content in "
                    "cleartext, making them visible to anyone sniffing the network — "
                    "including corporate Wi-Fi. This is never an acceptable security "
                    "practice. Corporate IT should not recommend disabling SSL."
                ),
            },
            {
                "id": "b",
                "text": "Install the corporate CA root certificate on the iPhone via a configuration profile (MDM or email delivery); this adds the certificate to the iOS trusted store so SSL validation succeeds.",
                "correct": True,
                "rationale": (
                    "Correct. iOS enforces strict SSL/TLS certificate validation. When a "
                    "server uses a self-signed or internally issued certificate, iOS will "
                    "reject the connection because it cannot validate the certificate chain. "
                    "Installing the corporate CA root certificate into the iOS trusted "
                    "certificate store (via MDM profile, Apple Configurator, or manual "
                    "profile install) causes iOS to trust all certificates issued by that "
                    "CA, resolving the SSL error without sacrificing encryption."
                ),
            },
            {
                "id": "c",
                "text": "Switch from the Exchange account type to the IMAP account type; IMAP does not perform SSL certificate validation.",
                "correct": False,
                "rationale": (
                    "Incorrect. iOS IMAP connections also validate SSL/TLS certificates. "
                    "The issue is the untrusted certificate, not the account type. Switching "
                    "to IMAP would produce the same SSL error and would not support the full "
                    "Exchange ActiveSync feature set (contacts, calendar, push email)."
                ),
            },
            {
                "id": "d",
                "text": "Ask the user to accept the certificate warning each time the app opens; iOS stores the user acceptance permanently.",
                "correct": False,
                "rationale": (
                    "Incorrect. While some iOS apps (like Safari) allow a per-session "
                    "certificate trust override, the native Mail app's Exchange connector "
                    "does not provide a persistent 'accept untrusted certificate' option "
                    "for ongoing use. The correct approach is to install the CA certificate "
                    "at the system level."
                ),
            },
        ],
        "explanation": (
            "iOS maintains a strict system-wide trusted certificate store. Connections using "
            "SSL/TLS (Exchange ActiveSync, IMAP, SMTP) fail if the server's certificate cannot "
            "be validated against a trusted root CA. For internal servers using privately issued "
            "certificates, the corporate root CA certificate must be installed on the device. "
            "Delivery methods: MDM configuration profile (preferred for enterprise), Apple "
            "Configurator, or manual profile install (Settings > Profile Downloaded > Install). "
            "Never disable SSL to work around this — always install the trust anchor."
        ),
    },
    # ------------------------------------------------------------------ #
    # 14 — Mobile connection types & ports
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-014",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A technician has a laptop with a Thunderbolt 4 port and needs to drive two "
            "4K/60Hz external displays simultaneously from a single cable connection to a "
            "Thunderbolt 4 dock. The dock has two DisplayPort 1.4 outputs. The technician "
            "connects both monitors and observes only one display is active at 4K/60Hz; "
            "the second monitor shows 4K/30Hz. The monitors support up to 4K/120Hz. "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Thunderbolt 4 provides only 40 Gbps total bandwidth, which is insufficient to drive two independent 4K/60Hz streams simultaneously.",
                "correct": False,
                "rationale": (
                    "Incorrect. Thunderbolt 4 provides 40 Gbps of bandwidth, which is "
                    "sufficient for two 4K/60Hz displays. Two 4K/60Hz 8-bit SDR streams "
                    "require roughly 2 × ~14.9 Gbps ≈ 30 Gbps before DSC compression — "
                    "well within Thunderbolt 4's 40 Gbps capacity. Bandwidth alone is not "
                    "the limiting factor here."
                ),
            },
            {
                "id": "b",
                "text": "The dock's DisplayPort 1.4 outputs are using Multi-Stream Transport (MST), but the laptop's Thunderbolt 4 controller has been configured for Single-Stream Transport (SST) only, limiting the second output to 4K/30Hz.",
                "correct": True,
                "rationale": (
                    "Correct. Thunderbolt 4 docks driving two displays over a single "
                    "Thunderbolt cable typically use DisplayPort 1.4 with Multi-Stream "
                    "Transport (MST) or two independent DisplayPort tunnels. If the host's "
                    "Thunderbolt/USB4 controller or firmware is configured for SST (single "
                    "stream) on the Thunderbolt tunnel, it provides only one full-bandwidth "
                    "DisplayPort stream. The dock then uses its available bandwidth for "
                    "MST, but the second monitor is bandwidth-constrained to 4K/30Hz. "
                    "Enabling MST or updating the Thunderbolt firmware/driver may resolve "
                    "the second display limitation."
                ),
            },
            {
                "id": "c",
                "text": "DisplayPort 1.4 cannot carry 4K/60Hz; the dock must use DisplayPort 2.0 outputs to achieve 4K/60Hz on both monitors.",
                "correct": False,
                "rationale": (
                    "Incorrect. DisplayPort 1.4 supports 4K/60Hz (and even 4K/120Hz with "
                    "DSC compression) on a single output. The first monitor achieving "
                    "4K/60Hz over the dock's DisplayPort 1.4 port proves this. The "
                    "limitation is in stream allocation, not the DisplayPort version."
                ),
            },
            {
                "id": "d",
                "text": "The Thunderbolt 4 cable does not support video; a separate HDMI cable is required for the second display.",
                "correct": False,
                "rationale": (
                    "Incorrect. Thunderbolt 4 cables carry DisplayPort Alt Mode tunnels "
                    "and are the correct interface for connecting a Thunderbolt 4 dock. "
                    "Thunderbolt 4 fully supports video output; the issue is stream "
                    "configuration, not the cable's video capability."
                ),
            },
        ],
        "explanation": (
            "Thunderbolt 4 tunnels up to two independent DisplayPort 1.4 streams over 40 Gbps. "
            "Docks implement this via MST hubs or dual DP tunnels. When only one full-bandwidth "
            "DP stream is provided (SST mode or host controller limitation), the dock splits "
            "available bandwidth across two outputs using MST, reducing each stream's maximum "
            "resolution/refresh rate. Ensuring the Thunderbolt controller uses DP MST tunneling "
            "(two independent DP tunnels) allows simultaneous 4K/60Hz on both outputs. Always "
            "check Thunderbolt/USB4 firmware and display driver settings when multi-display "
            "configurations underperform."
        ),
    },
    # ------------------------------------------------------------------ #
    # 15 — Mobile network connectivity
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-015",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile network connectivity",
        "stem": (
            "A user traveling internationally reports that her smartphone connects to "
            "the foreign carrier network and can make calls, but data speeds are very "
            "slow (2G/EDGE quality) despite her home carrier advertising '5G international "
            "roaming'. The phone shows a 5G icon in the status bar. Which is the MOST "
            "likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The user's SIM card is too old to support 5G and must be replaced with a 5G-capable SIM before roaming.",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM cards store subscriber identity information but do not "
                    "physically determine radio band support. 5G capability depends on the "
                    "device's modem, not the SIM card generation. SIM replacement would not "
                    "change the roaming data throughput."
                ),
            },
            {
                "id": "b",
                "text": "The home carrier's roaming agreement with the foreign network may only provision 2G/3G data speeds even though voice registers on 5G NR; the '5G icon' reflects radio registration, not the granted data tier.",
                "correct": True,
                "rationale": (
                    "Correct. Carrier roaming agreements define which services (voice, SMS, "
                    "data tier) are granted on the partner network. A roaming agreement may "
                    "allow 5G NR voice registration while provisioning data at 2G/3G speeds "
                    "in the billing/policy layer. The 5G icon indicates the device is "
                    "camped on a 5G cell (radio layer), not that the data session is running "
                    "at 5G throughput. The user should contact her carrier to verify roaming "
                    "data provisioning or purchase a local SIM for high-speed data."
                ),
            },
            {
                "id": "c",
                "text": "The phone needs to be rebooted daily when roaming internationally to re-register with the 5G data session.",
                "correct": False,
                "rationale": (
                    "Incorrect. Daily reboots do not change the data tier provisioned by "
                    "the roaming agreement. Re-registration after a reboot will result in "
                    "the same provisioned data speed because the constraint is at the "
                    "network policy layer, not the device registration state."
                ),
            },
            {
                "id": "d",
                "text": "5G is not available internationally; the 5G icon is a software display bug and the phone is actually on LTE.",
                "correct": False,
                "rationale": (
                    "Incorrect. 5G NR is deployed in many countries globally. The 5G icon "
                    "accurately reflects the radio access technology (RAT) the device is "
                    "registered on. The issue is the data throughput granted by the roaming "
                    "policy, not whether 5G physically exists in that country."
                ),
            },
        ],
        "explanation": (
            "Carrier roaming operates at two layers: (1) radio layer — the physical connection "
            "to a cell tower; and (2) policy/provisioning layer — what data tier the home "
            "carrier purchases from the foreign partner. A device can register on a 5G cell "
            "(radio layer) while being provisioned at 2G speeds (policy layer) if the roaming "
            "agreement only includes a low-speed data tier. The status bar icon reflects radio "
            "registration, not provisioned throughput. Always verify roaming data terms with "
            "the carrier before international travel."
        ),
    },
    # ------------------------------------------------------------------ #
    # 16 — MDM/MAM
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-016",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "MDM/MAM",
        "stem": (
            "An MDM administrator needs to push a Wi-Fi configuration profile to 500 "
            "corporate iPhones so that each device automatically connects to the corporate "
            "WPA2-Enterprise network using the device's unique certificate for "
            "authentication (EAP-TLS), without users needing to enter credentials. "
            "Which MDM capabilities must be combined to achieve this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Push a Wi-Fi profile with SSID and WPA2-Personal (PSK) passphrase; EAP-TLS is only available on desktop operating systems.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2-Personal (PSK) uses a shared passphrase, not per-device "
                    "certificates, and does not provide individual device identity. EAP-TLS "
                    "is fully supported on iOS (and Android) via MDM configuration profiles. "
                    "This answer uses the wrong authentication type."
                ),
            },
            {
                "id": "b",
                "text": "Push a device identity certificate via SCEP or PKCS#12 payload AND a Wi-Fi profile specifying WPA2-Enterprise/EAP-TLS referencing that certificate identity.",
                "correct": True,
                "rationale": (
                    "Correct. EAP-TLS authentication requires each device to present a unique "
                    "client certificate to the RADIUS server. MDM delivers this via: "
                    "(1) a certificate payload (SCEP for automated per-device enrollment from "
                    "a CA, or PKCS#12 for pre-provisioned certs); (2) a Wi-Fi payload "
                    "specifying the SSID, WPA2-Enterprise security type, EAP-TLS protocol, "
                    "and a reference to the device certificate identity. Both payloads must "
                    "be delivered together in the same (or sequenced) MDM profile."
                ),
            },
            {
                "id": "c",
                "text": "Push an S/MIME certificate payload and a Wi-Fi profile; S/MIME certificates are compatible with EAP-TLS Wi-Fi authentication.",
                "correct": False,
                "rationale": (
                    "Incorrect. S/MIME certificates are for email signing and encryption, "
                    "not Wi-Fi EAP-TLS authentication. While both use X.509 certificates, "
                    "they serve different purposes and are issued with different certificate "
                    "templates/key usage extensions. An S/MIME certificate is not appropriate "
                    "for network authentication."
                ),
            },
            {
                "id": "d",
                "text": "Enable NFC on all devices; EAP-TLS uses NFC to exchange certificates with the corporate Wi-Fi access point during authentication.",
                "correct": False,
                "rationale": (
                    "Incorrect. NFC has no role in EAP-TLS Wi-Fi authentication. EAP-TLS "
                    "operates entirely within the 802.1X authentication framework over the "
                    "wireless (802.11) connection between the client and RADIUS server. "
                    "NFC is a separate short-range communication technology."
                ),
            },
        ],
        "explanation": (
            "WPA2-Enterprise with EAP-TLS requires per-device X.509 client certificates issued "
            "by a trusted CA. MDM automates this at scale using: (1) SCEP (Simple Certificate "
            "Enrollment Protocol) or PKCS#12 certificate payloads to deliver unique device "
            "certificates; (2) Wi-Fi payloads specifying SSID, WPA2-Enterprise, EAP-TLS, and "
            "the certificate identity. The RADIUS server validates the device certificate during "
            "802.1X authentication. This provides strong, password-free, per-device identity "
            "that can be individually revoked if a device is compromised."
        ),
    },
    # ------------------------------------------------------------------ #
    # 17 — Laptop hardware
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-017",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A user reports that the laptop fan runs at maximum speed continuously and "
            "the chassis is hot to the touch, even when the system is idle with no "
            "applications open. The OS reports CPU utilization at 3–5%. Task Manager "
            "shows no unusual processes. Which is the MOST likely hardware cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The thermal paste has dried out and provides no insulation between the CPU and heat sink, causing infinite heat generation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Dried-out thermal paste increases thermal resistance, "
                    "causing the CPU to run hot under load. However, at 3–5% CPU utilization, "
                    "even poor thermal paste would not generate enough heat to require "
                    "maximum fan speed. More importantly, thermal paste degradation causes "
                    "heat, not 'infinite heat generation' — the framing is incorrect."
                ),
            },
            {
                "id": "b",
                "text": "A blocked or obstructed heatsink exhaust vent (dust buildup in the heat sink fins or blocked air intake) prevents heat dissipation and triggers continuous maximum fan speed.",
                "correct": True,
                "rationale": (
                    "Correct. Dust accumulation in heat sink fins, exhaust vents, or air "
                    "intake grilles severely restricts airflow. Even at low CPU utilization, "
                    "residual heat from the CPU/GPU/VRMs cannot dissipate, causing chassis "
                    "temperature to rise. The thermal management firmware responds by "
                    "ramping fans to maximum. Cleaning the vents with compressed air "
                    "typically resolves this without any part replacement."
                ),
            },
            {
                "id": "c",
                "text": "The battery is overcharging and dissipating excess charge as heat, which triggers the thermal protection fan response.",
                "correct": False,
                "rationale": (
                    "Incorrect. Modern lithium-ion battery management ICs prevent "
                    "overcharging with hardware cutoff circuits. While a failing battery "
                    "can generate heat, it would not cause the CPU thermal throttling "
                    "sensors to trigger maximum fan speed at 3–5% CPU utilization in the "
                    "way described."
                ),
            },
            {
                "id": "d",
                "text": "The laptop's embedded controller has permanently set the fan speed to maximum due to a firmware bug and must be reflashed.",
                "correct": False,
                "rationale": (
                    "Incorrect. While EC firmware bugs can affect fan control, a firmware "
                    "bug causing permanent max fan speed would not typically coexist with "
                    "accurate thermal sensor readings showing high chassis temperature. "
                    "The physical heat described points to a real thermal issue (obstruction) "
                    "rather than a firmware-only fan control bug."
                ),
            },
        ],
        "explanation": (
            "Dust buildup is the leading cause of chronic overheating in laptops. Heat sink "
            "fins and exhaust vents accumulate dust over time, reducing airflow. The thermal "
            "management system responds by running fans at high speed to compensate. At low "
            "CPU utilization, the CPU itself generates minimal heat, but if heat cannot escape "
            "due to blocked vents, the chassis temperature rises anyway. Cleaning with "
            "compressed air (blow from exhaust outward, never suck dust inward) restores "
            "airflow. Annual cleaning is recommended for heavily used laptops."
        ),
    },
    # ------------------------------------------------------------------ #
    # 18 — Mobile synchronization
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-018",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile synchronization",
        "stem": (
            "A user connects an Android phone to a Windows laptop via USB. The phone "
            "displays a notification asking for the USB connection type. The user selects "
            "'File Transfer (MTP)' but the phone does not appear as a drive in Windows "
            "File Explorer. Device Manager shows 'MTP USB Device' with a yellow warning "
            "triangle. Which is the MOST likely cause and resolution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MTP requires a physical data cable; the USB cable being used is a charge-only cable without data lines. Replace with a data-capable USB cable.",
                "correct": False,
                "rationale": (
                    "Incorrect. A charge-only cable would prevent the phone from even being "
                    "recognized by Windows — Device Manager would show nothing, not 'MTP USB "
                    "Device' with a warning. The fact that Device Manager shows the device "
                    "with a warning confirms the data lines are working and the issue is "
                    "driver-related."
                ),
            },
            {
                "id": "b",
                "text": "The Windows MTP driver (wpdmtp.inf / Windows Portable Device driver) is corrupted or not installed; updating or reinstalling the driver resolves the File Explorer issue.",
                "correct": True,
                "rationale": (
                    "Correct. A yellow warning triangle on 'MTP USB Device' in Device Manager "
                    "indicates a driver error, not a cable or connectivity problem. The MTP "
                    "driver (Windows Portable Devices) may be corrupted. Right-clicking the "
                    "device in Device Manager and selecting 'Update Driver' or 'Uninstall "
                    "Device' followed by rescanning for hardware (which reinstalls the "
                    "built-in Windows MTP driver) typically resolves this."
                ),
            },
            {
                "id": "c",
                "text": "File Transfer (MTP) is an Android-only feature not supported by Windows; the user must select PTP mode to browse files from Windows.",
                "correct": False,
                "rationale": (
                    "Incorrect. MTP (Media Transfer Protocol) is fully supported by Windows "
                    "and is the primary Windows protocol for accessing files on Android "
                    "devices. PTP (Picture Transfer Protocol) is a subset of MTP for "
                    "photos only. MTP works on Windows 7 and later natively."
                ),
            },
            {
                "id": "d",
                "text": "The user must install the phone manufacturer's custom sync software before any USB file transfer is possible.",
                "correct": False,
                "rationale": (
                    "Incorrect. Modern Android phones use standard MTP/PTP which Windows "
                    "supports natively via built-in drivers. Manufacturer sync software "
                    "(e.g., Samsung Smart Switch) is optional and not required for basic "
                    "MTP file access. The driver warning in Device Manager is the more "
                    "direct and accurate explanation."
                ),
            },
        ],
        "explanation": (
            "MTP (Media Transfer Protocol) allows Windows to access files on Android devices "
            "over USB. Windows includes native MTP drivers (Windows Portable Devices / WPD). "
            "A yellow warning in Device Manager indicates a driver error, not a physical "
            "connection issue. The fix is to update or reinstall the MTP driver: right-click "
            "in Device Manager → Update Driver, or uninstall and replug the device. If the "
            "Windows driver is corrupt, running 'sfc /scannow' may repair the WPD driver "
            "files. Always confirm a data-capable USB cable is used (charge-only cables "
            "have no data lines, but would show no device at all in Device Manager)."
        ),
    },
    # ------------------------------------------------------------------ #
    # 19 — Mobile connection types & ports
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-019",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A laptop technician is trying to identify a port on an older laptop. The "
            "port has a small rectangular connector, supports data transfer, video output "
            "over a Mini DisplayPort-compatible adapter, and provides up to 10W of power "
            "to connected peripherals. The laptop was manufactured in 2013. Which port "
            "is MOST likely described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "USB 3.0 Type-A",
                "correct": False,
                "rationale": (
                    "Incorrect. USB 3.0 Type-A is a rectangular port but does not natively "
                    "support video output via Mini DisplayPort adapters and does not provide "
                    "power in the way described. USB 3.0 provides 900 mA at 5V (~4.5W), not "
                    "10W. DisplayPort Alt Mode over USB-A is not a standard feature."
                ),
            },
            {
                "id": "b",
                "text": "Thunderbolt 1 or Thunderbolt 2 (using the Mini DisplayPort connector form factor)",
                "correct": True,
                "rationale": (
                    "Correct. Thunderbolt 1 and 2 (2011–2015 era) use the Mini DisplayPort "
                    "physical connector. They support data transfer (10 Gbps for TB1, 20 Gbps "
                    "for TB2), are compatible with Mini DisplayPort video adapters, and can "
                    "provide bus power to connected peripherals (up to 10W). A 2013 MacBook "
                    "or Ultrabook with this connector is almost certainly Thunderbolt 1/2."
                ),
            },
            {
                "id": "c",
                "text": "HDMI 2.0 mini connector",
                "correct": False,
                "rationale": (
                    "Incorrect. HDMI mini (Type C) has a different physical form factor from "
                    "Mini DisplayPort — it is smaller and shaped differently. HDMI does not "
                    "support data transfer (non-video), and HDMI connectors do not provide "
                    "peripheral power. Additionally, HDMI adapters and Mini DisplayPort "
                    "adapters are not cross-compatible."
                ),
            },
            {
                "id": "d",
                "text": "USB-C with DisplayPort Alt Mode",
                "correct": False,
                "rationale": (
                    "Incorrect. USB-C was not widely deployed in laptops until 2015–2016. "
                    "The USB-C connector is oval/rounded rectangular and is physically "
                    "distinct from the rectangular Mini DisplayPort connector. A 2013 laptop "
                    "is unlikely to have USB-C."
                ),
            },
        ],
        "explanation": (
            "Thunderbolt 1 (2011) and Thunderbolt 2 (2013) use the Mini DisplayPort (mDP) "
            "physical connector, making them physically compatible with Mini DisplayPort "
            "accessories. Thunderbolt adds high-speed PCIe tunneling for data (10/20 Gbps) "
            "and peripheral power delivery on top of the mDP signal. A Thunderbolt port on "
            "a 2013 laptop appears identical to a Mini DisplayPort and is identified by the "
            "lightning bolt icon next to the port. Thunderbolt 3 and later switched to the "
            "USB-C physical connector."
        ),
    },
    # ------------------------------------------------------------------ #
    # 20 — Location services
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-020",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Location services",
        "stem": (
            "A compliance officer asks a technician to explain how a company MDM policy "
            "that sets location services to 'Disabled' for all corporate devices affects "
            "both the dispatch app and E911 emergency calling. Which statement is "
            "MOST accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disabling location services via MDM prevents all location use including E911; emergency services will not receive location data when a user dials 911.",
                "correct": False,
                "rationale": (
                    "Incorrect. E911 (Enhanced 911) location is provided at the carrier "
                    "network and modem level, independent of OS-level location services. "
                    "Regulatory requirements (FCC E911 Phase II) mandate that cellular "
                    "carriers provide location to PSAP regardless of the device's software "
                    "location settings. MDM cannot disable the carrier/modem E911 location "
                    "mechanism."
                ),
            },
            {
                "id": "b",
                "text": "MDM disabling of OS-level location services prevents app-based location access (dispatch app) but does not prevent the cellular modem from providing location to emergency services (E911), which operates at the carrier network level.",
                "correct": True,
                "rationale": (
                    "Correct. OS-level location services (GPS, Wi-Fi positioning APIs) are "
                    "accessible to apps via the OS location framework. MDM can restrict these. "
                    "However, E911 operates through the cellular modem and carrier network — "
                    "the modem reports location (GPS, A-GPS, cell-based) directly to the PSAP "
                    "over the carrier's network, bypassing the OS location permission framework. "
                    "This is a legal requirement and cannot be overridden by MDM or app settings."
                ),
            },
            {
                "id": "c",
                "text": "MDM location restriction only applies to third-party apps; the dispatch app (if developed by the MDM vendor) is always exempt and can access GPS regardless.",
                "correct": False,
                "rationale": (
                    "Incorrect. MDM location policies apply at the OS level and restrict all "
                    "apps, including those from the MDM vendor. There is no 'MDM vendor app "
                    "exemption' in standard OS location permission frameworks. If location "
                    "services are disabled, all app-level location access is blocked."
                ),
            },
            {
                "id": "d",
                "text": "Disabling location services conserves battery but does not actually restrict any app from accessing GPS because Android and iOS do not enforce location permissions.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both Android and iOS strictly enforce app location permissions "
                    "and honor MDM-managed location restrictions. Apps without location "
                    "permission (or when location services are disabled by policy) receive "
                    "null/unavailable location data and cannot access GPS or Wi-Fi positioning."
                ),
            },
        ],
        "explanation": (
            "OS location services (GPS, Wi-Fi, cellular positioning APIs) are managed by the "
            "OS location framework and subject to app permissions and MDM restrictions. When "
            "MDM disables location services, all apps lose access to these APIs. E911, however, "
            "operates at the modem/carrier level: the FCC E911 mandate requires carriers to "
            "deliver location to Public Safety Answering Points (PSAP) when a 911 call is made, "
            "using network-based and/or handset-based (GNSS) location that bypasses the OS "
            "permission layer. MDM policies do not affect E911 location delivery."
        ),
    },
    # ------------------------------------------------------------------ #
    # 21 — Laptop hardware (multiple_response)
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-021",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is ordering a replacement keyboard for a laptop model that was "
            "sold in multiple regional variants. The OEM part catalog lists four keyboard "
            "SKUs for the same model. (Choose TWO factors the technician must verify to "
            "ensure the correct keyboard SKU is ordered.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Keyboard layout / locale (e.g., US ANSI, UK ISO, Nordic, etc.) to match the user's language and key arrangement.",
                "correct": True,
                "rationale": (
                    "Correct. Keyboard layouts differ by region: US ANSI vs. UK ISO have "
                    "different key shapes, Return key sizes, and character assignments. "
                    "Nordic, French AZERTY, and German QWERTZ layouts have entirely different "
                    "key legends and some physical key differences. Installing the wrong "
                    "locale keyboard produces incorrect key labels and may have slight "
                    "physical incompatibilities."
                ),
            },
            {
                "id": "b",
                "text": "Whether the keyboard includes a backlight (non-backlit vs. backlit vs. RGB per-key), as the connector pinout and cable may differ.",
                "correct": True,
                "rationale": (
                    "Correct. Backlit keyboards require additional electrical connections "
                    "for the lighting circuit (LED strips or per-key LEDs) and may use a "
                    "different ribbon cable or a second connector compared to non-backlit "
                    "variants. Installing a backlit keyboard in a chassis wired for non-"
                    "backlit (or vice versa) results in non-functional or absent backlight "
                    "and may produce physical fitment differences in the palm rest."
                ),
            },
            {
                "id": "c",
                "text": "The color of the keycaps to ensure it matches the chassis color.",
                "correct": False,
                "rationale": (
                    "Incorrect. While aesthetics are a practical consideration, keycap "
                    "color is not a functional or electrical compatibility factor. The "
                    "keyboard will operate identically regardless of keycap color. This "
                    "is a preference item, not a specification that determines whether the "
                    "correct part is ordered for functional compatibility."
                ),
            },
            {
                "id": "d",
                "text": "The storage capacity of the SSD installed in the laptop to ensure the keyboard model supports high-capacity drives.",
                "correct": False,
                "rationale": (
                    "Incorrect. Keyboard selection is entirely independent of the laptop's "
                    "storage configuration. SSD capacity has no bearing on which keyboard "
                    "SKU is compatible. This distractor tests whether candidates confuse "
                    "system specification matching with keyboard part selection."
                ),
            },
        ],
        "explanation": (
            "When ordering a replacement laptop keyboard, the two critical functional variables "
            "that differentiate OEM SKUs for the same model are: (1) locale/layout (affects "
            "physical key arrangement, legend printing, and sometimes minor physical key shape "
            "differences between ANSI and ISO); (2) backlight configuration (non-backlit, "
            "backlit, or RGB requires different cable harnesses and connectors). Other visible "
            "differences (color) are aesthetic. Always pull the exact part number from the "
            "OEM service manual or existing keyboard label before ordering."
        ),
    },
    # ------------------------------------------------------------------ #
    # 22 — Mobile display components
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-022",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile display components",
        "stem": (
            "A user reports vertical colored lines running from top to bottom on their "
            "laptop display. The lines are always present and do not move when the display "
            "is flexed. The same lines appear on an external monitor connected to the "
            "laptop's HDMI port. Which component has MOST likely failed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The LCD panel's ribbon cable has been damaged, causing the vertical lines.",
                "correct": False,
                "rationale": (
                    "Incorrect. A damaged LCD ribbon cable or eDP cable causes lines or "
                    "artifacts only on the laptop's built-in display. If the same artifact "
                    "appears on an external HDMI-connected monitor, the fault must be "
                    "upstream of the display — in the graphics subsystem, not the panel "
                    "or its cable."
                ),
            },
            {
                "id": "b",
                "text": "The GPU or integrated graphics processor has failed, producing the artifact in its rendered output before it reaches any display.",
                "correct": True,
                "rationale": (
                    "Correct. When identical artifacts appear on both the built-in display "
                    "AND an external monitor simultaneously, the fault is in the rendering "
                    "pipeline upstream of both outputs — namely the GPU or iGPU. The GPU "
                    "generates the artifact in its frame buffer, and both display outputs "
                    "inherit it. Panel replacement or cable replacement would not fix a "
                    "GPU-sourced artifact."
                ),
            },
            {
                "id": "c",
                "text": "The HDMI cable connecting the external monitor is faulty, back-feeding noise into the laptop's display controller.",
                "correct": False,
                "rationale": (
                    "Incorrect. HDMI cables carry a one-way digital signal from source to "
                    "display; they do not back-feed noise into the laptop's internal display "
                    "pipeline. A faulty HDMI cable would cause artifacts on the external "
                    "monitor only, not simultaneously on the built-in display."
                ),
            },
            {
                "id": "d",
                "text": "The display driver software has corrupted the GPU's look-up table (LUT), causing colored lines on all outputs; reinstalling the driver will resolve it.",
                "correct": False,
                "rationale": (
                    "Incorrect. While software can cause color issues, vertical lines that "
                    "persist regardless of OS state (present from POST) indicate hardware "
                    "failure. If lines appear only after the OS loads, driver issues are "
                    "possible, but the scenario implies persistent lines that are present "
                    "on both outputs — characteristic of GPU hardware failure, not a "
                    "correctable LUT/driver issue."
                ),
            },
        ],
        "explanation": (
            "Diagnostic rule: if a display artifact appears ONLY on the built-in screen, the "
            "fault is the panel, its cable, or the eDP/LVDS connector. If the artifact appears "
            "on an external monitor as well, the fault is in the GPU/graphics subsystem that "
            "feeds both outputs. Persistent vertical colored lines appearing from boot on both "
            "built-in and external displays are a classic symptom of GPU die failure or VRAM "
            "corruption. The GPU typically cannot be replaced on a laptop; system board "
            "replacement or an external GPU solution would be required."
        ),
    },
    # ------------------------------------------------------------------ #
    # 23 — Mobile email configuration
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-023",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile email configuration",
        "stem": (
            "A corporate mail server has been migrated from POP3 to IMAP, and all users "
            "have been asked to reconfigure their mobile devices. One user reports that "
            "after switching to IMAP, emails she deletes on her phone still appear on her "
            "laptop email client the next day. Both clients are now configured for IMAP "
            "on the same account. Which configuration setting is MOST likely causing "
            "this discrepancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The phone's IMAP account is using port 143 while the laptop uses port 993; different ports prevent sync of deletion flags.",
                "correct": False,
                "rationale": (
                    "Incorrect. Ports 143 (STARTTLS) and 993 (implicit TLS) are both valid "
                    "IMAP ports that connect to the same server backend. Both connection "
                    "types read and write to the same mailbox; deletion flags are stored "
                    "server-side and are independent of which port the client uses."
                ),
            },
            {
                "id": "b",
                "text": "The laptop's IMAP client is configured to 'mark as deleted' locally without expunging the message on the server, or the phone is deleting locally without issuing an IMAP EXPUNGE command.",
                "correct": True,
                "rationale": (
                    "Correct. IMAP deletion is a two-step process: first the \\Deleted flag "
                    "is set on the message (it is hidden or shown as struck-through); then "
                    "an EXPUNGE command permanently removes it from the mailbox. If the "
                    "phone's IMAP client sets the \\Deleted flag but does not EXPUNGE, other "
                    "clients may show the message as still present (just flagged). Conversely, "
                    "if the laptop client is configured to show deleted messages, it will "
                    "still display them. Configuring both clients to expunge on delete and "
                    "hide deleted messages synchronizes behavior."
                ),
            },
            {
                "id": "c",
                "text": "IMAP does not synchronize deletion across clients; deletion sync requires Exchange ActiveSync.",
                "correct": False,
                "rationale": (
                    "Incorrect. IMAP fully supports deletion synchronization. The \\Deleted "
                    "flag and EXPUNGE command allow one client's deletion to be visible to "
                    "all other clients accessing the same IMAP mailbox. If configured "
                    "correctly, deleting on one device removes the message for all devices."
                ),
            },
            {
                "id": "d",
                "text": "The user's mailbox quota has been exceeded, preventing deletion commands from being written back to the server.",
                "correct": False,
                "rationale": (
                    "Incorrect. A full mailbox quota typically prevents new messages from "
                    "arriving but does not prevent deletion commands (\\Deleted flags or "
                    "EXPUNGE) from processing, as those do not increase mailbox size. The "
                    "described symptom of deletions on one client not appearing on another "
                    "points to client-side expunge configuration, not quota."
                ),
            },
        ],
        "explanation": (
            "IMAP deletion: setting the \\Deleted flag marks a message for deletion but does "
            "not remove it from the server until EXPUNGE is issued. Some IMAP clients 'delete' "
            "by only setting the flag without expunging; others move messages to Trash without "
            "flagging the original. Client behavior varies: Outlook, Thunderbird, and mobile "
            "mail apps all handle IMAP deletion differently. For consistent cross-client "
            "behavior, configure all clients to: (1) immediately expunge on delete, or (2) "
            "move to a shared Trash/Deleted Items folder. Verify both clients reference the "
            "same IMAP Trash folder."
        ),
    },
    # ------------------------------------------------------------------ #
    # 24 — Bluetooth pairing
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-024",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Bluetooth pairing",
        "stem": (
            "A user wants to pair her smartphone to a Bluetooth speaker that supports "
            "Bluetooth 5.0 LE Audio with the LC3 codec. Her phone supports Bluetooth 5.2 "
            "with SBC and AAC codecs but does NOT list LC3 as a supported codec in its "
            "audio settings. After pairing, audio plays but the user reports noticeably "
            "lower quality than advertised. Which statement BEST explains the outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bluetooth 5.2 is not backward compatible with Bluetooth 5.0 devices; the devices are paired incorrectly.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth is fully backward compatible across versions. A "
                    "Bluetooth 5.2 device can pair and operate with a Bluetooth 5.0 device "
                    "without any compatibility issue. Version differences affect available "
                    "features but do not prevent pairing."
                ),
            },
            {
                "id": "b",
                "text": "Both devices negotiate the best mutually supported codec during pairing; since the phone lacks LC3, they fall back to SBC, which provides lower audio quality than LC3.",
                "correct": True,
                "rationale": (
                    "Correct. Bluetooth audio codec negotiation selects the highest-quality "
                    "codec supported by both devices. The speaker supports LC3 (part of LE "
                    "Audio / Bluetooth 5.2 specification) but the phone supports only SBC "
                    "and AAC. Since LC3 is unavailable on the phone side, the connection "
                    "falls back to SBC — the mandatory baseline codec — which delivers lower "
                    "fidelity than LC3. The speaker's advertised LC3 quality is achievable "
                    "only with a phone that also implements LC3."
                ),
            },
            {
                "id": "c",
                "text": "AAC is always selected over SBC when available; the phone and speaker are using AAC, and the quality difference is caused by the speaker's hardware, not the codec.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the speaker supports LE Audio with LC3. "
                    "LE Audio uses Bluetooth Low Energy (BLE) for audio, which is a different "
                    "transport from Classic Bluetooth (BR/EDR) used by AAC profiles (A2DP). "
                    "The LC3 vs. SBC comparison is the correct framing for LE Audio-capable "
                    "speakers paired with phones lacking LC3."
                ),
            },
            {
                "id": "d",
                "text": "The speaker must be reset to factory defaults and re-paired to enable LC3 codec mode on phones that do not list it in audio settings.",
                "correct": False,
                "rationale": (
                    "Incorrect. Factory reset of the speaker cannot add LC3 codec support "
                    "to the phone. Codec support is a software/hardware capability of the "
                    "device; the phone does not support LC3 and no amount of pairing or "
                    "speaker-side configuration can add a codec to the phone."
                ),
            },
        ],
        "explanation": (
            "Bluetooth audio codec negotiation: when pairing, both devices advertise supported "
            "codecs and select the best mutually supported option. SBC is the mandatory baseline "
            "codec for Classic Bluetooth A2DP; AAC, aptX, and LDAC are optional higher-quality "
            "codecs. LC3 (Low Complexity Communication Codec) is the LE Audio codec introduced "
            "with Bluetooth 5.2's LE Audio specification — it is lower power and higher quality "
            "than SBC. If the source device (phone) does not support LC3, the connection falls "
            "back to SBC even if the sink (speaker) supports LC3. Achieving LC3 quality requires "
            "both devices to support it."
        ),
    },
    # ------------------------------------------------------------------ #
    # 25 — MDM/MAM (multiple_response)
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-025",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "MDM/MAM",
        "stem": (
            "A security administrator is reviewing MDM policy options for BYOD Android "
            "devices at a financial services firm. Regulations require that corporate "
            "data cannot be transferred to personal apps, and that corporate apps use a "
            "separate encrypted container. (Choose TWO MDM features that directly satisfy "
            "these requirements.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Android Enterprise Work Profile: creates a separate, MDM-managed work container isolated from the personal profile, with encrypted storage and data-sharing restrictions between profiles.",
                "correct": True,
                "rationale": (
                    "Correct. Android Enterprise Work Profile (available on BYOD devices) "
                    "creates a separate work container with its own apps, storage, and "
                    "encryption. MDM policies can prevent data from being copied or shared "
                    "from work apps to personal apps (cross-profile data sharing restrictions), "
                    "satisfying both the data isolation and encryption requirements."
                ),
            },
            {
                "id": "b",
                "text": "MAM app protection policies: wrap corporate apps with DLP controls preventing copy/paste, save-as, or open-in to personal apps, enforced at the app layer regardless of device enrollment.",
                "correct": True,
                "rationale": (
                    "Correct. Mobile Application Management (MAM) app protection policies "
                    "(e.g., Microsoft Intune App Protection Policies) can enforce data "
                    "loss prevention (DLP) controls at the application layer: blocking "
                    "copy/paste between managed and unmanaged apps, preventing save-as to "
                    "personal storage, and requiring app-level PIN. These controls work "
                    "even on unenrolled BYOD devices and can provide encrypted app storage."
                ),
            },
            {
                "id": "c",
                "text": "Full device encryption mandate: require BitLocker encryption on all BYOD Android devices via MDM compliance policy.",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker is a Windows feature and does not apply to Android "
                    "devices. Android uses its own file-based or full-disk encryption. More "
                    "importantly, mandating full-device encryption on personal BYOD devices "
                    "via MDM may exceed what employees would agree to in a BYOD agreement. "
                    "Work Profile encryption (answer A) provides the required corporate data "
                    "encryption without encrypting the entire personal device."
                ),
            },
            {
                "id": "d",
                "text": "Enable screen capture blocking on the entire BYOD device via MDM to prevent data exfiltration via screenshots.",
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking screenshots on the entire BYOD device is an "
                    "overly invasive policy for personal devices (blocking personal app "
                    "screenshots) and does not create an encrypted corporate container. "
                    "Work Profile policies can restrict screenshots within the work profile "
                    "only, but blanket device-wide screenshot blocking does not satisfy "
                    "the encrypted container or data isolation requirements."
                ),
            },
        ],
        "explanation": (
            "For BYOD data isolation and encryption: Android Enterprise Work Profile creates "
            "a hardware-enforced separation between work and personal data with encrypted "
            "work container storage. MDM policies for the Work Profile can block cross-profile "
            "copy/paste and file sharing. MAM app protection policies (without device enrollment) "
            "wrap corporate apps with DLP controls at the application layer. Both approaches "
            "address the regulatory requirements without requiring full device control, which "
            "is appropriate for BYOD scenarios where employee consent and privacy are concerns."
        ),
    },
    # ------------------------------------------------------------------ #
    # 26 — Mobile synchronization (multiple_response)
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-026",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Mobile synchronization",
        "stem": (
            "A user sets up a new iPhone and wants to transfer all data from her old "
            "Android phone to the iPhone. She has contacts in her Google account, photos "
            "in Google Photos, and WhatsApp conversation history. (Choose TWO items that "
            "can be migrated using Apple's 'Move to iOS' app.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Contacts stored in the Google account",
                "correct": True,
                "rationale": (
                    "Correct. The 'Move to iOS' app (available for Android on Google Play) "
                    "can transfer Google account contacts to the iPhone. It copies contact "
                    "data to the user's iCloud account or directly to the iPhone's local "
                    "storage as part of the transfer process."
                ),
            },
            {
                "id": "b",
                "text": "Photos and videos from the device's camera roll / Google Photos local cache",
                "correct": True,
                "rationale": (
                    "Correct. 'Move to iOS' transfers photos and videos stored locally on "
                    "the Android device (including those cached from Google Photos) to the "
                    "new iPhone. The transferred photos are placed in the iPhone's Photo "
                    "Library."
                ),
            },
            {
                "id": "c",
                "text": "WhatsApp conversation history and media",
                "correct": False,
                "rationale": (
                    "Incorrect. WhatsApp conversation history is managed by WhatsApp's own "
                    "backup and transfer system, not by 'Move to iOS'. WhatsApp requires "
                    "its dedicated 'Move to iPhone' in-app transfer feature (introduced in "
                    "2021) to migrate chat history from Android to iOS. 'Move to iOS' does "
                    "not handle third-party messaging app data."
                ),
            },
            {
                "id": "d",
                "text": "Installed Android APK files to be converted to iOS apps",
                "correct": False,
                "rationale": (
                    "Incorrect. Android APK files are binary executables for the Android "
                    "runtime and cannot be converted to iOS apps. 'Move to iOS' transfers "
                    "data (contacts, photos, messages, bookmarks), not app binaries. iOS "
                    "apps must be downloaded separately from the App Store."
                ),
            },
        ],
        "explanation": (
            "'Move to iOS' (Apple's Android app) transfers: contacts, message history (SMS/MMS), "
            "camera roll photos/videos, web bookmarks, mail accounts, calendars, and free apps "
            "(app names are transferred; the iPhone App Store then downloads iOS equivalents "
            "where available). It does NOT transfer: third-party app data (WhatsApp, banking "
            "apps), app settings, ringtones, or Android-specific APK files. For WhatsApp, "
            "use WhatsApp's dedicated Android-to-iPhone transfer feature. For Google Photos, "
            "the photos remain accessible via the Google Photos iOS app."
        ),
    },
    # ------------------------------------------------------------------ #
    # 27 — Laptop hardware
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-027",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is replacing the DC power jack on a laptop. The original jack "
            "is a 5.5 mm outer diameter / 2.1 mm inner pin (center-positive) barrel "
            "connector rated for 19V/4.74A. The technician finds a visually similar "
            "5.5/2.5 mm jack in the parts bin and installs it. After assembly, the "
            "laptop charges intermittently and sometimes does not detect the AC adapter. "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The 19V adapter voltage is too high for the 2.5 mm jack; the inner pin diameter determines maximum voltage rating.",
                "correct": False,
                "rationale": (
                    "Incorrect. Barrel connector inner pin diameter does not determine "
                    "voltage rating; voltage rating depends on insulation and contact "
                    "material specifications. The symptom (intermittent charge) is caused "
                    "by poor mechanical mating, not a voltage incompatibility."
                ),
            },
            {
                "id": "b",
                "text": "The 5.5/2.5 mm jack has a larger inner bore than the 5.5/2.1 mm jack; the AC adapter's 2.1 mm pin does not make consistent contact inside the 2.5 mm bore, causing intermittent connection.",
                "correct": True,
                "rationale": (
                    "Correct. The 5.5/2.1 mm and 5.5/2.5 mm barrel connectors look nearly "
                    "identical externally but have different inner bore diameters (2.1 mm vs. "
                    "2.5 mm). The AC adapter has a 2.1 mm center pin. When inserted into a "
                    "2.5 mm jack, the smaller pin rattles inside the larger bore, making "
                    "intermittent or no contact. The correct OEM part (5.5/2.1 mm jack) "
                    "must be used."
                ),
            },
            {
                "id": "c",
                "text": "The power jack polarity was reversed during soldering; a center-negative adapter is needed for the 2.5 mm variant.",
                "correct": False,
                "rationale": (
                    "Incorrect. Center-positive vs. center-negative is a wiring convention "
                    "independent of the barrel connector's inner diameter. The replacement "
                    "jack's center pin would have been soldered to the same board trace as "
                    "the original. The symptom points to a mechanical fit issue, not polarity "
                    "reversal."
                ),
            },
            {
                "id": "d",
                "text": "The original jack was soldered with lead-free solder; using leaded solder on the replacement creates a galvanic reaction that causes intermittent contact.",
                "correct": False,
                "rationale": (
                    "Incorrect. While mixing solder types can affect joint quality, it does "
                    "not cause an intermittent connection through galvanic corrosion on a "
                    "timescale of hours. The immediate intermittent behavior after assembly "
                    "is caused by the mechanical dimensional mismatch between the 2.5 mm "
                    "jack bore and the 2.1 mm adapter pin."
                ),
            },
        ],
        "explanation": (
            "Barrel power connectors use a standard nomenclature: outer diameter × inner pin "
            "diameter. Common sizes include 5.5/2.1 mm and 5.5/2.5 mm. These look externally "
            "identical but have a 0.4 mm difference in the center pin bore. An adapter with a "
            "2.1 mm pin inserted into a 2.5 mm jack will not make reliable center-pin contact; "
            "an adapter with a 2.5 mm pin will not fit into a 2.1 mm jack (too tight). Always "
            "match the exact inner diameter when replacing a barrel power jack. Measure with "
            "calipers or reference the OEM service manual for the correct part number."
        ),
    },
    # ------------------------------------------------------------------ #
    # 28 — Mobile network connectivity
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-028",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile network connectivity",
        "stem": (
            "A corporate laptop user reports that when connected to the company Wi-Fi "
            "network the VPN software reports 'Network change detected' and drops every "
            "10–15 minutes, requiring manual reconnection. Other users on the same floor "
            "report no VPN issues. The user's wireless adapter shows signal strength at "
            "-62 dBm. Which configuration is MOST likely causing this user's specific "
            "issue?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The user's laptop Wi-Fi adapter has the 802.11 power saving mode (PSM) set to 'Maximum power saving', causing periodic beacon drops that the VPN interprets as a network change.",
                "correct": True,
                "rationale": (
                    "Correct. Wi-Fi Power Saving Mode (PSM) puts the wireless adapter to "
                    "sleep between beacon intervals to conserve battery. In aggressive PSM "
                    "settings, the adapter may miss access point beacons or take too long "
                    "to wake, briefly losing L2 connectivity. VPN software monitors the "
                    "network interface and interprets these momentary link-state changes as "
                    "'network change detected', triggering a tunnel drop. Changing the "
                    "Wi-Fi adapter's PSM to 'Maximum performance' or 'Disabled' in Device "
                    "Manager > Power Management typically resolves VPN disconnection issues "
                    "on specific laptops."
                ),
            },
            {
                "id": "b",
                "text": "The corporate Wi-Fi access point is broadcasting on DFS channel 100, which is reserved for radar detection and must be manually changed to channel 6.",
                "correct": False,
                "rationale": (
                    "Incorrect. DFS channels require access points to monitor for radar "
                    "and switch channels if detected, but this affects all devices on that "
                    "AP equally — not just one user. The scenario states other users have "
                    "no issues, ruling out an AP-wide DFS channel event as the cause."
                ),
            },
            {
                "id": "c",
                "text": "The VPN software version is incompatible with the user's OS update and must be downgraded.",
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN software incompatibility with an OS update would "
                    "typically affect all users who received the same OS update, not just "
                    "one user. The user-specific nature of the problem points to a "
                    "device-local configuration (like PSM) rather than a software-wide "
                    "compatibility issue."
                ),
            },
            {
                "id": "d",
                "text": "The -62 dBm signal strength is below the minimum threshold for VPN operation and the user needs to move closer to the access point.",
                "correct": False,
                "rationale": (
                    "Incorrect. -62 dBm is a reasonable signal strength for standard "
                    "802.11ac/Wi-Fi 5/Wi-Fi 6 operation (adequate for data rates up to "
                    "hundreds of Mbps). VPN operation does not require a minimum signal "
                    "strength beyond what is needed for a stable IP connection. The VPN "
                    "drops correlate to periodic 10–15 minute intervals, not to signal "
                    "fluctuations typical of weak signal."
                ),
            },
        ],
        "explanation": (
            "Wi-Fi Power Saving Mode (PSM / 802.11 PS-Poll) allows the wireless NIC to sleep "
            "between AP beacon intervals (typically every 100 ms) to save battery. In high "
            "PSM settings the adapter may miss multiple beacons, causing brief L2 link state "
            "changes. Stateful VPN software (IPsec, SSL VPN) monitors for interface events "
            "and drops the tunnel on perceived network changes. This is a well-known issue on "
            "laptops with aggressive power management. Fix: set Wi-Fi adapter Advanced "
            "properties to 'Maximum Performance' or disable PSM, or configure the VPN to "
            "tolerate brief interface events. Other users unaffected indicates a device-specific "
            "driver or power management setting."
        ),
    },
    # ------------------------------------------------------------------ #
    # 29 — Mobile display components
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-029",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile display components",
        "stem": (
            "A user notices that her laptop's built-in display flickers rapidly when the "
            "screen brightness is set below 50%, but does not flicker at 50% or above. "
            "An external monitor connected via HDMI shows no flicker. The flicker is "
            "visible in slow-motion video captured by a phone camera. Which technology "
            "is the MOST likely cause of the below-50% brightness flicker?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The display cable (eDP) is damaged and only transmits full signal above 50% brightness.",
                "correct": False,
                "rationale": (
                    "Incorrect. An eDP cable issue would affect the displayed image "
                    "regardless of brightness level (since eDP carries digital pixel data, "
                    "not a brightness signal) and would typically produce artifacts like "
                    "lines or dropouts, not brightness-correlated flicker."
                ),
            },
            {
                "id": "b",
                "text": "The display uses PWM (Pulse Width Modulation) dimming; at lower brightness levels the duty cycle drops, producing perceptible flicker at lower frequencies that some users and cameras can detect.",
                "correct": True,
                "rationale": (
                    "Correct. Many laptop LCDs dim the backlight using PWM — rapidly "
                    "switching the backlight on and off. At higher brightness, the 'on' "
                    "duty cycle is long and the perceived brightness is high; at lower "
                    "brightness, the duty cycle shortens. If the PWM frequency is low "
                    "(e.g., 200 Hz or less), the rapid switching becomes perceptible "
                    "as flicker at low brightness settings. Phone cameras, which sample "
                    "at known frame rates, can capture the flicker pattern. Displays "
                    "using DC dimming or high-frequency PWM (>1 kHz) do not exhibit "
                    "this issue."
                ),
            },
            {
                "id": "c",
                "text": "The GPU's display driver automatically reduces the display refresh rate from 60 Hz to 30 Hz below 50% brightness to save power, causing perceived flicker.",
                "correct": False,
                "rationale": (
                    "Incorrect. GPU display drivers do not automatically change the panel "
                    "refresh rate based on brightness level. Adaptive refresh rate features "
                    "(e.g., NVIDIA G-Sync, AMD FreeSync) adjust rate based on rendered "
                    "frame rate — not backlight brightness. A 60→30 Hz shift would also "
                    "produce a different, more noticeable symptom than typical PWM flicker."
                ),
            },
            {
                "id": "d",
                "text": "The laptop's battery is discharging below 50% capacity, causing power instability that produces display flicker.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes brightness-correlated flicker, not "
                    "battery-charge-correlated flicker. If battery discharge caused power "
                    "instability, other symptoms (random shutdowns, CPU throttling) would "
                    "appear simultaneously. The flicker occurring specifically below 50% "
                    "brightness (not 50% battery) is a precise correlation pointing to "
                    "PWM dimming, not power supply instability."
                ),
            },
        ],
        "explanation": (
            "PWM (Pulse Width Modulation) backlight dimming works by rapidly switching the "
            "backlight on/off. The ratio of on-time to total cycle time (duty cycle) determines "
            "perceived brightness. At low brightness settings the duty cycle is short and the "
            "'off' periods are longer, increasing the likelihood of perceptible flicker — "
            "especially at PWM frequencies below ~400 Hz. Users sensitive to flicker "
            "may experience eye strain. Solutions: use high-frequency PWM panels (>1 kHz) "
            "or DC dimming panels (no PWM), keep brightness above the flicker threshold, "
            "or use monitor software to overlay a slight brightness boost keeping duty cycle "
            "above the visible threshold."
        ),
    },
    # ------------------------------------------------------------------ #
    # 30 — Mobile connection types & ports
    # ------------------------------------------------------------------ #
    {
        "id": "a1d1v3-030",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A user plugs a USB-C cable from their laptop into a USB-C dock. The dock "
            "provides two USB-A 3.0 ports, HDMI output, SD card reader, and 65W power "
            "delivery passthrough. After connecting the dock, the laptop charges at only "
            "15W instead of the expected 65W. The USB-C cable included with the dock is "
            "labeled 'USB 2.0 certified, 5A'. Which is the MOST likely cause of the "
            "reduced charging speed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "USB Power Delivery at 65W requires USB 3.2 Gen 2 data capability in the cable; the USB 2.0 cable limits PD to 15W.",
                "correct": False,
                "rationale": (
                    "Incorrect. USB Power Delivery (USB PD) negotiation is independent of "
                    "the cable's data rate specification. A USB 2.0 cable can support USB PD "
                    "if it contains a valid e-Marker chip for cables rated above 3A/60W. "
                    "However, the specific issue here is related to cable markings, not data "
                    "speed."
                ),
            },
            {
                "id": "b",
                "text": "The USB 2.0 cable, despite its '5A' label, lacks a required e-Marker chip. USB PD above 60W (3A at 20V) requires an e-Marked cable; without the chip the PD controller falls back to a lower power contract.",
                "correct": True,
                "rationale": (
                    "Correct. USB PD requires cables rated for 5A to contain an e-Marker "
                    "chip (electronically marked) that communicates the cable's current "
                    "rating to the charger and device. A cable labeled '5A' without a "
                    "proper e-Marker chip will not communicate its rating; the PD "
                    "controllers fall back to the default 5V/3A (15W) contract — exactly "
                    "the symptom observed. A genuine e-Marked 5A USB-C cable would allow "
                    "the 65W (20V/3.25A) PD contract to be negotiated."
                ),
            },
            {
                "id": "c",
                "text": "The laptop's USB-C port is damaged; it can only receive 15W and must be repaired before 65W charging is possible.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the laptop port were damaged, the symptom would be "
                    "inconsistent or absent charging, not a clean fallback to exactly 15W "
                    "(the default USB PD baseline). The dock's included cable being labeled "
                    "'USB 2.0' is a specific and actionable clue pointing to a cable "
                    "capability issue."
                ),
            },
            {
                "id": "d",
                "text": "65W charging requires the dock to be plugged into a dedicated USB-C power port on the wall; connecting through the laptop USB-C port caps PD at 15W by design.",
                "correct": False,
                "rationale": (
                    "Incorrect. USB-C PD passthrough docks are specifically designed to "
                    "accept wall power via a DC barrel or USB-C port and pass it through "
                    "to the laptop via the upstream USB-C connection. The dock's 65W PD "
                    "passthrough is wall-powered and does not depend on the laptop's own "
                    "USB-C power output. The cable e-Marker issue is the correct explanation."
                ),
            },
        ],
        "explanation": (
            "USB PD e-Marker requirements: cables rated for currents above 3A (i.e., for >60W "
            "at 20V) must contain a USB PD e-Marker chip (also called an e-Mark or e-Marker "
            "IC). The e-Marker communicates the cable's capabilities (max current, max voltage, "
            "speed) to both connected devices. Without a valid e-Marker, PD controllers default "
            "to the safe fallback: 5V/3A = 15W. A cable labeled '5A' from a low-cost dock "
            "accessory may lack an e-Marker despite the label. Replace with a USB-C cable "
            "explicitly advertised as 'e-Marked' or '100W rated' to enable the full 65W PD "
            "contract."
        ),
    },
]

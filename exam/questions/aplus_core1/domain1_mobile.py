"""
CompTIA A+ Core 1 (220-1201) — Domain 1: Mobile Devices
24 practice questions at hard/expert difficulty.
"""

QUESTIONS = [
    {
        "id": "a1d1-001",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile email configuration",
        "stem": (
            "A user needs their corporate email configured on a personal phone so that "
            "messages and folders stay in sync across the phone, laptop, and webmail, "
            "and deleting a message on one device removes it everywhere. Which protocol "
            "and default secure port should the technician configure for incoming mail?"
        ),
        "options": [
            {
                "id": "a",
                "text": "IMAP over TCP 993",
                "correct": True,
                "rationale": (
                    "Correct. IMAP keeps mail on the server and synchronizes state "
                    "(read/unread, folders, deletions) across all clients. The secure "
                    "(implicit TLS) IMAP port is 993."
                ),
            },
            {
                "id": "b",
                "text": "POP3 over TCP 995",
                "correct": False,
                "rationale": (
                    "Incorrect. POP3 typically downloads and removes mail from the server "
                    "and does not synchronize folder state across devices; 995 is the "
                    "correct secure port for POP3 but POP3 is the wrong protocol for "
                    "multi-device sync."
                ),
            },
            {
                "id": "c",
                "text": "SMTP over TCP 587",
                "correct": False,
                "rationale": (
                    "Incorrect. SMTP is for sending (outgoing) mail, not retrieving or "
                    "synchronizing incoming mail; 587 is the SMTP submission port."
                ),
            },
            {
                "id": "d",
                "text": "IMAP over TCP 143",
                "correct": False,
                "rationale": (
                    "Incorrect. Port 143 is the cleartext/STARTTLS IMAP port. A secure "
                    "implicit-TLS connection requires port 993, not 143."
                ),
            },
        ],
        "explanation": (
            "IMAP synchronizes mailbox state across multiple devices (unlike POP3, which "
            "downloads and typically removes mail from the server). Changes such as "
            "deletions and folder moves propagate to all connected clients. Secure incoming "
            "ports: IMAPS 993, POP3S 995. Outgoing SMTP submission ports: 587 (STARTTLS) "
            "or 465 (implicit TLS)."
        ),
    },
    {
        "id": "a1d1-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is upgrading the storage in an ultrabook that has an M.2 slot "
            "labeled 'M.2 2280'. The existing drive is identified in the OS as an NVMe "
            "device. The technician sources a replacement M.2 drive that uses the SATA "
            "logical interface. Which outcome should the technician anticipate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SATA M.2 drive will function normally because the M.2 2280 physical slot is interface-agnostic.",
                "correct": False,
                "rationale": (
                    "Incorrect. While the M.2 2280 form factor describes only the physical "
                    "size (22 mm wide, 80 mm long), many ultrabooks with NVMe-only M.2 slots "
                    "do NOT electrically support SATA on that slot. Assuming interface-agnostic "
                    "operation is a common and costly misconception."
                ),
            },
            {
                "id": "b",
                "text": "The drive may not be recognized because the M.2 slot may be wired only for PCIe/NVMe and may not provide SATA signals.",
                "correct": True,
                "rationale": (
                    "Correct. M.2 slots can be keyed and wired for PCIe (NVMe), SATA, or "
                    "both. An M.2 slot that supported only NVMe will not provide the SATA "
                    "signals needed by a SATA M.2 drive, so the drive will be undetected. "
                    "The technician must verify the slot's supported interfaces in the system "
                    "documentation before purchasing a replacement."
                ),
            },
            {
                "id": "c",
                "text": "The SATA M.2 drive will be detected but will run at PCIe Gen 3 x4 speeds.",
                "correct": False,
                "rationale": (
                    "Incorrect. SATA M.2 drives run at SATA III speeds (~600 MB/s), not PCIe "
                    "Gen 3 x4 speeds (~3,500 MB/s). More importantly, a SATA drive cannot "
                    "operate in a PCIe-only slot regardless of speed expectations."
                ),
            },
            {
                "id": "d",
                "text": "The system will auto-negotiate between NVMe and SATA and use the slower SATA protocol.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no auto-negotiation between NVMe and SATA logical "
                    "interfaces. They use different command sets (NVM Express vs. AHCI) and "
                    "different electrical signals; the system cannot transparently switch "
                    "between them."
                ),
            },
        ],
        "explanation": (
            "The M.2 form factor uses a standardized connector but M.2 slots may be wired "
            "for PCIe/NVMe only, SATA only, or both. The key notch (B-key, M-key, or B+M-key) "
            "gives a physical clue but is not definitive — board documentation must be checked. "
            "Installing a SATA M.2 drive into an NVMe-only slot will result in the drive not "
            "being detected. Always verify the slot's supported interface before ordering parts."
        ),
    },
    {
        "id": "a1d1-003",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile display components",
        "stem": (
            "A laptop's display suddenly becomes very dim but a faint image is still visible "
            "when a bright flashlight is shone on the screen. The external monitor port "
            "works normally. Which component has most likely failed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Digitizer",
                "correct": False,
                "rationale": (
                    "Incorrect. The digitizer is the touch-input layer; its failure would "
                    "affect touch response, not screen brightness. A faint image rules out "
                    "a digitizer fault."
                ),
            },
            {
                "id": "b",
                "text": "LCD panel",
                "correct": False,
                "rationale": (
                    "Incorrect. A failed LCD panel would typically produce no image or severe "
                    "distortion. The fact that a faint image is visible indicates the LCD "
                    "matrix itself is still producing an image — the illumination source has "
                    "failed."
                ),
            },
            {
                "id": "c",
                "text": "Inverter or backlight",
                "correct": True,
                "rationale": (
                    "Correct. A faint image visible under direct flashlight illumination is "
                    "the classic symptom of a failed backlight or, on older CCFL-backlit "
                    "panels, a failed inverter. The LCD matrix is working (image is present) "
                    "but the backlight is not illuminating it. Modern LED-backlit panels do "
                    "not use an inverter; on those, the LED backlight strip or driver circuit "
                    "has failed."
                ),
            },
            {
                "id": "d",
                "text": "Wi-Fi antenna cable",
                "correct": False,
                "rationale": (
                    "Incorrect. Wi-Fi antenna cables run through the display lid but affect "
                    "wireless connectivity, not screen brightness. This distractor exploits "
                    "knowledge that antenna wires are routed in the lid alongside display "
                    "cables."
                ),
            },
        ],
        "explanation": (
            "When an LCD display is dim but a faint image is still visible under a flashlight, "
            "the LCD matrix is functioning but the backlight is not. On older CCFL-based "
            "displays the inverter converts DC to the high-voltage AC that drives the CCFL "
            "tube; inverter failure kills the backlight. On modern LED-backlit displays, the "
            "LED driver board or the LED strip itself has failed. OLED displays have no "
            "separate backlight and would show a completely dark (dead) panel, not a faint "
            "image."
        ),
    },
    {
        "id": "a1d1-004",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A field technician needs to transfer a 4 GB firmware image from a laptop to a "
            "ruggedized industrial controller that has only a DB-9 connector on its serial "
            "port. The technician's laptop has USB-A, USB-C, and HDMI ports. Which adapter "
            "and transfer consideration is most accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use a USB-C to HDMI adapter; HDMI can carry data as well as video.",
                "correct": False,
                "rationale": (
                    "Incorrect. HDMI is a video/audio interface; it does not carry arbitrary "
                    "data between a laptop and a serial device. A USB-C to HDMI adapter "
                    "would not allow serial communication with the controller."
                ),
            },
            {
                "id": "b",
                "text": "Use a USB-A to DB-9 serial adapter, and expect very slow transfer speeds because RS-232 serial is typically limited to 115,200 bps or lower.",
                "correct": True,
                "rationale": (
                    "Correct. The controller exposes an RS-232 serial port (DB-9). A USB-to-"
                    "serial (RS-232) adapter lets the laptop communicate over that interface. "
                    "RS-232 is limited to roughly 115,200 bps in typical configurations, so "
                    "a 4 GB transfer would take many hours — the technician must plan "
                    "accordingly or use an alternative transfer method if available."
                ),
            },
            {
                "id": "c",
                "text": "Use a USB-C to DB-9 adapter; USB-C natively supports RS-232 signaling at 5 Gbps.",
                "correct": False,
                "rationale": (
                    "Incorrect. USB-C does not natively output RS-232 signals. A USB-C to "
                    "DB-9 adapter still contains a USB-to-serial chip (e.g., FTDI or "
                    "Prolific) internally; the 5 Gbps figure refers to USB 3.x data rates "
                    "and is irrelevant to the RS-232 serial speed seen by the controller."
                ),
            },
            {
                "id": "d",
                "text": "DB-9 connectors are always PS/2; the technician needs a USB-to-PS/2 adapter instead.",
                "correct": False,
                "rationale": (
                    "Incorrect. DB-9 (DE-9) connectors are used for RS-232 serial in "
                    "industrial equipment. PS/2 uses a round 6-pin mini-DIN connector, not "
                    "DB-9. Confusing DB-9 with PS/2 is a common misconception."
                ),
            },
        ],
        "explanation": (
            "RS-232 serial ports use the DB-9 (DE-9) male or female connector in most PC and "
            "industrial equipment. RS-232 baud rates top out at 115,200 bps in typical "
            "configurations (though higher rates exist in specific implementations). "
            "Transferring gigabytes over RS-232 is impractical; the technician should seek "
            "an alternative (USB drive, Ethernet, or TFTP) if possible. A USB-to-serial "
            "adapter (with a USB-A or USB-C host end and a DB-9 serial end) is required."
        ),
    },
    {
        "id": "a1d1-005",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "MDM/MAM",
        "stem": (
            "A company allows employees to use personal smartphones for work (BYOD). The "
            "security team wants to enforce a PIN policy and remotely wipe ONLY the corporate "
            "email and company app data if a device is reported lost, without erasing the "
            "employee's personal photos and apps. Which technology best satisfies this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Full MDM enrollment with a remote full-device wipe policy",
                "correct": False,
                "rationale": (
                    "Incorrect. Full MDM with a full-device wipe would erase all data on the "
                    "device including personal content. This violates the BYOD requirement to "
                    "preserve personal data and is likely to face employee resistance and "
                    "legal challenges."
                ),
            },
            {
                "id": "b",
                "text": "Mobile Application Management (MAM) with a selective wipe capability",
                "correct": True,
                "rationale": (
                    "Correct. MAM manages and enforces policy at the application layer without "
                    "requiring full device enrollment. A selective wipe removes only corporate "
                    "app data and credentials, leaving personal content intact — exactly the "
                    "BYOD requirement described."
                ),
            },
            {
                "id": "c",
                "text": "S/MIME certificate deployment via OTA profile",
                "correct": False,
                "rationale": (
                    "Incorrect. S/MIME provides email signing and encryption but does not "
                    "enforce device PIN policies or enable selective remote wipe. It addresses "
                    "a different security concern."
                ),
            },
            {
                "id": "d",
                "text": "Two-factor authentication enforced through the corporate email server",
                "correct": False,
                "rationale": (
                    "Incorrect. Two-factor authentication improves access security but does not "
                    "enable policy enforcement (PIN requirements) or remote selective wipe of "
                    "corporate data on a lost device."
                ),
            },
        ],
        "explanation": (
            "Mobile Device Management (MDM) manages the whole device — useful for corporate-"
            "owned devices. Mobile Application Management (MAM) manages specific apps and their "
            "data, making it the right fit for BYOD scenarios where employees retain control "
            "of their personal data. MAM selective wipe removes corporate app data (email, "
            "documents, credentials) without touching personal content such as photos or "
            "third-party apps."
        ),
    },
    {
        "id": "a1d1-006",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician replaces the keyboard in a laptop. After reassembly the keyboard "
            "works, but the TouchPad and the webcam both stop functioning. The external USB "
            "mouse works normally. Which is the most likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The replacement keyboard is incompatible with the laptop model.",
                "correct": False,
                "rationale": (
                    "Incorrect. An incompatible keyboard would affect keyboard operation, not "
                    "the TouchPad or webcam, which use separate internal connectors. The "
                    "keyboard was stated to work correctly."
                ),
            },
            {
                "id": "b",
                "text": "The internal USB hub on the system board has failed due to ESD during reassembly.",
                "correct": False,
                "rationale": (
                    "Incorrect. While ESD damage is possible, this would typically also affect "
                    "external USB ports. The scenario states an external USB mouse works normally, "
                    "making isolated internal USB hub failure less likely."
                ),
            },
            {
                "id": "c",
                "text": "A ribbon cable for the TouchPad or a cable routed through the keyboard assembly was not fully reseated during reassembly.",
                "correct": True,
                "rationale": (
                    "Correct. On many laptops, the TouchPad and webcam cables are routed "
                    "underneath or adjacent to the keyboard and must be disconnected during "
                    "keyboard removal. Both devices failing simultaneously after a keyboard "
                    "replacement strongly suggests one or more ribbon/ZIF cable connectors "
                    "were not fully reseated or were inadvertently dislodged during "
                    "reassembly."
                ),
            },
            {
                "id": "d",
                "text": "The BIOS settings reset to defaults during the repair, disabling the TouchPad and webcam.",
                "correct": False,
                "rationale": (
                    "Incorrect. BIOS settings do not reset simply because the keyboard was "
                    "replaced. Even if BIOS reset, a generic 'TouchPad disabled in BIOS' "
                    "scenario would not simultaneously disable both the TouchPad and the "
                    "webcam, which typically use different subsystems."
                ),
            },
        ],
        "explanation": (
            "When multiple internal components fail simultaneously after a specific repair, "
            "the most logical cause is a disrupted cable connection related to that repair. "
            "Laptop keyboards often share routing space with ZIF/FFC ribbon cables connecting "
            "the TouchPad and webcam to the motherboard. Incomplete cable seating or accidental "
            "cable damage during keyboard swaps is the leading cause of post-repair peripheral "
            "failures. Always verify all ribbon cables are fully locked in their ZIF connectors "
            "before closing the chassis."
        ),
    },
    {
        "id": "a1d1-007",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile network connectivity",
        "stem": (
            "A smartphone user reports that cellular calls drop frequently in an area where "
            "they previously had good service. Other users on the same carrier have no issues. "
            "The technician checks: signal bars appear normal, Wi-Fi calling is disabled, and "
            "the SIM is seated correctly. Which action is most appropriate to attempt first?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace the SIM card.",
                "correct": False,
                "rationale": (
                    "Incorrect. While SIM replacement is a valid troubleshooting step, it "
                    "is an escalated action. The technician has already verified the SIM "
                    "is seated correctly. A software update to carrier provisioning data "
                    "should be attempted before physical hardware replacement."
                ),
            },
            {
                "id": "b",
                "text": "Perform a Preferred Roaming List (PRL) update or baseband/carrier settings update.",
                "correct": True,
                "rationale": (
                    "Correct. The PRL (on CDMA networks) and carrier/baseband settings (on "
                    "GSM/LTE networks) determine which towers and frequencies the device "
                    "prioritizes. An outdated PRL or carrier profile can cause call drops "
                    "even when signal appears adequate, because the device may be connecting "
                    "to suboptimal towers. This is a non-destructive first step before "
                    "hardware replacement."
                ),
            },
            {
                "id": "c",
                "text": "Enable airplane mode, wait 30 seconds, then disable it to force a new network registration.",
                "correct": False,
                "rationale": (
                    "Incorrect. Toggling airplane mode forces the device to re-register with "
                    "the network and is a useful quick troubleshoot for registration errors, "
                    "but it does not update the device's stored carrier preferences or PRL. "
                    "It would not address the underlying cause of call drops in a specific "
                    "area if the carrier provisioning data is stale."
                ),
            },
            {
                "id": "d",
                "text": "Reset the device to factory defaults.",
                "correct": False,
                "rationale": (
                    "Incorrect. A factory reset is a drastic last-resort step that destroys "
                    "user data. It should not precede targeted, less disruptive steps such as "
                    "a PRL or carrier settings update."
                ),
            },
        ],
        "explanation": (
            "PRL (Preferred Roaming List) updates tell CDMA phones which towers/frequencies "
            "to prefer. On GSM/LTE devices, carrier settings updates serve a similar role, "
            "updating network provisioning, APN, visual voicemail, and call settings. Stale "
            "carrier data can cause call drops even with adequate signal strength, because "
            "the phone may be handing off to towers or bands that the carrier has since "
            "reconfigured. This is a low-risk, non-destructive first action before hardware "
            "replacement or factory reset."
        ),
    },
    {
        "id": "a1d1-008",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A user wants to pay at a retail checkout using their smartphone by tapping it "
            "against the payment terminal. The phone has Bluetooth 5.2, Wi-Fi 6, and NFC. "
            "Which technology does the payment terminal use for this contactless transaction, "
            "and what is the typical maximum communication range?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bluetooth; approximately 10 meters",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth has a range of approximately 10 meters (Class 2) "
                    "to 100 meters (Class 1) and is not used for tap-to-pay contactless "
                    "payments. Its range would make proximity-only transactions insecure "
                    "and technically unreliable for point-of-sale use."
                ),
            },
            {
                "id": "b",
                "text": "NFC; approximately 20 cm (about 8 inches)",
                "correct": True,
                "rationale": (
                    "Correct. Near-Field Communication (NFC) operates at 13.56 MHz with a "
                    "practical range of up to ~20 cm (though most tap-to-pay interactions "
                    "require 4 cm or less). NFC is the technology behind Apple Pay, Google "
                    "Pay, and Samsung Pay contactless transactions at retail terminals."
                ),
            },
            {
                "id": "c",
                "text": "Wi-Fi Direct; approximately 200 meters",
                "correct": False,
                "rationale": (
                    "Incorrect. Wi-Fi Direct enables peer-to-peer Wi-Fi connections and has "
                    "a range of up to ~200 meters, but it is not used for tap-to-pay retail "
                    "payment transactions. Its range makes it unsuitable as a proximity-"
                    "verification mechanism at a point-of-sale terminal."
                ),
            },
            {
                "id": "d",
                "text": "NFC; approximately 1 meter",
                "correct": False,
                "rationale": (
                    "Incorrect. While NFC is the correct technology, the 1-meter range is "
                    "wrong. NFC's maximum practical range is about 20 cm; real-world tap-to-"
                    "pay requires the device to be within a few centimeters of the terminal."
                ),
            },
        ],
        "explanation": (
            "NFC (Near-Field Communication) is the standard for contactless payments (Apple "
            "Pay, Google Pay, etc.) and operates at 13.56 MHz with a maximum range of ~20 cm. "
            "The short range is a security feature, ensuring physical proximity between payer "
            "and terminal. NFC also enables other use cases such as transit cards, access "
            "badges, and device pairing. Bluetooth's longer range would make payment "
            "interception trivial and is not used for POS contactless payments."
        ),
    },
    {
        "id": "a1d1-009",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile display components",
        "stem": (
            "A graphic designer complains that colors on their new IPS laptop display look "
            "accurate head-on, but a colleague reviewing the design from an extreme side angle "
            "says the colors appear washed out. The designer's previous TN panel showed the "
            "same symptom from extreme angles. The designer asks whether upgrading to an OLED "
            "panel would resolve the issue. Which statement is most accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OLED panels have the same limited viewing angle as TN panels because both use a backlight.",
                "correct": False,
                "rationale": (
                    "Incorrect. OLED panels do not use a backlight; each pixel emits its own "
                    "light. OLED panels have near-perfect viewing angles with no color shift, "
                    "unlike TN panels."
                ),
            },
            {
                "id": "b",
                "text": "IPS already offers near-180° viewing angles; color shift at extreme angles on an IPS panel indicates a defective unit.",
                "correct": False,
                "rationale": (
                    "Incorrect. IPS panels do offer much wider viewing angles than TN, but "
                    "some color shift at extreme angles (near 180°) is normal for IPS "
                    "technology. It does not indicate a defective panel."
                ),
            },
            {
                "id": "c",
                "text": "Yes, upgrading to OLED would resolve the issue; OLED pixels emit light independently, providing near-perfect color accuracy at any viewing angle.",
                "correct": True,
                "rationale": (
                    "Correct. OLED (Organic Light-Emitting Diode) panels have each pixel "
                    "self-illuminate, eliminating the backlight-and-LCD-matrix architecture "
                    "that causes viewing-angle color shift. OLED displays maintain color "
                    "fidelity at extreme angles, making them ideal for color-critical work "
                    "viewed by multiple people."
                ),
            },
            {
                "id": "d",
                "text": "The issue is caused by the Wi-Fi antenna cables running along the display bezel, which interfere with color rendering at wide angles.",
                "correct": False,
                "rationale": (
                    "Incorrect. Wi-Fi antenna cables are routed in the display lid but have "
                    "no effect on color rendering or viewing angles. This distractor exploits "
                    "knowledge that cables are present in the display assembly."
                ),
            },
        ],
        "explanation": (
            "Viewing angle performance: TN < VA < IPS < OLED. TN panels have severe color "
            "shift beyond ~45°. IPS panels greatly improve viewing angles but still show some "
            "shift at extreme angles (near 180°). OLED panels use self-emissive pixels with no "
            "backlight, producing consistent color regardless of viewing angle. VA panels sit "
            "between TN and IPS — better contrast but more color shift than IPS at wide angles. "
            "For multi-viewer color-critical work, OLED is the superior choice."
        ),
    },
    {
        "id": "a1d1-010",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Bluetooth pairing",
        "stem": (
            "A technician is pairing a new Bluetooth headset to a company smartphone. The "
            "headset supports Secure Simple Pairing (SSP) with the Numeric Comparison "
            "method. After enabling pairing mode on the headset, what is the correct sequence "
            "of steps to complete pairing securely?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enter the headset's default PIN (0000 or 1234) on the smartphone when prompted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Entering a static PIN (0000 or 1234) is the legacy PIN-based "
                    "pairing method used before Bluetooth 2.1. Modern Secure Simple Pairing "
                    "with Numeric Comparison does not use a shared PIN; it generates and "
                    "displays a 6-digit number on both devices for the user to confirm."
                ),
            },
            {
                "id": "b",
                "text": "On the smartphone, navigate to Bluetooth settings, select the headset from discovered devices, and confirm that the numeric code displayed on the smartphone matches the code shown on the headset, then accept on both devices.",
                "correct": True,
                "rationale": (
                    "Correct. Numeric Comparison SSP generates a 6-digit number displayed on "
                    "both devices. The user verifies the numbers match (protecting against "
                    "MITM attacks) and confirms on both devices. For headsets with no display, "
                    "the Just Works SSP association model is used (no user confirmation), but "
                    "when both devices support Numeric Comparison, the described steps apply."
                ),
            },
            {
                "id": "c",
                "text": "Scan a QR code on the headset using the smartphone camera to exchange the Bluetooth link key.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth pairing does not use QR code scanning. QR codes "
                    "may be used for Wi-Fi provisioning (WPS equivalent) or app downloads "
                    "but are not part of the Bluetooth Secure Simple Pairing specification."
                ),
            },
            {
                "id": "d",
                "text": "Press the WPS button on the headset and the WPS button on the smartphone simultaneously.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPS (Wi-Fi Protected Setup) is a Wi-Fi network authentication "
                    "mechanism, not a Bluetooth pairing method. Bluetooth and Wi-Fi are "
                    "separate radio technologies with different pairing/authentication "
                    "processes. Headsets do not have WPS buttons."
                ),
            },
        ],
        "explanation": (
            "Bluetooth Secure Simple Pairing (SSP), introduced in Bluetooth 2.1, uses one of "
            "four association models: Just Works (no user interaction, vulnerable to MITM), "
            "Numeric Comparison (6-digit code shown on both devices, user confirms match), "
            "Passkey Entry (one device displays, user enters on the other), and Out of Band "
            "(NFC or other channel used for key exchange). Numeric Comparison provides MITM "
            "protection and is used when both devices have displays. Legacy PIN pairing is "
            "used only with Bluetooth 2.0 and earlier devices."
        ),
    },
    {
        "id": "a1d1-011",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A laptop technician needs to upgrade RAM. The system board supports DDR4 SODIMM "
            "at 3200 MHz with a maximum of 64 GB across two slots. The technician installs "
            "two 32 GB DDR4-3200 SODIMM sticks from two different manufacturers. The system "
            "boots and shows 64 GB in the OS, but runs in single-channel mode. Which condition "
            "most likely explains single-channel operation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DDR4 SODIMM cannot operate in dual-channel mode; dual-channel is only possible with standard DIMM form factors.",
                "correct": False,
                "rationale": (
                    "Incorrect. DDR4 SODIMM supports dual-channel operation just as standard "
                    "DIMMs do. Form factor does not dictate channel capability — the memory "
                    "controller on the system board determines dual-channel support."
                ),
            },
            {
                "id": "b",
                "text": "The two modules have different XMP profiles or slightly different timing subtimings, causing the memory controller to fall back to single-channel.",
                "correct": False,
                "rationale": (
                    "Incorrect. Mismatched XMP profiles or minor timing differences typically "
                    "cause the system to run both modules at the slower specification, but "
                    "they would still operate in dual-channel mode. XMP profile mismatch "
                    "alone does not force single-channel operation."
                ),
            },
            {
                "id": "c",
                "text": "Both modules are installed in the same channel's slots (e.g., both in slots A1 and A2) rather than one per channel (A1 and B1).",
                "correct": True,
                "rationale": (
                    "Correct. Dual-channel mode requires one module per memory channel. On "
                    "most laptops with two SODIMM slots, each slot is a separate channel, "
                    "so installing one module in each slot enables dual-channel. However, "
                    "some platforms wire both slots to the same channel, or a BIOS/slot "
                    "assignment error can result in both modules running on one channel. "
                    "The technician must verify slot assignments in the service manual."
                ),
            },
            {
                "id": "d",
                "text": "DDR4-3200 exceeds the controller's rated speed, forcing it to downclock and use single-channel to maintain stability.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the memory speed exceeds the controller's rated maximum, "
                    "the controller downclocks the modules to a supported speed, but this "
                    "does not cause a channel-mode change. The scenario states the board "
                    "supports DDR4-3200, so speed is not the issue."
                ),
            },
        ],
        "explanation": (
            "Dual-channel memory requires one DIMM per memory channel. On most laptops with "
            "two SODIMM slots, each slot maps to a separate channel, and installing one "
            "module per slot automatically enables dual-channel. If a platform has a non-"
            "obvious slot arrangement (some have two slots per channel on four-slot boards), "
            "placing both modules in the same channel yields single-channel performance. "
            "Always consult the OEM service manual for correct dual-channel slot pairings."
        ),
    },
    {
        "id": "a1d1-012",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile synchronization",
        "stem": (
            "An executive's iPhone is configured to sync contacts, calendar, and notes to "
            "iCloud. She also wants the same data accessible on her Windows laptop via "
            "Outlook. She does NOT want to use a USB cable. What is the most direct "
            "supported method to achieve iCloud data in Outlook on Windows?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Install iCloud for Windows, sign in with the Apple ID, and enable the Outlook integration for contacts and calendars.",
                "correct": True,
                "rationale": (
                    "Correct. Apple publishes iCloud for Windows, which installs an Outlook "
                    "add-in that syncs iCloud Contacts and Calendars (and optionally Mail) "
                    "directly into the Outlook client via CalDAV/CardDAV protocols. This is "
                    "the supported, cable-free integration path."
                ),
            },
            {
                "id": "b",
                "text": "Configure Outlook to connect directly to icloud.com using IMAP on port 993 for contacts and calendar sync.",
                "correct": False,
                "rationale": (
                    "Incorrect. IMAP can sync iCloud Mail to Outlook but does not sync "
                    "Contacts or Calendar data. Contacts use CardDAV and Calendars use "
                    "CalDAV — neither is IMAP. This is a common misconception about what "
                    "IMAP can transfer."
                ),
            },
            {
                "id": "c",
                "text": "Enable Bluetooth tethering between the iPhone and laptop, which allows Outlook to pull data over the Bluetooth connection.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth tethering provides an internet connection from the "
                    "phone to the laptop; it does not create a synchronization channel for "
                    "contacts, calendars, or notes. Outlook would need a separate sync "
                    "mechanism regardless of the network connection type."
                ),
            },
            {
                "id": "d",
                "text": "Export contacts from iCloud.com as a vCard and import them into Outlook manually each time changes are made.",
                "correct": False,
                "rationale": (
                    "Incorrect. Manual vCard export/import is a one-time migration, not "
                    "ongoing synchronization. It does not keep data updated automatically "
                    "and does not address calendar or notes synchronization."
                ),
            },
        ],
        "explanation": (
            "iCloud for Windows is Apple's supported application for integrating iCloud "
            "services with Windows PCs. It installs an Outlook add-in using CalDAV (calendars) "
            "and CardDAV (contacts) to sync iCloud data bidirectionally with Outlook without "
            "a USB cable. IMAP handles email only. For Android-to-cloud scenarios, Google "
            "Workspace uses similar CalDAV/CardDAV mechanisms or the Google Workspace Sync "
            "for Outlook plugin."
        ),
    },
    {
        "id": "a1d1-013",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile email configuration",
        "stem": (
            "A security administrator needs outgoing email from a mobile device to be "
            "digitally signed so that recipients can verify the sender's identity and "
            "confirm the message has not been tampered with in transit. The corporate mail "
            "server is Exchange Online. Which technology and configuration step is required "
            "on the mobile device?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable S/MIME and install a personal S/MIME certificate (private key) on the device.",
                "correct": True,
                "rationale": (
                    "Correct. S/MIME (Secure/Multipurpose Internet Mail Extensions) provides "
                    "digital signatures and optional encryption for email. The sender's device "
                    "must have the S/MIME certificate's private key installed to sign outgoing "
                    "messages. Exchange Online supports S/MIME for mobile devices via MDM "
                    "certificate deployment."
                ),
            },
            {
                "id": "b",
                "text": "Configure the device to send mail over SMTP port 465 (implicit TLS) instead of port 587.",
                "correct": False,
                "rationale": (
                    "Incorrect. Switching from port 587 (STARTTLS) to 465 (implicit TLS) "
                    "encrypts the transport layer between the device and the mail server but "
                    "does not digitally sign the message content. Recipients cannot verify "
                    "sender identity or detect tampering from transport encryption alone."
                ),
            },
            {
                "id": "c",
                "text": "Enable two-factor authentication on the corporate account.",
                "correct": False,
                "rationale": (
                    "Incorrect. Two-factor authentication protects account access but does "
                    "not sign email messages. Recipients have no mechanism to verify "
                    "message integrity or sender identity via 2FA."
                ),
            },
            {
                "id": "d",
                "text": "Install a root CA certificate from the corporate PKI on the device.",
                "correct": False,
                "rationale": (
                    "Incorrect. Installing a root CA certificate establishes trust for "
                    "verifying others' certificates (e.g., for receiving signed emails or "
                    "trusting corporate TLS certificates) but does not give the device the "
                    "ability to sign its own outgoing mail. The device needs its own "
                    "personal certificate with a private key for signing."
                ),
            },
        ],
        "explanation": (
            "S/MIME provides end-to-end email security: digital signatures authenticate the "
            "sender and detect tampering; encryption protects message confidentiality. For "
            "signing, the sender's device needs a personal S/MIME certificate (issued by a "
            "trusted CA) including the private key. The recipient uses the sender's public "
            "key (in the certificate) to verify the signature. Transport encryption (TLS on "
            "SMTP port 465 or 587) protects only the hop between device and server; it does "
            "not provide end-to-end message integrity."
        ),
    },
    {
        "id": "a1d1-014",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A road warrior connects her laptop to a single USB-C hub that simultaneously "
            "provides: charging (100W PD), a 4K external display via DisplayPort Alt Mode, "
            "two USB-A ports for peripherals, and Gigabit Ethernet. She notices that plugging "
            "the hub into a USB-A to USB-C adapter on an older laptop provides no video output. "
            "Why does the display fail when using the adapter?"
        ),
        "options": [
            {
                "id": "a",
                "text": "USB-A ports do not support DisplayPort Alt Mode; Alt Mode requires a native USB-C port with the appropriate controller.",
                "correct": True,
                "rationale": (
                    "Correct. Alternate Mode (Alt Mode) repurposes the USB-C connector's "
                    "pins to carry non-USB signals such as DisplayPort or Thunderbolt. A "
                    "passive USB-A to USB-C adapter connects electrically to a USB-A port, "
                    "which has no Alt Mode support and no mechanism to pass DisplayPort "
                    "signals. The host system must have a native USB-C port with a controller "
                    "that supports Alt Mode for the display to work."
                ),
            },
            {
                "id": "b",
                "text": "USB-A 3.0 lacks sufficient bandwidth to drive a 4K display at 60 Hz.",
                "correct": False,
                "rationale": (
                    "Incorrect. While bandwidth is a consideration, the fundamental issue is "
                    "not bandwidth but the absence of Alt Mode support on USB-A. USB-A "
                    "physically cannot carry DisplayPort signals regardless of its data rate, "
                    "because the extra pins required for Alt Mode signaling do not exist on "
                    "the USB-A connector."
                ),
            },
            {
                "id": "c",
                "text": "The hub requires USB Power Delivery to activate its DisplayPort output, and USB-A cannot supply PD charging.",
                "correct": False,
                "rationale": (
                    "Incorrect. While USB-A ports generally cannot source USB PD voltages "
                    "above 5V, the reason the display fails is not power delivery. Many USB-C "
                    "hubs can operate their DisplayPort output from USB-C PD or from a wall "
                    "adapter independently. The core issue is the absence of Alt Mode "
                    "signaling support on USB-A."
                ),
            },
            {
                "id": "d",
                "text": "The USB-A to USB-C adapter must be a Thunderbolt 4 certified cable for Alt Mode video to work.",
                "correct": False,
                "rationale": (
                    "Incorrect. Thunderbolt 4 certification applies to USB-C cables and ports, "
                    "not USB-A. A passive USB-A to USB-C adapter cannot become capable of Alt "
                    "Mode simply by being Thunderbolt-certified; the host-side USB-A port "
                    "fundamentally lacks Alt Mode capability."
                ),
            },
        ],
        "explanation": (
            "USB-C Alternate Mode allows the USB-C connector's SuperSpeed lanes to be "
            "repurposed for DisplayPort, HDMI, or Thunderbolt signals. This requires: (1) a "
            "USB-C port on the host with Alt Mode support in the system's USB controller, and "
            "(2) a USB-C cable/dock that supports Alt Mode. A USB-A port, even at 3.2 Gen 2 "
            "speeds, has no Alt Mode capability and no mechanism to pass DisplayPort signals. "
            "Passive adapters from USB-A to USB-C do not add Alt Mode support."
        ),
    },
    {
        "id": "a1d1-015",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile network connectivity",
        "stem": (
            "A user's Android phone shows 'Mobile Hotspot' is active and the laptop can see "
            "the hotspot SSID, but the laptop cannot obtain an IP address and cannot access "
            "the internet. Other phones near the user connect to the hotspot without issue. "
            "Which is the LEAST likely cause of the laptop-specific failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The laptop's DHCP client service is stopped or malfunctioning.",
                "correct": False,
                "rationale": (
                    "Incorrect (i.e., this IS a plausible cause). If the laptop's DHCP "
                    "client cannot request an IP address, it would fail to obtain connectivity "
                    "even though other devices connect successfully. This is a likely "
                    "laptop-specific cause."
                ),
            },
            {
                "id": "b",
                "text": "The laptop's wireless adapter driver is outdated or corrupted, preventing it from completing the DHCP handshake.",
                "correct": False,
                "rationale": (
                    "Incorrect (i.e., this IS a plausible cause). A faulty wireless adapter "
                    "driver on the specific laptop could cause failures after association "
                    "but before or during IP address acquisition, explaining why only the "
                    "laptop fails."
                ),
            },
            {
                "id": "c",
                "text": "The smartphone's carrier data plan has reached its hotspot data cap for the billing period.",
                "correct": True,
                "rationale": (
                    "Correct — this is the LEAST likely laptop-specific cause. If the carrier "
                    "hotspot data cap were exhausted, ALL devices connecting to the hotspot "
                    "would lose internet access, including the other phones that the scenario "
                    "states connect 'without issue'. This would not cause a laptop-specific "
                    "failure."
                ),
            },
            {
                "id": "d",
                "text": "The laptop's MAC address is not on the hotspot's allowed device list if MAC filtering is enabled.",
                "correct": False,
                "rationale": (
                    "Incorrect (i.e., this IS a plausible cause). Some hotspot implementations "
                    "allow MAC address filtering. If the laptop's MAC is not permitted, it "
                    "would explain why only the laptop cannot connect while other devices can."
                ),
            },
        ],
        "explanation": (
            "This question asks for the LEAST likely cause of a laptop-specific failure. When "
            "other devices connect successfully to the same hotspot, the problem is isolated "
            "to the laptop itself. A carrier data cap would affect all connected devices "
            "simultaneously, making it the least likely explanation for a device-specific "
            "issue. Laptop-specific causes include a stopped DHCP client service, a corrupted "
            "wireless driver, MAC filtering, or an IP address conflict."
        ),
    },
    {
        "id": "a1d1-016",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is replacing the HDD in a laptop with an SSD. The laptop has a "
            "2.5-inch SATA III HDD bay and no M.2 slot. After cloning the HDD to a 2.5-inch "
            "SATA SSD, the technician installs the SSD and powers on. The system posts "
            "correctly but stops at a 'No bootable device' error. The HDD was confirmed "
            "working in an external enclosure after cloning. Which is the most likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SATA III SSDs are not backward compatible with SATA II controllers.",
                "correct": False,
                "rationale": (
                    "Incorrect. SATA is backward and forward compatible. A SATA III SSD "
                    "will operate at SATA II speeds (3 Gbps) on a SATA II controller; it "
                    "will not fail to boot because of speed negotiation."
                ),
            },
            {
                "id": "b",
                "text": "The clone did not replicate the Master Boot Record or EFI System Partition, so the drive has data but no valid boot record.",
                "correct": True,
                "rationale": (
                    "Correct. 'No bootable device' after a successful clone almost always "
                    "indicates a cloning error. Sector-by-sector clones that skip partition "
                    "alignment, cloning tools that copy only data partitions (missing the "
                    "MBR or EFI System Partition), or destination drives smaller than the "
                    "source all result in data that is present but not bootable. The "
                    "technician should verify the clone included the boot partition using "
                    "the cloning tool's log, then re-clone or manually repair the bootloader."
                ),
            },
            {
                "id": "c",
                "text": "The BIOS boot order still lists the original HDD first; swapping it to the SSD will fix the error.",
                "correct": False,
                "rationale": (
                    "Incorrect. BIOS boot order is a valid troubleshooting step, but the "
                    "original HDD has been physically removed. The BIOS should fall through "
                    "to the next bootable device; it would not find the HDD and should "
                    "attempt the SSD. If the SSD has a valid boot record, a simple boot "
                    "order issue would not produce 'No bootable device' — the BIOS would "
                    "automatically try the SSD."
                ),
            },
            {
                "id": "d",
                "text": "The SSD requires a firmware update from the manufacturer before it can function as a system drive.",
                "correct": False,
                "rationale": (
                    "Incorrect. Consumer SSDs do not require firmware updates before they "
                    "can boot an OS. Factory firmware is always sufficient for basic "
                    "operation; firmware updates add features or fix bugs but are not "
                    "prerequisites for bootability."
                ),
            },
        ],
        "explanation": (
            "After a drive clone, 'No bootable device' most commonly indicates the boot "
            "structures were not replicated correctly. For MBR disks, the Master Boot Record "
            "and partition boot record must be present. For GPT/UEFI systems, the EFI System "
            "Partition (ESP) with the bootloader must exist and the partition marked 'active'. "
            "Cloning tools must perform a full partition-aware clone, not just a file copy. "
            "Always verify the clone includes all partitions (including hidden/system "
            "partitions) and that the destination drive's boot record is intact."
        ),
    },
    {
        "id": "a1d1-017",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Location services",
        "stem": (
            "A smartphone app requests permission to access location services. The device "
            "has GPS, Wi-Fi, and cellular radios. The user is indoors with no GPS signal "
            "lock. The app still shows an accurate location within 15 meters. Which "
            "technology is providing the location data?"
        ),
        "options": [
            {
                "id": "a",
                "text": "GPS satellite triangulation using the device's A-GPS chip.",
                "correct": False,
                "rationale": (
                    "Incorrect. GPS requires line-of-sight to at least four satellites. "
                    "Indoors, GPS signals are typically too attenuated to achieve a fix. "
                    "Assisted GPS (A-GPS) downloads satellite ephemeris data to speed "
                    "initial acquisition but still relies on the GPS radio receiving "
                    "satellite signals, which are unavailable indoors."
                ),
            },
            {
                "id": "b",
                "text": "Wi-Fi positioning using a database of nearby access point MAC addresses and signal strengths.",
                "correct": True,
                "rationale": (
                    "Correct. When GPS is unavailable (indoors), smartphones use Wi-Fi "
                    "Positioning System (WPS) technology — scanning nearby Wi-Fi access "
                    "point BSSIDs and comparing their signal strengths against a crowd-"
                    "sourced database (e.g., Google's or Apple's location services database) "
                    "to estimate location. This can achieve 15–40 meter accuracy indoors "
                    "without connecting to any Wi-Fi network."
                ),
            },
            {
                "id": "c",
                "text": "Bluetooth beacons installed in the building providing indoor positioning.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth beacon-based indoor positioning is a specialized "
                    "technology requiring infrastructure deployment of beacons and a "
                    "compatible app. It is not a generic smartphone location service available "
                    "in all apps. The scenario describes a standard app with OS location "
                    "permissions, not a dedicated beacon infrastructure."
                ),
            },
            {
                "id": "d",
                "text": "Cellular tower triangulation using signal strength from multiple cell towers.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cell tower triangulation is a location method, but it "
                    "typically provides accuracy of 100–1,000 meters — not 15 meters. "
                    "The 15-meter accuracy described is characteristic of Wi-Fi positioning, "
                    "not cellular triangulation."
                ),
            },
        ],
        "explanation": (
            "Modern smartphones use a combination of location technologies managed by the OS "
            "location engine: GPS (most accurate, 3–5 m, requires outdoor satellite view), "
            "Wi-Fi positioning (15–40 m, uses AP MAC/BSSID database), cell tower "
            "triangulation (100–1,000 m), and sensor fusion (accelerometer, barometer). "
            "When GPS is unavailable indoors, the OS automatically falls back to Wi-Fi "
            "positioning for sub-50-meter accuracy. The device does NOT need to be connected "
            "to Wi-Fi — passive scanning of nearby BSSIDs is sufficient."
        ),
    },
    {
        "id": "a1d1-018",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A user's laptop has a docking station and a colleague recommends using a port "
            "replicator instead. The user's workflow requires connecting three additional "
            "USB peripherals, a second display at 4K/60Hz, and Gigabit Ethernet — none of "
            "which the laptop's built-in ports can accommodate simultaneously. Which "
            "statement correctly distinguishes whether a port replicator meets the user's "
            "needs?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A port replicator is equivalent to a docking station and will fully support three USB devices, 4K display output, and Gigabit Ethernet simultaneously.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port replicators and docking stations are not equivalent. "
                    "A port replicator exposes ports that already exist on the laptop "
                    "(pass-through), providing convenience but no additional bandwidth or "
                    "functionality beyond what the laptop's built-in ports already support. "
                    "A docking station typically adds independent controllers (USB hub IC, "
                    "DisplayLink or Alt Mode video, Ethernet chip) that extend the laptop's "
                    "capabilities."
                ),
            },
            {
                "id": "b",
                "text": "A port replicator will not meet the user's needs because it only mirrors existing laptop ports and adds no new controllers; a docking station provides independent additional functionality.",
                "correct": True,
                "rationale": (
                    "Correct. A port replicator is a passive or near-passive device that "
                    "replicates the laptop's existing connectors in a more convenient "
                    "location (e.g., a proprietary bottom-docking connector exposing the "
                    "same ports as the laptop's sides). It does NOT add capabilities the "
                    "laptop doesn't already have. A docking station connects (usually via "
                    "USB-C/Thunderbolt) and includes additional chips to provide expanded "
                    "USB ports, independent display output, and Ethernet not present on the "
                    "laptop itself."
                ),
            },
            {
                "id": "c",
                "text": "A port replicator will work for USB and Ethernet but cannot provide 4K display output without a separate USB display adapter.",
                "correct": False,
                "rationale": (
                    "Incorrect. This partially mischaracterizes port replicators. A true "
                    "port replicator does not independently add Ethernet or USB controllers "
                    "either — it only replicates what the laptop already has. If the laptop "
                    "has no built-in Gigabit Ethernet, a port replicator will not provide it."
                ),
            },
            {
                "id": "d",
                "text": "Both docking stations and port replicators require Thunderbolt 4 ports on the laptop.",
                "correct": False,
                "rationale": (
                    "Incorrect. Docking stations can use USB-C (with or without Thunderbolt), "
                    "proprietary connectors, or even USB-A. Port replicators often use "
                    "proprietary laptop-specific connectors. Neither universally requires "
                    "Thunderbolt 4."
                ),
            },
        ],
        "explanation": (
            "Port replicator: a passive or near-passive device that extends the laptop's "
            "existing connectors to a more accessible location — it adds no new capabilities. "
            "Docking station: adds independent hardware controllers (USB hub, DisplayLink "
            "video, Ethernet MAC, audio codec) to provide capabilities beyond what the "
            "laptop's built-in ports offer. For a user requiring 4K external display, "
            "additional USB ports, and Gigabit Ethernet that the laptop lacks natively, "
            "a docking station is required."
        ),
    },
    {
        "id": "a1d1-019",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile display components",
        "stem": (
            "A technician is replacing a digitizer on a laptop touchscreen. After reassembly, "
            "the display shows the correct image but touch input is offset by about 2 cm "
            "toward the upper-left corner of the screen across all touch points. The touch "
            "response itself is accurate in relative movement (dragging follows the finger "
            "correctly). What is the most likely cause and resolution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The digitizer is a slightly different model with different resolution; it needs to be replaced again with the exact OEM part.",
                "correct": False,
                "rationale": (
                    "Incorrect. A resolution mismatch between the digitizer and display "
                    "panel would cause scaling issues across the entire touch surface, not "
                    "a consistent linear offset. The fact that relative movement is accurate "
                    "argues against a resolution mismatch."
                ),
            },
            {
                "id": "b",
                "text": "The touch calibration data stored in firmware is misaligned and needs to be reset or recalibrated in the OS or BIOS.",
                "correct": True,
                "rationale": (
                    "Correct. A consistent uniform offset (all touch points displaced by the "
                    "same vector) with accurate relative movement is the classic symptom of "
                    "a calibration offset, not a hardware fault. The digitizer reports touch "
                    "correctly in its own coordinate space, but the mapping to display "
                    "coordinates is shifted. Running the touchscreen calibration utility in "
                    "the OS (or resetting calibration data in BIOS/firmware) resolves this "
                    "without hardware replacement."
                ),
            },
            {
                "id": "c",
                "text": "The digitizer ribbon cable was reconnected incorrectly, reversing the X-axis, which must be corrected by rerouting the cable.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reversing the X-axis would mirror touch inputs horizontally "
                    "across the center line — dragging right would move the cursor left, "
                    "which contradicts the scenario stating relative movement is accurate. "
                    "A reversed axis also produces non-uniform offset, not a fixed offset "
                    "in one direction."
                ),
            },
            {
                "id": "d",
                "text": "The LCD panel and digitizer layers are physically misaligned; the display assembly must be disassembled and realigned.",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical layer misalignment between the LCD and digitizer "
                    "would produce a visual parallax effect visible to the user, and the "
                    "offset would vary depending on viewing angle. Software calibration "
                    "resolves a coordinate mapping offset without requiring physical "
                    "realignment of layers."
                ),
            },
        ],
        "explanation": (
            "Touchscreen digitizers report touch coordinates in their own coordinate space; "
            "the OS or firmware maps these to display pixels using calibration data. A "
            "uniform offset across all touch points with correct relative motion indicates "
            "the digitizer hardware is working but the calibration mapping is wrong. This "
            "commonly occurs after digitizer replacement when the new panel has slightly "
            "different physical dimensions or when old calibration data persists. "
            "Recalibration via the OS (Settings > Tablet PC Settings > Calibrate on Windows, "
            "or equivalent) or BIOS reset corrects the mapping."
        ),
    },
    {
        "id": "a1d1-020",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile synchronization",
        "stem": (
            "A user's vehicle infotainment system supports both Apple CarPlay and Android "
            "Auto via USB. The user recently switched from an iPhone to a new Android phone. "
            "After connecting the Android phone via the same USB cable, the car does not "
            "recognize Android Auto. The phone is running the latest Android version. "
            "Which is the most likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The USB cable is a Lightning cable, which is incompatible with the Android phone's USB-C port.",
                "correct": True,
                "rationale": (
                    "Correct. The user previously used an iPhone, which uses a Lightning "
                    "connector. The same cable would be a Lightning cable, which is physically "
                    "incompatible with the Android phone's USB-C port. Android Auto requires "
                    "a USB-C (or Micro-USB on older devices) cable. Using the 'same cable' "
                    "from an iPhone setup is the key clue."
                ),
            },
            {
                "id": "b",
                "text": "Android Auto requires Wi-Fi to function and cannot use a USB connection.",
                "correct": False,
                "rationale": (
                    "Incorrect. Android Auto supports both USB (wired) and wireless "
                    "connections (on supported vehicles). The question specifies the "
                    "infotainment supports USB for Android Auto. USB is a valid connection "
                    "method for Android Auto."
                ),
            },
            {
                "id": "c",
                "text": "The vehicle infotainment firmware needs to be updated to support Android Auto after previously being configured for CarPlay.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the infotainment supports both CarPlay "
                    "and Android Auto. Switching between them does not require a firmware "
                    "update; these are independent protocols selected by which device is "
                    "connected. A firmware update is a lower-probability cause given the "
                    "obvious cable mismatch clue in the scenario."
                ),
            },
            {
                "id": "d",
                "text": "The Android Auto app must be downloaded from the Google Play Store separately before it can be used.",
                "correct": False,
                "rationale": (
                    "Incorrect. On Android 10 and later, Android Auto is built into the OS "
                    "and does not require a separate download from the Play Store. On older "
                    "versions it was a downloadable app, but the scenario states the phone "
                    "runs the latest Android. Even if this were required, it would not be "
                    "the most likely cause compared to the physical cable incompatibility."
                ),
            },
        ],
        "explanation": (
            "iPhone uses the Lightning connector; Android phones use USB-C (modern) or "
            "Micro-USB (older). A Lightning cable is physically incompatible with USB-C and "
            "cannot be inserted — the most immediate and obvious cause of failure when "
            "'using the same cable'. Android Auto is natively integrated into Android 10+ "
            "and supports wired USB connections to compatible infotainment systems. Always "
            "verify the physical connector matches the device before escalating to software "
            "or firmware troubleshooting."
        ),
    },
    {
        "id": "a1d1-021",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Laptop hardware",
        "stem": (
            "A laptop fails to power on at all — no lights, no fan spin, no POST — even "
            "when connected to a verified working AC adapter. Removing and reinserting the "
            "battery has no effect. A colleague suggests performing a hard reset by "
            "disconnecting all power and holding the power button for 30 seconds. This "
            "resolves the issue and the laptop boots normally. What does the hard reset "
            "most likely accomplish in this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It resets the BIOS firmware to factory defaults, clearing a corrupt BIOS setting that prevented POST.",
                "correct": False,
                "rationale": (
                    "Incorrect. Holding the power button with no power connected does not "
                    "reset BIOS settings. BIOS/UEFI settings are stored in non-volatile "
                    "flash memory or CMOS backed by a coin cell battery; they are not "
                    "cleared by this procedure (which drains only capacitors)."
                ),
            },
            {
                "id": "b",
                "text": "It drains residual charge from capacitors on the system board, releasing a stuck Embedded Controller or power circuit latch that prevents power-on.",
                "correct": True,
                "rationale": (
                    "Correct. Modern laptops have an Embedded Controller (EC) that manages "
                    "power sequencing. If the EC enters a hung or undefined power state "
                    "(due to an interrupted shutdown, static discharge, or power fault), the "
                    "laptop may refuse to power on. Disconnecting all power sources and "
                    "holding the power button for 30 seconds drains residual capacitor charge, "
                    "resetting the EC to its initial state and allowing normal power-on to "
                    "proceed."
                ),
            },
            {
                "id": "c",
                "text": "It forces the system board to switch from battery power to AC power priority, resolving a power source arbitration error.",
                "correct": False,
                "rationale": (
                    "Incorrect. Power source arbitration between AC and battery is managed "
                    "by the power management controller and does not require a hard reset "
                    "procedure. The scenario specifies both AC and battery were connected "
                    "without effect before the hard reset; this explanation does not fit."
                ),
            },
            {
                "id": "d",
                "text": "It clears the TPM (Trusted Platform Module) state, which was blocking the boot sequence for security reasons.",
                "correct": False,
                "rationale": (
                    "Incorrect. The TPM stores cryptographic keys and measurements used for "
                    "Secure Boot and disk encryption. It does not prevent POST from initiating "
                    "entirely. A TPM issue would manifest as a BitLocker key request or "
                    "Secure Boot failure after POST, not as a complete no-power state."
                ),
            },
        ],
        "explanation": (
            "The Embedded Controller (EC) on modern laptops manages power rails, keyboard, "
            "fan control, and other functions. If the EC enters a fault or undefined state, "
            "it can latch the system in a no-power condition that persists even after AC/battery "
            "reconnection. The hard reset (disconnect all power, hold power button 30 seconds) "
            "drains residual capacitor charge from the EC's power rails, forcing it to cold-"
            "reset. This is a standard laptop troubleshooting step documented by most OEMs "
            "for 'completely dead' laptop scenarios."
        ),
    },
    {
        "id": "a1d1-022",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is preparing to replace the battery in a non-removable battery "
            "laptop. (Choose TWO actions that represent best practices during this procedure.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Discharge the battery to below 25% charge before opening the chassis to reduce the risk of thermal event if the battery is punctured.",
                "correct": True,
                "rationale": (
                    "Correct. A partially or fully charged lithium-ion battery contains "
                    "significant stored energy. Discharging below 25% (or as low as possible) "
                    "before replacement reduces the severity of a potential thermal runaway "
                    "event if the battery casing is accidentally punctured during removal."
                ),
            },
            {
                "id": "b",
                "text": "Use a spudger or plastic pry tool to disconnect the battery connector from the system board before removing any other internal components.",
                "correct": True,
                "rationale": (
                    "Correct. Disconnecting the battery connector (using a non-conductive "
                    "plastic tool to avoid shorting the connector) before working on other "
                    "internal components removes the risk of accidental power delivery to "
                    "circuits or components being serviced, preventing ESD damage and "
                    "short circuits."
                ),
            },
            {
                "id": "c",
                "text": "Leave the AC adapter connected throughout the procedure so the system board remains powered and the BIOS retains its settings.",
                "correct": False,
                "rationale": (
                    "Incorrect. Working inside a laptop with AC power connected is unsafe and "
                    "violates standard repair practice. AC power should be disconnected before "
                    "opening any laptop chassis. BIOS settings are stored in non-volatile "
                    "memory and are not lost when AC is disconnected."
                ),
            },
            {
                "id": "d",
                "text": "Cut the battery wires rather than unplug the connector if the connector is difficult to reach, then splice in the new battery wires.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cutting lithium-ion battery wires is extremely dangerous — "
                    "it risks shorting the battery cells, causing a thermal event, fire, or "
                    "explosion. Battery connectors should always be unplugged, not cut. If "
                    "access is difficult, the correct approach is to remove obstructing "
                    "components first."
                ),
            },
        ],
        "explanation": (
            "Lithium-ion laptop battery replacement safety: (1) Discharge the battery below "
            "25% to reduce stored energy before potential puncture. (2) Disconnect AC power "
            "before opening the chassis. (3) Use plastic/non-conductive tools to unplug the "
            "battery connector before other disassembly. (4) Never cut battery wires or use "
            "metal tools near exposed battery cells. Non-removable batteries are often "
            "adhered with adhesive pull-tabs; apply isopropyl alcohol to soften adhesive if "
            "needed. Always follow the OEM service manual."
        ),
    },
    {
        "id": "a1d1-023",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A user wants to use their smartphone as a hotspot to provide internet to a "
            "laptop. The carrier supports tethering on the plan. (Choose TWO methods the "
            "smartphone can use to share its cellular data connection with the laptop.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wi-Fi hotspot: the smartphone broadcasts an SSID and the laptop connects via Wi-Fi.",
                "correct": True,
                "rationale": (
                    "Correct. Wi-Fi hotspot (personal hotspot) is the most common tethering "
                    "method. The phone acts as a wireless access point, broadcasting an SSID. "
                    "The laptop connects to it as it would any Wi-Fi network. No special "
                    "drivers are needed on the laptop."
                ),
            },
            {
                "id": "b",
                "text": "USB tethering: the smartphone is connected to the laptop via USB cable and shares its cellular connection as a virtual network adapter.",
                "correct": True,
                "rationale": (
                    "Correct. USB tethering makes the smartphone appear as a RNDIS (Windows) "
                    "or ECM (macOS/Linux) network adapter when connected via USB. This "
                    "provides internet access and is often faster and more stable than Wi-Fi "
                    "hotspot because it doesn't consume the phone's Wi-Fi radio."
                ),
            },
            {
                "id": "c",
                "text": "NFC tethering: the laptop taps the smartphone to receive a static IP address from the carrier.",
                "correct": False,
                "rationale": (
                    "Incorrect. NFC cannot transfer internet traffic or provide tethering. "
                    "NFC can be used to initiate a connection (e.g., Android Beam/Nearby "
                    "Share to negotiate a Bluetooth or Wi-Fi Direct session) but cannot "
                    "itself carry IP tethering traffic. Carriers do not assign static IPs "
                    "via NFC."
                ),
            },
            {
                "id": "d",
                "text": "HDMI tethering: the smartphone shares its IP connection via the HDMI port using USBOTG.",
                "correct": False,
                "rationale": (
                    "Incorrect. HDMI is a video output interface and does not carry IP "
                    "network traffic for tethering. USB OTG allows a phone to act as a USB "
                    "host (e.g., to connect USB peripherals) but 'HDMI tethering' is not a "
                    "real technology."
                ),
            },
        ],
        "explanation": (
            "Smartphone tethering methods: (1) Wi-Fi hotspot — phone broadcasts SSID, laptop "
            "connects wirelessly; (2) USB tethering — phone appears as a RNDIS/ECM network "
            "adapter via USB cable; (3) Bluetooth tethering — phone shares cellular via "
            "Bluetooth PAN (slower, ~3 Mbps). NFC and HDMI are not tethering mechanisms. "
            "USB tethering is generally fastest; Wi-Fi hotspot is most convenient. Carrier "
            "plan must include hotspot/tethering; some carriers throttle hotspot data separately."
        ),
    },
    {
        "id": "a1d1-024",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "MDM/MAM",
        "stem": (
            "A company is implementing MDM for corporate-owned Android devices. The security "
            "policy requires: (1) remote lock/wipe capability, (2) enforcement of a minimum "
            "8-character alphanumeric PIN, and (3) prevention of users from installing "
            "unapproved apps. (Choose TWO MDM capabilities that directly enforce requirements "
            "2 and 3.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Device compliance policy: enforce a minimum password complexity and length rule that the device must satisfy to maintain access to corporate resources.",
                "correct": True,
                "rationale": (
                    "Correct. MDM compliance policies can mandate minimum password/PIN length, "
                    "character complexity (alphanumeric), and maximum password age. If a device "
                    "does not meet the policy, MDM can block access to corporate resources or "
                    "alert an administrator. This directly satisfies requirement 2."
                ),
            },
            {
                "id": "b",
                "text": "Kiosk mode or managed app allowlist: restrict the device to only MDM-approved applications, preventing installation of unapproved apps.",
                "correct": True,
                "rationale": (
                    "Correct. MDM can apply an application allowlist (managed Google Play on "
                    "Android Enterprise, or kiosk/single-app mode) that prevents users from "
                    "installing apps outside the approved catalog. The MDM pushes approved "
                    "apps silently and blocks or removes unapproved ones. This directly "
                    "satisfies requirement 3."
                ),
            },
            {
                "id": "c",
                "text": "S/MIME certificate enrollment: automatically push email signing certificates to all managed devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. S/MIME certificate enrollment is a valid MDM capability but "
                    "it addresses email signing/encryption, not PIN complexity enforcement or "
                    "app restriction. It does not directly satisfy requirements 2 or 3."
                ),
            },
            {
                "id": "d",
                "text": "PRL update push: remotely trigger a Preferred Roaming List update on all managed devices to ensure optimal cellular performance.",
                "correct": False,
                "rationale": (
                    "Incorrect. PRL updates manage cellular network preferences and are "
                    "relevant to cellular connectivity troubleshooting. PRL updates do not "
                    "enforce PIN policies or restrict application installation. This does "
                    "not satisfy requirements 2 or 3."
                ),
            },
        ],
        "explanation": (
            "MDM for corporate Android devices (via Android Enterprise) provides: password/"
            "PIN policy enforcement (length, complexity, biometric requirements); remote "
            "lock and full/selective wipe; managed Google Play for app allowlisting (only "
            "approved apps visible and installable); network configuration (Wi-Fi, VPN, "
            "APN); and certificate management (Wi-Fi, VPN, S/MIME certs). PIN complexity "
            "is enforced via compliance/configuration policies. App restriction uses managed "
            "Google Play with an allowlist or kiosk mode for single-purpose devices."
        ),
    },
]

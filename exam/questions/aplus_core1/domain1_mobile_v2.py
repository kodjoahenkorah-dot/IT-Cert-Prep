"""
CompTIA A+ Core 1 (220-1201) — Domain 1: Mobile Devices
25 additional practice questions at hard/expert difficulty (v2).
"""

QUESTIONS = [
    {
        "id": "a1d1v2-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is servicing a laptop that has a socketed CPU. The system "
            "powers on but immediately shuts off after three seconds. The fan spins "
            "briefly and the POST code LED shows a thermal fault. After reseating the "
            "CPU and applying new thermal compound, the problem persists. Which "
            "component is the NEXT most likely cause of the thermal fault shutdown?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The CPU itself has a cracked die and must be replaced.",
                "correct": False,
                "rationale": (
                    "Incorrect. A cracked die typically causes a dead system or random "
                    "errors, not a consistent thermal fault code. Thermal fault codes "
                    "originate from temperature sensors, not die integrity."
                ),
            },
            {
                "id": "b",
                "text": "The heat pipe or heatsink fins are clogged with debris, preventing adequate heat dissipation despite fresh thermal compound.",
                "correct": True,
                "rationale": (
                    "Correct. After reseating the CPU and applying fresh thermal compound, "
                    "the thermal interface between the CPU and heatsink is restored. If "
                    "the heatsink fins or heat pipe are blocked with dust and debris, heat "
                    "cannot be transferred away from the heatsink efficiently. The CPU "
                    "reaches thermal shutdown temperature within seconds regardless of "
                    "compound quality. Cleaning the heatsink assembly is the next "
                    "appropriate step."
                ),
            },
            {
                "id": "c",
                "text": "The BIOS thermal threshold is set too low and must be increased in the power management settings.",
                "correct": False,
                "rationale": (
                    "Incorrect. Laptop BIOS thermal thresholds are OEM-set safety values "
                    "and cannot typically be raised by a technician. More importantly, a "
                    "shutdown within three seconds indicates the CPU is genuinely overheating "
                    "rapidly, not that the threshold is artificially low."
                ),
            },
            {
                "id": "d",
                "text": "The replacement thermal compound has incorrect viscosity for this CPU socket type, reducing thermal conductivity.",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard non-conductive thermal compounds (e.g., silicone "
                    "or ceramic-based) are appropriate for laptop CPUs regardless of socket "
                    "type. Viscosity affects ease of application but not the final "
                    "conductivity once the heatsink is mounted and compound is spread. "
                    "This is not the primary cause of a three-second thermal shutdown."
                ),
            },
        ],
        "explanation": (
            "Laptop thermal shutdown within seconds of power-on, even after fresh thermal "
            "compound application, almost always indicates that the heatsink itself cannot "
            "dissipate heat. Heat pipes move heat from the CPU die to fin arrays; if those "
            "fins are heavily clogged, the heat has nowhere to go. Compressed air through "
            "the exhaust vents while the fan spins (or disassembling to clean the fin array "
            "directly) resolves this. Always inspect the full thermal path — compound, "
            "heat pipe contact, fin array, and fan — not just the CPU-to-heatsink interface."
        ),
    },
    {
        "id": "a1d1v2-002",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile display components",
        "stem": (
            "A technician notices that a laptop's LCD panel develops a dark liquid-like "
            "spreading stain near one corner after a user reports sitting on the lid. "
            "The display still powers on and shows content in the unaffected area. "
            "Which condition most accurately describes what has occurred?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The backlight CCFL tube has cracked and the mercury vapor is condensing on the inside of the panel.",
                "correct": False,
                "rationale": (
                    "Incorrect. Broken CCFL tubes cause the backlight to fail (display goes "
                    "dark), not a spreading liquid stain. Mercury from a cracked CCFL tube "
                    "would not produce a visible dark spreading stain on the display surface."
                ),
            },
            {
                "id": "b",
                "text": "The LCD panel's liquid crystal layer has been physically fractured, causing the liquid crystals to leak between the glass substrates and produce the dark spreading stain.",
                "correct": True,
                "rationale": (
                    "Correct. LCD panels sandwich liquid crystals between two glass substrates. "
                    "Physical pressure (such as sitting on the lid) can crack the inner glass, "
                    "allowing liquid crystals to migrate under capillary action — producing "
                    "a characteristic dark, ink-blot-like stain that can spread over time. "
                    "The panel must be replaced; there is no repair for internal LCD fracture."
                ),
            },
            {
                "id": "c",
                "text": "Moisture has condensed inside the display lid and is pooling behind the LCD panel, creating a dark shadow.",
                "correct": False,
                "rationale": (
                    "Incorrect. Moisture condensation inside a display lid typically produces "
                    "fogging or cloudiness across the panel surface, not a dark spreading "
                    "stain localized to a corner. The scenario describes physical damage from "
                    "sitting on the lid, which points to mechanical fracture, not condensation."
                ),
            },
            {
                "id": "d",
                "text": "The digitizer adhesive has delaminated and the layer is separating, refracting light and creating a dark appearance.",
                "correct": False,
                "rationale": (
                    "Incorrect. Digitizer delamination produces air gap reflections (rainbow "
                    "effect or white haze), not a dark spreading liquid-like stain. The "
                    "liquid-crystal migration symptom is distinctively different from "
                    "delamination artifacts."
                ),
            },
        ],
        "explanation": (
            "When physical pressure cracks the inner glass of an LCD panel, the liquid "
            "crystals between the substrates leak into the fracture zone and spread via "
            "capillary action, creating a characteristic spreading dark stain ('LCD bleed' "
            "or 'pressure damage'). This is irreparable — the entire LCD assembly must be "
            "replaced. The stain can grow over hours or days after the initial impact. "
            "This should not be confused with backlight bleeding (bright patches at panel "
            "edges from backlight leakage into the LCD matrix)."
        ),
    },
    {
        "id": "a1d1v2-003",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile email configuration",
        "stem": (
            "A technician configures a corporate Exchange account on an Android phone "
            "using ActiveSync. The account syncs email but calendar and contacts do "
            "not appear on the device. Email from the past 30 days is present. Which "
            "setting is most likely misconfigured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SMTP authentication credentials are incorrect, preventing calendar and contacts sync.",
                "correct": False,
                "rationale": (
                    "Incorrect. SMTP is the outgoing mail protocol and is not involved in "
                    "calendar or contacts synchronization. Incorrect SMTP credentials would "
                    "affect sending mail, not calendar/contacts sync."
                ),
            },
            {
                "id": "b",
                "text": "The ActiveSync sync options on the device are configured to sync only Mail, with Calendar and Contacts disabled.",
                "correct": True,
                "rationale": (
                    "Correct. Exchange ActiveSync account setup allows granular selection of "
                    "which data types to synchronize — Mail, Calendar, Contacts, and Tasks "
                    "can each be enabled or disabled independently. When calendar and contacts "
                    "do not appear but email syncs successfully, the sync type toggle for "
                    "those data types is the first place to check."
                ),
            },
            {
                "id": "c",
                "text": "The mail sync window is set to 30 days, which filters out calendar events and contacts by date.",
                "correct": False,
                "rationale": (
                    "Incorrect. The mail sync window (e.g., 30 days) controls how far back "
                    "email history is downloaded; it does not filter calendar events or "
                    "contacts. Calendar and contacts sync their full data set independently "
                    "of the mail history window."
                ),
            },
            {
                "id": "d",
                "text": "The Exchange server requires an S/MIME certificate before it will sync calendar and contacts to mobile devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. S/MIME is used for email signing and encryption; it is not "
                    "a prerequisite for calendar or contacts synchronization. An Exchange "
                    "policy requiring S/MIME would block mail sending/receiving, not "
                    "calendar and contacts data."
                ),
            },
        ],
        "explanation": (
            "Exchange ActiveSync (EAS) supports synchronization of Mail, Calendar, Contacts, "
            "and Tasks as separate toggles in the account configuration. When email syncs but "
            "calendar and contacts do not, the most likely cause is that those sync types are "
            "disabled in the account settings on the device. The email sync window (days of "
            "mail to download) is a separate setting that controls mail history depth only. "
            "Always verify all sync type toggles when partial sync issues are reported."
        ),
    },
    {
        "id": "a1d1v2-004",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A user has a USB-C laptop and wants to connect it to an older projector that "
            "has only a VGA (HD-15) input. The user purchases a passive USB-C to VGA cable. "
            "When connected, no image appears on the projector. A USB-C to HDMI adapter "
            "works on the same laptop to another display. Which is the most accurate "
            "explanation for the failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VGA requires a higher voltage than USB-C can supply, so active signal conversion is always required.",
                "correct": False,
                "rationale": (
                    "Incorrect. While some conversion does occur, the issue is not simply "
                    "voltage. VGA is an analog signal; the critical requirement is that the "
                    "USB-C port must support DisplayPort Alt Mode for video output. Not all "
                    "USB-C ports support video output at all, and passive adapters cannot "
                    "convert digital DisplayPort signals to analog VGA without active "
                    "circuitry."
                ),
            },
            {
                "id": "b",
                "text": "A passive USB-C to VGA cable cannot work because VGA is an analog interface and conversion from DisplayPort Alt Mode's digital signal to analog VGA requires an active adapter with a DAC.",
                "correct": True,
                "rationale": (
                    "Correct. USB-C video output uses DisplayPort (or HDMI) Alt Mode, which "
                    "is a digital signal. VGA is an analog interface requiring a Digital-to-"
                    "Analog Converter (DAC). A passive cable has no conversion circuitry; "
                    "it cannot convert digital DP signals to analog VGA. An active USB-C to "
                    "VGA adapter (containing a DAC chip) is required. This is different from "
                    "USB-C to HDMI, which can be passive because both are digital."
                ),
            },
            {
                "id": "c",
                "text": "The projector's VGA input only accepts resolutions up to 1024×768, which the laptop refuses to output.",
                "correct": False,
                "rationale": (
                    "Incorrect. Resolution incompatibility would produce an incorrect or "
                    "out-of-range image, not a complete lack of signal. The fundamental "
                    "problem is the analog vs. digital signal conversion requirement, not "
                    "resolution mismatch."
                ),
            },
            {
                "id": "d",
                "text": "USB-C ports that support HDMI Alt Mode do not support DisplayPort Alt Mode, so a VGA adapter using DisplayPort Alt Mode will never work on this laptop.",
                "correct": False,
                "rationale": (
                    "Incorrect. USB-C video output uses DisplayPort Alt Mode regardless of "
                    "whether the adapter end is HDMI or VGA — both adapter types rely on "
                    "DisplayPort Alt Mode from the USB-C port. A port that supports USB-C "
                    "to HDMI video output also supports DisplayPort Alt Mode. The issue is "
                    "the passive vs. active nature of the adapter, not Alt Mode compatibility."
                ),
            },
        ],
        "explanation": (
            "USB-C video output relies on DisplayPort Alt Mode (digital signal). HDMI is also "
            "digital, so a passive USB-C to HDMI adapter works by re-encoding the DP signal "
            "or using a direct electrical mapping. VGA, however, is purely analog (R/G/B "
            "voltage levels, H-sync/V-sync TTL). Converting digital DisplayPort to analog VGA "
            "requires an active DAC chip inside the adapter. Passive USB-C to VGA cables "
            "exist on the market but do not function for digital-to-analog conversion — they "
            "only work on USB-C ports that natively output a VGA analog signal, which is "
            "extremely rare. Always purchase an active USB-C to VGA adapter."
        ),
    },
    {
        "id": "a1d1v2-005",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "MDM/MAM",
        "stem": (
            "An organization deploys Android smartphones using Android Enterprise Work "
            "Profile. Employees use the same physical device for personal and work use. "
            "The IT department wants to ensure that corporate app data cannot be copied "
            "and pasted into personal apps. Which MDM control achieves this WITHOUT "
            "restricting personal app usage on the device?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enforce full-device encryption and require a PIN to unlock the screen.",
                "correct": False,
                "rationale": (
                    "Incorrect. Full-device encryption and PIN enforcement protect the device "
                    "from unauthorized access but do not prevent a logged-in user from copying "
                    "data between the work profile and personal profile while the device is "
                    "unlocked."
                ),
            },
            {
                "id": "b",
                "text": "Enable a cross-profile data sharing restriction policy that blocks clipboard and data transfer between the work profile and personal profile.",
                "correct": True,
                "rationale": (
                    "Correct. Android Enterprise Work Profile creates an isolated container "
                    "for work apps and data. An MDM cross-profile data restriction policy "
                    "prevents clipboard sharing, file sharing, and app interactions between "
                    "the work profile and the personal profile. This isolates corporate data "
                    "without touching or restricting the personal side of the device."
                ),
            },
            {
                "id": "c",
                "text": "Apply a containerization policy that disables all personal apps on the device.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling personal apps defeats the purpose of Work Profile, "
                    "which is to allow personal and work use on the same device. The question "
                    "explicitly requires that personal app usage is not restricted."
                ),
            },
            {
                "id": "d",
                "text": "Configure the MDM to perform a full device wipe if any clipboard data is detected leaving a managed app.",
                "correct": False,
                "rationale": (
                    "Incorrect. No MDM platform performs real-time clipboard content inspection "
                    "triggering a remote wipe — this is not a real capability. Even if it were, "
                    "wiping the device for a clipboard action would be disproportionate and would "
                    "destroy personal data, violating the BYOD requirement."
                ),
            },
        ],
        "explanation": (
            "Android Enterprise Work Profile (formerly Android for Work) separates the device "
            "into two isolated profiles: work and personal. Corporate MDM manages the work "
            "profile but has no visibility or control over the personal profile. Cross-profile "
            "data sharing policies (configured via the MDM) block clipboard, file, and intent "
            "sharing between work apps and personal apps — preventing exfiltration of corporate "
            "data into personal apps while leaving the personal side completely unrestricted. "
            "This is the designed BYOD architecture for Android Enterprise."
        ),
    },
    {
        "id": "a1d1v2-006",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile network connectivity",
        "stem": (
            "A corporate smartphone configured with a Wi-Fi profile via MDM connects "
            "successfully to the corporate SSID but cannot reach internal intranet "
            "sites or corporate file servers, even though internet access works. Other "
            "corporate devices on the same SSID have no such issue. Which is the most "
            "likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The MDM-pushed Wi-Fi profile assigned a static IP address that conflicts with the corporate DHCP scope, placing the device on the wrong subnet.",
                "correct": True,
                "rationale": (
                    "Correct. If the MDM profile assigned a static IP in an incorrect or "
                    "conflicting subnet, the device would associate with the AP (so Wi-Fi "
                    "shows connected) and can route to the internet via the default gateway, "
                    "but cannot reach internal hosts on other corporate subnets because the "
                    "device's IP is not in the correct VLAN/subnet. Internet access works "
                    "because the default gateway is reachable; internal routing fails. An "
                    "IP conflict can also cause erratic connectivity."
                ),
            },
            {
                "id": "b",
                "text": "The wireless AP does not support the frequency band the device is using, so internal traffic is dropped.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the AP did not support the device's frequency band, the "
                    "device would fail to associate entirely — Wi-Fi would not show as "
                    "connected. The scenario states Wi-Fi is connected and internet works, "
                    "ruling out a band incompatibility at the AP."
                ),
            },
            {
                "id": "c",
                "text": "The corporate firewall is blocking all outbound traffic from this device's MAC address.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the firewall blocked all traffic from the device's MAC, "
                    "internet access would also fail. The scenario specifies that internet "
                    "access works, so the firewall is not blocking all traffic from this device."
                ),
            },
            {
                "id": "d",
                "text": "The device's DNS suffix search list is empty, so short hostnames for intranet sites cannot be resolved.",
                "correct": False,
                "rationale": (
                    "Incorrect. A missing DNS search suffix would prevent resolution of "
                    "short hostnames (e.g., 'intranet' instead of 'intranet.corp.com') but "
                    "would not prevent access to file servers by IP address or FQDN. More "
                    "importantly, it would not prevent connectivity to other subnets. A "
                    "misconfigured IP address is a more complete explanation for the "
                    "described symptoms."
                ),
            },
        ],
        "explanation": (
            "When a device connects to Wi-Fi and can reach the internet but cannot reach "
            "internal resources, while other devices on the same SSID work fine, the most "
            "likely culprit is a network configuration error specific to that device — most "
            "commonly a static IP address in the wrong subnet or an IP conflict. The MDM "
            "Wi-Fi profile is the likely source since it is device-specific configuration. "
            "Verify the device's IP address, subnet mask, and default gateway match the "
            "expected DHCP assignment for the VLAN. Correcting the profile to use DHCP "
            "(or the correct static assignment) should resolve the issue."
        ),
    },
    {
        "id": "a1d1v2-007",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Bluetooth pairing",
        "stem": (
            "A user pairs their laptop with a Bluetooth speaker. Audio plays correctly "
            "for 20 minutes, then stutters and drops out whenever the user opens a web "
            "browser on the laptop. Closing the browser immediately restores audio "
            "quality. No other Bluetooth devices are paired. Which is the most likely "
            "cause of the audio dropout?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The Bluetooth speaker's battery is depleted, and the browser's notification sounds cause it to power off.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the battery were depleted, audio would drop regardless "
                    "of browser usage. The correlation between browser activity and audio "
                    "dropout points to an interference or resource contention issue on the "
                    "laptop, not the speaker's battery state."
                ),
            },
            {
                "id": "b",
                "text": "The laptop's Wi-Fi radio and Bluetooth radio share the 2.4 GHz band; the browser's network activity on Wi-Fi causes co-channel interference with the Bluetooth connection.",
                "correct": True,
                "rationale": (
                    "Correct. Bluetooth and Wi-Fi both operate in the 2.4 GHz ISM band. "
                    "Many laptop combo chips use coexistence firmware to avoid simultaneous "
                    "transmission, but heavy Wi-Fi activity (such as streaming or loading "
                    "web pages) can still cause Bluetooth audio dropout due to shared antenna "
                    "resource contention or co-channel interference. Closing the browser "
                    "reduces Wi-Fi traffic and restores Bluetooth audio. Moving Wi-Fi to 5 GHz "
                    "or using a 5 GHz band AP eliminates this coexistence issue."
                ),
            },
            {
                "id": "c",
                "text": "The browser's GPU acceleration uses the same processing resources as the Bluetooth audio stack, causing CPU starvation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth audio processing requires minimal CPU resources. "
                    "While browser GPU acceleration is CPU/GPU intensive, it does not cause "
                    "Bluetooth audio stutter through CPU starvation on any modern processor. "
                    "The 2.4 GHz co-channel interference explanation is far more consistent "
                    "with the described symptoms."
                ),
            },
            {
                "id": "d",
                "text": "The Bluetooth profile being used (A2DP) is incompatible with simultaneous internet use and must be switched to HSP.",
                "correct": False,
                "rationale": (
                    "Incorrect. A2DP (Advanced Audio Distribution Profile) is the correct "
                    "profile for high-quality stereo audio streaming and has no compatibility "
                    "restriction with simultaneous internet use. HSP (Headset Profile) is a "
                    "lower-quality mono profile for phone calls. The issue is radio "
                    "interference, not profile incompatibility."
                ),
            },
        ],
        "explanation": (
            "Bluetooth 2.4 GHz and Wi-Fi 2.4 GHz coexistence interference is a well-known "
            "source of Bluetooth audio dropout. Modern combo chips use mechanisms like "
            "Adaptive Frequency Hopping (AFH) and coexistence signaling, but heavy Wi-Fi "
            "activity can still degrade Bluetooth performance. Solutions: (1) Switch Wi-Fi "
            "to the 5 GHz band (eliminating the overlap entirely); (2) reduce Wi-Fi channel "
            "width; (3) update combo Wi-Fi/Bluetooth driver firmware. The symptom is "
            "distinctively reproducible by browser network activity and immediately reversible "
            "upon stopping it."
        ),
    },
    {
        "id": "a1d1v2-008",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician replaces a laptop's DC jack. After reassembly, the laptop "
            "charges correctly on AC power, but the battery icon in the OS shows "
            "'Plugged in, not charging' even though the battery level is at 43%. "
            "The battery charges normally to 100% when the laptop is powered off. "
            "Which explanation is most accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The DC jack replacement introduced a solder bridge that is causing the battery to report incorrect status to the OS.",
                "correct": False,
                "rationale": (
                    "Incorrect. A solder bridge at the DC jack would more likely cause a short "
                    "circuit or prevent charging entirely. It would not selectively stop charging "
                    "at 43% while the OS is running but allow charging when powered off."
                ),
            },
            {
                "id": "b",
                "text": "The battery has an OEM-enforced conservation mode (battery health limiting) active, which caps charging to a set percentage to prolong battery longevity when plugged in.",
                "correct": True,
                "rationale": (
                    "Correct. Many OEM laptop firmware and utilities implement 'battery "
                    "conservation mode' or 'battery health mode' that stops charging at a "
                    "set threshold (commonly 60–80%) when the AC adapter is plugged in for "
                    "extended periods. The battery still charges to 100% when the laptop is "
                    "powered off (or when conservation mode is disabled). This feature is "
                    "enabled via OEM software or BIOS and is unrelated to the DC jack repair. "
                    "The technician should check OEM battery management software or BIOS "
                    "settings before assuming a hardware fault."
                ),
            },
            {
                "id": "c",
                "text": "The battery EEPROM was reset during the DC jack replacement, locking the battery to read-only status.",
                "correct": False,
                "rationale": (
                    "Incorrect. Laptop battery EEPROMs store charge cycle counts and "
                    "calibration data, but replacing the DC jack does not reset or interact "
                    "with the battery EEPROM. There is no 'read-only status' in battery "
                    "firmware triggered by DC jack replacement."
                ),
            },
            {
                "id": "d",
                "text": "The AC adapter wattage is insufficient to simultaneously power the laptop and charge the battery above 43% under load.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the adapter wattage were insufficient to charge under "
                    "load, the battery percentage would decrease (not hold steady) while "
                    "the laptop runs under load, and it would charge past 43% under light "
                    "load. The scenario states the battery charges to 100% when powered "
                    "off, which contradicts an adapter wattage limitation."
                ),
            },
        ],
        "explanation": (
            "OEM battery conservation/health mode is a firmware feature found on most modern "
            "laptops (Lenovo Conservation Mode, Dell Battery Extender, HP Battery Care, ASUS "
            "Battery Health Charging, etc.). When enabled, it prevents charging above a set "
            "threshold (often 60–80%) to reduce battery degradation from keeping it at high "
            "charge while constantly plugged in. It appears in the OS as 'Plugged in, not "
            "charging'. Charging to 100% with the system off works because either the BIOS "
            "charges to full when shutdown, or the mode is temporarily overridden. Check OEM "
            "battery management tools or BIOS before diagnosing a hardware fault."
        ),
    },
    {
        "id": "a1d1v2-009",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Location services",
        "stem": (
            "A user reports that a navigation app on their phone constantly shows their "
            "location drifting by 50–200 meters even while standing still outdoors with "
            "a clear sky view. Other GPS-dependent apps also show the same drift. The "
            "phone has not been near strong RF interference. Which setting or hardware "
            "condition is the most likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The phone's Wi-Fi is turned off, so it cannot use Wi-Fi positioning to supplement GPS accuracy.",
                "correct": False,
                "rationale": (
                    "Incorrect. With a clear sky view outdoors, GPS satellites alone should "
                    "provide 3–5 meter accuracy. Wi-Fi positioning supplements GPS indoors "
                    "or under poor satellite conditions; it should not be necessary for "
                    "accurate positioning outdoors. Disabling Wi-Fi is not a reason for "
                    "50–200 meter drift under clear sky."
                ),
            },
            {
                "id": "b",
                "text": "The A-GPS assistance data (ephemeris) is stale or corrupted, causing the GPS chipset to compute inaccurate satellite pseudoranges.",
                "correct": True,
                "rationale": (
                    "Correct. Assisted GPS (A-GPS) downloads satellite ephemeris data (orbital "
                    "parameters) from a network server to speed up initial fix acquisition and "
                    "improve accuracy. If the AGPS data is stale (weeks old) or corrupted, the "
                    "chipset uses incorrect predicted satellite positions, producing a consistent "
                    "positional error and apparent drift. Forcing a GPS reset (clearing AGPS "
                    "cache via developer settings or the app) and downloading fresh ephemeris "
                    "data resolves this. All GPS-dependent apps share the same hardware, "
                    "explaining why multiple apps show the same drift."
                ),
            },
            {
                "id": "c",
                "text": "The phone's location permission is set to 'Approximate' rather than 'Precise', which limits accuracy to 50–200 meters by design.",
                "correct": False,
                "rationale": (
                    "Incorrect. Android 12+ introduced 'Approximate' location permission, "
                    "which limits app location accuracy to ~1 km (not 50–200 m). However, "
                    "if this were the cause, the system location indicator would still show "
                    "precise location — only app-reported location would be coarsened. The "
                    "scenario describes drift affecting all GPS-dependent apps including "
                    "navigation, suggesting a hardware/data issue, not a permission setting "
                    "that coarsens location to apps."
                ),
            },
            {
                "id": "d",
                "text": "The phone has reached its daily GPS fix quota enforced by the carrier, causing the chipset to revert to cell tower triangulation.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no carrier-enforced 'GPS fix quota'. GPS chipsets "
                    "operate independently of carrier data quotas. Cell tower triangulation "
                    "would produce accuracy of 100–1,000 meters, not 50–200 meter drift. "
                    "This concept does not exist in cellular or GPS technology."
                ),
            },
        ],
        "explanation": (
            "A-GPS uses network-downloaded ephemeris data to provide a fast first fix and "
            "improved accuracy. Stale or corrupted ephemeris data causes the GPS chipset to "
            "calculate satellite positions incorrectly, producing positional errors that appear "
            "as drift even when stationary. The fix is to clear the AGPS cache (Settings > "
            "Location > GPS Test app, or via Developer Options on Android) and allow fresh "
            "data to download on a cellular or Wi-Fi connection. Since all apps share the "
            "hardware GPS chipset, all GPS apps are equally affected."
        ),
    },
    {
        "id": "a1d1v2-010",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile synchronization",
        "stem": (
            "A user's Android phone is configured to back up app data, contacts, and "
            "photos to Google One. After a factory reset and sign-in with the same "
            "Google account, the user's contacts and app data restore correctly, but "
            "photos taken after the last Wi-Fi backup do not appear. The user always "
            "had Wi-Fi off while taking recent photos. Which setting explains the "
            "missing photos?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Google Photos backup requires a Google One paid subscription; the free 15 GB tier was exceeded, so recent photos were not uploaded.",
                "correct": False,
                "rationale": (
                    "Incorrect. While storage quota is a real issue, the scenario does not "
                    "indicate a quota-exceeded warning. More importantly, the scenario "
                    "explicitly states that Wi-Fi was always off when taking the recent "
                    "photos, which is a more direct and sufficient explanation."
                ),
            },
            {
                "id": "b",
                "text": "Google Photos backup was set to 'Upload over Wi-Fi only', and since Wi-Fi was off when photos were taken, they were never uploaded before the factory reset.",
                "correct": True,
                "rationale": (
                    "Correct. Google Photos (and most cloud backup apps) default to uploading "
                    "over Wi-Fi only to avoid mobile data charges. If the user always had Wi-Fi "
                    "off while using the camera, photos accumulated locally but were never "
                    "synced to the cloud. A factory reset erased those unsynced photos "
                    "permanently. The correct resolution is to enable cellular backup or "
                    "ensure Wi-Fi is on before performing a factory reset."
                ),
            },
            {
                "id": "c",
                "text": "Google Photos only backs up photos taken in the default camera app; photos from third-party camera apps are excluded.",
                "correct": False,
                "rationale": (
                    "Incorrect. Google Photos backs up all photos and videos from the device's "
                    "camera roll (DCIM folder) regardless of which camera app was used. It is "
                    "not restricted to photos taken with the stock camera app."
                ),
            },
            {
                "id": "d",
                "text": "The factory reset deleted the Google account authentication token, causing Google Photos to skip restoring photos from the cloud.",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-signing into the Google account after a factory reset "
                    "re-establishes authentication. The scenario states contacts and app data "
                    "restored correctly from the same account, proving authentication is "
                    "working. The photos were simply never uploaded to the cloud."
                ),
            },
        ],
        "explanation": (
            "Cloud backup apps typically offer a 'Wi-Fi only' backup option (often the default) "
            "to prevent unexpected mobile data consumption. Photos taken while offline or with "
            "Wi-Fi disabled accumulate in a pending upload queue. If the device is factory reset "
            "before Wi-Fi backup can occur, those photos are lost because they exist only locally. "
            "Best practice before any factory reset: connect to Wi-Fi, force a manual backup sync, "
            "and verify upload completion. For critical data, also use USB transfer as a secondary "
            "backup."
        ),
    },
    {
        "id": "a1d1v2-011",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is troubleshooting a laptop that randomly freezes and then "
            "recovers without a BSOD. The event log shows memory management warnings. "
            "Running Windows Memory Diagnostic shows no errors. Which follow-up test "
            "is most appropriate to further investigate the RAM?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run chkdsk /r on all drives to rule out filesystem corruption causing the memory management warnings.",
                "correct": False,
                "rationale": (
                    "Incorrect. While chkdsk can find storage errors, memory management "
                    "event log warnings paired with random freezes point to RAM or the "
                    "memory subsystem, not filesystem corruption. chkdsk would not test "
                    "RAM integrity."
                ),
            },
            {
                "id": "b",
                "text": "Run MemTest86 (or MemTest86+) from bootable USB for multiple full passes outside the OS environment.",
                "correct": True,
                "rationale": (
                    "Correct. Windows Memory Diagnostic runs a limited test within the "
                    "Windows bootloader environment and can miss intermittent or pattern-"
                    "sensitive errors. MemTest86 runs at bare-metal level, tests the entire "
                    "RAM address space using multiple test algorithms (including XOR patterns, "
                    "moving inversions, and address tests), and can run for many hours to "
                    "detect subtle errors that Windows Memory Diagnostic misses. Multiple "
                    "full passes (a minimum of two, ideally more) are needed for intermittent "
                    "faults."
                ),
            },
            {
                "id": "c",
                "text": "Use CPU-Z to check the RAM's SPD data and confirm the modules match the system's rated DDR speed.",
                "correct": False,
                "rationale": (
                    "Incorrect. CPU-Z reads SPD EEPROM data to display rated specifications "
                    "but does not test RAM data integrity. Mismatched speeds would typically "
                    "cause immediate boot failure or be auto-corrected by the BIOS, not "
                    "intermittent freezes."
                ),
            },
            {
                "id": "d",
                "text": "Update the laptop's BIOS to the latest version, as BIOS updates often include RAM compatibility fixes that will resolve the freezes.",
                "correct": False,
                "rationale": (
                    "Incorrect. A BIOS update is a reasonable general maintenance step but "
                    "is not a diagnostic test for RAM. Updating the BIOS before completing "
                    "the RAM diagnosis could mask the issue and risks a failed flash if the "
                    "RAM is unstable. Diagnosis should precede corrective actions."
                ),
            },
        ],
        "explanation": (
            "Windows Memory Diagnostic is a quick, built-in test but runs within the WinRE "
            "environment using limited test patterns. It is known to miss intermittent, "
            "pattern-specific, or thermally sensitive RAM errors. MemTest86 is a full-featured, "
            "OS-independent RAM testing tool that uses highly thorough test algorithms and "
            "runs at bare metal, maximizing test coverage. For suspected RAM issues where "
            "Windows Memory Diagnostic shows clean results, MemTest86 with multiple passes "
            "(including extended stress tests) is the definitive next step before replacing "
            "hardware."
        ),
    },
    {
        "id": "a1d1v2-012",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A user wants to connect a USB-C external SSD to their iPad Pro (USB-C). "
            "The drive is formatted as exFAT. The drive's status light illuminates but "
            "the iPad does not display the drive in the Files app. The same drive works "
            "on a Windows laptop. Which is the most likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "iPadOS does not support USB-C storage devices; only Lightning accessories can access external storage on Apple tablets.",
                "correct": False,
                "rationale": (
                    "Incorrect. iPadOS 13 and later supports USB-C external storage on iPad "
                    "Pro and Air models. Files from external drives appear in the Files app "
                    "under 'External'. USB-C storage access is a supported feature on "
                    "current iPad Pro hardware."
                ),
            },
            {
                "id": "b",
                "text": "The external SSD requires more bus power than the iPad's USB-C port can supply without a powered hub, causing the drive to fail to mount despite the status light.",
                "correct": True,
                "rationale": (
                    "Correct. USB-C bus-powered SSDs — especially high-speed NVMe enclosures "
                    "— can draw up to 900 mA or more during spin-up or peak access. iPad "
                    "Pro USB-C ports supply power but may not provide sufficient current for "
                    "all bus-powered drives. The status LED may illuminate on minimal current "
                    "while the drive fails to fully initialize. Using a USB-C hub with an "
                    "external power supply (powered hub) or a drive with lower power "
                    "requirements resolves this."
                ),
            },
            {
                "id": "c",
                "text": "exFAT is not supported by iPadOS; the drive must be reformatted to FAT32.",
                "correct": False,
                "rationale": (
                    "Incorrect. iPadOS supports exFAT, FAT32, APFS, and HFS+ formatted "
                    "external drives. exFAT is specifically recommended for cross-platform "
                    "drives because it removes FAT32's 4 GB file size limit. Reformatting "
                    "to FAT32 is unnecessary and would be a step backward."
                ),
            },
            {
                "id": "d",
                "text": "The Files app requires the iCloud Drive option to be enabled before it can display external storage devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. iCloud Drive is a cloud storage service within the Files app. "
                    "External storage appears under a separate 'External' section in the Files "
                    "app sidebar and does not require iCloud Drive to be enabled. These are "
                    "independent storage locations."
                ),
            },
        ],
        "explanation": (
            "iPad Pro USB-C ports deliver limited bus power. Many high-performance external "
            "SSDs (especially NVMe enclosures) require more current than a tablet USB-C port "
            "can supply. The drive LED may illuminate at minimum current levels while the "
            "controller fails to complete initialization. Solutions: (1) Use a USB-C hub with "
            "its own power supply; (2) use a drive with lower power requirements; (3) use a "
            "USB-C to USB-C cable that supports higher current ratings. iPadOS supports exFAT, "
            "FAT32, APFS, and HFS+ external drives natively since iPadOS 13."
        ),
    },
    {
        "id": "a1d1v2-013",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile email configuration",
        "stem": (
            "A newly hired employee cannot send email from their smartphone using the "
            "corporate SMTP server on port 25. Other employees using the same mail "
            "client settings on their smartphones send mail successfully. The new "
            "employee's phone is on the carrier's LTE network, not corporate Wi-Fi. "
            "Which is the most likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The employee's Active Directory account is locked out, preventing SMTP authentication.",
                "correct": False,
                "rationale": (
                    "Incorrect. An AD account lockout would prevent SMTP AUTH login and "
                    "would return an authentication failure error. However, other employees "
                    "are using the same settings successfully, and an AD lockout would not "
                    "be specific to which network the user is on (LTE vs. Wi-Fi)."
                ),
            },
            {
                "id": "b",
                "text": "The carrier's LTE network blocks outbound TCP port 25 to prevent spam from mobile devices, requiring the use of the SMTP submission port (587) instead.",
                "correct": True,
                "rationale": (
                    "Correct. Major ISPs and mobile carriers routinely block outbound TCP "
                    "port 25 (standard SMTP relay) from consumer and mobile networks to "
                    "prevent spam sent from compromised devices. The correct port for "
                    "authenticated client mail submission is TCP 587 (SMTP STARTTLS) or "
                    "465 (implicit TLS). Other employees on corporate Wi-Fi or different "
                    "ISPs may not have this block. The technician should update the SMTP "
                    "port to 587 in the mail client configuration."
                ),
            },
            {
                "id": "c",
                "text": "Port 25 requires a static public IP address; mobile LTE devices use NAT with dynamic IPs, which SMTP servers reject.",
                "correct": False,
                "rationale": (
                    "Incorrect. SMTP servers do not require clients to have static IP "
                    "addresses. Authenticated SMTP submission from mobile clients uses "
                    "username/password or certificate credentials, not static IPs. Dynamic "
                    "NAT addressing from LTE does not inherently block SMTP client "
                    "submissions."
                ),
            },
            {
                "id": "d",
                "text": "The corporate mail server has geofenced SMTP access to the office building's IP range, blocking connections from mobile data networks.",
                "correct": False,
                "rationale": (
                    "Incorrect. While geofencing SMTP access is technically possible, it "
                    "would not be the default configuration, would affect all employees on "
                    "cellular networks (not just this one), and would typically produce a "
                    "specific rejection message. The carrier port-25 block is a far more "
                    "common and universal explanation."
                ),
            },
        ],
        "explanation": (
            "Port 25 is the traditional SMTP relay port used between mail servers (MTA-to-MTA). "
            "It is blocked by most ISPs and all major mobile carriers on outbound connections "
            "from end-user devices and networks to prevent spam. Mobile mail clients must use "
            "TCP 587 (SMTP submission with STARTTLS) or TCP 465 (SMTP over implicit TLS) for "
            "authenticated outbound mail. Port 587 is the IANA-designated mail submission port "
            "for end clients. Always configure mobile mail clients with port 587 or 465 rather "
            "than port 25 for outgoing mail."
        ),
    },
    {
        "id": "a1d1v2-014",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician is asked to install an Intel Wi-Fi 6E M.2 card in a laptop "
            "that previously had a Wi-Fi 5 card. The M.2 slot is an E-key 2230 slot. "
            "After installation the card is detected and connects normally on 2.4 GHz "
            "and 5 GHz, but 6 GHz band access points never appear in the scan list. "
            "Other Wi-Fi 6E devices see the same 6 GHz AP. Which is the most likely "
            "cause of the missing 6 GHz band?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The E-key M.2 slot only supports PCIe x1, which lacks the bandwidth to carry 6 GHz Wi-Fi 6E traffic.",
                "correct": False,
                "rationale": (
                    "Incorrect. The E-key M.2 slot interface (PCIe x1 or USB 2.0) provides "
                    "more than adequate bandwidth for Wi-Fi 6E, which has a maximum PHY rate "
                    "around 9.6 Gbps but real-world throughput of under 2 Gbps — well within "
                    "PCIe x1 Gen 3's ~1 GB/s capacity. The slot interface is not the "
                    "limiting factor."
                ),
            },
            {
                "id": "b",
                "text": "The laptop's antenna cables (typically two: main and aux) are designed for 2.4/5 GHz bands and are not optimized or tuned for 6 GHz, causing insufficient 6 GHz signal reception.",
                "correct": True,
                "rationale": (
                    "Correct. Wi-Fi 6E adds the 6 GHz band (5.925–7.125 GHz). Laptop antenna "
                    "cables and antenna elements are tuned to specific frequency ranges. Antennas "
                    "designed for 2.4/5 GHz have significant attenuation at 6 GHz and may not "
                    "meet the sensitivity threshold needed to detect 6 GHz access points. "
                    "Upgrading to a Wi-Fi 6E card without replacing the antenna cables with "
                    "6 GHz-capable antennas results in poor or absent 6 GHz performance while "
                    "2.4/5 GHz continues to work normally."
                ),
            },
            {
                "id": "c",
                "text": "6 GHz Wi-Fi requires WPA3 security, and the laptop's driver has not been updated to support WPA3, so 6 GHz APs are filtered from scan results.",
                "correct": False,
                "rationale": (
                    "Incorrect. While Wi-Fi 6E requires WPA3 for 6 GHz band operation (per "
                    "the Wi-Fi Alliance specification), an outdated driver would typically show "
                    "the AP but fail to associate, not hide it from scan results entirely. "
                    "More importantly, the antenna incompatibility is the primary hardware "
                    "cause in a laptop upgrade scenario."
                ),
            },
            {
                "id": "d",
                "text": "6 GHz Wi-Fi is a licensed spectrum in most countries and requires carrier approval that must be provisioned via MDM before the card can use it.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 6 GHz band for Wi-Fi (used by Wi-Fi 6E and Wi-Fi 7) is "
                    "unlicensed spectrum in countries that have opened it (United States, "
                    "European Union, and others). No carrier approval or MDM provisioning "
                    "is required for standard Wi-Fi 6E operation."
                ),
            },
        ],
        "explanation": (
            "Wi-Fi 6E adds the 6 GHz band (5.925–7.125 GHz), which is substantially higher "
            "frequency than the 2.4 GHz and 5 GHz bands. Laptop antenna cables are designed "
            "with specific frequency response characteristics; older antennas tuned for 2.4/5 GHz "
            "exhibit high return loss at 6 GHz. Upgrading only the M.2 Wi-Fi card without "
            "replacing the antenna cables with tri-band (2.4/5/6 GHz) capable antennas results "
            "in no usable 6 GHz signal. Some OEMs provide Wi-Fi 6E-capable antennas as upgrade "
            "kits; otherwise the card will only use 2.4/5 GHz despite supporting 6 GHz in "
            "hardware."
        ),
    },
    {
        "id": "a1d1v2-015",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "MDM/MAM",
        "stem": (
            "An organization uses MDM to enforce certificate-based Wi-Fi authentication "
            "(802.1X/EAP-TLS) on corporate mobile devices. A new employee's phone cannot "
            "connect to the corporate SSID and reports 'Authentication failed'. Their "
            "phone is enrolled in MDM and has a valid MDM enrollment certificate. Other "
            "enrolled devices connect without issue. Which is the most likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The MDM Wi-Fi profile has not been pushed to this specific device, so it is attempting to connect without the required EAP-TLS certificate.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the Wi-Fi profile had not been pushed, the SSID might not "
                    "even appear in the configured networks, or the device would fail to send "
                    "any certificate at all. The 'Authentication failed' message implies a "
                    "certificate exchange occurred but failed validation — suggesting a profile "
                    "was applied but with an issue."
                ),
            },
            {
                "id": "b",
                "text": "The device's user-specific Wi-Fi authentication certificate has not been issued or was not included in the MDM profile push, so the RADIUS server rejects the device because it presents no valid user certificate.",
                "correct": True,
                "rationale": (
                    "Correct. EAP-TLS requires a client certificate trusted by the RADIUS "
                    "server. MDM can push a device certificate (for device authentication) "
                    "or must trigger a SCEP/NDES certificate enrollment for a user-specific "
                    "certificate. If the user-specific Wi-Fi certificate was not issued (e.g., "
                    "the SCEP enrollment did not complete, or the certificate template was not "
                    "applied to this user), the RADIUS server will reject the authentication. "
                    "The MDM enrollment certificate is a separate certificate used for device "
                    "management, not Wi-Fi authentication."
                ),
            },
            {
                "id": "c",
                "text": "The corporate SSID uses WPA2-Enterprise but the device only supports WPA3, causing a security downgrade rejection.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3-Enterprise is backward compatible with WPA2-Enterprise "
                    "on the same AP (when the AP supports both). A device that supports WPA3 "
                    "can still connect to a WPA2-Enterprise SSID. This would not cause an "
                    "EAP-TLS authentication failure."
                ),
            },
            {
                "id": "d",
                "text": "802.1X EAP-TLS requires the device to be physically located within the building; remote enrollment causes certificate validation to fail.",
                "correct": False,
                "rationale": (
                    "Incorrect. EAP-TLS certificate validation is based on cryptographic "
                    "trust chains, not physical device location. There is no location "
                    "restriction built into 802.1X EAP-TLS certificate-based authentication."
                ),
            },
        ],
        "explanation": (
            "In 802.1X EAP-TLS, the RADIUS server validates the client's certificate against "
            "a trusted CA. There are two distinct certificates involved in MDM/802.1X deployments: "
            "(1) the MDM enrollment certificate — used to establish trust between the device and "
            "the MDM server; and (2) the Wi-Fi authentication certificate — issued via SCEP/NDES "
            "or a certificate authority and pushed via the MDM Wi-Fi payload. These are different "
            "certificates. If the Wi-Fi authentication certificate was not properly issued and "
            "pushed, the RADIUS server will see no valid client certificate and reject the "
            "authentication. Check the MDM console for SCEP enrollment status for the device."
        ),
    },
    {
        "id": "a1d1v2-016",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile display components",
        "stem": (
            "A convertible 2-in-1 laptop is used in tablet mode. The user reports that "
            "the display is crisp when the device is in laptop mode (clamshell), but "
            "when rotated to tablet mode, the image is upside-down and touch targets "
            "are misaligned with visual content. The auto-rotate feature is enabled. "
            "Which component or setting is most likely at fault?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The accelerometer or gyroscope sensor used for screen rotation detection has failed or is not calibrated, causing the OS to rotate incorrectly.",
                "correct": True,
                "rationale": (
                    "Correct. Automatic screen rotation in convertible devices is controlled "
                    "by the accelerometer (and often gyroscope) sensor. If the sensor is "
                    "defective, miscalibrated, or returning incorrect orientation data, the "
                    "OS will rotate the display to the wrong orientation. When the display "
                    "rotates incorrectly, the touch digitizer's coordinate mapping remains "
                    "anchored to the physical display orientation, creating the misaligned "
                    "touch targets described. Sensor recalibration or replacement resolves "
                    "this."
                ),
            },
            {
                "id": "b",
                "text": "The display's refresh rate drops below the minimum threshold in tablet mode, causing the image to appear rotated.",
                "correct": False,
                "rationale": (
                    "Incorrect. Display refresh rate has no effect on screen orientation. "
                    "A low refresh rate causes flickering or motion artifacts, not an "
                    "upside-down image. Screen rotation is handled by the display driver "
                    "based on sensor data, not by the refresh rate."
                ),
            },
            {
                "id": "c",
                "text": "The convertible hinge sensor (Hall effect sensor) that triggers tablet mode is stuck in the clamshell state, preventing the OS from reconfiguring the display.",
                "correct": False,
                "rationale": (
                    "Incorrect. The Hall effect hinge sensor typically detects when the device "
                    "is fully rotated (360°) to trigger tablet mode UI changes (e.g., hiding "
                    "the taskbar). The image rotation itself is controlled by the "
                    "accelerometer. A stuck Hall sensor might prevent tablet mode UI features "
                    "but would not explain an upside-down display with misaligned touch inputs."
                ),
            },
            {
                "id": "d",
                "text": "The screen orientation lock was activated by the user and is set to an inverted portrait mode.",
                "correct": False,
                "rationale": (
                    "Incorrect. While manually setting an incorrect screen orientation would "
                    "produce an upside-down image, the scenario states auto-rotate is enabled "
                    "and the problem only occurs in tablet mode (not laptop mode). A manually "
                    "locked orientation would persist in both modes. The sensor failure "
                    "explanation is more consistent with the conditional nature of the problem."
                ),
            },
        ],
        "explanation": (
            "Convertible device screen auto-rotation relies on an accelerometer (measures "
            "gravitational force along X/Y/Z axes) and sometimes a gyroscope (measures "
            "angular velocity). The OS reads sensor data to determine device orientation "
            "and rotates the display accordingly. The touch digitizer's coordinate system "
            "is also adjusted with the rotation. A failed or miscalibrated accelerometer "
            "provides incorrect orientation data, causing wrong rotations. The fix may "
            "involve driver reinstallation, sensor recalibration (via OEM utility or "
            "Settings > Sensors), or hardware replacement if the sensor chip has failed."
        ),
    },
    {
        "id": "a1d1v2-017",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile network connectivity",
        "stem": (
            "A user's iPhone can browse websites and use apps over Wi-Fi, but iMessage "
            "and FaceTime do not activate on the new device. The phone has a valid SIM "
            "and can make standard voice calls. Apple ID sign-in is successful. Which "
            "is the most likely cause of iMessage and FaceTime activation failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "iMessage and FaceTime require a Wi-Fi 6 connection and the user's router only supports Wi-Fi 5.",
                "correct": False,
                "rationale": (
                    "Incorrect. iMessage and FaceTime have no Wi-Fi generation requirement. "
                    "They function on any Wi-Fi standard, 3G cellular, 4G LTE, or 5G. "
                    "Wi-Fi generation does not affect Apple service activation."
                ),
            },
            {
                "id": "b",
                "text": "iMessage and FaceTime activation requires outbound connections to Apple's activation servers over cellular data; the carrier's APN settings or data plan may be blocking SMS-based or data-based activation.",
                "correct": True,
                "rationale": (
                    "Correct. Activating iMessage and FaceTime involves Apple's servers "
                    "verifying the phone number by sending an activation SMS or data request "
                    "through the carrier. If the carrier's APN data settings are incorrect, "
                    "cellular data is restricted, or the plan does not include international "
                    "SMS in certain regions, iMessage and FaceTime will fail to activate even "
                    "though Wi-Fi browsing and voice calls work. Resetting network settings "
                    "or updating carrier settings often resolves this."
                ),
            },
            {
                "id": "c",
                "text": "iMessage activation fails because the Apple ID two-factor authentication code was entered incorrectly.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states Apple ID sign-in is successful, which "
                    "means 2FA completed correctly. An incorrect 2FA code would prevent "
                    "Apple ID login entirely, not just iMessage and FaceTime activation."
                ),
            },
            {
                "id": "d",
                "text": "FaceTime is disabled by the user's MDM profile, which also blocks iMessage as a side effect.",
                "correct": False,
                "rationale": (
                    "Incorrect. An MDM restriction on FaceTime would block FaceTime but "
                    "not necessarily iMessage — these are controlled by separate MDM "
                    "restrictions. More importantly, the question does not indicate an MDM "
                    "profile is installed. The carrier/APN explanation is more consistent "
                    "with both services failing simultaneously on activation."
                ),
            },
        ],
        "explanation": (
            "iMessage and FaceTime activation on iPhone uses a combination of Apple ID "
            "credentials and carrier-level phone number verification. The carrier must "
            "send an activation message (via SMS or a cellular data channel) to Apple's "
            "servers to link the phone number to the Apple ID. Incorrect APN settings, "
            "missing cellular data, or carrier restrictions can block this process while "
            "allowing standard voice calls and Wi-Fi browsing to work normally. "
            "Troubleshooting steps: Settings > General > Transfer or Reset iPhone > Reset > "
            "Reset Network Settings; check carrier settings update; contact carrier to "
            "verify data plan and APN."
        ),
    },
    {
        "id": "a1d1v2-018",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Laptop hardware",
        "stem": (
            "A laptop screen flickers only when the display is at a specific hinge "
            "angle between approximately 60° and 90°, but works normally at all other "
            "angles. The flickering stops immediately when the hinge angle changes even "
            "slightly. An external display through the HDMI port works perfectly at all "
            "times. Which component is most likely causing this symptom?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The LCD backlight inverter frequency is modulated by hinge position sensors, causing flicker at specific angles.",
                "correct": False,
                "rationale": (
                    "Incorrect. Backlight inverters (on CCFL-based displays) or LED drivers "
                    "are not modulated by hinge position. Hinge position sensors do not exist "
                    "as a standard laptop component that interacts with backlight control "
                    "circuitry."
                ),
            },
            {
                "id": "b",
                "text": "The eDP (embedded DisplayPort) or LVDS cable connecting the display panel to the motherboard has a partial break or intermittent contact that is stressed at the specific hinge angle.",
                "correct": True,
                "rationale": (
                    "Correct. The display cable (eDP or LVDS ribbon cable) routes from the "
                    "system board through the hinge and into the display lid. Bending the "
                    "cable repeatedly as the lid opens and closes can cause hairline wire "
                    "breaks or frayed conductors that make intermittent contact only under "
                    "specific stress angles. The symptom — flicker at a specific hinge angle "
                    "only — is the classic presentation of a damaged display cable. The "
                    "external display works because it connects via HDMI directly to the GPU "
                    "output, bypassing the internal cable path entirely."
                ),
            },
            {
                "id": "c",
                "text": "The GPU is throttling at a specific hinge angle due to thermal hotspots caused by reduced airflow when the lid is partially closed.",
                "correct": False,
                "rationale": (
                    "Incorrect. GPU thermal throttling causes performance reduction "
                    "(frame rate drops, slower processing) but does not cause display "
                    "signal flickering. Furthermore, a 60–90° angle does not restrict "
                    "airflow to the GPU more than other angles."
                ),
            },
            {
                "id": "d",
                "text": "The display panel's PWM (Pulse Width Modulation) backlight dimming frequency resonates at the specific hinge angle due to mechanical vibration.",
                "correct": False,
                "rationale": (
                    "Incorrect. PWM backlight flicker is a constant frequency unrelated to "
                    "hinge position. Mechanical resonance does not affect PWM frequency or "
                    "cause angle-dependent display flickering. This is a fabricated "
                    "mechanism that does not reflect real laptop hardware behavior."
                ),
            },
        ],
        "explanation": (
            "The display cable (eDP on modern laptops, LVDS on older models) runs from the "
            "motherboard, through the hinge, and up into the display lid. This cable flexes "
            "every time the lid is opened or closed. Over time, repeated flexing causes "
            "hairline fractures in individual conductors within the ribbon cable. A partial "
            "break will make or lose contact only at specific hinge angles where the flex "
            "stress is maximum. The hallmark symptom is flickering or signal loss at a "
            "specific, narrow hinge angle range, with full function at all other angles. "
            "Replacement of the display cable resolves the issue."
        ),
    },
    {
        "id": "a1d1v2-019",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile synchronization",
        "stem": (
            "A user's Android phone and Windows laptop both have Microsoft OneDrive "
            "installed and signed in to the same account. Photos taken on the phone "
            "upload to OneDrive Camera Roll successfully. However, the user notices "
            "that edits made to Word documents on the laptop do not appear on the "
            "phone's OneDrive app within 5 minutes, but do appear after approximately "
            "2 hours. Which setting most likely explains the delayed sync to the phone?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OneDrive on Android is set to sync only when the device is charging, and the phone is not plugged in during the day.",
                "correct": True,
                "rationale": (
                    "Correct. OneDrive for Android (and other mobile cloud apps) includes "
                    "a battery optimization option that restricts sync to when the device "
                    "is charging. If this is enabled, document changes made on other devices "
                    "accumulate on OneDrive's servers but are not pulled to the phone's local "
                    "cache until the phone is plugged in. Photos upload because Camera Roll "
                    "upload may have a separate 'upload while charging' trigger, but the sync "
                    "delay for document downloads aligns with charging cycles."
                ),
            },
            {
                "id": "b",
                "text": "Microsoft OneDrive has a 2-hour server-side propagation delay for files edited on Windows before they appear on mobile.",
                "correct": False,
                "rationale": (
                    "Incorrect. OneDrive server-side propagation is nearly real-time (seconds "
                    "to minutes). A consistent 2-hour delay is not caused by server propagation; "
                    "it points to a client-side sync interval or restriction on the phone, not "
                    "a server delay."
                ),
            },
            {
                "id": "c",
                "text": "Word documents require file conversion from .docx to a mobile-compatible format, which OneDrive servers queue for up to 2 hours.",
                "correct": False,
                "rationale": (
                    "Incorrect. OneDrive stores and syncs .docx files natively without "
                    "conversion delays. Microsoft Office files are not queued for "
                    "conversion on OneDrive servers; they sync as binary blobs. The "
                    "OneDrive mobile app opens .docx files using Word for Android."
                ),
            },
            {
                "id": "d",
                "text": "OneDrive requires both devices to be on the same Wi-Fi network for sync to occur in real time; cross-network sync is batched every 2 hours.",
                "correct": False,
                "rationale": (
                    "Incorrect. OneDrive syncs through Microsoft's cloud servers, not "
                    "directly between devices. Both devices communicate independently with "
                    "the cloud over any internet connection. There is no requirement for "
                    "both devices to be on the same Wi-Fi network, and no 2-hour batch "
                    "window for cross-network sync."
                ),
            },
        ],
        "explanation": (
            "Cloud sync apps on mobile devices often have battery-optimization settings that "
            "restrict background sync to when the device is charging (or connected to Wi-Fi). "
            "Android's own Doze mode and battery optimization features can also restrict "
            "background network activity for apps. When OneDrive (or other sync apps) only "
            "syncs during charging cycles, changes from other devices appear on the phone only "
            "when the user plugs in — which may be a 2+ hour gap during the workday. To enable "
            "real-time sync, disable battery optimization for OneDrive in Android settings "
            "(Settings > Apps > OneDrive > Battery > Unrestricted) and adjust OneDrive sync "
            "settings to allow background sync."
        ),
    },
    {
        "id": "a1d1v2-020",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Mobile connection types & ports",
        "stem": (
            "A technician is deploying a new tablet to a warehouse worker. The tablet "
            "needs to connect to a handheld barcode scanner and also charge from a "
            "single USB-C cable connected to a wall adapter. The USB-C port on the "
            "tablet supports USB 3.2 Gen 1 and USB Power Delivery. (Choose TWO "
            "technologies that the tablet's USB-C port can support simultaneously "
            "in this scenario.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "USB Power Delivery (USB PD) charging from the wall adapter.",
                "correct": True,
                "rationale": (
                    "Correct. USB Power Delivery allows the USB-C port to receive power from "
                    "a compliant wall adapter while simultaneously performing data transfers. "
                    "USB PD is supported on the port as stated in the scenario. The wall "
                    "adapter charges the tablet while the port also handles data."
                ),
            },
            {
                "id": "b",
                "text": "USB OTG (On-The-Go) or USB Host mode to connect the barcode scanner as a peripheral device.",
                "correct": True,
                "rationale": (
                    "Correct. USB-C ports that support USB OTG (Host mode) can enumerate "
                    "connected USB peripherals such as barcode scanners, keyboards, or USB "
                    "drives. A USB-C hub with a power delivery pass-through port allows "
                    "the tablet to charge via PD while also hosting peripherals. Modern "
                    "USB-C tablets commonly support simultaneous charging and peripheral "
                    "hosting."
                ),
            },
            {
                "id": "c",
                "text": "Thunderbolt 3 data transfer to connect to a Thunderbolt dock for extended peripherals.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario specifies USB 3.2 Gen 1 support — Thunderbolt 3 "
                    "is a separate Intel-licensed protocol that uses the USB-C connector but "
                    "requires dedicated Thunderbolt controller hardware. A USB 3.2 Gen 1 port "
                    "is not Thunderbolt 3, and a Thunderbolt dock would not function on a "
                    "USB 3.2-only USB-C port."
                ),
            },
            {
                "id": "d",
                "text": "eSATA data transfer to a high-speed external SATA SSD.",
                "correct": False,
                "rationale": (
                    "Incorrect. eSATA is a separate physical interface standard (it uses a "
                    "dedicated eSATA connector, not USB-C). There is no eSATA signal over "
                    "USB-C — USB-C does not carry SATA signals. An external SATA SSD would "
                    "require either an eSATA port or a SATA-to-USB bridge enclosure."
                ),
            },
        ],
        "explanation": (
            "USB-C supports multiple simultaneous functions via its multi-function design: "
            "USB Power Delivery (for charging), USB data (for peripherals via Host/OTG mode), "
            "and DisplayPort Alt Mode (for video) can coexist through a hub or dock. In this "
            "scenario, the tablet charges via USB PD from the wall adapter while also enumerating "
            "the barcode scanner as a USB HID device. A USB-C hub with PD pass-through achieves "
            "both simultaneously. Thunderbolt 3 requires specific hardware not present in a "
            "USB 3.2 Gen 1 port. eSATA is a completely separate physical interface."
        ),
    },
    {
        "id": "a1d1v2-021",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Laptop hardware",
        "stem": (
            "A technician must upgrade a laptop's storage from a 256 GB NVMe SSD to a "
            "1 TB NVMe SSD. The laptop has a single M.2 slot. The OS is Windows 11. "
            "(Choose TWO steps that are required BEFORE removing the original SSD to "
            "ensure a successful migration with no data loss.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clone the source SSD to the destination SSD using a USB-to-M.2 enclosure or cloning software BEFORE swapping the drive.",
                "correct": True,
                "rationale": (
                    "Correct. With only one M.2 slot, the drives cannot both be installed "
                    "simultaneously. The technician must clone the source drive to the "
                    "destination drive while the source is still installed (using a USB-to-"
                    "M.2 NVMe enclosure for the destination, or by temporarily connecting "
                    "the destination via an external enclosure). Only after a verified clone "
                    "should the source be removed."
                ),
            },
            {
                "id": "b",
                "text": "Suspend or disable BitLocker encryption on the drive, or record the BitLocker recovery key, before cloning to ensure the cloned drive boots correctly on the same hardware.",
                "correct": True,
                "rationale": (
                    "Correct. If BitLocker is active, a hardware change (replacing the storage "
                    "device) may trigger a BitLocker recovery prompt on the next boot, or "
                    "the clone may fail to unlock. Suspending BitLocker before cloning (and "
                    "re-enabling it after) prevents recovery key prompts. At minimum, the "
                    "recovery key should be backed up before any storage migration on a "
                    "BitLocker-protected drive."
                ),
            },
            {
                "id": "c",
                "text": "Delete the Windows Recovery partition before cloning to prevent dual-copy conflicts on the larger destination drive.",
                "correct": False,
                "rationale": (
                    "Incorrect. The Windows Recovery partition should NOT be deleted before "
                    "cloning. It is a critical component for system recovery (Windows RE). "
                    "A proper clone tool will include the recovery partition and expand the "
                    "data partition to fill the additional space on the larger drive."
                ),
            },
            {
                "id": "d",
                "text": "Downgrade the destination NVMe SSD to the same firmware version as the source drive for compatibility.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no requirement to match firmware versions between "
                    "source and destination NVMe drives. The destination drive receives a "
                    "copy of the OS and data partition; the drive firmware does not need to "
                    "match the source. In fact, keeping the destination drive on its current "
                    "or latest firmware is preferable."
                ),
            },
        ],
        "explanation": (
            "Single-slot M.2 laptop upgrades require the clone to be performed while the source "
            "is installed in the laptop and the destination is connected externally (USB-to-M.2 "
            "NVMe enclosure). Key pre-migration steps: (1) Clone the drive bit-for-bit including "
            "all partitions (EFI, OS, Recovery); (2) handle BitLocker by suspending it, backing "
            "up the recovery key, or fully decrypting the drive to avoid post-migration recovery "
            "prompts. After swapping, re-enable BitLocker if needed. Verify the clone includes "
            "the EFI System Partition; missing it produces 'no bootable device' after swap."
        ),
    },
    {
        "id": "a1d1v2-022",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "MDM/MAM",
        "stem": (
            "A company's MDM administrator must ensure that corporate iOS devices "
            "automatically connect to the corporate VPN whenever users access company "
            "intranet hostnames, WITHOUT requiring users to manually toggle the VPN. "
            "Users should be able to browse non-corporate sites without VPN. "
            "(Choose TWO MDM capabilities that together accomplish this requirement.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure an Always-On VPN profile that forces ALL traffic through the VPN at all times.",
                "correct": False,
                "rationale": (
                    "Incorrect. Always-On VPN tunnels all traffic through the VPN regardless "
                    "of destination — this does not meet the requirement to allow non-corporate "
                    "traffic without VPN. Always-On VPN also consumes more battery and corporate "
                    "bandwidth unnecessarily."
                ),
            },
            {
                "id": "b",
                "text": "Deploy a Per-App VPN profile that triggers the VPN automatically when specified managed apps initiate connections.",
                "correct": True,
                "rationale": (
                    "Correct. Per-App VPN (supported on iOS via MDM VPN payload) automatically "
                    "establishes a VPN tunnel when a specified managed app launches or "
                    "initiates a connection. Non-managed apps do not use the VPN. This "
                    "allows granular control over which app traffic is tunneled, satisfying "
                    "the corporate-only VPN requirement without routing all traffic."
                ),
            },
            {
                "id": "c",
                "text": "Configure On-Demand VPN rules with match-domain triggers for corporate intranet domain suffixes, establishing the VPN automatically when those domains are accessed.",
                "correct": True,
                "rationale": (
                    "Correct. iOS MDM supports On-Demand VPN with domain-based rules "
                    "(using the OnDemandRules array in the VPN payload). The Connect action "
                    "is triggered when DNS queries match corporate domain suffixes (e.g., "
                    "*.corp.example.com). Non-matching domains use the normal internet path. "
                    "This is the standard MDM mechanism for automatic, domain-based VPN "
                    "activation without user interaction."
                ),
            },
            {
                "id": "d",
                "text": "Install a PAC (Proxy Auto-Configuration) file on the devices that redirects intranet hostnames through a SOCKS proxy instead of VPN.",
                "correct": False,
                "rationale": (
                    "Incorrect. A PAC file directs HTTP/HTTPS traffic to a proxy server; it "
                    "does not establish a VPN tunnel. A SOCKS proxy through PAC would require "
                    "the proxy server to be externally accessible and would not provide the "
                    "same network-layer access as a VPN for non-HTTP intranet resources "
                    "(such as file servers or internal services on non-HTTP ports)."
                ),
            },
        ],
        "explanation": (
            "iOS MDM provides two mechanisms for automatic VPN: (1) Per-App VPN — tunnels only "
            "traffic from specified managed apps, not all device traffic; and (2) On-Demand VPN "
            "— automatically connects or disconnects the VPN based on domain, SSID, or other "
            "rules. Using On-Demand VPN with domain-match rules is the primary mechanism to "
            "auto-connect the VPN when accessing *.corp.example.com hostnames while leaving "
            "all other traffic on the direct internet path. Per-App VPN complements this "
            "for app-specific enforcement. Always-On VPN is for scenarios requiring all "
            "traffic to be inspected and does not satisfy the selective routing requirement."
        ),
    },
    {
        "id": "a1d1v2-023",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile email configuration",
        "stem": (
            "A user's mobile email client is configured with an Exchange ActiveSync "
            "account that successfully syncs email but the user cannot view their free/"
            "busy calendar availability from a corporate scheduling app. The scheduling "
            "app accesses Exchange calendars via EWS (Exchange Web Services). Which "
            "port and protocol does EWS use, and why might it be inaccessible from "
            "a mobile device on a carrier network?"
        ),
        "options": [
            {
                "id": "a",
                "text": "EWS uses port 443 (HTTPS); it may be inaccessible because the organization restricts EWS access to on-premises IP ranges, and the mobile device's carrier IP is not in the allowed list.",
                "correct": True,
                "rationale": (
                    "Correct. Exchange Web Services (EWS) is accessed over HTTPS on port 443 "
                    "(the standard secure web port). Organizations frequently restrict EWS "
                    "access to specific IP address ranges (e.g., the corporate office subnet "
                    "or VPN egress IPs) to reduce attack surface. A mobile device on a carrier "
                    "network has a carrier-assigned public IP, which is not in the corporate "
                    "allow list, causing EWS connections to be blocked while ActiveSync (which "
                    "may be allowed from any IP) continues to work."
                ),
            },
            {
                "id": "b",
                "text": "EWS uses port 8080 (HTTP alternate); carrier networks NAT this port to a different port, breaking EWS connectivity.",
                "correct": False,
                "rationale": (
                    "Incorrect. EWS does not use port 8080. Exchange Web Services is a "
                    "SOAP/HTTPS web service that uses port 443 (HTTPS) exclusively in "
                    "production deployments. Port 8080 is an HTTP development/alternate "
                    "port not used by Exchange in enterprise configurations."
                ),
            },
            {
                "id": "c",
                "text": "EWS uses port 135 (RPC); carrier networks block all RPC ports to prevent exploitation, causing EWS to fail on mobile.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port 135 is the RPC Endpoint Mapper port used by legacy "
                    "Outlook with MAPI-over-RPC (classic Outlook connection method). Modern "
                    "EWS uses HTTPS on port 443, not RPC port 135. EWS was specifically "
                    "designed as an HTTP-based API to avoid firewall issues with RPC."
                ),
            },
            {
                "id": "d",
                "text": "EWS uses port 587; mobile carriers block port 587 on the same policy that blocks port 25, causing EWS to be unreachable.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port 587 is the SMTP submission port for outgoing email, "
                    "not an EWS port. EWS uses HTTPS on port 443. Confusing email submission "
                    "ports with Exchange Web Services ports is a common knowledge gap that "
                    "this distractor targets."
                ),
            },
        ],
        "explanation": (
            "Exchange Web Services (EWS) is a SOAP-based API that uses HTTPS on port 443 to "
            "provide access to calendar, contacts, email, and free/busy data. Because it runs "
            "on standard HTTPS, it is rarely blocked by carrier networks at the protocol level. "
            "However, organizations commonly implement Conditional Access or IP allowlisting "
            "on their Exchange servers or reverse proxies to restrict EWS to known IP ranges "
            "(VPN, office, or Azure AD Conditional Access policies). Mobile devices on carrier "
            "networks fall outside these ranges. Solution: require VPN connection for EWS "
            "access, or use Conditional Access policies that permit compliant enrolled devices."
        ),
    },
    {
        "id": "a1d1v2-024",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Location services",
        "stem": (
            "A retail chain deploys tablets in stores to track customer foot traffic "
            "patterns using Bluetooth Low Energy (BLE) beacons placed throughout the "
            "store. A technician notices that the positioning system loses accuracy in "
            "one section of the store where a large metal shelving unit was recently "
            "installed. No BLE beacons are blocked or powered off. Which phenomenon "
            "is most likely causing the reduced accuracy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The metal shelving unit is emitting its own RF signals on the 2.4 GHz band, jamming the BLE beacons.",
                "correct": False,
                "rationale": (
                    "Incorrect. Metal shelving units are passive objects; they do not emit "
                    "RF signals. They can reflect, absorb, and diffract RF signals, but "
                    "they do not actively jam or generate 2.4 GHz transmissions."
                ),
            },
            {
                "id": "b",
                "text": "The metal shelving unit reflects and absorbs 2.4 GHz BLE signals, causing multipath interference and RSSI measurement errors that degrade position calculations.",
                "correct": True,
                "rationale": (
                    "Correct. BLE positioning systems calculate location based on Received "
                    "Signal Strength Indicator (RSSI) measurements from multiple beacons. "
                    "Metal surfaces are highly reflective at 2.4 GHz, creating multipath "
                    "propagation — signals arrive at the receiver via multiple reflected "
                    "paths with different delays and strengths. This causes RSSI readings "
                    "to be inconsistent, reducing the accuracy of trilateration-based position "
                    "estimates. The solution is to add additional beacons in the affected "
                    "area or use a time-of-flight (ToF) system less susceptible to multipath."
                ),
            },
            {
                "id": "c",
                "text": "The metal shelving unit's grounding wire is creating an electrical ground loop that interferes with the tablet's BLE radio.",
                "correct": False,
                "rationale": (
                    "Incorrect. Ground loops cause audio hum in electrical circuits, not "
                    "RF interference at 2.4 GHz. A shelving unit ground wire at 50/60 Hz "
                    "would not produce significant interference at 2.4 GHz. This is not "
                    "a real cause of BLE positioning degradation."
                ),
            },
            {
                "id": "d",
                "text": "Metal shelving reduces battery voltage in nearby BLE beacons through induction, causing beacons to transmit at lower power.",
                "correct": False,
                "rationale": (
                    "Incorrect. BLE beacons are battery-powered or powered by low-voltage "
                    "DC supplies. Passive metal shelving does not induce voltage changes in "
                    "nearby beacon batteries through static induction under normal operating "
                    "conditions. This is not a real phenomenon affecting BLE beacon performance."
                ),
            },
        ],
        "explanation": (
            "BLE indoor positioning uses RSSI from multiple beacons to trilaterate device "
            "position. Metal surfaces reflect 2.4 GHz radio waves strongly, creating multipath "
            "— multiple signal copies arriving via reflected paths, each with different amplitudes "
            "and phases. The receiver's RSSI measurement becomes a sum of direct and reflected "
            "paths, making it unstable and inaccurate. This is a known challenge in retail and "
            "warehouse environments. Mitigation strategies include denser beacon placement, "
            "using UWB (Ultra-Wideband) for time-of-flight positioning (which is more resistant "
            "to multipath), and applying signal filtering algorithms that account for reflections."
        ),
    },
    {
        "id": "a1d1v2-025",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile network connectivity",
        "stem": (
            "A corporate smartphone user connects to a new hotel Wi-Fi network. The "
            "MDM profile on the device enforces a per-app VPN that should automatically "
            "tunnel all managed app traffic. After connecting to the hotel Wi-Fi, "
            "managed apps fail to connect and the VPN shows 'Unable to connect to "
            "VPN server'. The user can browse public websites normally from unmanaged "
            "apps. Which is the most likely cause of the VPN failure specifically "
            "in this hotel network context?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The hotel Wi-Fi uses a captive portal that requires browser-based authentication before allowing arbitrary internet traffic, which blocks the VPN connection attempt before authentication completes.",
                "correct": True,
                "rationale": (
                    "Correct. Captive portals intercept all traffic from unauthenticated "
                    "clients and redirect HTTP requests to a login page. VPN protocols "
                    "(IKEv2, IPsec, SSL/TLS) are not HTTP and are typically blocked by the "
                    "captive portal firewall until the user authenticates via the portal. "
                    "Unmanaged browser-based apps succeed because the captive portal allows "
                    "basic HTTP/HTTPS to the login page. Managed apps using the per-app VPN "
                    "fail because the VPN tunnel cannot be established until the captive "
                    "portal is cleared. The user must open a browser, complete the captive "
                    "portal login, and then retry the VPN."
                ),
            },
            {
                "id": "b",
                "text": "The hotel's SSID uses WPA3-Enterprise, which is incompatible with the MDM's per-app VPN profile.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3-Enterprise provides wireless authentication and "
                    "encryption at the Wi-Fi layer — it is independent of VPN protocol "
                    "compatibility. Per-app VPN operates above the Wi-Fi layer and is not "
                    "affected by the WPA security version of the network."
                ),
            },
            {
                "id": "c",
                "text": "The MDM server cannot communicate with the device to push the VPN trigger policy because the device is on a guest network with MDM port 8443 blocked.",
                "correct": False,
                "rationale": (
                    "Incorrect. Per-app VPN on iOS is configured via the MDM profile already "
                    "installed on the device; it does not require a real-time push from the "
                    "MDM server to trigger. The trigger runs locally on the device when "
                    "a managed app initiates a connection. MDM port availability affects "
                    "ongoing policy updates, not locally-triggered VPN rules."
                ),
            },
            {
                "id": "d",
                "text": "The VPN server's certificate has expired and the hotel network's stricter DNS is resolving the VPN hostname to a different IP.",
                "correct": False,
                "rationale": (
                    "Incorrect. An expired VPN certificate would cause authentication failure "
                    "at the TLS handshake level after the VPN connection is initiated — the "
                    "error would be a certificate trust error, not 'unable to connect'. DNS "
                    "resolution of VPN hostnames would function on any internet-connected "
                    "network. Neither explanation is specific to a hotel network context or "
                    "explains why unmanaged apps succeed."
                ),
            },
        ],
        "explanation": (
            "Captive portals are ubiquitous on hotel, airport, and public Wi-Fi networks. They "
            "intercept all traffic from unauthenticated clients and redirect HTTP/HTTPS to a "
            "login page. VPN protocols (IKEv2 on UDP 500/4500, IPsec, OpenVPN on UDP/TCP 1194, "
            "SSL VPN on TCP 443) are blocked by the captive portal firewall. The OS typically "
            "detects the captive portal and displays a notification; if dismissed, no browser "
            "login occurs and VPN attempts fail. Resolution: open the default browser to trigger "
            "the captive portal redirect, complete authentication, then reconnect the VPN. "
            "This is one of the most common real-world VPN failure scenarios for mobile users."
        ),
    },
]

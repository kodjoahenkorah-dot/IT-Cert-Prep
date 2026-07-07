"""
CompTIA A+ Core 1 (220-1201) — Domain 1: Mobile Devices
Study notes organized following the Professor Messer 220-1201 playlist order.
Original content written from expert knowledge of the 220-1201 exam objectives.
"""

NOTES = [
    {
        "domain": 1,
        "topic": "Laptop hardware",
        "objective": "1.1",
        "video": "Laptop Hardware",
        "study_topics": ["Laptop hardware"],
        "body": (
            "<p>Laptops share many components with desktop PCs but are designed for portability, "
            "which imposes unique form-factor and serviceability constraints. Understanding which "
            "parts are user-replaceable versus soldered is a core exam competency.</p>"
            "<ul>"
            "<li><strong>RAM:</strong> Most modern laptops use SO-DIMM (Small Outline Dual Inline "
            "Memory Module) slots. Some ultrabooks solder RAM directly to the motherboard, making "
            "it non-upgradeable. DDR4 and DDR5 SO-DIMMs are not cross-compatible.</li>"
            "<li><strong>Storage:</strong> Laptops may use 2.5-inch SATA drives, M.2 NVMe/SATA "
            "SSDs, or eMMC (soldered). M.2 slots are keyed — B+M key supports both SATA and NVMe; "
            "M key is NVMe-only.</li>"
            "<li><strong>CPU:</strong> Typically soldered (BGA package) and not user-replaceable. "
            "Mobile CPUs use lower TDPs (thermal design power) for battery life.</li>"
            "<li><strong>Battery:</strong> Lithium-ion or lithium-polymer. Connected via ribbon or "
            "harness connector. Replaceable in many models; embedded in ultrabooks.</li>"
            "<li><strong>Keyboard / Trackpad:</strong> Connected via ribbon cables (ZIF connectors). "
            "Often replaceable as a unit.</li>"
            "<li><strong>Optical Drive:</strong> Rare in modern laptops; uses a SATA interface and "
            "slides into a caddy.</li>"
            "<li><strong>DC Jack:</strong> The barrel or USB-C power connector; can loosen with use "
            "and may require soldering or a replacement board.</li>"
            "<li><strong>Speakers:</strong> Small drivers connected via thin wire harnesses; replaced "
            "as discrete units.</li>"
            "<li><strong>Heat sink / Fan:</strong> CPU and GPU share a heat pipe assembly. Cleaning "
            "or replacing thermal paste restores cooling performance.</li>"
            "</ul>"
            "<p>When disassembling a laptop, always disconnect the battery first, use an ESD wrist "
            "strap, and consult the manufacturer's service manual for torque specs and cable routing.</p>"
        ),
        "key_points": [
            "SO-DIMM is the standard laptop RAM form factor; DDR4 and DDR5 are not cross-compatible.",
            "M.2 drives can be SATA or NVMe — the slot key and protocol must match.",
            "Most laptop CPUs are BGA-soldered and cannot be swapped by the end user.",
            "Always disconnect the battery before opening a laptop to prevent ESD and short circuits.",
            "Ribbon cables use ZIF (Zero Insertion Force) connectors — lift the locking tab before pulling.",
            "Reapplying quality thermal paste to the CPU/GPU heat sink can dramatically reduce temperatures.",
        ],
    },
    {
        "domain": 1,
        "topic": "Mobile display components",
        "objective": "1.1",
        "video": "Mobile Display Components",
        "study_topics": ["Mobile display components"],
        "body": (
            "<p>Mobile device displays are multilayer assemblies. Knowing the role of each layer "
            "is essential for diagnosing display defects and understanding replacement procedures.</p>"
            "<table>"
            "<tr><th>Component</th><th>Function</th></tr>"
            "<tr><td><strong>LCD Panel</strong></td><td>Twisted Nematic (TN) or IPS; backlit by "
            "LED strips. Produces the image but requires a backlight.</td></tr>"
            "<tr><td><strong>OLED/AMOLED</strong></td><td>Each pixel is self-emissive; no separate "
            "backlight needed. Offers true blacks and high contrast. Common in premium phones.</td></tr>"
            "<tr><td><strong>Backlight</strong></td><td>LED strip (edge-lit or direct). Failure "
            "causes a dim or dark screen; image may still be faintly visible with a flashlight.</td></tr>"
            "<tr><td><strong>Digitizer</strong></td><td>Capacitive touch layer bonded above or "
            "below glass. Translates finger position to digital coordinates. Can fail independently "
            "of the LCD.</td></tr>"
            "<tr><td><strong>Glass/Gorilla Glass</strong></td><td>Protective outer layer. Cracks "
            "here do not always damage the LCD beneath.</td></tr>"
            "<tr><td><strong>Inverter</strong></td><td>Found in older CCFL-backlit laptops; converts "
            "DC to AC for the cold-cathode fluorescent lamp. Rare in modern devices.</td></tr>"
            "</table>"
            "<p><strong>Display interfaces:</strong> Internal laptop displays use LVDS (older) or "
            "eDP (Embedded DisplayPort, current standard). External ports include HDMI, DisplayPort, "
            "USB-C (Alt Mode DP), and Thunderbolt.</p>"
            "<p><strong>Resolution terms:</strong> HD (1280×720), FHD (1920×1080), QHD (2560×1440), "
            "4K UHD (3840×2160). Higher DPI improves text clarity but demands more GPU power.</p>"
            "<p><strong>Troubleshooting tips:</strong> A cracked digitizer but intact LCD shows "
            "correct image but touch fails. A failed backlight shows a dark screen with faint image. "
            "Dead pixels are permanent LCD defects.</p>"
        ),
        "key_points": [
            "OLED pixels are self-emissive — no backlight is needed; provides true blacks.",
            "The digitizer is the capacitive touch sensor; it can break independently of the LCD.",
            "A failed backlight produces a dark screen where the image is still faintly visible with a light.",
            "Modern laptop displays use eDP (Embedded DisplayPort) internally.",
            "Inverters are only found in older CCFL-backlit displays; LED backlights do not use them.",
            "Glass/screen protector cracks do not always damage the digitizer or LCD underneath.",
        ],
    },
    {
        "domain": 1,
        "topic": "Mobile connection types & ports",
        "objective": "1.1",
        "video": "Mobile Connection Types and Ports",
        "study_topics": ["Mobile connection types & ports"],
        "body": (
            "<p>Mobile devices use a variety of physical connectors for power, data, and accessories. "
            "Identifying each connector and its capabilities is a frequent exam topic.</p>"
            "<table>"
            "<tr><th>Connector</th><th>Key Facts</th></tr>"
            "<tr><td><strong>USB-C</strong></td><td>Reversible 24-pin connector. Supports USB 2.0–4, "
            "DisplayPort Alt Mode, Thunderbolt 3/4 (on supported hardware), and USB Power Delivery "
            "(up to 240 W). Ubiquitous on modern Android devices and laptops.</td></tr>"
            "<tr><td><strong>Lightning</strong></td><td>Apple proprietary 8-pin connector (iPhone/iPad "
            "pre-USB-C). Reversible. Max USB 2.0 speeds unless adapted. Being phased out in favor of "
            "USB-C per EU regulation.</td></tr>"
            "<tr><td><strong>Micro-USB</strong></td><td>5-pin; older Android and peripheral standard. "
            "Not reversible. USB 2.0 speeds; USB 3.0 Micro-B adds extra pins.</td></tr>"
            "<tr><td><strong>Mini-USB</strong></td><td>Older standard found on cameras and early "
            "smartphones; largely obsolete.</td></tr>"
            "<tr><td><strong>3.5 mm Audio Jack</strong></td><td>TRRS connector carries stereo audio "
            "plus microphone. Removed from many flagship phones.</td></tr>"
            "<tr><td><strong>SD / MicroSD</strong></td><td>Removable flash storage. MicroSD adapters "
            "allow use in full-size SD slots. Maximum capacity depends on SDXC/SDHC standard.</td></tr>"
            "<tr><td><strong>SIM Card Slot</strong></td><td>Standard SIM, Micro-SIM, Nano-SIM "
            "(current), or eSIM (embedded, software-provisioned). Holds carrier credentials (IMSI).</td></tr>"
            "</table>"
            "<p><strong>Thunderbolt</strong> (Intel/Apple): Uses USB-C physical connector on modern "
            "systems. Thunderbolt 3/4 supports 40 Gbps data, dual 4K displays, and daisy-chaining up "
            "to 6 devices. Identified by the lightning-bolt icon.</p>"
            "<p><strong>Docking stations</strong> connect via USB-C/Thunderbolt and expand a single "
            "port into multiple USB-A, HDMI, Ethernet, and card-reader ports.</p>"
        ),
        "key_points": [
            "USB-C is reversible and supports data, video (DP Alt Mode), and up to 240 W charging.",
            "Lightning is Apple proprietary (8-pin, reversible); phased out in favor of USB-C.",
            "Micro-USB is not reversible; USB 3.0 Micro-B adds a wider connector section.",
            "Thunderbolt 3/4 uses the USB-C physical form factor and runs at 40 Gbps.",
            "eSIM is a software-provisioned embedded SIM; no physical card is inserted.",
            "MicroSD cards require the SDHC or SDXC standard for cards above 2 GB or 32 GB respectively.",
        ],
    },
    {
        "domain": 1,
        "topic": "Mobile network connectivity",
        "objective": "1.2",
        "video": "Mobile Network Connectivity",
        "study_topics": ["Mobile network connectivity"],
        "body": (
            "<p>Mobile devices connect to networks via cellular radio, Wi-Fi, and other wireless "
            "standards. Understanding each technology's characteristics supports both configuration "
            "and troubleshooting questions on the exam.</p>"
            "<p><strong>Cellular generations:</strong></p>"
            "<ul>"
            "<li><strong>3G (HSPA+):</strong> Theoretical ~21 Mbps down. Legacy; still used in "
            "rural fallback.</li>"
            "<li><strong>4G LTE:</strong> 100–300 Mbps typical; low latency; the current widespread "
            "standard. VoLTE (Voice over LTE) carries calls as data.</li>"
            "<li><strong>5G:</strong> Sub-6 GHz (wide coverage, ~1 Gbps) and mmWave (high density, "
            "up to 10 Gbps, short range). Requires 5G-capable device and carrier support.</li>"
            "</ul>"
            "<p><strong>Wi-Fi standards (IEEE 802.11):</strong></p>"
            "<table>"
            "<tr><th>Standard</th><th>Alias</th><th>Band</th><th>Max Speed</th></tr>"
            "<tr><td>802.11n</td><td>Wi-Fi 4</td><td>2.4/5 GHz</td><td>600 Mbps</td></tr>"
            "<tr><td>802.11ac</td><td>Wi-Fi 5</td><td>5 GHz</td><td>3.5 Gbps</td></tr>"
            "<tr><td>802.11ax</td><td>Wi-Fi 6/6E</td><td>2.4/5/6 GHz</td><td>9.6 Gbps</td></tr>"
            "<tr><td>802.11be</td><td>Wi-Fi 7</td><td>2.4/5/6 GHz</td><td>46 Gbps</td></tr>"
            "</table>"
            "<p><strong>Hotspot / Tethering:</strong> A mobile device can share its cellular data "
            "connection via Wi-Fi hotspot, USB tethering, or Bluetooth tethering. Carrier data plans "
            "may limit or throttle hotspot usage.</p>"
            "<p><strong>Airplane Mode</strong> disables all radios (cellular, Wi-Fi, Bluetooth, GPS) "
            "simultaneously. Individual radios can be re-enabled while airplane mode is on (e.g., "
            "Wi-Fi calling on a flight).</p>"
            "<p><strong>VPN on mobile:</strong> Encrypts all traffic over untrusted networks. Can be "
            "configured per-app (per-app VPN) or device-wide through MDM policies.</p>"
        ),
        "key_points": [
            "4G LTE is the dominant cellular standard; 5G adds sub-6 GHz and mmWave options.",
            "802.11ax (Wi-Fi 6) operates on 2.4, 5, and 6 GHz bands and reaches 9.6 Gbps theoretical.",
            "Airplane Mode disables all radios; individual radios (Wi-Fi, BT) can be re-enabled on top of it.",
            "Hotspot tethering shares cellular data via Wi-Fi, USB, or Bluetooth — carrier plans may throttle it.",
            "5G mmWave delivers very high speeds but has limited range and poor wall penetration.",
            "VoLTE carries voice calls as LTE data packets, enabling simultaneous voice and data.",
        ],
    },
    {
        "domain": 1,
        "topic": "Mobile email configuration",
        "objective": "1.3",
        "video": "Mobile Email Configuration",
        "study_topics": ["Mobile email configuration"],
        "body": (
            "<p>Configuring email on mobile devices requires knowing the correct server addresses, "
            "protocol ports, and encryption settings. The A+ exam tests specific port numbers and "
            "protocol behaviors.</p>"
            "<p><strong>Incoming mail protocols:</strong></p>"
            "<table>"
            "<tr><th>Protocol</th><th>Port (Encrypted)</th><th>Port (Unencrypted)</th><th>Behavior</th></tr>"
            "<tr><td><strong>IMAP4</strong></td><td>993 (SSL/TLS)</td><td>143</td>"
            "<td>Synchronizes mail folders on the server. Messages stay on server. Best for "
            "multi-device access.</td></tr>"
            "<tr><td><strong>POP3</strong></td><td>995 (SSL/TLS)</td><td>110</td>"
            "<td>Downloads and (by default) deletes mail from server. Single-device oriented.</td></tr>"
            "</table>"
            "<p><strong>Outgoing mail protocol:</strong></p>"
            "<table>"
            "<tr><th>Protocol</th><th>Port</th><th>Notes</th></tr>"
            "<tr><td><strong>SMTP</strong></td><td>587 (STARTTLS, submission)</td>"
            "<td>Standard authenticated submission port. Preferred for client-to-server sending.</td></tr>"
            "<tr><td><strong>SMTP</strong></td><td>465 (SSL/TLS, SMTPS)</td>"
            "<td>Implicit TLS; used by some providers (e.g., Gmail). RFC 8314 reaffirmed.</td></tr>"
            "<tr><td><strong>SMTP</strong></td><td>25</td>"
            "<td>Server-to-server relay; typically blocked by ISPs for end-user clients.</td></tr>"
            "</table>"
            "<p><strong>Corporate email (Exchange / ActiveSync):</strong> Microsoft Exchange uses "
            "<code>ActiveSync</code> over HTTPS (port 443). Autodiscover simplifies configuration "
            "by providing settings from <code>autodiscover.domain.com</code>. Exchange also supports "
            "IMAP/SMTP for non-Microsoft clients.</p>"
            "<p><strong>S/MIME:</strong> Digitally signs and encrypts email using certificates. "
            "Requires the sender's certificate and the recipient's public key. Configured in "
            "advanced mail settings.</p>"
            "<p><strong>Common troubleshooting:</strong> Verify server name, correct port, and SSL/TLS "
            "toggle. Authentication errors often indicate wrong username format "
            "(<code>user@domain.com</code> vs. <code>DOMAIN\\user</code>).</p>"
        ),
        "key_points": [
            "IMAP port 993 (SSL) / 143 (plain) — keeps mail on server, syncs across devices.",
            "POP3 port 995 (SSL) / 110 (plain) — downloads mail, typically removes from server.",
            "SMTP port 587 (STARTTLS) is the standard client submission port; 465 uses implicit SSL.",
            "ActiveSync over HTTPS (443) is used for Exchange/Microsoft 365 mobile clients.",
            "Autodiscover at autodiscover.domain.com automates Exchange client configuration.",
            "S/MIME provides end-to-end email signing and encryption using PKI certificates.",
        ],
    },
    {
        "domain": 1,
        "topic": "MDM/MAM",
        "objective": "1.5",
        "video": "MDM and MAM",
        "study_topics": ["MDM/MAM"],
        "body": (
            "<p>Mobile Device Management (MDM) and Mobile Application Management (MAM) are "
            "enterprise tools for controlling corporate data on mobile endpoints.</p>"
            "<p><strong>MDM (Mobile Device Management):</strong> Manages the entire device. "
            "The MDM agent is enrolled and given device-level control. Capabilities include:</p>"
            "<ul>"
            "<li>Enforcing PIN/password policies and screen-lock timers</li>"
            "<li>Pushing Wi-Fi, VPN, and email profiles automatically</li>"
            "<li>Remotely locking or wiping the device (<strong>full wipe</strong> returns the "
            "device to factory state, destroying all data)</li>"
            "<li>Enabling device encryption</li>"
            "<li>Geofencing and location tracking</li>"
            "<li>Blocking camera, app installs, or specific device features</li>"
            "</ul>"
            "<p><strong>MAM (Mobile Application Management):</strong> Manages only corporate "
            "applications and their data, not the whole device. Ideal for BYOD (Bring Your Own "
            "Device) scenarios where the employer has no right to wipe personal data.</p>"
            "<ul>"
            "<li><strong>Selective wipe</strong> removes only corporate app data and credentials "
            "while leaving personal photos, contacts, and apps intact.</li>"
            "<li>MAM can enforce copy-paste restrictions between managed and unmanaged apps.</li>"
            "</ul>"
            "<p><strong>Containerization:</strong> Creates an encrypted, isolated partition or "
            "workspace (e.g., Samsung Knox, Android Enterprise Work Profile, Microsoft Intune "
            "container) that keeps corporate data separate from personal data on the same device. "
            "The container can be selectively wiped by IT without touching personal content.</p>"
            "<p><strong>Enrollment methods:</strong> Zero-touch enrollment (Android Enterprise), "
            "Apple Business Manager (ABM/DEP), or manual enrollment via a web portal or QR code. "
            "Corporate-Owned Personally Enabled (COPE) and BYOD are common ownership models.</p>"
            "<p><strong>MDM solutions:</strong> Microsoft Intune, VMware Workspace ONE, Jamf Pro "
            "(Apple-focused), and IBM MaaS360 are common platforms referenced in enterprise contexts.</p>"
        ),
        "key_points": [
            "MDM manages the full device; MAM manages only corporate apps and data.",
            "Full wipe resets the device to factory defaults — all data is erased.",
            "Selective wipe (MAM) removes only corporate data, leaving personal content untouched.",
            "Containerization isolates corporate data in an encrypted workspace on BYOD devices.",
            "MDM can push Wi-Fi/VPN/email profiles, enforce encryption, and remotely lock devices.",
            "BYOD deployments favor MAM/containerization to respect employee personal privacy.",
        ],
    },
    {
        "domain": 1,
        "topic": "Mobile synchronization",
        "objective": "1.4",
        "video": "Mobile Synchronization",
        "study_topics": ["Mobile synchronization"],
        "body": (
            "<p>Synchronization keeps data consistent across a mobile device and cloud or desktop "
            "platforms. Understanding sync methods, data types, and troubleshooting is exam-critical.</p>"
            "<p><strong>Data types commonly synchronized:</strong></p>"
            "<ul>"
            "<li>Contacts, calendar events, email, and tasks</li>"
            "<li>Photos and videos (iCloud Photos, Google Photos, OneDrive)</li>"
            "<li>App data, settings, and purchased app lists</li>"
            "<li>Bookmarks, passwords (iCloud Keychain, Google Password Manager)</li>"
            "<li>Music and media libraries</li>"
            "</ul>"
            "<p><strong>Sync methods:</strong></p>"
            "<table>"
            "<tr><th>Method</th><th>Description</th></tr>"
            "<tr><td><strong>Cloud sync</strong></td><td>Continuous background sync over Wi-Fi or "
            "cellular. iCloud (Apple), Google Account (Android), Microsoft 365. Requires adequate "
            "storage allocation in the cloud account.</td></tr>"
            "<tr><td><strong>Desktop sync (cable)</strong></td><td>iTunes/Finder (iOS) or Android "
            "File Transfer over USB. Manual or automatic when connected.</td></tr>"
            "<tr><td><strong>Exchange ActiveSync</strong></td><td>Push-based sync for email, "
            "contacts, and calendar from a corporate Exchange/Microsoft 365 server.</td></tr>"
            "</table>"
            "<p><strong>Mutual authentication in sync:</strong> Devices must trust the sync server's "
            "certificate. Expired or self-signed certificates can break sync with an SSL error.</p>"
            "<p><strong>Sync troubleshooting steps:</strong></p>"
            "<ol>"
            "<li>Confirm the device has a working network connection.</li>"
            "<li>Check that the cloud account credentials are valid and not locked out.</li>"
            "<li>Verify sufficient cloud storage is available.</li>"
            "<li>Check for conflicting items (duplicate contacts, calendar overlaps).</li>"
            "<li>Sign out and re-sign into the sync account to force re-authentication.</li>"
            "</ol>"
        ),
        "key_points": [
            "Cloud sync (iCloud, Google, OneDrive) operates continuously in the background.",
            "USB/cable sync via iTunes, Finder, or Android File Transfer provides offline backup.",
            "ActiveSync pushes email, contacts, and calendar from Exchange to mobile clients in near real time.",
            "Expired or untrusted SSL certificates can silently break cloud and ActiveSync sync.",
            "Insufficient cloud storage quota is a common cause of photos and backups failing to sync.",
            "Signing out and back into a cloud account forces credential refresh and can resolve stuck syncs.",
        ],
    },
    {
        "domain": 1,
        "topic": "Bluetooth pairing",
        "objective": "1.2",
        "video": "Bluetooth Pairing",
        "study_topics": ["Bluetooth pairing"],
        "body": (
            "<p>Bluetooth is a short-range (typically up to 10 meters for Class 2) wireless standard "
            "operating in the 2.4 GHz ISM band. Version 5.x extends range up to 40 m and improves "
            "speed for peripherals and IoT devices.</p>"
            "<p><strong>Pairing process:</strong></p>"
            "<ol>"
            "<li><strong>Discovery:</strong> Put the accessory in pairing/discoverable mode "
            "(usually a button hold). Enable Bluetooth on the mobile device.</li>"
            "<li><strong>Scanning:</strong> The device scans and lists nearby Bluetooth devices.</li>"
            "<li><strong>Pairing request:</strong> Select the accessory from the list.</li>"
            "<li><strong>Authentication:</strong> Confirm a passkey or PIN. Methods include:<br>"
            "&nbsp;&nbsp;• <em>Numeric comparison</em> — both devices display a 6-digit code; user confirms match.<br>"
            "&nbsp;&nbsp;• <em>Passkey entry</em> — user types a PIN (common: 0000, 1234).<br>"
            "&nbsp;&nbsp;• <em>Just Works</em> — no user confirmation (used for headsets); lower security.<br>"
            "&nbsp;&nbsp;• <em>Out-of-Band (OOB)</em> — pairing data exchanged via NFC.</li>"
            "<li><strong>Bonding:</strong> Devices store pairing keys for automatic reconnection.</li>"
            "</ol>"
            "<p><strong>Bluetooth profiles</strong> define device capabilities:</p>"
            "<ul>"
            "<li><strong>HFP</strong> — Hands-Free Profile (car kits, headsets with mic)</li>"
            "<li><strong>A2DP</strong> — Advanced Audio Distribution Profile (stereo audio streaming)</li>"
            "<li><strong>AVRCP</strong> — Audio/Video Remote Control Profile (play/pause/skip)</li>"
            "<li><strong>HID</strong> — Human Interface Device (keyboards, mice)</li>"
            "<li><strong>PAN</strong> — Personal Area Network (Bluetooth tethering)</li>"
            "</ul>"
            "<p><strong>Troubleshooting:</strong> If pairing fails, clear the pairing on both "
            "devices and restart. Interference from 2.4 GHz Wi-Fi can degrade audio. Move away "
            "from microwaves and dense Wi-Fi environments.</p>"
        ),
        "key_points": [
            "Put the accessory in discoverable/pairing mode before attempting to pair.",
            "Bonding stores the link key so devices reconnect automatically without re-pairing.",
            "A2DP streams stereo audio; HFP provides hands-free calling with a microphone.",
            "'Just Works' pairing requires no PIN but offers no MITM protection — lower security.",
            "Bluetooth 5.x operates at 2.4 GHz and extends range to ~40 m at lower data rates.",
            "Clear saved pairings on both devices if automatic reconnection fails.",
        ],
    },
    {
        "domain": 1,
        "topic": "Location services",
        "objective": "1.6",
        "video": "Location Services",
        "study_topics": ["Location services"],
        "body": (
            "<p>Location services combine multiple technologies to determine a device's geographic "
            "position. Mobile operating systems provide granular permission controls over which apps "
            "can access location data.</p>"
            "<p><strong>Location technologies:</strong></p>"
            "<table>"
            "<tr><th>Technology</th><th>Accuracy</th><th>How it works</th></tr>"
            "<tr><td><strong>GPS</strong></td><td>3–5 m</td>"
            "<td>Receives signals from ≥4 satellites. Most accurate outdoors. High battery drain. "
            "Requires clear sky view; slow to acquire first fix (TTFF).</td></tr>"
            "<tr><td><strong>A-GPS (Assisted GPS)</strong></td><td>3–5 m</td>"
            "<td>Downloads satellite almanac data over cellular/Wi-Fi to accelerate initial GPS fix.</td></tr>"
            "<tr><td><strong>Wi-Fi Positioning</strong></td><td>15–40 m</td>"
            "<td>Compares detected SSIDs/BSSIDs against a database of known AP locations (e.g., "
            "Google, Apple Location Services).</td></tr>"
            "<tr><td><strong>Cell Tower Triangulation</strong></td><td>100 m–several km</td>"
            "<td>Uses signal strength from nearby cell towers. Less accurate; useful indoors.</td></tr>"
            "<tr><td><strong>Bluetooth Beacons</strong></td><td>1–3 m</td>"
            "<td>Indoor positioning using BLE beacons; used in retail and navigation apps.</td></tr>"
            "</table>"
            "<p><strong>OS permission levels (iOS/Android):</strong></p>"
            "<ul>"
            "<li><em>Always</em> — app can access location at any time, even in the background.</li>"
            "<li><em>While in use</em> — only when the app is in the foreground.</li>"
            "<li><em>Never / Deny</em> — no location access.</li>"
            "</ul>"
            "<p><strong>Privacy considerations:</strong> Location history can reveal sensitive "
            "behavioral patterns. MDM policies can disable location services or restrict apps from "
            "using them. Geotagging in photos embeds GPS coordinates in EXIF metadata — can be "
            "a privacy risk if photos are shared publicly.</p>"
            "<p><strong>GPS vs. A-GPS:</strong> GPS alone can take 30–60 seconds to acquire a first "
            "fix; A-GPS reduces this to under 5 seconds by pre-loading satellite orbital data.</p>"
        ),
        "key_points": [
            "GPS is most accurate (3–5 m) but requires outdoor line-of-sight and drains battery.",
            "A-GPS uses cellular/Wi-Fi to download almanac data, dramatically reducing time-to-first-fix.",
            "Wi-Fi positioning compares nearby access points against a location database (~15–40 m accuracy).",
            "Cell tower triangulation is least accurate but works indoors where GPS fails.",
            "Apps should request 'While in use' location permission unless background access is truly needed.",
            "EXIF geotagging embeds GPS coordinates in photos — a privacy risk when sharing images publicly.",
        ],
    },
    {
        "domain": 1,
        "topic": "Safe swollen (lithium-ion) battery response procedure",
        "objective": "1.1",
        "video": "Safe Battery Handling",
        "study_topics": ["Safe swollen (lithium-ion) battery response procedure"],
        "body": (
            "<p>A swollen (puffed) lithium-ion or lithium-polymer battery is a safety hazard. "
            "Swelling is caused by internal cell degradation, overcharging, heat, or physical "
            "damage — it produces flammable gas inside the battery pack. Immediate and correct "
            "action is critical to prevent fire, explosion, or toxic exposure.</p>"
            "<p><strong>Immediate steps when a swollen battery is identified:</strong></p>"
            "<ol>"
            "<li><strong>Stop using the device immediately.</strong> Continued use generates heat "
            "and pressure that can rupture the cell.</li>"
            "<li><strong>Power off the device</strong> if it is safe to do so (i.e., the casing is "
            "not already hot or deformed).</li>"
            "<li><strong>Do NOT puncture, bend, crush, or apply pressure</strong> to the battery. "
            "Mechanical stress can trigger thermal runaway — a rapid, uncontrolled exothermic "
            "reaction.</li>"
            "<li><strong>Do NOT charge the device.</strong> Applying charge to a swollen cell "
            "accelerates gas production and increases rupture risk.</li>"
            "<li><strong>Remove from heat sources.</strong> Move the device to a cool, dry, "
            "well-ventilated area away from flammable materials.</li>"
            "<li><strong>Do not place in a sealed container</strong> unless it is a dedicated "
            "lithium fire containment bag. A sealed bag can intensify pressure buildup.</li>"
            "<li><strong>Monitor the device</strong> for increasing heat, hissing sounds, or "
            "visible smoke — these indicate imminent failure. Evacuate the area if observed.</li>"
            "<li><strong>Do NOT dispose of in regular trash or recycling bins.</strong> Lithium "
            "batteries are hazardous waste.</li>"
            "<li><strong>Proper disposal:</strong> Take the battery to a certified e-waste recycler, "
            "a retailer with battery drop-off (e.g., Best Buy, Staples, Home Depot), or a municipal "
            "hazardous waste facility. Call2Recycle is a recognized U.S. program.</li>"
            "</ol>"
            "<p><strong>If the battery is already venting (hissing/smoking):</strong> Evacuate the "
            "immediate area, call emergency services if fire occurs, and use a Class D or dry-sand "
            "extinguisher — standard CO₂ or ABC extinguishers are not effective on lithium fires.</p>"
            "<p><strong>Prevention:</strong> Use only manufacturer-approved chargers, avoid "
            "overnight charging in hot environments, and replace batteries that are 2–3 years "
            "old or showing reduced capacity.</p>"
        ),
        "key_points": [
            "Stop using and power off the device immediately when a swollen battery is detected.",
            "Never puncture, bend, or apply pressure — this can trigger dangerous thermal runaway.",
            "Do not charge a swollen battery; charging accelerates gas production and rupture risk.",
            "Move the device to a cool, ventilated area away from flammable materials.",
            "Dispose of lithium batteries only at certified e-waste or hazardous waste facilities — never in regular trash.",
            "Venting (hissing/smoke) indicates imminent failure — evacuate and use Class D extinguisher if fire erupts.",
        ],
    },
]

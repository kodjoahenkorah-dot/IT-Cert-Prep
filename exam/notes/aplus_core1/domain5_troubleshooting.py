"""
CompTIA A+ Core 1 (220-1201) — Domain 5: Hardware and Network Troubleshooting
Original study notes. Not copied from any copyrighted source.
Follows Professor Messer's playlist order.
"""

NOTES = [
    {
        "domain": 5,
        "topic": "Troubleshooting methodology",
        "objective": "5.1",
        "video": "How to Troubleshoot",
        "study_topics": ["Troubleshooting methodology"],
        "body": (
            "<p>CompTIA defines a structured six-step troubleshooting process that applies to "
            "every hardware and software problem you encounter as a technician.</p>"
            "<ol>"
            "<li><strong>Identify the problem</strong> — Gather information from the user "
            "(what changed, when it started, any error messages). Question without leading "
            "the witness. Check system event logs and reproduce the issue if possible.</li>"
            "<li><strong>Establish a theory of probable cause</strong> — Consider the "
            "obvious first (question the obvious). Use divide-and-conquer or top-down / "
            "bottom-up approaches. List multiple hypotheses from most to least likely.</li>"
            "<li><strong>Test the theory to determine the cause</strong> — Confirm or deny "
            "each hypothesis systematically. If a theory is confirmed, move to step 4. "
            "If denied, establish a new theory or escalate.</li>"
            "<li><strong>Establish a plan of action and implement the solution</strong> — "
            "Consider the impact on the rest of the system. Back up data before making "
            "changes. Execute the fix methodically, one change at a time.</li>"
            "<li><strong>Verify full system functionality and implement preventive "
            "measures</strong> — Confirm the original symptom is gone and no new issues "
            "were introduced. Apply updates, reconfigure settings, or adjust procedures "
            "to prevent recurrence.</li>"
            "<li><strong>Document findings, actions, and outcomes</strong> — Record what "
            "was wrong, what was done, and the final result. Good documentation builds a "
            "knowledge base for future issues and satisfies change-management requirements.</li>"
            "</ol>"
            "<p>Always consider corporate policies, procedures, and impacts before "
            "implementing a solution, especially in enterprise environments.</p>"
        ),
        "key_points": [
            "Step order: Identify → Theory → Test → Plan/Implement → Verify/Prevent → Document",
            "Question the obvious first — simple causes are most common",
            "Change only one variable at a time when testing",
            "Escalate if you cannot determine the cause after exhausting theories",
            "Documentation in step 6 is mandatory, not optional",
        ],
    },
    {
        "domain": 5,
        "topic": "Motherboard, CPU, RAM, and power troubleshooting",
        "objective": "5.3",
        "video": "Troubleshooting Motherboards, CPUs, RAM, and Power",
        "study_topics": ["Motherboard/CPU/RAM/power issues"],
        "body": (
            "<p>Hardware component failures often produce overlapping symptoms; systematic "
            "isolation is essential.</p>"
            "<h3>Power Supply</h3>"
            "<ul>"
            "<li>No POST, no fans: check power cable, outlet, and PSU switch; use a PSU "
            "tester or swap with known-good unit.</li>"
            "<li>Random shutdowns or reboots: overheating (check fan/thermal paste) or "
            "failing PSU unable to sustain load.</li>"
            "<li>Burning smell / visible burn marks: replace PSU immediately — do not "
            "power on again.</li>"
            "<li>Excessive noise: failing PSU fan or coil whine; schedule replacement.</li>"
            "</ul>"
            "<h3>Motherboard</h3>"
            "<ul>"
            "<li>Wrong date/time after every reboot: CMOS/RTC battery is dead — replace "
            "the CR2032 coin cell.</li>"
            "<li>POST beep codes: consult motherboard manual; common patterns — 1 long + "
            "2 short = video error, repeating short beeps = RAM/power issue.</li>"
            "<li>BIOS reset needed: use clear-CMOS jumper or remove CMOS battery for "
            "30 seconds.</li>"
            "<li>Capacitor bulge or leakage on the board: replace the motherboard.</li>"
            "</ul>"
            "<h3>CPU</h3>"
            "<ul>"
            "<li>Overheating / thermal shutdown: reapply thermal paste, reseat heatsink, "
            "verify fan speed in BIOS.</li>"
            "<li>System runs but is unstable: check CPU voltage and multiplier settings "
            "in BIOS; overclock instability.</li>"
            "<li>CPU not recognized: verify socket compatibility and BIOS version supports "
            "the processor.</li>"
            "</ul>"
            "<h3>RAM</h3>"
            "<ul>"
            "<li>Blue Screen of Death (BSOD) with memory errors: run Windows Memory "
            "Diagnostic or MemTest86; reseat DIMMs.</li>"
            "<li>System won't POST with RAM installed: try one stick at a time; check "
            "supported speeds and slots in manual.</li>"
            "<li>Intermittent crashes: possible bad RAM slot — swap to different slots.</li>"
            "<li>Insufficient RAM for OS: upgrade or close background processes.</li>"
            "</ul>"
        ),
        "key_points": [
            "Wrong date/time after reboot = dead CMOS battery (CR2032)",
            "Repeated BSODs with 0x0000007A or similar = RAM failure; run MemTest86",
            "Random shutdowns under load = PSU failing or CPU overheating",
            "POST beep codes are board-specific — always consult the manual",
            "Bulging capacitors on the motherboard require board replacement",
            "No POST with all components: isolate by removing non-essential hardware",
        ],
    },
    {
        "domain": 5,
        "topic": "Storage and RAID troubleshooting",
        "objective": "5.3",
        "video": "Troubleshooting Hard Drives and RAID Arrays",
        "study_topics": ["Storage & RAID troubleshooting"],
        "body": (
            "<p>Storage failures range from gradual performance degradation to sudden "
            "complete failure. Early detection with diagnostics prevents data loss.</p>"
            "<h3>Hard Drive Symptoms</h3>"
            "<ul>"
            "<li><strong>SMART failure warning</strong>: Self-Monitoring, Analysis and "
            "Reporting Technology has detected the drive is near end of life — back up "
            "immediately and replace the drive.</li>"
            "<li>Clicking or grinding sounds (click of death): mechanical HDD head crash "
            "imminent — power off, do not attempt software repair.</li>"
            "<li>Slow read/write performance: fragmentation (HDD), bad sectors, or "
            "controller issues.</li>"
            "<li>Drive not detected in BIOS: check SATA/power cable, try different port, "
            "verify BIOS storage controller mode (AHCI vs IDE).</li>"
            "<li>OS not found / MBR corruption: run bootrec /fixmbr or bootrec /fixboot "
            "from Windows Recovery Environment.</li>"
            "</ul>"
            "<h3>SSD-Specific Issues</h3>"
            "<ul>"
            "<li>Performance degrades over time: TRIM not running; verify TRIM is enabled "
            "(fsutil behavior query DisableDeleteNotify).</li>"
            "<li>Drive disappears intermittently: power delivery or PCIe/M.2 slot issue.</li>"
            "<li>Sudden death: SSDs can fail without audible warning — regular backups are "
            "critical.</li>"
            "</ul>"
            "<h3>RAID Troubleshooting</h3>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>RAID Level</th><th>Drives</th><th>Fault Tolerance</th><th>Symptom on Failure</th></tr>"
            "<tr><td>RAID 0</td><td>2+</td><td>None</td><td>One drive fails = total data loss</td></tr>"
            "<tr><td>RAID 1</td><td>2</td><td>1 drive</td><td>Degraded mode; replace failed drive, allow rebuild</td></tr>"
            "<tr><td>RAID 5</td><td>3+</td><td>1 drive</td><td>Degraded on 1 failure; 2 failures = data loss</td></tr>"
            "<tr><td>RAID 10</td><td>4+</td><td>1 per mirror pair</td><td>Degraded; rebuild after replacement</td></tr>"
            "</table>"
            "<p>A degraded RAID array still functions but has no redundancy — replace the "
            "failed drive promptly. Never pull a second drive while a rebuild is in "
            "progress (especially RAID 5).</p>"
        ),
        "key_points": [
            "SMART failure = drive is predicting its own failure; back up and replace immediately",
            "Clicking/grinding on HDD = imminent head crash; power off immediately",
            "RAID 0 has zero fault tolerance — one drive failure loses everything",
            "RAID 5 tolerates one drive failure; a second failure during rebuild causes total loss",
            "SSD performance issues: verify TRIM is enabled",
            "OS not found after update: bootrec /fixmbr and bootrec /fixboot from WinRE",
        ],
    },
    {
        "domain": 5,
        "topic": "Display and projector troubleshooting",
        "objective": "5.4",
        "video": "Troubleshooting Video and Display Issues",
        "study_topics": ["Display & projector issues"],
        "body": (
            "<p>Display problems can originate from the GPU, cable, display panel, "
            "backlight, or OS driver. Isolating the layer is key.</p>"
            "<h3>Common Display Symptoms</h3>"
            "<ul>"
            "<li><strong>No image, power LED on</strong>: check cable connection and input "
            "source selection. Test with a known-good cable or monitor.</li>"
            "<li><strong>Dim image / backlight off</strong>: LCD backlight failure or "
            "inverter (older CCFL displays). Shine a flashlight — if you can faintly see "
            "the image, backlight/inverter has failed.</li>"
            "<li><strong>Dead pixels</strong>: permanently dark dots on LCD; manufacturer "
            "policies vary (typically 5+ dead pixels = warranty replacement).</li>"
            "<li><strong>Incorrect colors / color cast</strong>: adjust color profile in "
            "display settings or run built-in monitor calibration.</li>"
            "<li><strong>Flickering</strong>: loose cable, failing backlight, or refresh "
            "rate mismatch — verify refresh rate in display settings.</li>"
            "<li><strong>Image burn-in / persistence</strong>: common on OLED and older "
            "CRTs; use screen savers or enable auto-off.</li>"
            "<li><strong>Distorted geometry / stretched image</strong>: resolution or "
            "aspect ratio set incorrectly.</li>"
            "<li><strong>Overscan</strong>: image extends past screen edges — common with "
            "HDMI to TV; disable overscan in TV settings.</li>"
            "</ul>"
            "<h3>Projector-Specific Issues</h3>"
            "<ul>"
            "<li>No image but lamp LED lit: verify input source and cable; check if lamp "
            "has reached end-of-life hour rating.</li>"
            "<li>Dim or color-shifted image: lamp nearing end of life — replace lamp.</li>"
            "<li>Overheating / shutdown: blocked vents or dirty filter; clean filter and "
            "ensure adequate ventilation.</li>"
            "<li>Keystone distortion: projector is not perpendicular to screen — adjust "
            "keystone correction in menu or reposition unit.</li>"
            "</ul>"
            "<h3>GPU / Driver Issues</h3>"
            "<ul>"
            "<li>Artifacting (random pixels/shapes): GPU overheating or failing VRAM.</li>"
            "<li>Driver crash (TDR error): update or roll back GPU driver.</li>"
            "</ul>"
        ),
        "key_points": [
            "Dim image with faint visible content = backlight/inverter failure, not GPU",
            "Dead pixels: check manufacturer minimum pixel policy for warranty replacement",
            "Flickering can indicate loose cable, failing backlight, or wrong refresh rate",
            "Projector overheating: clean air filter and ensure ventilation clearance",
            "Artifacting on screen = GPU overheating or VRAM failure",
            "Keystone distortion on projector: adjust angle or use keystone correction",
        ],
    },
    {
        "domain": 5,
        "topic": "Mobile device troubleshooting",
        "objective": "5.5",
        "video": "Troubleshooting Mobile Devices",
        "study_topics": ["Mobile device issues"],
        "body": (
            "<p>Mobile devices present unique challenges because they combine hardware "
            "and software tightly and are difficult to disassemble.</p>"
            "<h3>Battery and Power</h3>"
            "<ul>"
            "<li><strong>Swollen/bulging battery</strong>: a lithium battery that is "
            "swelling is a fire/explosion hazard — stop using the device immediately, "
            "do not charge it, and dispose of it properly at an approved recycling "
            "facility. Never puncture.</li>"
            "<li>Short battery life: check battery health in settings, disable background "
            "app refresh, location services, and push email to extend life.</li>"
            "<li>Device won't charge: inspect charging port for debris, try a different "
            "cable and adapter, test wireless charging if supported.</li>"
            "</ul>"
            "<h3>Display Issues</h3>"
            "<ul>"
            "<li>Cracked screen: digitizer damage may cause unresponsive touch areas — "
            "screen assembly replacement required.</li>"
            "<li>Dim screen: auto-brightness miscalibration or failing backlight; "
            "check ambient light sensor.</li>"
            "<li>Touchscreen unresponsive: remove screen protector, dry hands, hard "
            "reset (hold power + volume). If hardware, digitizer replacement needed.</li>"
            "</ul>"
            "<h3>Connectivity</h3>"
            "<ul>"
            "<li>Wi-Fi drops: forget and reconnect network, reset network settings, "
            "check for interference (2.4 GHz vs 5 GHz).</li>"
            "<li>Bluetooth not pairing: ensure both devices are in pairing mode, "
            "remove old pairings, reboot both devices.</li>"
            "<li>No cellular signal: toggle airplane mode on/off, check carrier settings "
            "update, reseat SIM card.</li>"
            "</ul>"
            "<h3>Performance and Other</h3>"
            "<ul>"
            "<li>Overheating: remove case, avoid direct sunlight, close background apps; "
            "persistent overheating may indicate failing battery.</li>"
            "<li>App crashes: update app, clear cache/data, reinstall app.</li>"
            "<li>Liquid damage indicator (LDI): small sticker inside SIM tray turns red "
            "when wet — voids warranty; do not power on a wet device.</li>"
            "</ul>"
        ),
        "key_points": [
            "Swollen battery = immediate stop-use, fire hazard; do not charge or puncture",
            "Touchscreen unresponsive: try hard reset before assuming hardware failure",
            "No cellular: toggle airplane mode, reseat SIM, check carrier settings update",
            "Liquid damage indicator (LDI) turns red when device is exposed to moisture",
            "Short battery life: disable location, background refresh, and push notifications",
            "Overheating mobile device can signal a failing/swelling battery",
        ],
    },
    {
        "domain": 5,
        "topic": "Printer troubleshooting and printer-type-specific symptoms",
        "objective": "5.7",
        "video": "Troubleshooting Printers",
        "study_topics": ["Printer troubleshooting", "Printer symptoms — categorize by printer type causing the symptom"],
        "body": (
            "<p>Printer problems often point directly to the printer type. Mapping symptoms "
            "to printer technology narrows the cause quickly.</p>"
            "<h3>General Printer Troubleshooting</h3>"
            "<ul>"
            "<li>No output: verify printer is online (not paused), check print queue for "
            "stuck jobs, restart Print Spooler service (services.msc).</li>"
            "<li>Garbled / incorrect output: wrong or corrupted driver — reinstall correct "
            "driver from manufacturer's site.</li>"
            "<li>Print spooler error: clear spool folder "
            "(C:\\Windows\\System32\\spool\\PRINTERS), restart spooler service.</li>"
            "<li>Out of paper / paper jam: clear jammed paper following manufacturer path, "
            "fan paper before loading, verify correct paper size in tray settings.</li>"
            "</ul>"
            "<h3>Laser Printer Symptoms</h3>"
            "<ul>"
            "<li><strong>Vertical lines on page</strong>: scratched or worn imaging drum — "
            "replace drum unit or toner cartridge containing the drum.</li>"
            "<li><strong>Ghosting (faint duplicate image)</strong>: worn drum or failing "
            "cleaning blade not clearing residual toner — replace drum/cleaning assembly.</li>"
            "<li><strong>Faded or light print</strong>: toner low or density setting too "
            "light; shake toner cartridge as temporary fix.</li>"
            "<li><strong>Toner smearing / not fused</strong>: failing fuser assembly not "
            "reaching proper heat — replace fuser.</li>"
            "<li><strong>Horizontal white lines</strong>: toner starvation or clogged "
            "developer roller.</li>"
            "<li><strong>Paper not feeding</strong>: worn pickup/separation rollers — "
            "clean with IPA or replace rollers.</li>"
            "</ul>"
            "<h3>Inkjet Printer Symptoms</h3>"
            "<ul>"
            "<li><strong>Streaks or missing colors</strong>: clogged print head — run "
            "print head cleaning utility; print a test page.</li>"
            "<li><strong>Colors incorrect / ink smearing</strong>: wrong paper type, "
            "incompatible ink, or head alignment needed — run alignment tool.</li>"
            "<li><strong>Print head hitting paper</strong>: paper thickness setting "
            "incorrect or warped paper.</li>"
            "</ul>"
            "<h3>Thermal Printer Symptoms</h3>"
            "<ul>"
            "<li><strong>Blank output</strong>: paper loaded backwards (thermal-sensitive "
            "side must face the print head).</li>"
            "<li><strong>Faded output</strong>: worn thermal print head or low-quality "
            "thermal paper — replace head or upgrade paper.</li>"
            "<li><strong>Paper jams</strong>: paper roll diameter too large for compartment "
            "or debris in paper path.</li>"
            "</ul>"
            "<h3>Impact / Dot Matrix Symptoms</h3>"
            "<ul>"
            "<li><strong>Faded print</strong>: worn ribbon — replace ribbon cartridge.</li>"
            "<li><strong>Missing dots in characters</strong>: broken print wire(s) in "
            "print head — replace print head.</li>"
            "</ul>"
        ),
        "key_points": [
            "Vertical lines on laser print = scratched drum; replace drum unit",
            "Ghosting on laser print = worn drum or failing cleaning blade",
            "Smearing / unfused toner = failing laser fuser; replace fuser assembly",
            "Blank thermal print = paper loaded backwards (shiny/sensitive side faces head)",
            "Inkjet streaks = clogged print head; run cleaning utility",
            "Stuck print jobs: clear spooler folder and restart Print Spooler service",
            "Faded dot-matrix print = worn ribbon; replace ribbon cartridge",
        ],
    },
    {
        "domain": 5,
        "topic": "Network troubleshooting",
        "objective": "5.2",
        "video": "Troubleshooting Networks",
        "study_topics": ["Network troubleshooting"],
        "body": (
            "<p>Network troubleshooting follows the OSI model from bottom up: physical "
            "layer first, then data link, network, and application.</p>"
            "<h3>Physical Layer Checks</h3>"
            "<ul>"
            "<li>Check link lights on NIC and switch port — no light means no physical "
            "connection (bad cable, wrong port, NIC failure).</li>"
            "<li>Cable tester: verify correct wiring (T568A vs T568B) and continuity; "
            "look for open, short, or crossed pairs.</li>"
            "<li>Maximum cable length for Cat5e/Cat6 Ethernet: 100 m — exceeding this "
            "causes attenuation and packet loss.</li>"
            "</ul>"
            "<h3>Common Network Symptoms and Causes</h3>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Symptom</th><th>Likely Cause</th><th>Fix</th></tr>"
            "<tr><td>169.254.x.x IP address (APIPA)</td><td>DHCP server unreachable</td>"
            "<td>Check DHCP server, NIC, and cable; run ipconfig /release and /renew</td></tr>"
            "<tr><td>Limited/no connectivity</td><td>IP conflict or wrong subnet</td>"
            "<td>Run ipconfig; check for duplicate IPs; verify default gateway</td></tr>"
            "<tr><td>Intermittent connectivity</td><td>Loose cable, failing NIC, or "
            "half-duplex mismatch</td><td>Check cable, set duplex/speed to auto or match</td></tr>"
            "<tr><td>Slow network performance</td><td>Duplex mismatch, congestion, "
            "or high utilization</td><td>Check switch port stats, verify duplex settings</td></tr>"
            "<tr><td>Cannot reach specific host</td><td>DNS failure or routing issue</td>"
            "<td>Ping by IP; if works, DNS problem; use nslookup</td></tr>"
            "<tr><td>Wi-Fi weak signal</td><td>Distance, interference, or wrong channel</td>"
            "<td>Move closer, change channel (1/6/11 for 2.4 GHz), upgrade antenna</td></tr>"
            "</table>"
            "<h3>APIPA and IP Addressing</h3>"
            "<ul>"
            "<li>169.254.x.x = Automatic Private IP Addressing; assigned when DHCP fails.</li>"
            "<li>Always verify: IP address, subnet mask, default gateway, and DNS servers.</li>"
            "</ul>"
            "<h3>Wireless Troubleshooting</h3>"
            "<ul>"
            "<li>Interference sources: microwave ovens, cordless phones, neighboring APs "
            "(2.4 GHz band). Switch to 5 GHz for less congestion.</li>"
            "<li>Wrong SSID or security key: verify SSID case-sensitivity and passphrase.</li>"
            "<li>MAC filtering: ensure client MAC is in the allowed list.</li>"
            "</ul>"
        ),
        "key_points": [
            "169.254.x.x (APIPA) means DHCP server is not responding",
            "Start troubleshooting at physical layer: link lights, cables, connectors",
            "Max Ethernet cable run is 100 m for Cat5e/Cat6",
            "Can ping by IP but not hostname = DNS failure; use nslookup to confirm",
            "Duplex mismatch causes slow/intermittent connectivity — set both sides to auto",
            "2.4 GHz non-overlapping channels: 1, 6, and 11",
        ],
    },
    {
        "domain": 5,
        "topic": "Network command-line tools",
        "objective": "5.2",
        "video": "Network Troubleshooting Tools",
        "study_topics": ["Network command-line tools"],
        "body": (
            "<p>Command-line tools are essential for diagnosing network issues quickly "
            "without a GUI. Know the purpose and key output of each tool.</p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Command</th><th>Platform</th><th>Purpose</th><th>Key Usage / Notes</th></tr>"
            "<tr><td><code>ping</code></td><td>All</td>"
            "<td>Tests ICMP connectivity to a host</td>"
            "<td>ping 8.8.8.8 — success = IP reachable; "
            "ping hostname — success = DNS working. "
            "Request timed out = host unreachable or ICMP blocked.</td></tr>"
            "<tr><td><code>ipconfig</code> / <code>ifconfig</code></td>"
            "<td>Windows / Linux-macOS</td>"
            "<td>Displays NIC IP configuration</td>"
            "<td>ipconfig /all — shows MAC, DHCP server, DNS. "
            "ipconfig /release + /renew — forces new DHCP lease. "
            "ipconfig /flushdns — clears DNS resolver cache.</td></tr>"
            "<tr><td><code>tracert</code> / <code>traceroute</code></td>"
            "<td>Windows / Linux</td>"
            "<td>Shows hop-by-hop path to destination</td>"
            "<td>Identifies where packets are being dropped or delayed. "
            "High latency at a specific hop indicates a congested or failing router.</td></tr>"
            "<tr><td><code>nslookup</code></td><td>All</td>"
            "<td>Queries DNS servers to resolve names/IPs</td>"
            "<td>nslookup google.com — returns IP. "
            "Can specify alternate DNS server: nslookup google.com 8.8.8.8. "
            "Used to verify DNS resolution vs connectivity.</td></tr>"
            "<tr><td><code>netstat</code></td><td>All</td>"
            "<td>Displays active connections and listening ports</td>"
            "<td>netstat -an — all connections with port numbers. "
            "netstat -b (Windows) — shows executable using each port. "
            "Useful for identifying rogue processes or open ports.</td></tr>"
            "<tr><td><code>net use</code></td><td>Windows</td>"
            "<td>Maps / disconnects network drives and printers</td>"
            "<td>net use Z: \\\\server\\share — maps share to drive Z. "
            "net use * /delete — disconnects all mapped drives. "
            "net use with no arguments — lists current connections.</td></tr>"
            "</table>"
            "<h3>Quick Diagnostic Sequence</h3>"
            "<ol>"
            "<li>ping 127.0.0.1 — tests local TCP/IP stack.</li>"
            "<li>ping &lt;default gateway&gt; — tests local network.</li>"
            "<li>ping 8.8.8.8 — tests internet routing (bypasses DNS).</li>"
            "<li>ping google.com — tests DNS resolution.</li>"
            "<li>tracert google.com — identify where routing fails.</li>"
            "<li>nslookup — confirm DNS server is answering correctly.</li>"
            "</ol>"
        ),
        "key_points": [
            "ping 127.0.0.1 tests the local TCP/IP stack — always start here",
            "ipconfig /release and /renew forces a new DHCP lease",
            "ipconfig /flushdns clears stale DNS cache entries",
            "tracert reveals which hop introduces latency or packet loss",
            "nslookup can test an alternate DNS server to rule out server-specific failure",
            "netstat -an shows all open ports and connections; useful for security checks",
            "net use maps Windows network drives from the command line",
        ],
    },
    {
        "domain": 5,
        "topic": "Safe RAM installation procedure",
        "objective": "5.3",
        "video": "Troubleshooting Motherboards, CPUs, RAM, and Power",
        "study_topics": ["Safe RAM installation procedure — correct sequence including ESD precautions"],
        "body": (
            "<p>Improper RAM handling is a leading cause of ESD damage and installation "
            "failures. Follow this exact sequence every time.</p>"
            "<h3>Step-by-Step RAM Installation</h3>"
            "<ol>"
            "<li><strong>Power down completely</strong> — shut down the OS, then flip the "
            "PSU rocker switch to OFF (or unplug the power cord). Pressing the power button "
            "alone is not sufficient — standby voltage is still present.</li>"
            "<li><strong>Ground yourself (ESD precautions)</strong> — put on an antistatic "
            "wrist strap and clip it to a bare metal part of the chassis. If no strap is "
            "available, touch the chassis periodically. Never work on carpet without ESD "
            "protection. Use an antistatic mat if available.</li>"
            "<li><strong>Remove the side panel and locate DIMM slots</strong> — consult "
            "the motherboard manual to identify the correct slots for single-channel vs "
            "dual-channel installation (often slots A2 and B2 for dual-channel).</li>"
            "<li><strong>Handle the RAM module by the edges only</strong> — do not touch "
            "the gold edge connector or chips. Hold the module along its sides.</li>"
            "<li><strong>Open the retention clips</strong> — press both end clips (or one "
            "clip on newer boards) outward until they click open.</li>"
            "<li><strong>Align the notch</strong> — DDR4 and DDR5 modules have a key notch "
            "that prevents backwards insertion. Align the module's notch with the slot key.</li>"
            "<li><strong>Seat the module</strong> — place the module into the slot at a "
            "90-degree angle (straight down). Apply firm, even pressure on both ends until "
            "the retention clips snap closed. You should hear/feel two clicks.</li>"
            "<li><strong>Verify seating</strong> — both clips should be fully engaged. "
            "Gently tug the module to confirm it is locked.</li>"
            "<li><strong>Reassemble and power on</strong> — replace the side panel, "
            "reconnect power, and power on. Enter BIOS to confirm the system detects the "
            "correct total RAM and speed.</li>"
            "<li><strong>Validate with diagnostics</strong> — run Windows Memory Diagnostic "
            "or MemTest86 to verify the new RAM is stable before returning the system "
            "to production.</li>"
            "</ol>"
            "<h3>ESD Key Facts</h3>"
            "<ul>"
            "<li>ESD (Electrostatic Discharge) can destroy components with as little as "
            "100 V — imperceptible to humans (humans feel ~3,000 V).</li>"
            "<li>Always store unused RAM in antistatic bags.</li>"
            "<li>Never work on a powered or plugged-in system.</li>"
            "<li>Wrist strap must contact bare skin for proper grounding.</li>"
            "</ul>"
        ),
        "key_points": [
            "Power off AND disconnect from AC (or flip PSU switch) before handling RAM",
            "Wear ESD wrist strap clipped to bare metal chassis throughout the procedure",
            "Handle modules by edges only — never touch the gold contacts or chips",
            "Align notch before inserting; DDR4 and DDR5 are keyed to prevent reversal",
            "Press straight down evenly until both retention clips snap closed (two clicks)",
            "Verify in BIOS after powering on that RAM capacity and speed are correct",
            "Run MemTest86 to validate stability of newly installed RAM",
        ],
    },
]

"""
CompTIA A+ Core 2 (220-1202) — Domain 3: Software Troubleshooting
Study notes following Professor Messer's 220-1202 playlist order.
"""

NOTES = [
    {
        "domain": 3,
        "topic": "Windows OS troubleshooting",
        "objective": "3.1",
        "video": "Troubleshooting Windows",
        "study_topics": ["Windows OS troubleshooting"],
        "body": (
            "<p>Windows OS problems fall into several symptom categories, each with "
            "matching diagnostic tools:</p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Symptom</th><th>Common Causes</th><th>Tools / Remedies</th></tr>"
            "<tr><td>Blue Screen of Death (BSOD / Stop Error)</td>"
            "<td>Bad driver, RAM failure, corrupt system file</td>"
            "<td>Check stop code, update/roll back driver, run <code>sfc /scannow</code>, "
            "memory diagnostics (mdsched.exe)</td></tr>"
            "<tr><td>Sluggish / low performance</td>"
            "<td>High CPU/RAM, disk fragmentation, malware, startup bloat</td>"
            "<td>Task Manager, Resource Monitor, msconfig (selective startup), "
            "Disk Cleanup, Defragment &amp; Optimize Drives</td></tr>"
            "<tr><td>Application crashes / won't start</td>"
            "<td>Corrupt install, missing DLL, incompatible version</td>"
            "<td>Event Viewer (Application log), reinstall, compatibility mode</td></tr>"
            "<tr><td>Services not starting</td>"
            "<td>Dependency failure, corrupt binary, wrong account</td>"
            "<td>services.msc, Event Viewer (System log), <code>sfc /scannow</code>, "
            "<code>DISM /Online /Cleanup-Image /RestoreHealth</code></td></tr>"
            "<tr><td>User profile issues (corrupt profile)</td>"
            "<td>Profile database corruption, permission errors</td>"
            "<td>Create new local admin account, copy profile data, rebuild profile</td></tr>"
            "<tr><td>Missing DLL / side-by-side errors</td>"
            "<td>Uninstalled dependency, registry damage</td>"
            "<td>Reinstall app, run SFC, check Windows Event Log</td></tr>"
            "</table>"
            "<p><strong>Key utilities:</strong> <code>sfc /scannow</code> — repairs protected "
            "system files; <code>DISM</code> — repairs the Windows image itself; "
            "<strong>Safe Mode</strong> — loads minimal drivers to isolate third-party conflicts; "
            "<strong>msconfig</strong> — controls startup services and boot options; "
            "<strong>System Restore</strong> — rolls back system state to a known-good restore point "
            "without affecting personal files.</p>"
        ),
        "key_points": [
            "BSOD stop codes identify the failing component; always note the code before rebooting.",
            "SFC repairs individual protected files; DISM repairs the Windows image source SFC uses.",
            "Safe Mode loads only essential Microsoft drivers — use it to isolate third-party driver conflicts.",
            "msconfig selective startup disables all non-Microsoft services and startup items for diagnostics.",
            "Corrupt user profiles are rebuilt by creating a new account and copying AppData content.",
            "Event Viewer (System and Application logs) is the first place to look for service-start failures.",
        ],
    },
    {
        "domain": 3,
        "topic": "Windows boot troubleshooting",
        "objective": "3.1",
        "video": "Troubleshooting Windows",
        "study_topics": ["Windows boot troubleshooting"],
        "body": (
            "<p>Boot failures occur before Windows fully loads and require different tools than "
            "in-OS troubleshooting.</p>"
            "<h4>Common symptoms and causes</h4>"
            "<ul>"
            "<li><strong>No OS found / 'Operating system not found'</strong> — incorrect BIOS/UEFI "
            "boot order, disconnected or failed drive, corrupted Master Boot Record (MBR) or "
            "GUID Partition Table (GPT).</li>"
            "<li><strong>Startup repair loop</strong> — corrupt BCD (Boot Configuration Data), "
            "missing boot manager file (bootmgr), or failed Windows update.</li>"
            "<li><strong>Windows stops at splash screen</strong> — driver conflict, corrupt system "
            "hive, or hardware issue.</li>"
            "<li><strong>Black screen after POST</strong> — no active partition, corrupt VBR "
            "(Volume Boot Record).</li>"
            "</ul>"
            "<h4>Diagnostic and repair tools</h4>"
            "<ul>"
            "<li><strong>BIOS/UEFI boot order</strong> — verify the correct drive is listed first; "
            "check Secure Boot settings on UEFI systems.</li>"
            "<li><strong>Windows Recovery Environment (WinRE)</strong> — accessed via install media "
            "or F8/Shift+F8; provides Startup Repair, System Restore, and command prompt.</li>"
            "<li><strong>Startup Repair</strong> — automated tool inside WinRE that scans and fixes "
            "common boot problems.</li>"
            "<li><strong>bootrec.exe</strong> — command-line tool with key switches: "
            "<code>/fixmbr</code> (rewrite MBR), <code>/fixboot</code> (rewrite VBR), "
            "<code>/rebuildbcd</code> (scan all drives and rebuild BCD store).</li>"
            "<li><strong>bcdedit</strong> — manually view or edit BCD entries; useful when "
            "bootrec cannot auto-detect an OS.</li>"
            "<li><strong>diskpart</strong> — mark partition active, fix drive letter assignments, "
            "or identify GPT vs. MBR layout.</li>"
            "</ul>"
            "<p>Always check the simplest cause first — verify boot order in firmware before "
            "attempting MBR repair.</p>"
        ),
        "key_points": [
            "Verify BIOS/UEFI boot order before any software repair — a mis-ordered device is the most common cause of 'no OS found'.",
            "bootrec /fixmbr rewrites the MBR code; /fixboot rewrites the volume boot record; /rebuildbcd scans for Windows installations.",
            "WinRE (Windows Recovery Environment) is the starting point for all boot repairs — launch from installation media if unavailable on disk.",
            "Startup Repair is automated; use bootrec/bcdedit manually when it fails.",
            "Secure Boot (UEFI) will block boot from unsigned media — may need to temporarily disable it for third-party repair tools.",
            "diskpart can mark a partition active on MBR disks, which is required for the VBR to be loaded.",
        ],
    },
    {
        "domain": 3,
        "topic": "PC security issue troubleshooting",
        "objective": "3.2",
        "video": "Troubleshooting Security Issues",
        "study_topics": ["PC security issue troubleshooting"],
        "body": (
            "<p>Security-related symptoms on a PC often indicate malware infection, unauthorized "
            "access, or misconfigured security settings.</p>"
            "<h4>Common security symptoms</h4>"
            "<ul>"
            "<li><strong>Antivirus disabled / won't update</strong> — malware frequently targets "
            "security software to prevent detection; check Task Manager for unknown processes.</li>"
            "<li><strong>Unwanted programs / toolbars installed</strong> — potentially unwanted "
            "programs (PUPs) bundled with freeware; remove via Programs and Features or third-party "
            "removal tools.</li>"
            "<li><strong>Unauthorized account activity</strong> — password changes, new accounts "
            "created, or failed login alerts may indicate a compromised credential or insider threat.</li>"
            "<li><strong>File encryption / ransom note</strong> — classic ransomware indicator; "
            "isolate immediately to prevent spread.</li>"
            "<li><strong>High outbound network traffic</strong> — may indicate a botnet client, "
            "data exfiltration, or cryptominer; review with Resource Monitor or Wireshark.</li>"
            "<li><strong>Missing or modified files</strong> — rootkits hide themselves by "
            "intercepting file system calls; run an offline scan to detect.</li>"
            "<li><strong>Windows Firewall or UAC disabled</strong> — often a sign malware has "
            "made administrative changes.</li>"
            "</ul>"
            "<h4>Diagnostic steps</h4>"
            "<ol>"
            "<li>Inspect running processes in Task Manager; research unknown process names.</li>"
            "<li>Check startup entries via msconfig or Autoruns (Sysinternals).</li>"
            "<li>Review Windows Security Center status and Event Viewer security log.</li>"
            "<li>Run a full scan with updated anti-malware in Safe Mode.</li>"
            "<li>Check user accounts and group memberships for unauthorized additions.</li>"
            "</ol>"
        ),
        "key_points": [
            "Disabled antivirus or security software is a primary indicator of active malware.",
            "Ransomware encrypts user files and demands payment — isolate the system immediately to prevent network spread.",
            "Autoruns (Sysinternals) reveals every auto-start location in Windows, making it more thorough than msconfig for malware hunting.",
            "Unexpected outbound traffic should be correlated with process IDs using Resource Monitor's Network tab.",
            "UAC and Windows Firewall being disabled without user action is a strong sign of administrative-level compromise.",
            "Always check local user accounts and administrators group after suspected breach.",
        ],
    },
    {
        "domain": 3,
        "topic": "Browser security symptoms",
        "objective": "3.2",
        "video": "Troubleshooting Security Issues",
        "study_topics": ["Browser security symptoms"],
        "body": (
            "<p>Browsers are a primary attack surface. Recognizing symptoms helps identify "
            "adware, hijackers, and phishing infrastructure.</p>"
            "<h4>Key symptoms and their meaning</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Symptom</th><th>Likely Cause</th><th>Remediation</th></tr>"
            "<tr><td>Excessive pop-up ads</td>"
            "<td>Adware, malicious browser extension</td>"
            "<td>Remove suspicious extensions, run anti-malware scan, reset browser</td></tr>"
            "<tr><td>Homepage / search engine changed without consent</td>"
            "<td>Browser hijacker</td>"
            "<td>Check browser settings and Group Policy; remove extension or PUP responsible</td></tr>"
            "<tr><td>Redirected to unexpected sites</td>"
            "<td>DNS hijacking, malicious hosts file, browser hijacker</td>"
            "<td>Inspect hosts file (C:\\Windows\\System32\\drivers\\etc\\hosts), check DNS "
            "server settings, scan for malware</td></tr>"
            "<tr><td>Certificate warnings (invalid/expired cert)</td>"
            "<td>Expired server cert, SSL stripping attack, wrong system date/time, "
            "MITM proxy</td>"
            "<td>Verify system clock, check certificate details and issuer, do not proceed "
            "on untrusted networks</td></tr>"
            "<tr><td>Browser crashes frequently</td>"
            "<td>Malicious extension, memory leak, outdated browser</td>"
            "<td>Disable extensions one-by-one, update browser, clear cache</td></tr>"
            "<tr><td>Slow browsing despite fast connection</td>"
            "<td>Resource-hijacking extension (cryptominer), proxy redirect</td>"
            "<td>Check browser extensions, Task Manager for CPU spikes, inspect proxy settings</td></tr>"
            "</table>"
            "<p><strong>Remediation toolkit:</strong> Reset browser to defaults, remove unknown "
            "extensions, clear cache/cookies, check Windows hosts file and DNS settings, "
            "run anti-malware scan. On corporate systems, verify no unauthorized Group Policy "
            "or registry entries are forcing proxy settings.</p>"
        ),
        "key_points": [
            "Browser hijackers change homepage and default search engine by modifying registry keys or Group Policy — not just browser settings.",
            "DNS hijacking redirects all DNS queries to a rogue server; symptoms include redirection even after clearing browser data.",
            "A certificate warning on a site that previously worked is a red flag for a man-in-the-middle attack, especially on public Wi-Fi.",
            "Always check the hosts file (C:\\Windows\\System32\\drivers\\etc\\hosts) for unauthorized entries when redirection occurs.",
            "Cryptomining extensions cause high CPU usage while browsing — visible in Task Manager per-tab in Chromium browsers.",
            "Resetting the browser removes extensions and custom settings but preserves bookmarks — use as a last resort before reinstalling.",
        ],
    },
    {
        "domain": 3,
        "topic": "Malware removal best-practice process",
        "objective": "3.3",
        "video": "Removing Malware",
        "study_topics": ["Malware removal best-practice process"],
        "body": (
            "<p>CompTIA defines a seven-step best-practice process for malware removal. "
            "Follow these steps in order to safely and completely remediate an infection.</p>"
            "<ol>"
            "<li><strong>Investigate and verify malware symptoms</strong> — Confirm that the "
            "observed behavior is actually caused by malware (not hardware failure or user error). "
            "Check antivirus alerts, unexpected processes, and network traffic.</li>"
            "<li><strong>Quarantine the infected system</strong> — Disconnect the machine from the "
            "network (unplug Ethernet, disable Wi-Fi) to prevent the malware from spreading, "
            "receiving C2 commands, or exfiltrating data.</li>"
            "<li><strong>Disable System Restore (Windows)</strong> — System Restore snapshots can "
            "contain copies of malware. Disabling it prevents reinfection from a tainted restore "
            "point and forces creation of a clean snapshot after remediation.</li>"
            "<li><strong>Remediate</strong> — Update anti-malware definitions to the latest "
            "version. Run a full scan in Safe Mode or from a bootable pre-installation environment "
            "(WinPE/live USB) where malware cannot actively defend itself. Remove or quarantine "
            "all detected threats.</li>"
            "<li><strong>Schedule scans and run updates</strong> — After removal, configure "
            "automatic scans on a regular schedule. Apply all pending OS and application patches "
            "to close the vulnerabilities the malware exploited.</li>"
            "<li><strong>Enable System Restore and create a restore point</strong> — Re-enable "
            "System Restore and immediately create a new restore point that reflects the "
            "clean, patched state of the system.</li>"
            "<li><strong>Educate the end user</strong> — Explain how the infection occurred "
            "(phishing email, drive-by download, removable media) and provide guidance on "
            "safe computing practices to reduce the risk of future infection.</li>"
            "</ol>"
            "<p><em>Note:</em> If malware cannot be fully removed (e.g., advanced rootkit or "
            "firmware-level threat), the safest option is to wipe and reimage the system from "
            "a known-good baseline.</p>"
        ),
        "key_points": [
            "Step 1: Investigate and verify — confirm malware is the actual cause before taking action.",
            "Step 2: Quarantine — disconnect from network immediately to stop spread and C2 communication.",
            "Step 3: Disable System Restore — prevents reinfection from snapshots containing malware.",
            "Step 4: Remediate — update definitions, then scan in Safe Mode or pre-installation environment for maximum detection.",
            "Step 5: Schedule scans and run updates — patch the OS and apps to close the exploit pathway.",
            "Step 6: Enable System Restore and create a restore point — capture the clean state.",
            "Step 7: Educate the end user — address the human factor to prevent recurrence.",
        ],
    },
    {
        "domain": 3,
        "topic": "Mobile OS troubleshooting",
        "objective": "3.4",
        "video": "Troubleshooting Mobile Devices",
        "study_topics": ["Mobile OS troubleshooting"],
        "body": (
            "<p>Mobile OS issues span iOS and Android platforms and include connectivity, "
            "performance, and application problems.</p>"
            "<h4>Common symptoms and remediation</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Symptom</th><th>Steps to Resolve</th></tr>"
            "<tr><td>Device runs slowly / unresponsive</td>"
            "<td>Close background apps, restart device, clear app cache (Android: Settings &gt; "
            "Apps), free storage space (rule: keep at least 10–15% free), factory reset as "
            "last resort</td></tr>"
            "<tr><td>Battery drains rapidly</td>"
            "<td>Check battery usage by app, disable location services / background refresh, "
            "reduce screen brightness, check for rogue apps consuming CPU</td></tr>"
            "<tr><td>Wi-Fi / Bluetooth connectivity issues</td>"
            "<td>Toggle airplane mode on/off, forget and rejoin network, reset network settings "
            "(Settings &gt; General &gt; Reset &gt; Reset Network Settings on iOS)</td></tr>"
            "<tr><td>Apps crashing</td>"
            "<td>Force-stop app, clear cache/data, uninstall and reinstall, update app or OS</td></tr>"
            "<tr><td>Device overheating</td>"
            "<td>Remove case, stop charging while using, close intensive apps, check for malware "
            "or background processes consuming CPU</td></tr>"
            "<tr><td>Touchscreen not responding</td>"
            "<td>Clean screen, remove screen protector, restart device, check for OS update; "
            "hardware failure requires repair</td></tr>"
            "<tr><td>OS update failure</td>"
            "<td>Ensure sufficient storage and battery (&gt;50%), connect to Wi-Fi, try update "
            "via iTunes/Finder (iOS) or recovery mode (Android)</td></tr>"
            "</table>"
            "<p><strong>Factory reset</strong> is the nuclear option — it erases all user data "
            "and restores factory defaults. Always back up to iCloud/Google Drive first. "
            "On Android, enable encryption before reset to ensure wiped data cannot be recovered.</p>"
        ),
        "key_points": [
            "Toggling airplane mode resets all radio stacks (Wi-Fi, Bluetooth, cellular) and is a fast first step for connectivity issues.",
            "Clearing app cache (Android) resolves many crash and performance issues without losing user data.",
            "Rapid battery drain combined with high CPU is a common indicator of a malicious or poorly coded background process.",
            "iOS network settings reset (Settings > General > Transfer or Reset > Reset > Reset Network Settings) removes all saved Wi-Fi passwords and VPN configs.",
            "Factory reset should always be preceded by a verified cloud backup.",
            "Insufficient free storage is a leading cause of app crashes and OS update failures on mobile devices.",
        ],
    },
    {
        "domain": 3,
        "topic": "Mobile app security troubleshooting",
        "objective": "3.4",
        "video": "Troubleshooting Mobile Devices",
        "study_topics": ["Mobile app security troubleshooting"],
        "body": (
            "<p>Mobile security threats differ from PC threats due to platform sandboxing, "
            "app store gatekeeping, and unique attack vectors like SMS phishing and rogue apps.</p>"
            "<h4>Security symptoms on mobile devices</h4>"
            "<ul>"
            "<li><strong>Unexpected data usage spikes</strong> — may indicate spyware, adware, "
            "or a botnet client exfiltrating data or sending spam; review per-app data usage "
            "in Settings.</li>"
            "<li><strong>Unauthorized account access / unfamiliar charges</strong> — credential-"
            "stealing malware or SMS-based MFA bypass; immediately change passwords and review "
            "linked payment methods.</li>"
            "<li><strong>Apps requesting excessive permissions</strong> — a flashlight app "
            "requesting contacts and location is a red flag; review and revoke unnecessary "
            "permissions (Settings &gt; Privacy).</li>"
            "<li><strong>Device rooted / jailbroken without user action</strong> — removes OS "
            "security sandboxing; check for root-detection apps or MDM policy alerts.</li>"
            "<li><strong>Fake / rogue security apps</strong> — scareware that displays false "
            "infection warnings to trick users into purchasing fake AV or revealing credentials.</li>"
            "<li><strong>SMS / MMS-based attacks (smishing)</strong> — links in text messages "
            "lead to phishing sites or trigger drive-by downloads; do not tap unsolicited links.</li>"
            "</ul>"
            "<h4>Remediation steps</h4>"
            "<ol>"
            "<li>Uninstall suspicious apps; on Android check for device administrator apps "
            "that resist removal (Settings &gt; Security &gt; Device Admin Apps).</li>"
            "<li>Revoke excessive app permissions immediately.</li>"
            "<li>Run a reputable mobile security scan (only from official app stores).</li>"
            "<li>Update the OS and all apps to patch known vulnerabilities.</li>"
            "<li>If compromise is confirmed, perform a factory reset and restore from a "
            "pre-infection backup, or set up as new device.</li>"
            "<li>Enable MDM/EMM enrollment if corporate — MDM can remotely wipe, enforce "
            "encryption, and restrict sideloading.</li>"
            "</ol>"
            "<p><strong>Sideloading</strong> (installing APKs outside Google Play on Android) "
            "bypasses app store security vetting and significantly raises malware risk. "
            "iOS sideloading outside TestFlight/enterprise profiles requires a jailbreak.</p>"
        ),
        "key_points": [
            "Per-app data usage reporting (built into both iOS and Android) is the fastest way to identify a data-exfiltrating app.",
            "Device administrator apps (Android) can prevent uninstallation — revoke admin rights before attempting removal.",
            "Rooting (Android) or jailbreaking (iOS) removes the OS security sandbox, making all apps on the device equally privileged.",
            "Sideloading apps bypasses app store malware screening — a major risk vector on Android.",
            "MDM/EMM solutions allow remote wipe, certificate deployment, and policy enforcement on corporate mobile devices.",
            "Smishing (SMS phishing) often delivers credential harvesting links disguised as bank or delivery service messages.",
            "Excessive permission requests at install time are a leading indicator of potentially malicious apps.",
        ],
    },
]

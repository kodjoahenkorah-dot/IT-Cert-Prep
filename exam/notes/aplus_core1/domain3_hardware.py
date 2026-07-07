"""
CompTIA A+ Core 1 (220-1201) Domain 3: Hardware
Study notes following Professor Messer's playlist order.
"""

NOTES = [
    {
        "domain": 3,
        "topic": "Peripheral & video cables and connectors",
        "objective": "3.1",
        "video": "Peripheral Cables and Connectors",
        "study_topics": ["Peripheral & video cables", "Video & display connectors"],
        "body": (
            "<p><strong>Peripheral Cables</strong></p>"
            "<ul>"
            "<li><strong>USB:</strong> USB-A (standard host), USB-B (square printer connector), "
            "USB-C (reversible, supports USB 3.2, Thunderbolt 3/4, up to 40 Gbps). "
            "USB 2.0 = 480 Mbps; USB 3.0/3.2 Gen 1 = 5 Gbps; USB 3.2 Gen 2 = 10 Gbps; "
            "USB 3.2 Gen 2x2 = 20 Gbps.</li>"
            "<li><strong>Thunderbolt:</strong> TB1/2 uses Mini DisplayPort connector; TB3/4 uses USB-C. "
            "TB3 = 40 Gbps; TB4 also 40 Gbps with stricter certification.</li>"
            "<li><strong>Serial (DB-9/RS-232):</strong> Legacy COM port for console/UPS connections.</li>"
            "<li><strong>SATA data cable:</strong> 7-pin L-shaped connector; SATA power = 15-pin.</li>"
            "<li><strong>eSATA:</strong> External SATA up to 6 Gbps; no bus power.</li>"
            "</ul>"
            "<p><strong>Video &amp; Display Connectors</strong></p>"
            "<ul>"
            "<li><strong>VGA (DB-15):</strong> Analog, 15-pin, 3 rows. No audio. Max ~2048x1536.</li>"
            "<li><strong>DVI-A:</strong> Analog only; <strong>DVI-D:</strong> Digital only (single or dual link); "
            "<strong>DVI-I:</strong> Integrated (both). Dual-link DVI up to 2560x1600.</li>"
            "<li><strong>HDMI:</strong> Digital audio + video; Type A (19-pin standard), Type C (mini), "
            "Type D (micro). HDMI 2.1 supports 4K/120Hz and 8K/60Hz.</li>"
            "<li><strong>DisplayPort:</strong> DP 1.4 = 32.4 Gbps HBR3; supports daisy-chaining via MST. "
            "Mini DisplayPort physically identical to Thunderbolt 1/2.</li>"
            "<li><strong>HDBaseT:</strong> AV over Cat5e/6 up to 100 m.</li>"
            "</ul>"
        ),
        "key_points": [
            "USB-C is reversible and can carry USB, Thunderbolt, DisplayPort, and power over same cable.",
            "HDMI carries both audio and video; VGA carries only analog video.",
            "DVI-I supports both analog and digital; DVI-D is digital only.",
            "Thunderbolt 3 and 4 use the USB-C connector and operate at 40 Gbps.",
            "eSATA provides external SATA speeds but requires separate power.",
        ],
    },
    {
        "domain": 3,
        "topic": "RAM types and channels",
        "objective": "3.3",
        "video": "An Overview of Memory",
        "study_topics": ["RAM types & channels"],
        "body": (
            "<p><strong>RAM Form Factors</strong></p>"
            "<ul>"
            "<li><strong>DIMM:</strong> 64-bit bus, used in desktops/servers. 288-pin for DDR4/DDR5.</li>"
            "<li><strong>SO-DIMM:</strong> Smaller notebook version. 260-pin (DDR4), 262-pin (DDR5).</li>"
            "</ul>"
            "<p><strong>DDR Generations (Double Data Rate)</strong></p>"
            "<ul>"
            "<li><strong>DDR3:</strong> 1.5 V, up to 2133 MT/s. 240-pin DIMM.</li>"
            "<li><strong>DDR4:</strong> 1.2 V, 2133–3200 MT/s (OC higher). 288-pin DIMM. "
            "Keyed differently from DDR3 — not interchangeable.</li>"
            "<li><strong>DDR5:</strong> 1.1 V, starts at 4800 MT/s; on-module voltage regulation. "
            "288-pin but different key position from DDR4.</li>"
            "<li><strong>LPDDR:</strong> Low-Power DDR, soldered on mobile/ultrabook boards.</li>"
            "</ul>"
            "<p><strong>Channel Configurations</strong></p>"
            "<ul>"
            "<li><strong>Single-channel:</strong> One 64-bit path.</li>"
            "<li><strong>Dual-channel:</strong> Two DIMMs in matching slots (usually color-coded) "
            "doubles theoretical bandwidth to 128-bit.</li>"
            "<li><strong>Quad-channel:</strong> Four matched DIMMs; common in workstation/server platforms.</li>"
            "</ul>"
            "<p><strong>ECC vs Non-ECC</strong></p>"
            "<ul>"
            "<li><strong>ECC (Error-Correcting Code):</strong> Detects and corrects single-bit errors; "
            "requires ECC-capable CPU and motherboard. Used in servers.</li>"
            "<li><strong>Registered/Buffered (RDIMM):</strong> Extra register between controller and DRAM; "
            "allows more DIMMs per channel in servers.</li>"
            "</ul>"
            "<p><strong>Virtual RAM:</strong> Paging file on disk used when physical RAM is exhausted; "
            "much slower than DRAM.</p>"
        ),
        "key_points": [
            "DDR4 uses 288-pin DIMM with a different key than DDR3 (240-pin); not interchangeable.",
            "Dual-channel requires two matched DIMMs installed in the correct (usually color-coded) slots.",
            "ECC RAM detects and corrects single-bit errors; required for servers, not supported by all CPUs.",
            "DDR5 moves voltage regulation onto the DIMM itself (on-module PMIC).",
            "SO-DIMM is the notebook form factor; DDR4 SO-DIMM is 260-pin.",
        ],
    },
    {
        "domain": 3,
        "topic": "Storage devices and form factors",
        "objective": "3.4",
        "video": "Storage Devices",
        "study_topics": [
            "Storage devices & form factors",
            "Storage form factors — desktop vs laptop vs enterprise",
        ],
        "body": (
            "<p><strong>HDD (Hard Disk Drive)</strong></p>"
            "<ul>"
            "<li>Magnetic platters; 5400 RPM (laptop/NAS) or 7200 RPM (desktop); 10K/15K RPM (enterprise SCAS/SAS).</li>"
            "<li>Form factors: <strong>3.5&quot;</strong> (desktop), <strong>2.5&quot;</strong> (laptop, SFF desktop).</li>"
            "<li>Interface: SATA (most common), SAS (enterprise).</li>"
            "</ul>"
            "<p><strong>SSD (Solid State Drive)</strong></p>"
            "<ul>"
            "<li>No moving parts; NAND flash memory.</li>"
            "<li><strong>2.5&quot; SATA SSD:</strong> Drop-in HDD replacement, up to ~550 MB/s.</li>"
            "<li><strong>mSATA:</strong> Mini SATA; legacy small form factor.</li>"
            "<li><strong>M.2:</strong> Compact slot-mounted drive. Key types: "
            "<em>B-key</em> (SATA/PCIe x2), <em>M-key</em> (PCIe x4/NVMe). "
            "Sizes: 2242, 2260, 2280 (most common), 22110.</li>"
            "<li><strong>NVMe (Non-Volatile Memory Express):</strong> PCIe-based protocol; "
            "Gen 3 x4 ~3500 MB/s read; Gen 4 x4 ~7000 MB/s; Gen 5 x4 ~14000 MB/s.</li>"
            "<li><strong>U.2:</strong> Enterprise NVMe in 2.5&quot; chassis.</li>"
            "</ul>"
            "<p><strong>Desktop vs Laptop vs Enterprise</strong></p>"
            "<ul>"
            "<li><strong>Desktop:</strong> 3.5&quot; HDD or 2.5&quot;/M.2 SSD; standard SATA or M.2 slots on ATX boards.</li>"
            "<li><strong>Laptop:</strong> 2.5&quot; SATA or M.2 (2242/2280); power-efficient; limited slots.</li>"
            "<li><strong>Enterprise:</strong> 2.5&quot; SAS/NVMe U.2; hot-swap bays; RAID controllers; "
            "high IOPS NVMe drives (HHHL PCIe AIC cards or U.2).</li>"
            "</ul>"
            "<p><strong>Optical &amp; Flash:</strong> BD/DVD/CD drives (5.25&quot; or slim slot); "
            "USB flash drives; SD cards (full-size, microSD).</p>"
        ),
        "key_points": [
            "M.2 2280 is the most common NVMe SSD size in modern laptops and desktops.",
            "NVMe over PCIe is significantly faster than SATA SSD (~7x on Gen 4 vs SATA).",
            "M-key M.2 slots support PCIe/NVMe; B-key supports SATA or PCIe x2.",
            "Enterprise drives use SAS or NVMe U.2 with hot-swap bays for high availability.",
            "2.5\" is the standard laptop HDD/SSD form factor; 3.5\" is desktop standard.",
        ],
    },
    {
        "domain": 3,
        "topic": "RAID levels",
        "objective": "3.4",
        "video": "RAID",
        "study_topics": ["RAID levels", "RAID levels — characteristics and fault tolerance"],
        "body": (
            "<p>RAID (Redundant Array of Independent Disks) combines multiple drives for performance, "
            "redundancy, or both. Key metrics: <em>fault tolerance</em> (drives that can fail), "
            "<em>minimum drives</em>, and <em>usable capacity</em>.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<thead><tr><th>Level</th><th>Name</th><th>Min Drives</th><th>Fault Tolerance</th>"
            "<th>Usable Space</th><th>Notes</th></tr></thead>"
            "<tbody>"
            "<tr><td>RAID 0</td><td>Striping</td><td>2</td><td>0 (none)</td>"
            "<td>100% of total</td><td>Best performance; no redundancy; one failure = total loss.</td></tr>"
            "<tr><td>RAID 1</td><td>Mirroring</td><td>2</td><td>1 drive</td>"
            "<td>50% of total</td><td>Exact duplicate; read performance boost possible.</td></tr>"
            "<tr><td>RAID 5</td><td>Striping + Parity</td><td>3</td><td>1 drive</td>"
            "<td>(N-1)/N of total</td><td>Parity distributed across all drives; good balance of speed and redundancy.</td></tr>"
            "<tr><td>RAID 6</td><td>Dual Parity</td><td>4</td><td>2 drives</td>"
            "<td>(N-2)/N of total</td><td>Survives two simultaneous drive failures; slower writes than RAID 5.</td></tr>"
            "<tr><td>RAID 10</td><td>Mirror + Stripe</td><td>4</td><td>1 per mirrored pair</td>"
            "<td>50% of total</td><td>Combines RAID 1 pairs then stripes; high performance + redundancy.</td></tr>"
            "</tbody></table>"
            "<p><strong>Controller types:</strong> Hardware RAID (dedicated controller card, best performance), "
            "Software RAID (OS managed, uses CPU), Firmware/Hybrid RAID (motherboard RAID, aka fake RAID).</p>"
            "<p><strong>Hot spare:</strong> An idle drive that automatically replaces a failed drive and begins "
            "rebuilding immediately.</p>"
            "<p><strong>Rebuild time risk:</strong> During RAID 5 rebuild another drive failure causes total data loss; "
            "RAID 6 tolerates a failure even during rebuild.</p>"
        ),
        "key_points": [
            "RAID 0 offers no fault tolerance; a single drive failure loses all data.",
            "RAID 1 mirrors data across 2 drives; 50% usable capacity.",
            "RAID 5 requires at least 3 drives; tolerates 1 drive failure; parity is distributed.",
            "RAID 6 requires at least 4 drives; tolerates 2 simultaneous drive failures.",
            "RAID 10 requires at least 4 drives; combines mirroring and striping; 50% usable space.",
            "A hot spare automatically joins a RAID array when a member drive fails.",
        ],
    },
    {
        "domain": 3,
        "topic": "Motherboard form factors",
        "objective": "3.5",
        "video": "Motherboard Form Factors",
        "study_topics": ["Motherboard form factors"],
        "body": (
            "<p>The motherboard form factor defines physical size, mounting hole positions, "
            "power connector placement, and expansion slot count.</p>"
            "<p><strong>Common Form Factors (largest to smallest)</strong></p>"
            "<ul>"
            "<li><strong>E-ATX (Extended ATX):</strong> 305 &times; 330 mm; workstation/HEDT; "
            "more PCIe slots and RAM slots.</li>"
            "<li><strong>ATX:</strong> 305 &times; 244 mm; standard full-size desktop; "
            "typically 4–7 PCIe slots, 4 RAM slots.</li>"
            "<li><strong>Micro-ATX (mATX):</strong> 244 &times; 244 mm; fits ATX cases; "
            "2–4 PCIe slots, 2–4 RAM slots.</li>"
            "<li><strong>Mini-ITX:</strong> 170 &times; 170 mm; very compact; 1 PCIe x16 slot, "
            "2 RAM slots; low-power builds.</li>"
            "<li><strong>Nano/Pico-ITX:</strong> Even smaller; embedded/IoT applications.</li>"
            "</ul>"
            "<p><strong>Key Motherboard Components</strong></p>"
            "<ul>"
            "<li><strong>CPU socket:</strong> Intel LGA (pins on motherboard); AMD AM5/AM4 (PGA — pins on CPU).</li>"
            "<li><strong>Chipset:</strong> Manages communication between CPU, RAM, PCIe, and I/O; "
            "modern Intel uses a single PCH (Platform Controller Hub).</li>"
            "<li><strong>PCIe slots:</strong> x1, x4, x8, x16; GPU in x16; NVMe/capture cards in x4.</li>"
            "<li><strong>CMOS battery:</strong> CR2032 coin cell maintains RTC and BIOS settings when power is off.</li>"
            "<li><strong>Front panel headers:</strong> Power, reset, HDD LED, speaker pins.</li>"
            "<li><strong>24-pin ATX power + 4/8-pin CPU power connectors.</strong></li>"
            "</ul>"
        ),
        "key_points": [
            "ATX is 305x244 mm; Micro-ATX is 244x244 mm; Mini-ITX is 170x170 mm.",
            "Intel CPUs use LGA sockets (pins on motherboard); AMD uses PGA (pins on CPU) for AM4, LGA for AM5.",
            "PCIe x16 slot is standard for GPUs; x1 for sound/network cards.",
            "CMOS battery (CR2032) keeps system clock and BIOS settings when the PC is unplugged.",
            "Micro-ATX boards fit in ATX cases but not vice versa (larger boards don't fit smaller cases).",
        ],
    },
    {
        "domain": 3,
        "topic": "CPU architecture",
        "objective": "3.6",
        "video": "CPU Architecture",
        "study_topics": ["CPU architecture"],
        "body": (
            "<p><strong>Instruction Set Architectures (ISA)</strong></p>"
            "<ul>"
            "<li><strong>x86-64 (AMD64):</strong> CISC; dominant in desktops, laptops, servers. "
            "Intel Core/Xeon; AMD Ryzen/EPYC.</li>"
            "<li><strong>ARM:</strong> RISC; dominant in mobile (iOS, Android); Apple Silicon (M-series) "
            "in Macs; Windows on ARM.</li>"
            "</ul>"
            "<p><strong>CPU Performance Concepts</strong></p>"
            "<ul>"
            "<li><strong>Clock speed:</strong> GHz — cycles per second; higher = faster (same architecture).</li>"
            "<li><strong>Cores:</strong> Independent processing units on one die; more cores = better multitasking/multithread.</li>"
            "<li><strong>Threads / SMT / Hyper-Threading:</strong> Each core handles multiple threads simultaneously; "
            "Intel HT = 2 threads per core.</li>"
            "<li><strong>Cache:</strong> L1 (fastest, per-core, ~32–64 KB), L2 (per-core, ~256 KB–1 MB), "
            "L3 (shared across cores, several MB to hundreds of MB).</li>"
            "<li><strong>TDP (Thermal Design Power):</strong> Maximum heat output in watts; dictates cooling solution.</li>"
            "</ul>"
            "<p><strong>CPU Sockets (current)</strong></p>"
            "<ul>"
            "<li><strong>Intel LGA 1700:</strong> 12th–14th Gen Core (Alder/Raptor Lake).</li>"
            "<li><strong>Intel LGA 1851:</strong> 14th Gen Core Ultra / Arrow Lake.</li>"
            "<li><strong>AMD AM4:</strong> Ryzen 1000–5000 series; PGA 1331 pins.</li>"
            "<li><strong>AMD AM5:</strong> Ryzen 7000+ series; LGA 1718 pins.</li>"
            "</ul>"
            "<p><strong>Integrated vs Discrete GPU:</strong> iGPU built into CPU die (Intel UHD, AMD Radeon Graphics); "
            "discrete GPU in PCIe x16 slot for demanding workloads.</p>"
            "<p><strong>32-bit vs 64-bit:</strong> 64-bit CPUs can address &gt;4 GB RAM; "
            "64-bit OS required to use &gt;4 GB.</p>"
        ),
        "key_points": [
            "x86-64 (CISC) dominates desktops/servers; ARM (RISC) dominates mobile and Apple Silicon.",
            "More cores improve multithreaded performance; higher GHz improves single-threaded tasks.",
            "L1 cache is fastest and smallest; L3 is largest and shared across cores.",
            "Hyper-Threading (Intel SMT) allows 2 threads per physical core.",
            "64-bit CPU and OS are required to address more than 4 GB of RAM.",
            "TDP indicates the cooling requirement; higher TDP = more heat to dissipate.",
        ],
    },
    {
        "domain": 3,
        "topic": "Cooling",
        "objective": "3.7",
        "video": "Cooling",
        "study_topics": ["Cooling"],
        "body": (
            "<p>Proper cooling prevents thermal throttling and hardware damage. "
            "Cooling solutions scale with TDP requirements.</p>"
            "<p><strong>Air Cooling</strong></p>"
            "<ul>"
            "<li><strong>Stock/boxed cooler:</strong> Included with retail CPUs; adequate for stock speeds.</li>"
            "<li><strong>Tower heatsink:</strong> Large aluminum/copper fins with copper heat pipes; "
            "direct-touch or base-contact to IHS (Integrated Heat Spreader) of CPU.</li>"
            "<li><strong>Thermal paste (TIM):</strong> Applied between CPU IHS and cooler base to fill "
            "microscopic air gaps; never skip — dramatically increases temps without it.</li>"
            "<li><strong>Case fans:</strong> Intake (front/bottom) + exhaust (rear/top) create positive or "
            "negative air pressure airflow. Positive = more intake than exhaust (less dust ingress). "
            "Negative = more exhaust.</li>"
            "</ul>"
            "<p><strong>Liquid / AIO Cooling</strong></p>"
            "<ul>"
            "<li><strong>AIO (All-In-One) liquid cooler:</strong> Pre-filled closed loop; pump + cold plate + "
            "radiator + fans. Radiator sizes: 120 mm, 240 mm, 280 mm, 360 mm.</li>"
            "<li><strong>Custom loop:</strong> Separate reservoir, pump, waterblocks, radiator; higher maintenance.</li>"
            "</ul>"
            "<p><strong>Laptop Cooling</strong></p>"
            "<ul>"
            "<li>Copper heat pipes transfer heat from CPU/GPU to radiator fins; single thin fan exhausts out the side/rear.</li>"
            "<li>Thermal paste dries out over time — repasting extends laptop life.</li>"
            "</ul>"
            "<p><strong>Passive Cooling:</strong> No fans; heatsink only; used in low-power/embedded systems "
            "and silent HTPC builds.</p>"
            "<p><strong>Fan connectors:</strong> 3-pin (voltage-controlled speed) vs 4-pin PWM (pulse-width "
            "modulation speed control — preferred).</p>"
        ),
        "key_points": [
            "Thermal paste fills microscopic gaps between CPU IHS and cooler base to conduct heat.",
            "AIO liquid coolers use a closed loop with a radiator; common sizes are 240 mm and 360 mm.",
            "4-pin PWM fans allow precise speed control vs 3-pin voltage-regulated fans.",
            "Positive case pressure (more intake) reduces dust buildup compared to negative pressure.",
            "Laptop heat pipes must remain clear; repasting a laptop CPU/GPU can significantly reduce temperatures.",
        ],
    },
    {
        "domain": 3,
        "topic": "BIOS/UEFI and Secure Boot",
        "objective": "3.5",
        "video": "BIOS and UEFI",
        "study_topics": ["BIOS/UEFI & secure boot"],
        "body": (
            "<p><strong>BIOS (Basic Input/Output System)</strong></p>"
            "<ul>"
            "<li>Legacy firmware stored in ROM/flash chip on motherboard.</li>"
            "<li>16-bit real mode; MBR-based boot; limited to 4 primary partitions; 2 TB drive limit (MBR).</li>"
            "<li>POST (Power-On Self-Test) runs at startup to check hardware.</li>"
            "<li>Accessed by pressing Delete, F2, F10, or F12 during POST (varies by manufacturer).</li>"
            "</ul>"
            "<p><strong>UEFI (Unified Extensible Firmware Interface)</strong></p>"
            "<ul>"
            "<li>Modern replacement for BIOS; 32/64-bit; GUI interface with mouse support.</li>"
            "<li>Supports GPT (GUID Partition Table): up to 128 partitions, drives &gt;2 TB.</li>"
            "<li>Faster boot times via Boot Manager; network boot (PXE) built-in.</li>"
            "<li>Stores boot variables in NVRAM instead of CMOS.</li>"
            "</ul>"
            "<p><strong>Secure Boot</strong></p>"
            "<ul>"
            "<li>UEFI feature that verifies the digital signature of bootloaders and OS kernels.</li>"
            "<li>Prevents malware (bootkits, rootkits) from loading before the OS.</li>"
            "<li>Uses a certificate database (db) and revocation list (dbx) stored in UEFI.</li>"
            "<li>Required for Windows 11 installation.</li>"
            "<li>Can be disabled in UEFI to boot unsigned OSes (e.g., some Linux distros without shim).</li>"
            "</ul>"
            "<p><strong>TPM (Trusted Platform Module)</strong></p>"
            "<ul>"
            "<li>Hardware chip (or firmware TPM) that stores cryptographic keys.</li>"
            "<li>Used by BitLocker, Windows Hello, and Secure Boot key storage.</li>"
            "<li>TPM 2.0 required for Windows 11.</li>"
            "</ul>"
            "<p><strong>CMOS settings:</strong> Boot order, system time/date, CPU/RAM overclocking, "
            "virtualization (VT-x/AMD-V), fan control, power management.</p>"
        ),
        "key_points": [
            "UEFI replaces legacy BIOS; supports GPT, drives >2 TB, and 128 partitions.",
            "Secure Boot verifies bootloader digital signatures to block bootkits/rootkits.",
            "TPM 2.0 is required for Windows 11 and is used by BitLocker for key storage.",
            "POST (Power-On Self-Test) checks hardware health at every startup.",
            "Boot order is configured in UEFI/BIOS to determine which device the system boots from.",
            "NVRAM stores UEFI settings; CMOS RAM stores legacy BIOS settings (backed by CR2032 battery).",
        ],
    },
    {
        "domain": 3,
        "topic": "Power supplies",
        "objective": "3.7",
        "video": "Power Supplies",
        "study_topics": ["Power supplies"],
        "body": (
            "<p>The PSU (Power Supply Unit) converts AC mains voltage to regulated DC voltages "
            "required by computer components.</p>"
            "<p><strong>Output Voltages</strong></p>"
            "<ul>"
            "<li><strong>+12 V:</strong> Primary rail for CPU, GPU, motors (most power).</li>"
            "<li><strong>+5 V:</strong> Motherboard logic, USB power, older drives.</li>"
            "<li><strong>+3.3 V:</strong> RAM, PCIe slots, modern logic circuits.</li>"
            "<li><strong>-12 V:</strong> Legacy serial ports.</li>"
            "<li><strong>+5 VSB (standby):</strong> Always on when PSU is plugged in; powers WOL circuitry.</li>"
            "</ul>"
            "<p><strong>Connectors</strong></p>"
            "<ul>"
            "<li><strong>24-pin ATX:</strong> Main motherboard power.</li>"
            "<li><strong>4+4-pin (8-pin) EPS/ATX12V:</strong> CPU power.</li>"
            "<li><strong>6+2-pin PCIe:</strong> GPU auxiliary power (6-pin = 75 W, 8-pin = 150 W). "
            "16-pin 12VHPWR connector for high-end GPUs (up to 600 W).</li>"
            "<li><strong>SATA power (15-pin):</strong> HDDs, SSDs, optical drives.</li>"
            "<li><strong>Molex (4-pin):</strong> Legacy fans, older drives.</li>"
            "</ul>"
            "<p><strong>Wattage &amp; Efficiency</strong></p>"
            "<ul>"
            "<li>PSU wattage must exceed peak system draw; leave ~20–30% headroom.</li>"
            "<li><strong>80 PLUS certification:</strong> Guarantees ≥80% efficiency at 20/50/100% load. "
            "Tiers: 80 PLUS, Bronze, Silver, Gold, Platinum, Titanium.</li>"
            "</ul>"
            "<p><strong>Form Factors:</strong> ATX (most common), SFX (small form factor), TFX/Flex ATX (slim cases).</p>"
            "<p><strong>Modular vs Non-modular:</strong> Fully modular PSUs allow removing unused cables "
            "for better airflow; non-modular have all cables permanently attached.</p>"
        ),
        "key_points": [
            "The 24-pin ATX connector is the main motherboard power; 8-pin EPS/ATX12V powers the CPU.",
            "+12V rail delivers the most power and is used by CPU and GPU.",
            "80 PLUS certification ensures at least 80% efficiency; Gold/Platinum are common high-efficiency tiers.",
            "Size the PSU with ~20-30% headroom above estimated system peak draw.",
            "Modular PSUs improve cable management and airflow by allowing unused cables to be removed.",
            "+5VSB (standby) is always energized when the PSU is plugged in, enabling Wake-on-LAN.",
        ],
    },
    {
        "domain": 3,
        "topic": "Laser printer imaging process",
        "objective": "3.9",
        "video": "Laser Printers",
        "study_topics": [
            "Laser printer imaging process",
            "Laser printer imaging process — seven stages in correct order",
        ],
        "body": (
            "<p>Laser printers use a photosensitive drum and electrostatic charge to transfer toner "
            "to paper. The process has <strong>seven stages</strong> — memorize them in order:</p>"
            "<ol>"
            "<li><strong>Processing:</strong> The RIP (Raster Image Processor) converts the print job "
            "into a bitmap/page description that the printer can render. Occurs in printer memory.</li>"
            "<li><strong>Charging:</strong> The primary corona wire (or charge roller) applies a uniform "
            "strong negative charge (~-600 V) across the entire surface of the photosensitive drum.</li>"
            "<li><strong>Exposing:</strong> The laser beam (or LED array in LED printers) selectively "
            "discharges areas of the drum to a lower negative potential (~-100 V), writing the latent "
            "image of the page as a pattern of charge differences.</li>"
            "<li><strong>Developing:</strong> Negatively charged toner particles are attracted to the "
            "less-negative (exposed) areas of the drum, making the latent image visible.</li>"
            "<li><strong>Transferring:</strong> The transfer corona/roller applies a positive charge to "
            "the paper, attracting negatively charged toner from the drum surface onto the paper.</li>"
            "<li><strong>Fusing:</strong> Heated fuser rollers melt and bond the toner permanently into "
            "the paper fibers using heat (~200 °C) and pressure.</li>"
            "<li><strong>Cleaning:</strong> A rubber blade scrapes residual toner from the drum; "
            "an erase lamp or charge roller neutralizes any remaining charge to prepare for the next page.</li>"
            "</ol>"
            "<p><em>Memory aid: <strong>PCEDT FC</strong> — Processing, Charging, Exposing, Developing, "
            "Transferring, Fusing, Cleaning.</em></p>"
        ),
        "key_points": [
            "The seven stages IN ORDER: Processing, Charging, Exposing, Developing, Transferring, Fusing, Cleaning.",
            "Charging applies a uniform strong negative charge (~-600V) to the drum via the primary corona/charge roller.",
            "Exposing uses the laser to selectively reduce the drum's charge, writing the latent image.",
            "Developing: toner (negatively charged) is attracted to the less-negative exposed areas of the drum.",
            "Transferring: positive charge on paper pulls toner off the drum onto the paper.",
            "Fusing permanently bonds toner to paper using heat (~200°C) and pressure rollers.",
            "Cleaning removes residual toner and resets the drum charge for the next print cycle.",
        ],
    },
    {
        "domain": 3,
        "topic": "Inkjet, thermal, and impact printers",
        "objective": "3.9",
        "video": "Inkjet, Thermal, and Impact Printers",
        "study_topics": ["Inkjet/thermal/impact printers"],
        "body": (
            "<p><strong>Inkjet Printers</strong></p>"
            "<ul>"
            "<li>Spray microscopic droplets of liquid ink through nozzles onto paper.</li>"
            "<li><strong>Thermal inkjet:</strong> Heating element vaporizes ink to create a bubble that "
            "forces a droplet out (HP, Canon).</li>"
            "<li><strong>Piezoelectric inkjet:</strong> Piezo crystal deforms under voltage to eject ink "
            "without heat (Epson).</li>"
            "<li>Uses CMYK (Cyan, Magenta, Yellow, Black) ink cartridges; separate or combined.</li>"
            "<li>Prone to clogged heads if left unused; maintenance cycle prints to keep nozzles clear.</li>"
            "<li>Media: plain paper, photo paper, glossy, transparencies.</li>"
            "</ul>"
            "<p><strong>Thermal Printers</strong></p>"
            "<ul>"
            "<li><strong>Direct thermal:</strong> Heat-sensitive paper darkens when heated; no ink/ribbon needed. "
            "Used for receipts, shipping labels. Fades with heat/light over time.</li>"
            "<li><strong>Thermal transfer:</strong> Heated printhead melts ink from a ribbon onto paper/label. "
            "More durable output; used for barcode labels, wristbands.</li>"
            "<li>No ink cartridges to replace (direct thermal); ribbon replacement for thermal transfer.</li>"
            "</ul>"
            "<p><strong>Impact Printers (Dot Matrix)</strong></p>"
            "<ul>"
            "<li>Pins in the printhead strike an ink ribbon against paper to form characters.</li>"
            "<li>Noisy; slow; but can print multi-part (carbon copy) forms — unique advantage.</li>"
            "<li>Used in invoices, receipts, and environments where carbon copies are required.</li>"
            "<li>Ink ribbon replacement is the primary consumable.</li>"
            "</ul>"
        ),
        "key_points": [
            "Inkjet uses CMYK liquid ink sprayed through nozzles; prone to clogging if unused.",
            "Direct thermal uses heat-sensitive paper (no ink/ribbon); common for receipts but fades over time.",
            "Thermal transfer uses a heated ribbon for durable labels and barcodes.",
            "Impact (dot matrix) printers can print multi-part carbon copy forms — unique capability.",
            "Piezoelectric inkjet (Epson) uses voltage-deformed crystals; thermal inkjet (HP) uses a heating element.",
        ],
    },
    {
        "domain": 3,
        "topic": "Printer maintenance",
        "objective": "3.9",
        "video": "Printer Maintenance",
        "study_topics": ["Printer maintenance"],
        "body": (
            "<p>Regular maintenance prevents print quality issues and extends printer life.</p>"
            "<p><strong>Laser Printer Maintenance</strong></p>"
            "<ul>"
            "<li><strong>Toner cartridge replacement:</strong> Shake cartridge gently before installing to "
            "redistribute toner. Replace when pages show faded or streaky output.</li>"
            "<li><strong>Fuser replacement:</strong> Fuser has a page life rating; replace when causing "
            "smearing/not fusing toner (output smears when rubbed).</li>"
            "<li><strong>Drum replacement:</strong> Separate from toner in some models; replace for "
            "repetitive ghost images or spots on every page.</li>"
            "<li><strong>Pickup/feed rollers:</strong> Clean with lint-free cloth + isopropyl alcohol; "
            "replace when causing paper jams or feed failures.</li>"
            "<li><strong>Transfer corona wire/roller:</strong> Clean with supplied brush to prevent "
            "uneven charge and banding.</li>"
            "<li><strong>Calibration:</strong> Color lasers require color registration/calibration to "
            "align CMYK planes.</li>"
            "</ul>"
            "<p><strong>Inkjet Printer Maintenance</strong></p>"
            "<ul>"
            "<li>Run <strong>printhead cleaning</strong> cycle from software when output is streaky.</li>"
            "<li><strong>Nozzle check/test page:</strong> Diagnose clogged nozzles.</li>"
            "<li>Replace ink cartridges when low; use OEM or compatible cartridges.</li>"
            "<li>Clean printhead manually with distilled water on lint-free cloth for severe clogs.</li>"
            "</ul>"
            "<p><strong>Thermal Printer Maintenance</strong></p>"
            "<ul>"
            "<li>Clean printhead with isopropyl alcohol and cotton swab.</li>"
            "<li>Replace direct thermal paper roll when output fades.</li>"
            "<li>Thermal transfer: replace ribbon when output is faded or incomplete.</li>"
            "</ul>"
            "<p><strong>General:</strong> Keep printers dust-free; use recommended paper weights; "
            "avoid storing paper in humid conditions (causes curl/jams).</p>"
        ),
        "key_points": [
            "Smearing toner when rubbed indicates fuser failure on a laser printer.",
            "Repetitive ghost images or spots on every page suggest a worn drum unit.",
            "Inkjet printhead cleaning cycles use ink; run only when needed to avoid wasting cartridges.",
            "Pickup roller wear causes paper jams; clean first, replace if jams persist.",
            "Color laser printers require color calibration/registration to align CMYK output planes.",
            "Store paper in a cool, dry environment to prevent moisture-related feed issues.",
        ],
    },
    {
        "domain": 3,
        "topic": "Print and scan configuration",
        "objective": "3.9",
        "video": "Printer Configuration",
        "study_topics": ["Print/scan configuration"],
        "body": (
            "<p><strong>Printer Connection Methods</strong></p>"
            "<ul>"
            "<li><strong>USB:</strong> Most common direct connection; plug-and-play; driver installation usually required.</li>"
            "<li><strong>Ethernet (wired network):</strong> Static or DHCP IP address assigned; accessible by all LAN clients.</li>"
            "<li><strong>Wi-Fi:</strong> Configure via WPS button or SSID/passphrase through printer menu or web interface.</li>"
            "<li><strong>Bluetooth:</strong> Short-range; used for mobile printing.</li>"
            "<li><strong>Cloud printing:</strong> Google Cloud Print (deprecated), AirPrint (Apple), Mopria (Android).</li>"
            "</ul>"
            "<p><strong>Sharing &amp; Configuration</strong></p>"
            "<ul>"
            "<li><strong>Shared printer:</strong> Host PC shares printer over network; clients map to \\\\hostname\\printername. "
            "Host must be on for printing.</li>"
            "<li><strong>Print server:</strong> Dedicated device or software service manages jobs; eliminates need for a "
            "host PC to remain on.</li>"
            "<li><strong>Driver installation:</strong> Match driver to exact printer model and OS (32/64-bit). "
            "PCL (Printer Command Language) vs PostScript (PS) drivers — PS preferred for graphics/publishing.</li>"
            "<li><strong>Print queue management:</strong> Pause, resume, cancel, or reorder jobs in the Windows Print Spooler.</li>"
            "<li><strong>Spooler service:</strong> Print Spooler (spoolsv.exe) must be running; restart if jobs are stuck.</li>"
            "</ul>"
            "<p><strong>Scanner Configuration</strong></p>"
            "<ul>"
            "<li>Flatbed, ADF (Automatic Document Feeder), and drum scanners.</li>"
            "<li>Resolution measured in DPI (dots per inch); higher DPI = more detail but larger file size.</li>"
            "<li>Scan-to-email, scan-to-folder (SMB share), scan-to-cloud configured via printer web UI or embedded menu.</li>"
            "<li>TWAIN / WIA (Windows Image Acquisition) drivers enable scanning from applications.</li>"
            "</ul>"
        ),
        "key_points": [
            "USB printers are direct-connect; network printers use Ethernet or Wi-Fi for shared access.",
            "Restart the Print Spooler service (spoolsv.exe) to clear stuck print jobs.",
            "PCL is a general-purpose printer language; PostScript is preferred for graphics and publishing.",
            "AirPrint (Apple) and Mopria (Android) enable driverless mobile printing to compatible printers.",
            "Scan resolution in DPI controls detail level; match DPI to the intended output use.",
            "Scan-to-folder requires SMB share credentials configured on the printer's web interface.",
        ],
    },
]

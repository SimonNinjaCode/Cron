# Microsoft Patch Tuesday Review — August 2026

_Generated 2026-08-14_

## Summary

- **Total CVEs patched:** ~421 (sources range 394–421 depending on counting methodology; SecurityWeek, Splashtop, BleepingComputer converge at 421)
- **Zero-days:** 3 total — 1 actively exploited in the wild (CVE-2026-68820), 2 publicly disclosed (CVE-2026-62832, CVE-2026-72971)
- **Critical severity:** 62 vulnerabilities rated Critical
- **Edge / Chromium:** 0 — Microsoft shipped no Edge/Chromium security updates this month
- **Notable:** CISA added CVE-2026-68820 to the KEV catalog the same day the patch released (Aug 11), attributed to North Korea's Lazarus Group ("Operation Dream Job")

---

### Breakdown by Type

Counts from CrowdStrike's August 2026 analysis; percentages are share of the ~421-CVE total.

| Category | Count | % of Total |
|---|---|---|
| Elevation of Privilege | 174 | 42 % |
| Remote Code Execution | 109 | 26 % |
| Information Disclosure | 85 | 20 % |
| Security Feature Bypass | n/a — not separately enumerated across sources reviewed | — |
| Denial of Service | n/a — not separately enumerated across sources reviewed | — |
| Spoofing | n/a — not separately enumerated across sources reviewed | — |
| Edge – Chromium | 0 | 0 % |

---

## Exploited in the Wild

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-68820 | 7.0 | Important | Windows Ancillary Function Driver for WinSock (afd.sys) — Elevation of Privilege | **Required** — CISA KEV deadline Aug 25 for federal agencies | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820) |

**Details:** Use-after-free in the afd.sys kernel-mode driver (the backbone of the Windows Sockets API). A locally authenticated attacker with low privileges exploits a race condition to elevate to SYSTEM. North Korea's Lazarus Group had been exploiting this for at least five weeks before the patch — a compiled FudModule rootkit artifact carries a timestamp of 2026-07-07. CISA added to KEV on 2026-08-11 with a 14-day remediation window.

---

## Publicly Disclosed

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-62832 | 7.8 | Important | Windows User Profile Service — Elevation of Privilege ("LegacyHive") | **Required** — public PoC available | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62832) |
| CVE-2026-72971 | n/a | n/a | Windows Container Isolation — Elevation of Privilege | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72971) |

**CVE-2026-62832 details:** Improper link resolution (link following) in the Windows User Profile Service. An authenticated attacker with credentials for any local account can load another user's registry hive, access or modify their data, and escalate to administrator with no user interaction. Disclosed by researcher "Nightmare Eclipse" who published a working PoC hours after the July 2026 Patch Tuesday — giving attackers a 30-day window before the fix landed.

**CVE-2026-72971 details:** Publicly disclosed privilege escalation in the Windows Container Isolation stack. CVSS score could not be confirmed across two or more independent sources; listed as n/a.

---

## Highest Rated — CVSS ≥ 8.0 or Critical

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-62815 | 9.8 | Critical | Microsoft QUIC — Remote Code Execution | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62815) |
| CVE-2026-62878 | 9.8 | Critical | Windows DNS Server — Remote Code Execution (potentially wormable) | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62878) |
| CVE-2026-62893 | 9.8 | Critical | Windows Deployment Services TFTP Server — Remote Code Execution | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62893) |
| CVE-2026-62827 | 8.8 | Critical | Microsoft SharePoint Server — Remote Code Execution | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62827) |
| CVE-2026-64921 | 8.8 | Critical | Microsoft SharePoint Server — Remote Code Execution | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64921) |
| CVE-2026-65665 | 8.8 | Critical | Microsoft SharePoint Server — Remote Code Execution | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65665) |
| CVE-2026-62889 | 8.1 | Critical | Windows Secure Socket Tunneling Protocol (SSTP) — Remote Code Execution | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62889) |
| CVE-2026-59124 | n/a | Critical | Microsoft High Performance Computing (HPC) Pack — Remote Code Execution | **Required** | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-59124) |

**Notable details:**
- **CVE-2026-62815 (Microsoft QUIC):** Use-after-free (CWE-416) in Microsoft's HTTP/3 transport layer. Unauthenticated, network-reachable, no user interaction required. Affects approximately 13.5 million websites running on Microsoft QUIC-enabled services.
- **CVE-2026-62878 (Windows DNS Server):** Stack-based buffer overflow (CWE-121); unauthenticated remote code execution with SYSTEM privileges. Flagged as potentially wormable — DNS servers that are internet-facing should be treated as P1.
- **CVE-2026-62893 (WDS TFTP):** Unauthenticated attacker on the network can execute code against Windows Deployment Services servers — significant exposure in network boot/provisioning environments.
- **SharePoint cluster (CVE-2026-62827 / 64921 / 65665):** Three distinct Critical RCE paths in SharePoint Server, all at CVSS 8.8 with authenticated-but-low-privilege entry points.

---

## Exploitation More Likely

Microsoft's "Exploitation More Likely" assessment tags vulnerabilities with credible weaponisation paths even before confirmed in-the-wild activity. Sources reviewed (BleepingComputer, Qualys, CrowdStrike, Rapid7, Tenable) highlighted the following as carrying this tag or equivalent elevated prioritisation:

| CVE | CVSS | Title | Note |
|---|---|---|---|
| CVE-2026-62832 | 7.8 | Windows User Profile Service EoP | Public PoC exists; Microsoft says exploitation likely |
| CVE-2026-62878 | 9.8 | Windows DNS Server RCE | Wormable potential; CrowdStrike / Rapid7 flag as top priority |
| CVE-2026-62815 | 9.8 | Microsoft QUIC RCE | No-auth, no-interaction; wide internet attack surface |

> **Note:** A comprehensive enumeration of every CVE tagged "Exploitation More Likely" in the MSRC portal was not available from sources reviewed at time of publication. Organisations should cross-reference the [MSRC August 2026 release notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Aug) directly for the complete list.

---

## Notable Themes from This Month

- **Kernel EoP as a force-multiplier:** CVE-2026-68820 is the latest in a trend of nation-state actors chaining a modest kernel EoP (CVSS 7.0, "Important") with an initial foothold to achieve total system compromise. The low CVSS score understates urgency when a confirmed nation-state exploit is in circulation — "Important" no longer means "defer."
- **Protocol stacks as wormable attack surfaces:** Both the DNS Server (CVE-2026-62878) and Microsoft QUIC (CVE-2026-62815) reach CVSS 9.8 with zero authentication and zero user interaction. Two separate unauthenticated, network-level RCE flaws in the same month signals continued adversary interest in weaponising foundational protocol implementations.
- **SharePoint under sustained pressure:** Three distinct Critical RCE CVEs against SharePoint Server in a single month, following SharePoint CVEs added to CISA KEV in June and July 2026 (CVE-2026-58644, CVE-2026-45659). SharePoint remains the highest-value collaboration attack surface in the Microsoft ecosystem — any internet-facing deployment needs immediate attention.
- **PoC-to-patch timing risk:** The "LegacyHive" disclosure (CVE-2026-62832) illustrates a maturing researcher behaviour pattern — publishing a working exploit the same day as Patch Tuesday to maximise attention while the vendor cannot immediately react. Organisations without same-day patching SLAs for publicly-disclosed EoP bugs face a ~30-day exposure window.
- **CISA KEV same-day mandates:** CISA adding CVE-2026-68820 to the KEV catalog on the same day as the patch release (Aug 11) with a 14-day deadline reflects a tighter coordination posture between Microsoft's Patch Tuesday and CISA's enforcement mechanism. Private-sector organisations should treat KEV additions with same-day urgency regardless of federal mandate applicability.

---

## Sources

- [BleepingComputer — Microsoft August 2026 Patch Tuesday fixes 400 flaws, 3 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-august-2026-patch-tuesday-fixes-400-flaws-3-zero-days/)
- [SecurityWeek — August 2026 Patch Tuesday: Microsoft Fixes 421 CVEs, One Exploited Zero-Day](https://www.securityweek.com/august-2026-patch-tuesday-microsoft-fixes-421-cves-one-exploited-zero-day/)
- [Qualys — Microsoft and Adobe Patch Tuesday, August 2026 Security Update Review](https://blog.qualys.com/vulnerabilities-threat-research/patch-tuesday/2026/08/11/microsoft-patch-tuesday-august-2026-security-update-review)
- [CrowdStrike — August 2026 Patch Tuesday: Updates and Analysis](https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-august-2026/)
- [Rapid7 — Patch Tuesday – August 2026](https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/)
- [Tenable — Microsoft's August 2026 Patch Tuesday Addresses 398 CVEs (CVE-2026-68820)](https://www.tenable.com/blog/microsofts-august-2026-patch-tuesday-addresses-398-cves-cve-2026-68820)
- [Security Affairs — Microsoft Patch Tuesday for August 2026 Fixed a Zero-Day and Wormable RCE](https://securityaffairs.com/197048/security/microsoft-patch-tuesday-for-august-2026-fixed-a-zero-day-and-wormable-rce.html)
- [The Hacker News / SANS ISC — Microsoft Patch Tuesday August 2026](https://isc.sans.edu/diary/Microsoft+Patch+Tuesday+August+2026/33236/)
- [Help Net Security — Microsoft patches 400+ vulnerabilities, one zero-day under attack (CVE-2026-68820)](https://www.helpnetsecurity.com/2026/08/12/august-2026-patch-tuesday-cve-2026-68820/)
- [The Record (Recorded Future) — CISA gives federal agencies two weeks to patch Microsoft bug exploited in DPRK campaign](https://therecord.media/cisa-gives-federal-agencies-two-weeks-to-patch-dprk-microsoft-bug)
- [Brinztech — CISA Mandates Emergency Patching for Windows WinSock Zero-Day (CVE-2026-68820) Exploited in North Korean 'Dream Job' Campaign](https://www.brinztech.com/breach-alerts/brinztech-alert-cisa-mandates-emergency-patching-for-windows-winsock-zero-day-cve-2026-68820-exploited-in-north-korean-dream-job-campaign)
- [Zero Day Initiative — The August 2026 Security Update Review](https://www.zerodayinitiative.com/blog/2026/8/11/the-august-2026-security-update-review)
- [CISA — CISA Adds Three Known Exploited Vulnerabilities to Catalog (Aug 11 2026)](https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog)
- [MSRC — August 2026 Security Updates Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Aug)

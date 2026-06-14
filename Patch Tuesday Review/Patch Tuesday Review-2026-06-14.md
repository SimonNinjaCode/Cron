# Microsoft Patch Tuesday Review — June 2026

_Generated 2026-06-14_

## Summary

- **Total CVEs patched:** ~206 (198 Microsoft-specific CVEs + ~8 Edge/Chromium; exact count varies by source methodology — Tenable: 198, BleepingComputer/THN/CrowdStrike: 206, Absolute Security: 211)
- **Zero-days:** 6 total — 3 exploited in the wild (CISA KEV), 3 publicly disclosed
- **Critical severity:** 32 CVEs
- **Edge/Chromium CVEs:** ~8 (included in BleepingComputer/THN totals; excluded from Tenable's 198 count)
- **This is the largest single Patch Tuesday release on record since the programme's founding in 2003**

### Breakdown by type

| Category | Count |
|---|---|
| Elevation of Privilege | 49 |
| Remote Code Execution | 54 |
| Spoofing | 27 |
| Information Disclosure | 16 |
| Security Feature Bypass | 15 |
| Denial of Service | 7 |
| Edge – Chromium | ~8 |

_Source: Qualys / BleepingComputer analysis. Some CVEs may span multiple categories. Edge/Chromium count estimated from delta between Tenable (198) and BleepingComputer (206) totals. Remaining CVEs (~30) not fully enumerated by type in reviewed sources — may include Tampering and other categories._

---

## Exploited in the Wild

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-41091 | 7.8 | Important | Microsoft Defender Elevation of Privilege ("RedSun") — local EoP to SYSTEM; CISA KEV deadline June 3, 2026 | [FIXED] auto-patched via Malware Protection Engine (Windows Update) | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41091) |
| CVE-2026-42897 | n/a | Important | Microsoft Exchange Server OWA Cross-Site Scripting — arbitrary JS execution in Outlook Web Access via crafted email; CISA KEV deadline June 5, 2026 | Required — apply Exchange Server CU/SU | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42897) |
| CVE-2026-45498 | n/a | Important | Microsoft Defender Denial of Service — heap-based buffer overflow in Malware Protection Engine; CISA KEV deadline June 3, 2026 | [FIXED] auto-patched via Malware Protection Engine (Windows Update) | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45498) |

> **CISA KEV note:** All three are listed in the CISA Known Exploited Vulnerabilities catalog. CVE-2026-41091 and CVE-2026-45498 remediation deadlines (June 3, 2026) were met automatically via Defender's rolling engine update; CVE-2026-42897 required a manual Exchange Server patch by June 5, 2026.

---

## Publicly Disclosed

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-45586 | 7.8 | Important | Windows Collaborative Translation Framework (CTFMON) Elevation of Privilege ("GreenPlasma") — link-following flaw; low-priv local attacker → SYSTEM, no user interaction | Required — apply Windows Update | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586) |
| CVE-2026-49160 | 7.5 | Important | Windows HTTP.sys Denial of Service ("YellowKey" / HTTP/2 Bomb) — uncontrolled resource consumption; unauthenticated remote attacker, no user interaction; Microsoft added optional `MaxHeadersCount` registry mitigation | Required — apply Windows Update; consider registry mitigation for internet-facing IIS/WinRM | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-49160) |
| CVE-2026-50507 | 6.8 | Important | Windows BitLocker Security Feature Bypass ("MiniPlasma") — physical-access attacker can circumvent BitLocker Device Encryption | Required — apply Windows Update | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50507) |

---

## Highest Rated — CVSS ≥ 8.0 or Critical

_32 total CVEs rated Critical; table lists all confirmed Critical CVEs with available detail, plus CVEs with CVSS ≥ 8.0. CVSS scores for RDP, Hyper-V, and Office entries not confirmed across two independent sources._

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-45657 | 9.8 | Critical | Windows Kernel Remote Code Execution — use-after-free; wormable, no auth, no user interaction, SYSTEM-level | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45657) |
| CVE-2026-44815 | 9.8 | Critical | Windows DHCP Client Remote Code Execution — stack-based buffer overflow; malicious DHCP response → code execution on any DHCP client | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44815) |
| CVE-2026-47291 | 9.8 | Critical | Windows HTTP.sys Remote Code Execution — integer overflow + heap overflow; unauthenticated remote, no user interaction; affects IIS, WinRM, Windows Admin Center | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47291) |
| CVE-2026-42904 | 9.6 | Critical | Windows TCP/IP Heap Buffer Overflow — adjacent-network attacker can elevate privileges via crafted packets | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42904) |
| CVE-2026-45602 | 9.1 | Critical | Windows DHCP Server Tampering — unauthenticated network attacker can manipulate DHCP responses | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45602) |
| CVE-2026-42985 | n/a | Critical | Remote Desktop Client Remote Code Execution — heap-based buffer overflow; attacker-controlled RD server → client code execution | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42985) |
| CVE-2026-44801 | n/a | Critical | Remote Desktop Client Remote Code Execution | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44801) |
| CVE-2026-44799 | n/a | Critical | Remote Desktop Client Remote Code Execution | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44799) |
| CVE-2026-42992 | n/a | Critical | Remote Desktop Client Remote Code Execution | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42992) |
| CVE-2026-47652 | n/a | Critical | Windows Hyper-V Remote Code Execution — VM guest escape, code execution on hypervisor host | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47652) |
| CVE-2026-45641 | n/a | Critical | Windows Hyper-V Remote Code Execution — VM guest escape | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45641) |
| CVE-2026-45607 | n/a | Critical | Windows Hyper-V Remote Code Execution — VM guest escape | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45607) |
| CVE-2026-45458 | n/a | Critical | Microsoft Office / Word Remote Code Execution — malicious document | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45458) |
| CVE-2026-45456 | n/a | Critical | Microsoft Office Remote Code Execution — malicious document | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45456) |
| CVE-2026-45474 | n/a | Critical | Microsoft Office Remote Code Execution — malicious document | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45474) |
| CVE-2026-45472 | n/a | Critical | Microsoft Office Remote Code Execution — malicious document / email content | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45472) |

---

## Exploitation More Likely

Microsoft tagged the following CVEs with "Exploitation More Likely" in its exploitability index. Sources enumerate at least four confirmed entries:

| CVE | CVSS | Criticality | Title |
|---|---|---|---|
| CVE-2026-45586 | 7.8 | Important | Windows CTFMON Elevation of Privilege ("GreenPlasma") |
| CVE-2026-49160 | 7.5 | Important | Windows HTTP.sys DoS — HTTP/2 Bomb ("YellowKey") |
| CVE-2026-50507 | 6.8 | Important | Windows BitLocker Security Feature Bypass ("MiniPlasma") |
| CVE-2026-42985 | n/a | Critical | Remote Desktop Client RCE — heap buffer overflow |

_Note: MSRC's full exploitability index applies across all 206 entries; not all "Exploitation More Likely" assessments could be confirmed across two independent sources. The four above are confirmed from multiple analyses (Tenable, CrowdStrike, SOCRadar)._

---

## Notable themes from this month

- **Wormable kernel and DHCP attack chains demand immediate priority.** CVE-2026-45657 (Windows Kernel, CVSS 9.8) and CVE-2026-44815 (DHCP Client, CVSS 9.8) are unauthenticated, zero-interaction, no-privileges-required flaws — textbook worm propagation primitives. Combined with CVE-2026-44815's targeting of any host that performs DHCP negotiation, these represent an exceptionally broad lateral-movement surface across flat enterprise networks.
- **Windows networking subsystem under concentrated pressure.** HTTP.sys, TCP/IP, DHCP Client, and DHCP Server all received Critical patches in a single month, signalling sustained researcher and adversary focus on Windows kernel-mode network drivers as a pre-authentication entry point. The HTTP/2 Bomb DoS (CVE-2026-49160) adds a denial-of-availability dimension to the same attack surface.
- **Hypervisor boundary erosion at scale.** Three simultaneous Hyper-V guest-escape RCEs (CVE-2026-47652, CVE-2026-45641, CVE-2026-45607) in one release is an unusual concentration risk for cloud IaaS and hosting providers where tenant isolation is entirely hypervisor-dependent.
- **Security tooling and encryption bypass as a first-stage attacker tactic.** Active in-the-wild exploitation of CVE-2026-41091 and CVE-2026-45498 (both Microsoft Defender) alongside public disclosure of CVE-2026-50507 (BitLocker) reflects a maturing attacker playbook: neutralise defences and defeat disk encryption before pivoting laterally, rather than seeking application-layer footholds.
- **Record CVE volume signals a structural shift in the patch cadence.** At ~206 CVEs, June 2026 is the largest single Patch Tuesday since 2003. Industry commentary (CSO Online, CyberScoop) characterises this as a potential "new normal" driven by accelerated internal fuzzing pipelines and a larger external research community — creating sustained pressure on enterprise patch cycles and prioritisation workflows.

---

## Sources

- [BleepingComputer — Microsoft June 2026 Patch Tuesday fixes 6 zero-days, 200 flaws](https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-6-zero-days-200-flaws/)
- [BleepingComputer — Microsoft patches YellowKey, GreenPlasma, MiniPlasma zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)
- [Tenable — Microsoft's June 2026 Patch Tuesday Addresses 198 CVEs (CVE-2026-49160, CVE-2026-50507)](https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507)
- [Qualys — Microsoft and Adobe Patch Tuesday, June 2026 Security Update Review](https://blog.qualys.com/vulnerabilities-threat-research/2026/06/09/microsoft-and-adobe-patch-tuesday-june-2026-security-update-review)
- [CrowdStrike — June 2026 Patch Tuesday: Updates and Analysis](https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/)
- [The Hacker News — Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs](https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html)
- [Cisco Talos — Microsoft Patch Tuesday for June 2026: Snort rules and prominent vulnerabilities](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-june-2026-snort-rules-and-prominent-vulnerabilities/)
- [Rapid7 — Patch Tuesday — June 2026](https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026/)
- [SOCRadar — June 2026 Patch Tuesday: 206 Vulnerabilities, Three Zero-Days Including HTTP/2 Bomb Flaw (CVE-2026-49160)](https://socradar.io/blog/june-2026-patch-tuesday-zero-day/)
- [Zero Day Initiative — The June 2026 Security Update Review](https://www.zerodayinitiative.com/blog/2026/6/9/the-june-2026-security-update-review)
- [Threat-Modeling.com — Microsoft June 2026 Patch Tuesday Critical Vulnerabilities (CVE-2026-45657, CVE-2026-42904, CVE-2026-44815, CVE-2026-47291, CVE-2026-45602)](https://threat-modeling.com/microsoft-june-2026-patch-tuesday-critical-cves/)
- [Help Net Security — Microsoft Defender vulnerabilities exploited in the wild (CVE-2026-41091, CVE-2026-45498)](https://www.helpnetsecurity.com/2026/05/21/microsoft-defender-vulnerabilities-cve-2026-41091-cve-2026-45498/)
- [Windows News — CVE-2026-42897: Critical Exchange OWA XSS Vulnerability Added to CISA KEV Catalog](https://windowsnews.ai/article/cve-2026-42897-critical-exchange-owa-xss-vulnerability-added-to-cisa-kev-catalog-patch-now.418483)
- [CSO Online — June Patch Tuesday marks a 'new normal' with over 200 CVEs, 32 rated 'critical'](https://www.csoonline.com/article/4183632/june-patch-tuesday-marks-a-new-normal-with-over-200-cves-32-rated-critical.html)
- [CyberScoop — Microsoft breaks Patch Tuesday record with 206 vulnerabilities](https://cyberscoop.com/microsoft-patch-tuesday-june-2026/)
- [MSRC — Security Update Guide — June 2026 Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun)

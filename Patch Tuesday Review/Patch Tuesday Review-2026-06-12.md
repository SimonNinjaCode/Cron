# Microsoft Patch Tuesday Review — June 2026

_Generated 2026-06-12_

## Summary

- **Total CVEs patched:** 206 (Microsoft products); 74 additional Edge/Chromium CVEs published separately; ~208 per ZDI counting methodology
- **Zero-days:** 6 total — 1 actively exploited in the wild, 5 publicly disclosed before patch (BleepingComputer; 4 confirmed by name in available sources, see sections below)
- **Critical severity:** 32–37 rated Critical depending on source methodology (28 of these are RCE)
- **Edge / Chromium CVEs:** 74 (separate Chromium release coinciding with Patch Tuesday)
- **Record release:** Largest Patch Tuesday in program history, surpassing the previous record of ~167 CVEs set in October 2025

### Breakdown by type

| Vulnerability Type | Count |
|--------------------|-------|
| Elevation of Privilege | 63 |
| Remote Code Execution | 56 |
| Information Disclosure | 30 |
| Spoofing | 27 |
| Security Feature Bypass | 20 |
| Denial of Service | 7 |
| Tampering | 3 |
| **Edge – Chromium** | **74** |
| **Total (Microsoft)** | **206** |

> Sources: BleepingComputer / CrowdStrike / Qualys cross-referenced. Tenable independently reports 198 (methodological difference in Edge counting). ZDI reports 208.

---

## Exploited in the Wild

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|-----|------|-------------|-------|-----------------|------|
| CVE-2026-41091 | 7.8 | Important | Microsoft Defender Elevation of Privilege ("RedSun") — local privilege escalation to SYSTEM; exploited in the wild since April 15, 2026; added to CISA KEV May 20, 2026 | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41091) |

> Note: CVE-2026-41091 is auto-remediated via the Defender engine update distributed through Windows Update for endpoints with automatic updates enabled. Manual verification of engine version is recommended for air-gapped or WSUS-managed environments.

---

## Publicly Disclosed

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|-----|------|-------------|-------|-----------------|------|
| CVE-2026-45586 | 7.8 | Important | Windows Collaborative Translation Framework (CTFMON) EoP ("GreenPlasma") — local attacker gains SYSTEM privileges; publicly disclosed by researcher "Nightmare Eclipse"; Microsoft: Exploitation More Likely | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586) |
| CVE-2026-50507 | 6.8 | Important | Windows BitLocker Security Feature Bypass ("YellowKey") — physical attacker bypasses BitLocker Device Encryption and reads encrypted drive; Microsoft: Exploitation More Likely | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50507) |
| CVE-2026-49160 | 7.5 | Important | Windows HTTP.sys Denial of Service ("HTTP2/Bomb") — HTTP/2 request flood can crash kernel-mode HTTP listener; publicly disclosed before patch; could affect hundreds of thousands of internet-facing Windows servers; Microsoft: Exploitation More Likely | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-49160) |

> BleepingComputer's full article cites 5 publicly disclosed zero-days; 3 are confirmed and named above. Available search-result excerpts do not enumerate the remaining 2 by CVE ID — additional CVEs may be identified via the MSRC release notes linked in Sources.

---

## Highest Rated — CVSS ≥ 8.0 or Critical

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|-----|------|-------------|-------|-----------------|------|
| CVE-2026-47291 | 9.8 | Critical | Windows HTTP.sys Remote Code Execution — unauthenticated network attacker executes code; no user interaction required; integer overflow / heap buffer overflow in HTTP Protocol Stack; **wormable potential**; Microsoft: Exploitation More Likely | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47291) |
| CVE-2026-45657 | 9.8 | Critical | Windows Kernel Remote Code Execution — use-after-free in kernel TCP/IP handling; unauthenticated remote attacker executes code at SYSTEM level; **wormable**; affects Windows 11 23H2–26H1 and Server 2022/2025 | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45657) |
| CVE-2026-44801 | n/a | Critical | Remote Desktop Client RCE — one of 4 Critical RDC patches this cycle; exploitation requires a malicious RDP server | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44801) |
| CVE-2026-44799 | n/a | Critical | Remote Desktop Client RCE | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44799) |
| CVE-2026-42992 | n/a | Critical | Remote Desktop Client RCE | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42992) |
| CVE-2026-42985 | n/a | Critical | Remote Desktop Client RCE | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42985) |
| CVE-2026-47652 | n/a | Critical | Windows Hyper-V RCE — VM guest-to-host escape; attacker runs code on hypervisor host | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47652) |
| CVE-2026-45641 | n/a | Critical | Windows Hyper-V RCE — VM guest escape | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45641) |
| CVE-2026-45607 | n/a | Critical | Windows Hyper-V RCE — VM guest escape | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45607) |
| CVE-2026-45458 | n/a | Critical | Microsoft Outlook RCE — exploitable via malicious e-mail/document delivery | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45458) |
| CVE-2026-45456 | n/a | Critical | Microsoft Word RCE — exploitable via malicious document | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45456) |
| CVE-2026-45474 | n/a | Critical | Microsoft Office RCE | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45474) |
| CVE-2026-45472 | n/a | Critical | Microsoft Office RCE | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45472) |
| CVE-2026-42904 | n/a | Critical | Windows TCP/IP RCE — flagged alongside CVE-2026-45657 in critical kernel/network cluster | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42904) |
| CVE-2026-44815 | n/a | Critical | Windows DHCP Client RCE | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44815) |

> CVSS scores for CVEs listed as "n/a" could not be confirmed from available public sources at time of report generation. Consult MSRC or NVD for authoritative scores.

---

## Exploitation More Likely

Microsoft tagged the following CVEs with its **"Exploitation More Likely"** exploitability assessment in the June 2026 MSRC release notes:

| CVE | CVSS | Type | Title |
|-----|------|------|-------|
| CVE-2026-47291 | 9.8 | RCE | Windows HTTP.sys Remote Code Execution |
| CVE-2026-49160 | 7.5 | DoS | Windows HTTP.sys Denial of Service (HTTP2/Bomb) |
| CVE-2026-45586 | 7.8 | EoP | Windows CTFMON Elevation of Privilege (GreenPlasma) |
| CVE-2026-50507 | 6.8 | SFB | Windows BitLocker Security Feature Bypass (YellowKey) |
| CVE-2026-50508 | n/a | Spoofing | Windows NTLM Spoofing — network-accessible, no authentication required, captures NTLM hash via user interaction (file open / page visit) |

> Sources do not enumerate the full list of "Exploitation More Likely" CVEs for this cycle. The above are those specifically called out. Consult the MSRC release notes for the complete set.

---

## Notable themes from this month

- **HTTP/network stack as a critical attack surface:** Two of the month's most dangerous CVEs (CVE-2026-47291 and CVE-2026-45657) are wormable, unauthenticated network-layer RCEs via HTTP.sys and the Windows kernel TCP/IP stack respectively, mirroring the pattern seen with MS17-010/EternalBlue. Any internet-facing Windows server must be treated as an emergency patch target this cycle.
- **Hypervisor containment eroding:** Three Critical Hyper-V guest-escape RCEs (CVE-2026-47652, CVE-2026-45641, CVE-2026-45607) in a single month signals sustained researcher focus on VM isolation boundaries; organisations relying on Hyper-V for tenant separation or security boundaries should prioritise host patching.
- **Client-side document delivery remains a persistent vector:** Four Critical RDC RCEs and five Critical Office/Outlook RCEs reinforce the phishing-to-RCE chain; the combination of a malicious document or RDP redirect with a zero-click kernel escalation path (CTFMON/GreenPlasma) creates a ready-made attack composition.
- **Named researcher disclosures accelerating the patch urgency cycle:** Three nicknamed zero-days (GreenPlasma, YellowKey, HTTP2/Bomb) were publicly disclosed before Microsoft patched them, likely as coordinated disclosure pressure. The involvement of a single researcher ("Nightmare Eclipse") in multiple disclosures suggests an organised vulnerability research campaign against Windows internals.
- **AI-assisted vuln discovery inflating total exposure counts:** The June 3 Chromium batch of 429 CVEs — attributed in part to AI-assisted fuzzing tools — and the coincident 74-CVE Edge update push the true patching burden for the month well above 280 CVEs for browser-inclusive environments, establishing a potential new baseline for patch workloads.

---

## CISA Known Exploited Vulnerabilities (KEV) — June 2026 Deadlines

| CVE | Title | Added to KEV | Deadline |
|-----|-------|--------------|----------|
| CVE-2026-41091 | Microsoft Defender EoP (RedSun) | 2026-05-20 | 2026-06-03 |
| CVE-2026-45498 | Microsoft Defender DoS | 2026-05-20 | 2026-06-03 |
| CVE-2026-42897 | Microsoft Exchange OWA Cross-Site Scripting | 2026-05-15 | 2026-06-05 |

> All three deadlines have passed as of this report's run date (2026-06-12). US federal civilian agencies (FCEB) subject to BOD 22-01 should confirm remediation is complete.

---

## Sources

- [BleepingComputer — Microsoft June 2026 Patch Tuesday fixes 6 zero-days, 200 flaws](https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-6-zero-days-200-flaws/)
- [BleepingComputer — Microsoft patches YellowKey, GreenPlasma, MiniPlasma zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)
- [The Hacker News — Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs](https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html)
- [Tenable — June 2026 Microsoft Patch Tuesday (CVE-2026-49160, CVE-2026-50507)](https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507)
- [Qualys — Microsoft and Adobe Patch Tuesday June 2026 Security Update Review](https://blog.qualys.com/vulnerabilities-threat-research/2026/06/09/microsoft-and-adobe-patch-tuesday-june-2026-security-update-review)
- [CrowdStrike — June 2026 Patch Tuesday: Updates and Analysis](https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-june-2026/)
- [Rapid7 — Patch Tuesday June 2026](https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026/)
- [Cisco Talos — Microsoft Patch Tuesday for June 2026 — Snort rules and prominent vulnerabilities](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-june-2026-snort-rules-and-prominent-vulnerabilities/)
- [SOCRadar — June 2026 Patch Tuesday: 206 Vulnerabilities, Three Zero-Days Including HTTP/2 Bomb Flaw](https://socradar.io/blog/june-2026-patch-tuesday-zero-day/)
- [Absolute Security — June 2026 Patch Tuesday: 211 Fixes, Critical CVEs](https://www.absolute.com/blog/microsoft-patch-tuesday-june-2026-211-fixes-critical-risks)
- [Zero Day Initiative — The June 2026 Security Update Review](https://www.zerodayinitiative.com/blog/2026/6/9/the-june-2026-security-update-review)
- [Malwarebytes — Microsoft's biggest-ever Patch Tuesday fixes 206 bugs, including 3 zero-days](https://www.malwarebytes.com/blog/bugs/2026/06/microsofts-biggest-ever-patch-tuesday-fixes-206-bugs-including-3-zero-days)
- [Security Affairs — Microsoft Releases Record-Breaking Patch Tuesday With 208 CVEs](https://securityaffairs.com/193417/security/microsoft-releases-record-breaking-patch-tuesday-with-208-cves.html)
- [SecurityWeek — Microsoft Patches 200 Vulnerabilities](https://www.securityweek.com/microsoft-patches-200-vulnerabilities/)
- [CISA — Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [CISA — Adds Seven Known Exploited Vulnerabilities to Catalog (2026-05-20)](https://www.cisa.gov/news-events/alerts/2026/05/20/cisa-adds-seven-known-exploited-vulnerabilities-catalog)
- [NVD — CVE-2026-47291](https://nvd.nist.gov/vuln/detail/CVE-2026-47291)
- [NVD — CVE-2026-45657](https://nvd.nist.gov/vuln/detail/CVE-2026-45657)
- [MSRC — June 2026 Security Updates Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun)

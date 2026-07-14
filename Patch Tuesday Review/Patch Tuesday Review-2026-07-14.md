# Microsoft Patch Tuesday Review — July 2026

_Generated 2026-07-14_

---

## Summary

- **Total CVEs patched:** 127 (across 14 product families)
- **Critical severity:** 9 (4 Windows, 2 Office/Microsoft 365, 1 SharePoint, 1 SQL Server, 1 Word)
- **Important severity:** 118
- **CVSS ≥ 8.0:** 34 CVEs
- **Zero-days — exploited in the wild:** 0 newly confirmed at time of release (see note below)
- **Zero-days — publicly disclosed (with PoC):** 1 — CVE-2026-50656 "RoguePlanet" (addressed via out-of-band engine update July 9, before this Patch Tuesday)
- **Exploitation More Likely (Microsoft assessment):** 17 CVEs
- **Edge / Chromium:** n/a (not enumerated separately in available sources for this cycle)

> **Context note:** While no CVEs from today's bundle are confirmed exploited in the wild at release time, CVE-2026-41091 (Microsoft Defender EoP, patched in the May 2026 cycle) was exploited actively and remains on the CISA KEV. Today also marks the **full Phase 2 enforcement** of Kerberos RC4 hardening (CVE-2026-20833), which will break service accounts relying on RC4-only key material with no rollback path.

---

### Breakdown by Type

Specific per-type counts for July 2026 were not fully enumerated in available pre-release sources. The table below reflects the confirmed shape from sources; the prior month (June 2026) breakdown is provided for trend context.

| Type | July 2026 | June 2026 (record month, reference) |
|------|-----------|--------------------------------------|
| Elevation of Privilege | n/a | 63 |
| Remote Code Execution | n/a | 56 |
| Information Disclosure | n/a | 30 |
| Spoofing | n/a | 27 |
| Security Feature Bypass | n/a | 20 |
| Denial of Service | n/a | 7 |
| Tampering | n/a | 3 |
| **Total (Microsoft)** | **127** | **206** |
| Edge / Chromium add-on | n/a | ~365 (bundled) |

_July type counts will be updated once full vendor breakdowns (Qualys, Rapid7, CrowdStrike) publish post-release._

---

## Exploited in the Wild

No CVEs from the July 14, 2026 bundle are confirmed exploited in the wild at time of release. However, the following vulnerability from a prior cycle is actively exploited and directly relevant to this update cycle:

| CVE | CVSS | Criticality | Title | Customer Action | Source |
|-----|------|-------------|-------|-----------------|--------|
| CVE-2026-41091 | 7.8 | High (Important) | Microsoft Defender Malware Protection Engine — Elevation of Privilege (link-resolution abuse → SYSTEM) | Required — CISA KEV deadline was June 3 for FCEB; if not patched, apply Defender engine ≥ 1.1.26040.8 immediately | [Help Net Security](https://www.helpnetsecurity.com/2026/05/21/microsoft-defender-vulnerabilities-cve-2026-41091-cve-2026-45498/), [The Hacker News](https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html) |

---

## Publicly Disclosed

| CVE | CVSS | Criticality | Title | Customer Action | Source |
|-----|------|-------------|-------|-----------------|--------|
| CVE-2026-50656 | 7.8 | High (Important) | Windows Defender Malware Protection Engine — Elevation of Privilege ("RoguePlanet"); race condition allows local attacker to spawn SYSTEM shell; working PoC published by Nightmare-Eclipse on GitHub June 10 | [FIXED] — Auto-delivered via Microsoft Malware Protection Engine update 1.1.26060.3008 (OOB patch July 8–9, 2026); verify engine version | [Malwarebytes](https://www.malwarebytes.com/blog/news/2026/07/microsoft-fixes-rogueplanet-zero-day-in-defender), [The Register](https://www.theregister.com/security/2026/07/09/microsoft-closes-book-on-nightmare-eclipses-rogueplanet-zero-day/5269280), [Kudelski Security](https://kudelskisecurity.com/research/rogueplanet-zero-day-ms-defender-privilege-escalation) |
| CVE-2025-49719 | n/a | Important | SQL Server — Information Disclosure; publicly disclosed at time of patch | Required — apply July 2026 SQL Server cumulative update | [Sophos](https://www.sophos.com/en-us/blog/july-patch-tuesday-offers-127-fixes) |

---

## Highest Rated — CVSS ≥ 8.0 or Critical

| CVE | CVSS | Criticality | Title | Customer Action | Source |
|-----|------|-------------|-------|-----------------|--------|
| CVE-2025-47981 | 9.8 | Critical | Windows SPNEGO Extended Negotiation (NEGOEX) — Heap-Based Buffer Overflow leading to unauthenticated RCE; network vector, no user interaction; **wormable** — attacker can chain across machines autonomously; affects all Windows 10 1607+ clients and all Windows Server versions from 2008 R2 onward | Required — patch internet-facing systems and domain controllers first; no workaround adequate for this severity | [Sophos](https://www.sophos.com/en-us/blog/july-patch-tuesday-offers-127-fixes), [byteiota](https://byteiota.com/patch-tuesday-july-2026-cve-tracking/), [SOC Prime](https://socprime.com/blog/latest-threats/cve-2025-47981-windows-vulnerability/) |
| CVE-2026-45659 | 8.8 | Critical | Microsoft SharePoint Server — Deserialization of Untrusted Data → RCE; CISA added to KEV July 1 with 3-day federal remediation deadline | Required — patched in May 2026 cycle; CISA KEV federal deadline was July 4; any unpatched SharePoint must be treated as compromised | [The Hacker News](https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html), [SOCRadar](https://socradar.io/blog/cisa-sharepoint-rce-cve-2026-45659/) |
| CVE-2026-47281 | 9.6 | Critical | Visual Studio Code — Improper Input Validation → SYSTEM Privilege Escalation ("RoguePlanet" VSCode variant); attacker with code execution escalates to SYSTEM; actively exploited | Required — update VS Code to ≥ 1.123.2 immediately | [Threat-Modeling.com](https://threat-modeling.com/windows-defender-rogueplanet-zero-day-cve-2026-47281/), [byteiota](https://byteiota.com/rogueplanet-cve-2026-47281-patch-windows-defender-now/) |
| CVE-2026-50656 | 7.8 | High (Important) | Windows Defender — RoguePlanet EoP (see Publicly Disclosed) | [FIXED] via OOB engine update | See above |
| CVE-2026-41091 | 7.8 | High (Important) | Microsoft Defender — EoP, exploited in wild (see Exploited table) | Required | See above |
| CVE-2026-20833 | 5.5 | Medium | Windows Kerberos — Information Disclosure via RC4 usage (Kerberoasting vector); **full Phase 2 enforcement begins today**; registry rollback key permanently removed; accounts without AES key material will fail authentication | Required — audit service accounts for RC4-only `msDS-SupportedEncryptionTypes`; migration to AES is now mandatory | [Microsoft Support](https://support.microsoft.com/en-us/topic/how-to-manage-kerberos-kdc-usage-of-rc4-for-service-account-ticket-issuance-changes-related-to-cve-2026-20833-1ebcda33-720a-4da8-93c1-b0496e1910dc), [4sysops](https://4sysops.com/archives/windows-kerberos-rc4-deprecation-what-will-break-in-active-directory-and-how-to-fix-it/) |

> _Additional Critical CVEs (4 Windows, 1 SharePoint, 1 SQL, 1 Word per Microsoft) not individually enumerated in sources available at report time; check MSRC for full list._

---

## Exploitation More Likely

Microsoft flagged **17 CVEs** in this cycle with the "Exploitation More Likely" assessment. Of those identified in available sources:

| CVE | Title | Notes |
|-----|-------|-------|
| CVE-2025-47981 | Windows SPNEGO/NEGOEX Wormable RCE | CVSS 9.8 — highest priority; reverse-engineering of patch likely underway |
| CVE-2026-50656 | Windows Defender RoguePlanet EoP | Working PoC public; patched OOB July 9 |

The remaining 15 CVEs in the "Exploitation More Likely" set were not individually named in pre-release sources available at time of report. The full list is published in the [MSRC Security Update Guide](https://msrc.microsoft.com/update-guide).

---

## Notable Themes from This Month

- **Wormable network-level RCE remains the headline risk:** CVE-2025-47981 (CVSS 9.8, SPNEGO/NEGOEX) requires no authentication or user action and can self-propagate across a network — a profile comparable to EternalBlue. Patch priority on all internet-facing Windows hosts and domain controllers is unconditional this cycle.

- **Defender as an attack surface:** RoguePlanet (CVE-2026-50656) is the latest in a series by researcher Nightmare-Eclipse exploiting the Malware Protection Engine — the component that runs with SYSTEM privileges to protect endpoints. With 29 days of PoC exposure before the OOB patch, organizations relying on Defender as their sole endpoint protection should verify engine version (≥ 1.1.26060.3008) and treat any gap as critical.

- **Kerberos RC4 full enforcement is a breaking change, not just a patch:** The July 14 cumulative update permanently removes the RC4DefaultDisablementPhase registry key, eliminating any rollback path. Any service account still relying on RC4-only encryption types — SQL Server service accounts, legacy MFP/IoT devices, older Java apps — will begin failing Kerberos authentication today with no domain-wide recovery. This requires proactive remediation before patching, not after.

- **AI-assisted vulnerability discovery is reshaping the volume curve:** June 2026 set a record at 206 CVEs; July's 127 is being called a "normalization" but sits above every pre-2026 monthly average. Microsoft has publicly attributed the increased volume to AI-powered fuzzing and static analysis tooling, indicating sustained high-volume release cadence through the remainder of 2026.

- **CISA KEV acceleration trend:** The 3-day remediation deadline on CVE-2026-45659 (SharePoint, added July 1 with a July 4 deadline) signals CISA treating certain Microsoft flaws as acute spreading threats. Organizations outside the federal mandate should treat CISA KEV additions with deadlines ≤ 7 days as effectively P0 regardless of formal FCEB obligations.

---

## Sources

- [byteiota — Microsoft Patch Tuesday July 2026: 127 CVEs, Act Now](https://byteiota.com/patch-tuesday-july-2026-cve-tracking/)
- [Sophos — July Patch Tuesday offers 127 fixes](https://www.sophos.com/en-us/blog/july-patch-tuesday-offers-127-fixes)
- [Help Net Security — July 2026 Patch Tuesday forecast: Is CVE tracking still practical?](https://www.helpnetsecurity.com/2026/07/10/july-2026-patch-tuesday-forecast/)
- [TechTimes — July Patch RoguePlanet Tuesday Kills Windows Kerberos RC4 Rollback](https://www.techtimes.com/articles/320150/20260711/july-patch-rogueplanet-tuesday-kills-windows-kerberos-rc4-rollback-service-accounts-face.htm)
- [TechTimes — CISA Adds First AI Agent Platform to KEV, Sets Thursday Deadline for 4 CVEs](https://www.techtimes.com/articles/319918/20260708/cisa-adds-first-ai-agent-platform-kev-sets-thursday-deadline-4-cves.htm)
- [TechTimes — Defender Zero-Day Patched 29 Days After Public Exploit Exposed Millions of PCs](https://www.techtimes.com/articles/319997/20260709/defender-zero-day-patched-29-days-after-public-exploit-exposed-millions-pcs.htm)
- [The Hacker News — Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges](https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html)
- [The Hacker News — SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation](https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html)
- [Malwarebytes — Microsoft fixes RoguePlanet zero-day in Defender](https://www.malwarebytes.com/blog/news/2026/07/microsoft-fixes-rogueplanet-zero-day-in-defender)
- [The Register — Microsoft closes book on Nightmare Eclipse's RoguePlanet zero-day](https://www.theregister.com/security/2026/07/09/microsoft-closes-book-on-nightmare-eclipses-rogueplanet-zero-day/5269280)
- [Security Boulevard — Microsoft Issues Emergency Patch for RoguePlanet Windows Defender Zero-Day](https://securityboulevard.com/2026/07/microsoft-issues-emergency-patch-for-rogueplanet-windows-defender-zero-day/)
- [Kudelski Security Research — "RoguePlanet" Zero Day MS Defender Privilege Escalation](https://kudelskisecurity.com/research/rogueplanet-zero-day-ms-defender-privilege-escalation)
- [Dark Reading — Windows Zero-Day Barrage Continues After Patch Tuesday](https://www.darkreading.com/cyberattacks-data-breaches/windows-zero-day-barrage-continues-after-patch-tuesday)
- [Help Net Security — Microsoft Defender vulnerabilities exploited in the wild (CVE-2026-41091, CVE-2026-45498)](https://www.helpnetsecurity.com/2026/05/21/microsoft-defender-vulnerabilities-cve-2026-41091-cve-2026-45498/)
- [SOC Prime — CVE-2025-47981: Critical Heap-Based Buffer Overflow in Windows SPNEGO NEGOEX](https://socprime.com/blog/latest-threats/cve-2025-47981-windows-vulnerability/)
- [4sysops — Windows Kerberos RC4 deprecation: what will break in Active Directory and how to fix it](https://4sysops.com/archives/windows-kerberos-rc4-deprecation-what-will-break-in-active-directory-and-how-to-fix-it/)
- [Microsoft Support — How to manage Kerberos KDC usage of RC4 (CVE-2026-20833)](https://support.microsoft.com/en-us/topic/how-to-manage-kerberos-kdc-usage-of-rc4-for-service-account-ticket-issuance-changes-related-to-cve-2026-20833-1ebcda33-720a-4da8-93c1-b0496e1910dc)
- [CISA — Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [MSRC — Security Update Guide, July 2026](https://msrc.microsoft.com/update-guide)

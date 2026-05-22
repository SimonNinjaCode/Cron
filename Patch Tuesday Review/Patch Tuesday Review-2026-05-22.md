# Microsoft Patch Tuesday Review — May 2026

_Generated 2026-05-22_

## Summary

- **Total CVEs patched:** 120 (Microsoft products — BleepingComputer / CybersecurityNews); 137–139 when Edge–Chromium and broader portfolio (Azure, Copilot) are included per Qualys / ZDI methodology
- **Zero-days exploited in the wild at release:** 0 — first zero-day-free release since June 2024, ending a 22-month consecutive streak averaging 3.5 zero-days per month
- **Zero-days publicly disclosed before patch:** 0
- **Critical (MSRC):** 16; up to 30 when counting all product lines (Qualys / The Register methodology)
- **Edge–Chromium:** ~18 CVEs (delta between 120-CVE core count and ~138 total)
- **Notable post-release:** CVE-2026-42897 (Exchange Server OWA XSS) added to CISA KEV on 15 May 2026 — three days after Patch Tuesday — with federal remediation deadline 29 May 2026

### Breakdown by type

Counts per Qualys (all Microsoft product lines, ~137 total). CrowdStrike / Tenable report slightly lower totals (118–120) with correspondingly smaller per-category numbers; differences reflect product-scope methodology.

| Vulnerability Type | Count |
|---|---:|
| Elevation of Privilege | 62 |
| Remote Code Execution | 31 |
| Information Disclosure | 15 |
| Spoofing | 13 |
| Denial of Service | 8 |
| Security Feature Bypass | 6 |
| Tampering | 2 |
| Edge–Chromium | ~18 |

## Exploited in the Wild

No CVEs were patched with confirmed active exploitation at time of release (12 May 2026). CVE-2026-42897 was subsequently added to the CISA KEV catalog on 15 May after post-release exploitation was confirmed — the patch was already available since Patch Tuesday.

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-42897 | 8.1 | High (Important) | Microsoft Exchange Server OWA Cross-Site Scripting — active exploitation confirmed post-release; CISA KEV deadline 29 May 2026 (federal) | Required | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42897) |

## Publicly Disclosed

No CVEs were publicly disclosed before the patch release.

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| — | — | — | None this cycle | — | — |

## Highest Rated — CVSS ≥ 8.0 or Critical

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-42898 | 9.9 | Critical | Microsoft Dynamics 365 On-Premises RCE — authenticated attacker, scope change; can affect resources beyond the vulnerable component | Required | [THN](https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html) |
| CVE-2026-41089 | 9.8 | Critical | Windows Netlogon RCE — unauthenticated, network-reachable stack overflow; potentially wormable against domain controllers | Required | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41089) |
| CVE-2026-41096 | 9.8 | Critical | Windows DNS Client RCE — heap-based buffer overflow triggered by a malicious DNS response; no authentication required | Required | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41096) |
| CVE-2026-41103 | 9.1 | Critical | Microsoft SSO Plugin for Jira & Confluence Elevation of Privilege — tagged "Exploitation More Likely" | Required | [Tenable](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103) |
| CVE-2026-42833 | n/a | Critical | Microsoft Dynamics 365 On-Premises RCE (second Dynamics 365 critical this month) | Required | [THN](https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html) |
| CVE-2026-40365 | n/a | Critical | Microsoft SharePoint Server RCE — authenticated attacker, network-based; executes code on the SharePoint server | Required | [CybersecurityNews](https://cybersecuritynews.com/microsoft-patch-tuesday-may-2026/) |
| CVE-2026-35421 | n/a | n/a | Windows GDI RCE — triggered by opening a malicious Enhanced Metafile (EMF) in Microsoft Paint | Required | [CybersecurityNews](https://cybersecuritynews.com/microsoft-patch-tuesday-may-2026/) |
| CVE-2026-42831 | n/a | n/a | Microsoft Word RCE | Required | [SC Media](https://www.scworld.com/news/patch-tuesday-no-zero-days-among-137-microsoft-cves-4-word-rces) |
| CVE-2026-40363 | n/a | n/a | Microsoft Office RCE | Required | [SC Media](https://www.scworld.com/news/patch-tuesday-no-zero-days-among-137-microsoft-cves-4-word-rces) |
| CVE-2026-40358 | n/a | n/a | Microsoft Office RCE | Required | [SC Media](https://www.scworld.com/news/patch-tuesday-no-zero-days-among-137-microsoft-cves-4-word-rces) |
| CVE-2026-40361 | n/a | n/a | Microsoft Word RCE via Preview Pane — no file open required; tagged "Exploitation More Likely" | Required | [Tenable](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103) |
| CVE-2026-40364 | n/a | n/a | Microsoft Word RCE via Preview Pane — no file open required; tagged "Exploitation More Likely" | Required | [Tenable](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103) |
| CVE-2026-42897 | 8.1 | High | Microsoft Exchange Server OWA XSS — CISA KEV, federal deadline 29 May 2026 | Required | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42897) |

## Exploitation More Likely

Microsoft tagged the following CVEs with "Exploitation More Likely" in the MSRC Security Update Guide. Sources collectively identify 12–14 CVEs with this assessment this month; the table below covers those confirmed across two or more vendor analyses:

| CVE | CVSS | Product | Title |
|---|---|---|---|
| CVE-2026-41103 | 9.1 | Microsoft SSO Plugin (Jira / Confluence) | Elevation of Privilege |
| CVE-2026-33841 | n/a | Windows Kernel | Elevation of Privilege |
| CVE-2026-40369 | n/a | Windows Kernel | Elevation of Privilege |
| CVE-2026-40361 | n/a | Microsoft Word | RCE via Preview Pane (no file open required) |
| CVE-2026-40364 | n/a | Microsoft Word | RCE via Preview Pane (no file open required) |

Not all 12–14 "Exploitation More Likely" CVEs are individually enumerated in available public analyses. Full list: [MSRC May 2026 Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-May).

## Notable themes from this month

- **Authentication stack in the crosshairs:** CVE-2026-41089 (Netlogon, CVSS 9.8) and CVE-2026-41096 (DNS Client, CVSS 9.8) are unauthenticated, network-reachable flaws at the heart of Windows domain infrastructure — a high-value pairing for lateral movement and ransomware pre-positioning against Active Directory environments.
- **Preview Pane as phishing entry point:** Two Word RCEs (CVE-2026-40361, CVE-2026-40364) trigger without opening the document, exploitable just by viewing a malicious file in Outlook's Preview Pane — both are tagged "Exploitation More Likely," significantly lowering the phishing bar.
- **Dynamics 365 on-premises scope creep:** Two Critical RCEs in Dynamics 365 on-premises — including the highest-scoring CVE this month at 9.9 (CVE-2026-42898, scope-change impact) — highlight elevated risk for organizations still running self-hosted ERP/CRM who have deprioritized cloud migration.
- **EoP dominance (~47%) reflects attacker tradecraft:** Nearly half of all patches address privilege escalation, consistent with the well-established pattern of combining a low-privilege initial access with a local kernel or service EoP to reach SYSTEM. The two Windows Kernel EoPs both carry "Exploitation More Likely" ratings.
- **"Zero-day-free" ≠ no active exploitation:** CVE-2026-42897 was exploited in the wild before CISA confirmed it on 15 May — illustrating that the absence of a zero-day designation at release time does not guarantee all patched flaws were unknown to attackers. CISA KEV additions in the days following Patch Tuesday should be treated as supplemental prioritization signals.

---

## Sources

- [BleepingComputer — Microsoft May 2026 Patch Tuesday fixes 120 flaws, no zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-may-2026-patch-tuesday-fixes-120-flaws-no-zero-days/)
- [Tenable — May 2026 Microsoft Patch Tuesday Addresses 118 CVEs (CVE-2026-41103)](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103)
- [Qualys — Microsoft and Adobe Patch Tuesday, May 2026 Security Update Review](https://blog.qualys.com/vulnerabilities-threat-research/2026/05/12/microsoft-patch-tuesday-may-2026-security-update-review)
- [CrowdStrike — May 2026 Patch Tuesday: Updates and Analysis](https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-may-2026/)
- [CybersecurityNews — Microsoft Patch Tuesday May 2026 – 120 Vulnerabilities Fixed, Including 29 Critical RCE Flaws](https://cybersecuritynews.com/microsoft-patch-tuesday-may-2026/)
- [The Hacker News — Microsoft Patches 138 Vulnerabilities, Including DNS and Netlogon RCE Flaws](https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html)
- [The Register — Doozy of a Patch Tuesday includes 30 critical Microsoft CVEs](https://www.theregister.com/patches/2026/05/13/doozy-of-a-patch-tuesday-includes-30-critical-microsoft-cves/5239224)
- [Cisco Talos — Microsoft Patch Tuesday for May 2026 — Snort rules and prominent vulnerabilities](https://blog.talosintelligence.com/microsoft-patch-tuesday-may-2026/)
- [SC Media — Patch Tuesday: No zero days among 137 Microsoft CVEs, 4 Word RCEs](https://www.scworld.com/news/patch-tuesday-no-zero-days-among-137-microsoft-cves-4-word-rces)
- [Zero Day Initiative — The May 2026 Security Update Review](https://www.thezdi.com/blog/2026/5/12/the-may-2026-security-update-review)
- [Krebs on Security — Patch Tuesday, May 2026 Edition](https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition/)
- [Malwarebytes — May 2026 Patch Tuesday: no zero-days but plenty to fix](https://www.malwarebytes.com/blog/news/2026/05/may-2026-patch-tuesday-no-zero-days-but-plenty-to-fix)
- [Help Net Security — Microsoft May 2026 Patch Tuesday: Many fixes, but no zero-days](https://www.helpnetsecurity.com/2026/05/12/microsoft-may-2026-patch-tuesday/)
- [CISA — Adds One Known Exploited Vulnerability to Catalog (CVE-2026-42897, 15 May 2026)](https://www.cisa.gov/news-events/alerts/2026/05/15/cisa-adds-one-known-exploited-vulnerability-catalog)
- [NVD — CVE-2026-41089 (Windows Netlogon RCE)](https://nvd.nist.gov/vuln/detail/CVE-2026-41089)
- [NVD — CVE-2026-41096 (Windows DNS Client RCE)](https://nvd.nist.gov/vuln/detail/CVE-2026-41096)
- [NVD — CVE-2026-42897 (Exchange OWA XSS)](https://nvd.nist.gov/vuln/detail/CVE-2026-42897)
- [MSRC — May 2026 Security Updates Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-May)

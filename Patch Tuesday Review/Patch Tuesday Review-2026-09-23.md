---
layout:
  width: wide
---

# Microsoft Patch Tuesday Review — September 2026

_Generated 2026-09-23_

## Summary

- **Total CVEs patched:** 974 (record-breaking — the largest Patch Tuesday release in Microsoft history)
- **Customer-actionable CVEs:** ~964 (excludes ~10 cloud-service-only fixes requiring no customer action)
- **Zero-days exploited in the wild:** 2 (CVE-2026-85880, CVE-2026-81963)
- **Publicly disclosed (unpatched before release):** 0
- **Critical severity:** 113
- **Important severity:** 860
- **Edge / Chromium CVEs:** ~46 (shipped via Edge's own updater alongside this release)
- **Wormable RCE bugs (no auth, no click):** ~20, spanning DHCP Server, Active Directory, DNS Server, SMB client, Netlogon, NFS, RRAS, and Message Queuing

### Breakdown by type

| Vulnerability Type | Count |
|---|---|
| Elevation of Privilege | 438 |
| Remote Code Execution | 258 |
| Information Disclosure | 173 |
| Denial of Service | 56 |
| Security Feature Bypass | 19 |
| Spoofing | 16 |
| Tampering | 13 |
| Edge – Chromium | ~46 |

---

## Exploited in the Wild

Both zero-days are local privilege-escalation flaws rated **Important (CVSS 7.8)**. Neither requires user interaction beyond the attacker already having low-privilege code execution. CISA added both to its KEV catalog on 2026-09-08 with a **September 22, 2026** remediation deadline for US federal civilian agencies (BOD 22-01).

| CVE | CVSS | Criticality | Title | Product | Customer Action | CISA KEV Deadline |
|---|---|---|---|---|---|---|
| CVE-2026-85880 | 7.8 | Important | Windows Advanced Local Procedure Call (ALPC) Elevation of Privilege | Windows (all supported) | **Required** | 2026-09-22 |
| CVE-2026-81963 | 7.8 | Important | Windows Update Stack Elevation of Privilege | Windows (all supported) | **Required** | 2026-09-22 |

**CVE-2026-85880 detail:** Heap-based buffer overflow combined with an uninitialized resource in Windows ALPC. A low-privileged attacker running inside an AppContainer can exploit the flaw locally to escape the sandbox and obtain SYSTEM privileges. First ALPC EoP to be weaponized in the wild.

**CVE-2026-81963 detail:** Improper link resolution before file access ("link following") in the Windows Update Stack. A low-privileged local attacker abuses the link-following behaviour to overwrite SYSTEM-owned files and escalate to SYSTEM. First Windows Update Stack EoP zero-day confirmed exploited in the wild across seven months of patched variants.

---

## Publicly Disclosed

No CVEs in this release were publicly disclosed prior to patch availability. Multiple sources (Rapid7, Computerworld, SecurityOnline) confirmed zero publicly disclosed vulnerabilities this cycle.

| CVE | CVSS | Criticality | Title | Customer Action | Notes |
|---|---|---|---|---|---|
| — | — | — | None | — | — |

---

## Highest Rated — CVSS ≥ 8.0 or Critical

This cycle includes 113 Critical-rated vulnerabilities; 82 of the Critical bugs are Remote Code Execution flaws. The table below covers confirmed high-impact CVEs cross-referenced across at least two sources. The full 82-CVE Critical RCE list is enumerated in MSRC release notes.

| CVE | CVSS | Criticality | Title | Product | Customer Action | Notes |
|---|---|---|---|---|---|---|
| CVE-2026-69730 | 9.8 | Critical | Windows DNS Server Remote Code Execution | Windows DNS Server | Required | Use-after-free; no auth, no user interaction; wormable candidate; "Exploitation More Likely" |
| CVE-2026-69829 | 9.8 | Critical | Windows Shell Remote Code Execution | Windows Shell | Required | No user interaction required; unauthenticated remote exploitation possible |
| CVE-2026-69676 | 8.8 | Critical | Windows Kerberos Remote Code Execution | Windows Kerberos | Required | Authentication bypass by capture-replay; "Exploitation More Likely"; network-adjacent |
| CVE-2026-69852 | n/a | Critical | Windows RRAS Remote Code Execution | Windows Routing and Remote Access Service | Required | "Exploitation More Likely"; wormable-class network service |
| CVE-2026-72957 | n/a | Critical | Windows Deployment Services Remote Code Execution | Windows Deployment Services | Required | "Exploitation More Likely"; infrastructure-facing |
| CVE-2026-70585 | n/a | Critical | NFS ONCRPC XDR Driver Remote Code Execution | Services for NFS | Required | "Exploitation More Likely"; unauthenticated network path |
| CVE-2026-85880 | 7.8 | Important | Windows ALPC Elevation of Privilege | Windows | Required | **Actively exploited zero-day** (see above) |
| CVE-2026-81963 | 7.8 | Important | Windows Update Stack Elevation of Privilege | Windows | Required | **Actively exploited zero-day** (see above) |

> **Office Preview Pane exposure:** Microsoft patched 22 Critical Office vulnerabilities this cycle; 12 of them are exploitable via Preview Pane or Reading Pane — viewing a crafted document in Outlook without opening it or enabling macros is sufficient to trigger code execution.

---

## Exploitation More Likely

Microsoft assigned its **"Exploitation More Likely"** assessment to at least five CVEs this cycle. Sources (Rapid7, CrowdStrike, Talos) note the full list of tagged CVEs is larger but not fully enumerated in public write-ups:

| CVE | CVSS | Title | Product | Notes |
|---|---|---|---|---|
| CVE-2026-69730 | 9.8 | Windows DNS Server RCE | Windows DNS Server | CVSS 9.8; unauthenticated; wormable candidate |
| CVE-2026-69676 | 8.8 | Windows Kerberos RCE | Windows Kerberos | Network-adjacent; Kerberos abuse chain starter |
| CVE-2026-69852 | n/a | Windows RRAS RCE | RRAS | Perimeter-exposed remote access service |
| CVE-2026-72957 | n/a | Windows Deployment Services RCE | WDS | Infrastructure/imaging servers |
| CVE-2026-70585 | n/a | NFS ONCRPC XDR Driver RCE | Services for NFS | Unauthenticated network path to file servers |

> Sources do not enumerate the complete "Exploitation More Likely" list for this cycle. The five CVEs above are confirmed across multiple write-ups; additional entries likely exist in the MSRC release notes.

---

## Notable themes from this month

- **Record volume signals systemic code-quality debt.** 974 CVEs in a single Patch Tuesday — nearly double a typical heavy month — points to an unusually large batch (possibly held or accelerated) combined with ongoing discovery of EoP chains across Windows internals. Elevation of Privilege alone accounts for 45% (438/974) of all CVEs, suggesting broad access-control weaknesses across the OS surface area.

- **Wormable infrastructure exposure at scale.** Approximately 20 Critical RCEs require no authentication and no user interaction across DHCP, Active Directory, DNS, SMB, Netlogon, NFS, RRAS, and MSMQ — the exact components that form the backbone of enterprise networks. Any one of these on an internet-exposed or LAN-accessible server could serve as a lateral-movement multiplier without a phishing prerequisite.

- **ALPC zero-day marks AppContainer sandbox escape maturity.** CVE-2026-85880 demonstrates that attackers are actively developing post-exploitation chains that escape modern Windows sandboxes (AppContainer is the isolation model used by Microsoft Edge, Windows Store apps, and many EDR components). This indicates threat actors are operating with sophisticated post-compromise playbooks, not just initial-access capabilities.

- **Office Preview Pane as a no-click code-execution gateway.** Twelve of the 22 Critical Office patches are triggered simply by previewing a file in Outlook — no macro, no click, no warning. This zero-interaction attack surface lowers the bar for email-delivered campaigns significantly and warrants disabling Preview Pane in high-risk environments while patches are deployed.

- **Credential/authentication attack surface widened.** CVE-2026-69676 (Windows Kerberos RCE, CVSS 8.8, "Exploitation More Likely") shows that Kerberos — the authentication spine of Active Directory environments — is being researched as an RCE vector beyond classic ticket-forging. Combined with the RRAS and DNS RCEs, attackers have multiple unauthenticated network-level entry points that chain naturally into credential harvesting and domain compromise.

---

## Sources

- [SecurityWeek — Microsoft Patches Record 974 Vulnerabilities, Including Two Exploited Zero-Days](https://www.securityweek.com/microsoft-patches-record-974-vulnerabilities-including-two-exploited-zero-days/)
- [Security Affairs — Microsoft's Biggest Patch Tuesday: 974 CVEs, 2 Zero-Days and 20 Wormable Bugs](https://securityaffairs.com/198705/security/microsofts-biggest-patch-tuesday-974-cves-2-zero-days-and-20-wormable-bugs.html)
- [BleepingComputer — Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/)
- [Tenable — September 2026 Microsoft Patch Tuesday addresses 964 CVEs (CVE-2026-81963, CVE-2026-85880)](https://www.tenable.com/blog/microsofts-september-2026-patch-tuesday-addresses-964-cves-cve-2026-81963-cve-2026-85880)
- [Qualys — Microsoft and Adobe Patch Tuesday, September 2026 Security Update Review](https://blog.qualys.com/vulnerabilities-threat-research/2026/09/08/microsoft-patch-tuesday-september-2026-security-update-review)
- [CrowdStrike — September 2026 Patch Tuesday: Updates and Analysis](https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/)
- [Rapid7 — Patch Tuesday — September 2026](https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026/)
- [Cisco Talos — Microsoft Patch Tuesday for September 2026 — Snort rules and prominent vulnerabilities](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/)
- [Zero Day Initiative — The September 2026 Security Update Review](https://www.zerodayinitiative.com/blog/2026/9/8/the-september-2026-security-update-review)
- [Malwarebytes — Microsoft fixes record 964 flaws, including 2 exploited zero-days](https://www.malwarebytes.com/blog/news/2026/09/microsoft-fixes-record-964-flaws-including-2-exploited-zero-days)
- [Cybersecurity News — Massive Microsoft Patch Tuesday September 2026 - 973 Vulnerabilities Fixed, Including 2 Zero-Days](https://cybersecuritynews.com/microsoft-patch-tuesday-update-september-2026/)
- [SANS ISC — September 2026 Microsoft Patch Tuesday](https://isc.sans.edu/diary/33320)
- [SOCPrime — CVE-2026-85880 & CVE-2026-81963 Windows Zero-Days Analysis](https://socprime.com/blog/cve-2026-85880-and-cve-2026-81963-analysis/)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [MSRC — September 2026 Security Updates Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep)

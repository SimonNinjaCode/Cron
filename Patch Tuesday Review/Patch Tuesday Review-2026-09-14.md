---
layout:
  width: wide
---

# Microsoft Patch Tuesday Review — September 2026

_Generated 2026-09-14_

---

## Summary

- **Total CVEs patched:** ~973 (counts vary by vendor methodology: BleepingComputer 966, Tenable 964, majority of sources 973–974; largest Patch Tuesday on record)
- **Zero-days — exploited in the wild:** 2 (CVE-2026-81963, CVE-2026-85880) — both added to CISA KEV on Sept 8, 2026; federal remediation deadline Sept 22, 2026
- **Zero-days — publicly disclosed (not exploited):** 0
- **Critical-rated CVEs:** 113
- **Microsoft Edge / Chromium CVEs:** 0 (no new Edge patches shipped this cycle; Google patched CVE-2026-85046 in Chrome V8 on Sept 3 — not yet reflected in an Edge release)

---

### Breakdown by type

| Vulnerability Type | Count | % of Total |
|---|---|---|
| Elevation of Privilege (EoP) | 437 | ~45% |
| Remote Code Execution (RCE) | 258 | ~26% |
| Information Disclosure | 171 | ~18% |
| Denial of Service (DoS) | 56 | ~6% |
| Security Feature Bypass | 19 | ~2% |
| Spoofing | 16 | ~2% |
| Edge – Chromium | 0 | — |
| **Total (approx.)** | **~973** | |

> Counts are derived from CrowdStrike / Qualys / BleepingComputer analyses; minor variation exists across vendors due to differing inclusion criteria (ESU, advisory-only, and third-party bundled CVEs).

---

## Exploited in the Wild

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-81963 | 7.8 | Important | Windows Update Stack Elevation of Privilege Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963) |
| CVE-2026-85880 | 7.8 | Important | Windows Advanced Local Procedure Call (ALPC) Elevation of Privilege Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880) |

**Notes:**
- **CVE-2026-81963** — Improper link-resolution flaw in the Windows Update Stack allowing a local, authenticated attacker to escalate to SYSTEM. Affects Windows 11 and Windows Server 2025.
- **CVE-2026-85880** — Heap-based buffer overflow in Windows ALPC; an attacker with low-privilege code execution inside an AppContainer can escape the sandbox and escalate to SYSTEM. Affects Windows 10 and Windows Server 2012–2022.
- Both CVEs were added to the [CISA Known Exploited Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) on September 8, 2026, with a **September 22, 2026 federal remediation deadline** under BOD 22-01.

---

## Publicly Disclosed

No vulnerabilities were publicly disclosed prior to this Patch Tuesday release.

---

## Highest Rated — CVSS ≥ 8.0 or Critical

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---|---|---|---|---|
| CVE-2026-69730 | 9.8 | Critical | Windows DNS Server Remote Code Execution Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69730) |
| CVE-2026-73009 | 9.8 | Critical | Windows Secure Socket Tunneling Protocol (SSTP) Remote Code Execution Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-73009) |
| CVE-2026-69676 | 8.8 | Critical | Windows Kerberos Remote Code Execution Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69676) |
| _(21 Office Critical RCEs)_ | n/a | Critical | Microsoft Office / Outlook / Word / Excel / PowerPoint / Graphics Component RCE (batch) | Required | [MSRC Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep) |
| _(17 infrastructure RCEs)_ | n/a | Critical | Windows DHCP, MSMQ, NFS, SSTP, and related network services RCE (batch) | Required | [MSRC Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep) |

**Notable CVE details:**

- **CVE-2026-69730 (DNS Server RCE, CVSS 9.8):** Use-after-free flaw. An unauthenticated, remote attacker sends a crafted packet to exploit the flaw and achieve RCE. Domain controllers run DNS by default — compromise of DNS on a DC extends to Active Directory authentication infrastructure. Tagged **Exploitation More Likely**. Sources describe this as a spiritual successor to SigRed (CVE-2020-1350).
- **CVE-2026-73009 (SSTP RCE, CVSS 9.8):** Use-after-free in the SSTP VPN listener on TCP/443. Unauthenticated, no user interaction required. Organizations that expose SSTP-based VPN directly to the internet face perimeter-level risk with immediate lateral movement opportunity.
- **CVE-2026-69676 (Kerberos RCE, CVSS 8.8):** Authentication-bypass-by-capture-replay. A low-privileged authenticated attacker intercepts and replays a modified Kerberos authentication exchange; the server processes it as valid and executes attacker-controlled code. Requires network positioning, limiting real-world immediate exploitability somewhat.
- **Office Critical RCEs:** 22 Critical patches for Office products this month, of which **12 are exploitable via the Preview Pane or Reading Pane** — no user action beyond opening a mail client is required.
- Individual CVE IDs for the Office and broader infrastructure batch were not fully enumerated in third-party sources; consult the [MSRC September 2026 release notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep) for the complete list.

---

## Exploitation More Likely

Microsoft tagged the following CVEs with the "Exploitation More Likely" assessment (confirmed from cross-referenced sources; this list may not be exhaustive — full enumeration is in the [MSRC Security Update Guide](https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep)):

| CVE | CVSS | Title |
|---|---|---|
| CVE-2026-69730 | 9.8 | Windows DNS Server Remote Code Execution Vulnerability |

> **Note:** Sources (CrowdStrike, Tenable, Rapid7) indicate that several of the 17 unauthenticated network-reachable RCEs across DNS, DHCP, MSMQ, NFS, and SSTP were tagged "Exploitation More Likely" by Microsoft, but specific CVE IDs beyond CVE-2026-69730 were not enumerated in available third-party analyses at time of publication. Practitioners should consult the MSRC Security Update Guide directly and filter by Exploitation Assessment.

---

## Notable themes from this month

- **Record-breaking patch volume signals systemic accumulation of debt.** At ~973 CVEs — more than double the previous monthly average and ahead of the prior record of 664 from July 2026 — this release signals that Windows and Office code surface continues to expand faster than it is being hardened. A single month's patch cycle now rivals entire annual totals from a decade ago.

- **Unauthenticated RCEs across network services create perimeter-to-core attack chains.** At least 17 Critical RCEs span DNS, DHCP, MSMQ, NFS, and SSTP — all services commonly exposed at the network perimeter or reachable without credentials. The DNS RCE (CVE-2026-69730, CVSS 9.8) on domain controllers is particularly dangerous: a single unauthenticated packet can pivot from name resolution to Active Directory compromise.

- **EoP is the dominant patch class (45%), and both zero-days were EoP flaws.** Elevation of privilege is the building block of almost every multi-stage intrusion — an attacker with any code execution foothold can upgrade to SYSTEM. The exploitation of CVE-2026-81963 and CVE-2026-85880 in the wild confirms that threat actors are actively chaining EoP with other initial access methods. Patching EoP bugs is not optional even when the affected host appears low-value.

- **Office productivity suite remains a high-volume phishing entry point.** Twenty-two Critical Office RCEs this month, including 12 that trigger through the Preview or Reading Pane, mean that even cautious users who do not open attachments are exposed. The breadth of affected apps (Outlook, Word, Excel, PowerPoint, Graphics Component) limits any single-application mitigations.

- **Domain controller attack surface is uniquely concentrated.** DNS RCE on DCs, combined with Kerberos RCE (CVE-2026-69676) and the broader ALPC/Update-Stack EoP zero-days, means that all four of the highest-priority patches this month intersect with Active Directory infrastructure. Organizations should audit whether September updates have been deployed to all DCs before any other system class.

---

## Sources

- [BleepingComputer — Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/)
- [CrowdStrike — September 2026 Patch Tuesday: Updates and Analysis](https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/)
- [Qualys — Microsoft and Adobe Patch Tuesday, September 2026 Security Update Review](https://blog.qualys.com/vulnerabilities-threat-research/2026/09/08/microsoft-patch-tuesday-september-2026-security-update-review)
- [Tenable — Microsoft's September 2026 Patch Tuesday Addresses 964 CVEs](https://www.tenable.com/blog/microsofts-september-2026-patch-tuesday-addresses-964-cves-cve-2026-81963-cve-2026-85880)
- [The Hacker News — Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html)
- [SecurityWeek — Microsoft Patches Record 974 Vulnerabilities, Including Two Exploited Zero-Days](https://www.securityweek.com/microsoft-patches-record-974-vulnerabilities-including-two-exploited-zero-days/)
- [SecurityAffairs — Microsoft's Biggest Patch Tuesday: 974 CVEs, 2 Zero-Days and 20 Wormable Bugs](https://securityaffairs.com/198705/security/microsofts-biggest-patch-tuesday-974-cves-2-zero-days-and-20-wormable-bugs.html)
- [Rapid7 — Patch Tuesday - September 2026](https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026/)
- [Cisco Talos — Microsoft Patch Tuesday for September 2026 — Snort rules and prominent vulnerabilities](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/)
- [Help Net Security — September 2026 Patch Tuesday: Record patch count, 2 zero-days, and a SigRed successor](https://www.helpnetsecurity.com/2026/09/09/september-2026-patch-tuesday-zero-days-sigred-successor/)
- [Zero Day Initiative — The September 2026 Security Update Review](https://www.zerodayinitiative.com/blog/2026/9/8/the-september-2026-security-update-review)
- [SOCPrime — CVE-2026-85880 & CVE-2026-81963 Windows Zero-Days Analysis](https://socprime.com/blog/cve-2026-85880-and-cve-2026-81963-analysis/)
- [SANS ISC — September 2026 Microsoft Patch Tuesday](https://isc.sans.edu/diary/September%202026%20Microsoft%20Patch%20Tuesday/33320)
- [CyberSecurityNews — Massive Microsoft Patch Tuesday September 2026 - 973 Vulnerabilities Fixed](https://cybersecuritynews.com/microsoft-patch-tuesday-update-september-2026/)
- [MSRC — September 2026 Security Update Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep)

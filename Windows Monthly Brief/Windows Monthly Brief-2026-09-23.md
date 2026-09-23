---
layout:
  width: wide
---

# Windows Monthly Brief — August 2026
_Generated 2026-09-23_

---

## Section 1 — Windows Roadmap Features

The following features appeared or changed status on the Windows roadmap (Platform: Windows 11 PC, Feature type: Feature, Edition: Retail) during August 2026. Source: [Windows business roadmap](https://www.microsoft.com/en-us/windows/business/roadmap).

| Title | Status | Description | Target Version |
|---|---|---|---|
| Administrator protection | Rolling out | Reduces elevation-of-privilege risk by using profile separation and just-in-time administrative privileges. Off by default; enable via Microsoft Intune (OMA-URI) or Group Policy. | 24H2 / 25H2 |
| Taskbar position customization | Rolling out | Users can reposition the taskbar to the bottom, top, left, or right side of the screen. A smaller taskbar option is also available to maximize screen space. Notification badges now use the Windows accent colour instead of red. | 24H2 / 25H2 / 26H1 |
| Windows Hello ESS for external fingerprint readers | Rolling out | Enhanced Sign-in Security (ESS) support extended to external USB fingerprint sensors. Biometric processing is isolated in a secure memory space away from the OS. Previously limited to devices with built-in sensors (Copilot+ PCs). | All supported versions |
| Voice Access — Voice Isolation + Korean | Rolling out | Voice Access now filters out background speakers and ambient noise via Voice Isolation. Korean language support also added. | All supported versions |
| File Explorer file-size units | Rolling out | Details view now displays file sizes in appropriate units (KB, MB, GB) instead of always defaulting to KB. | All supported versions |
| Windows Update extended postponement | Rolling out | Users can postpone Windows Updates for up to 35 days (increased from 7 days). | 26H1 |
| Magnifier accessibility improvements | Rolling out | Magnifier gains a new screen tint option and a flexible zoom-level control to improve usability for low-vision users. | All supported versions |
| WMIC removal | **Change — August 2026** | The Windows Management Instrumentation Command-line (WMIC) utility is no longer included in Windows 11 version 24H2 and later. Organizations relying on WMIC in scripts or management tooling should migrate to PowerShell/CIM cmdlets before deploying the August cumulative update. | 24H2 / 25H2 |

> **Most notable:** **Administrator Protection** begins broad rollout in August 2026 — a meaningful security improvement that replaces always-on admin tokens with just-in-time elevation, materially reducing the attack surface for privilege-escalation exploits.

---

## Section 2 — Patch Information

Current supported retail versions covered: **26H1**, **25H2**, **24H2**.

> Note: 25H2 and 24H2 share the same cumulative update packages (same KB, separate OS build numbers). 26H1 runs on a different Windows core and ships separate KBs.
>
> ⚠️ Known issue: After installing KB5121000 (26H1 Patch Tuesday), Microsoft Teams and the new Outlook for Windows may fail to launch on ARM-based devices (e.g. Surface Pro 11, Surface Laptop 7). Resolved by the September 8, 2026 update **KB5124012**.
>
> 📅 Windows 11, version 24H2 Home/Pro end-of-support date: **October 13, 2026**.

---

### Windows 11, version 26H1 (OS Build 28000.x)

#### Patch Tuesday — Security Update

| Field | Detail |
|---|---|
| Release date | August 11, 2026 |
| KB | KB5121000 |
| OS Build | 28000.2704 |
| CVEs addressed | 421 |
| Support link | [KB5121000](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/08/kb5121000-windows-11-26h1-security-update) |

**Highlights:** TPM/EK certificate accuracy improvements; expanded Secure Boot certificate targeting; Magnifier screen-tint control; Windows Update postponement up to 35 days; Windows AI component fixes on Copilot+ PCs.

#### Non-Security Preview Update (end of month)

| Field | Detail |
|---|---|
| Release date | August 27, 2026 |
| KB | KB5120996 |
| OS Build | 28000.2804 |
| Support link | [KB5120996](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/08/kb5120996-windows-11-26h1-update) |

**Highlights:** Taskbar repositioning (bottom / top / left / right); improved Natural Voices installer reliability in Narrator settings.

---

### Windows 11, version 25H2 (OS Build 26200.x)

#### Patch Tuesday — Security Update

| Field | Detail |
|---|---|
| Release date | August 11, 2026 |
| KB | KB5121003 |
| OS Build | 26200.9168 |
| Support link | [KB5121003](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/08/kb5121003-windows-11-24h2-25h2-security-update) |

> A Hotpatch variant is also available: **KB5120994** (OS Build 26200.9106) for devices enrolled in Windows Hotpatch.

**Highlights:** 400+ CVEs addressed including 3 zero-days; Windows Hello ESS for external fingerprint readers; Voice Access Voice Isolation + Korean; File Explorer file-size units; WMIC removed; Administrator Protection rollout (gradual).

#### Non-Security Preview Update (end of month)

| Field | Detail |
|---|---|
| Release date | August 27, 2026 |
| KB | KB5120998 |
| OS Build | 26200.9278 |
| Support link | [KB5120998](https://support.microsoft.com/en-US/servicing/os/windows-11/2026/08/kb5120998-windows-11-24h2-25h2-update) |

**Highlights:** Taskbar repositioning; emoji panel GIPHY support (following Google Tenor API deprecation); improved Narrator Natural Voices setup.

---

### Windows 11, version 24H2 (OS Build 26100.x)

#### Patch Tuesday — Security Update

| Field | Detail |
|---|---|
| Release date | August 11, 2026 |
| KB | KB5121003 |
| OS Build | 26100.9168 |
| Support link | [KB5121003](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/08/kb5121003-windows-11-24h2-25h2-security-update) |

> A Hotpatch variant is also available: **KB5120994** (OS Build 26100.9106) for devices enrolled in Windows Hotpatch.

**Highlights:** Same security payload as 25H2 above. WMIC removal takes effect with this update. End-of-support approaching — October 13, 2026.

#### Non-Security Preview Update (end of month)

| Field | Detail |
|---|---|
| Release date | August 27, 2026 |
| KB | KB5120998 |
| OS Build | 26100.9278 |
| Support link | [KB5120998](https://support.microsoft.com/en-US/servicing/os/windows-11/2026/08/kb5120998-windows-11-24h2-25h2-update) |

**Highlights:** Same payload as 25H2 preview.

---

_Sources: [Microsoft Windows Roadmap](https://www.microsoft.com/en-us/windows/business/roadmap) · [Windows IT Pro Blog — August 2026](https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-news-you-can-use-august-2026/4552394) · [KB5121000 (26H1)](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/08/kb5121000-windows-11-26h1-security-update) · [KB5121003 (25H2/24H2)](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/08/kb5121003-windows-11-24h2-25h2-security-update) · [KB5120996 preview (26H1)](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/08/kb5120996-windows-11-26h1-update) · [KB5120998 preview (25H2/24H2)](https://support.microsoft.com/en-US/servicing/os/windows-11/2026/08/kb5120998-windows-11-24h2-25h2-update)_

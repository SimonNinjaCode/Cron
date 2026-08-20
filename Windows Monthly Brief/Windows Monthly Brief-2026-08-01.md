# Windows Monthly Brief — July 2026
_Generated 2026-08-01_

---

## Section 1 — Windows Roadmap Features

> **Note:** The Windows roadmap page (`microsoft.com/en-us/windows/business/roadmap`) is dynamically rendered and was not directly accessible. Features below are derived from official Microsoft patch notes, the Windows IT Pro Blog, and corroborating tech press coverage of July 2026 releases. All features listed here reached Rolling out status via the July 14 or July 28, 2026 updates.

### Features that appeared or changed status in July 2026

| Feature | Status | Description | Target Version |
|---|---|---|---|
| Point-in-time Restore | Rolling out | New system recovery tool that automatically creates restore points (settings, files, apps via VSS) from the last 72 hours, allowing rapid rollback to a known-good state. Enabled by default on Home and Pro; requires at least 200 GB of storage. | 24H2 / 25H2 |
| Windows Update Pause Calendar | Rolling out | Replaces the fixed pause-duration toggles with a calendar picker. Users can defer updates by choosing a specific end date, up to 35 days out. Designed to give IT-adjacent consumers more control without requiring a management policy. | 24H2 / 25H2 |
| Windows Hello ESS — Peripheral Fingerprint Sensors | Rolling out | Extends Enhanced Sign-in Security (ESS) beyond built-in fingerprint readers to USB/Bluetooth peripheral sensors. Adds Copilot+ PCs and conventional desktops to the ESS-capable device pool. | 24H2 / 25H2 |
| Screen Tint (Color Overlay) | Rolling out | Full-screen color overlay to reduce eye strain. Available in Accessibility settings; complements Night Light with customizable tint color and opacity. | 24H2 / 25H2 / 26H1 |
| Widgets — Reduced Interruptions | Rolling out | Widgets no longer open on hover; taskbar badges and notification counts are minimized by default. | 24H2 / 25H2 |
| Voice Isolation for Voice Access | Rolling out | Adds acoustic noise-suppression preprocessing to Voice Access, separating the primary speaker from background noise and other voices to improve recognition accuracy. | 24H2 / 25H2 |
| Internet Printing Protocol (IPP) as Default | Rolling out | New printer installations now default to IPP class drivers rather than vendor-supplied drivers, where the device supports it. Falls back to legacy drivers for unsupported hardware. | 24H2 / 25H2 |
| File Explorer Improvements | Rolling out | File sizes now displayed with human-readable units (KB / MB / GB) in Details view. Navigation performance improved; search now handles misspelled or partial app names. | 24H2 / 25H2 |
| Magnifier Enhancements | Rolling out | Users can type a zoom percentage directly into the Magnifier window and change it in increments, replacing the slider-only interaction. | 24H2 / 25H2 |
| Bluetooth Stack Updates | Rolling out | Faster AirPods pairing, improved Beats Studio Pro microphone reliability, and steadier LE Audio. Microsoft calls this the largest Bluetooth improvement in Windows 11 to date. | 24H2 / 25H2 |
| Taskbar Position & Size Options | Rolling out | Additional customization controls for taskbar position (bottom-anchored) and height in Settings. | 24H2 / 25H2 |
| Voice Typing — French, German, Spanish | Rolling out | Voice typing language support expanded to French, German, and Spanish on 26H1 devices. | 26H1 only |
| Copilot Quick Actions in File Explorer (Work/School) | Rolling out | Copilot quick-action shortcuts in File Explorer context menus now work for Entra ID (work and school) accounts, not only personal Microsoft accounts. | 26H1 only |
| AI Model Memory Management (32 GB+ RAM) | Rolling out | Improved memory scheduling for devices with more than 32 GB of RAM to support larger local AI/LLM inference workloads. | 26H1 only |

---

## Section 2 — Patch Information

**Covered versions:** Windows 11 26H1 · 25H2 · 24H2  
**Note on 23H2:** Home and Pro editions of 23H2 reached end of servicing on 2025-11-11. Enterprise and Education editions continue to receive security updates until **2026-11-10**. A Patch Tuesday update (KB5099414, build 22631.7376) was released on July 14, 2026. No optional preview update was published for 23H2 in July 2026.

---

### Windows 11 version 26H1 (OS build 28000)

_Available from 2026-02-10. Scoped to new devices with select silicon; not offered as an in-place upgrade from 24H2/25H2 on existing hardware._  
End of updates — Home/Pro: **2028-03-14** · Enterprise/Education: **2029-03-13**

#### Patch Tuesday — July 14, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5101649](https://support.microsoft.com/help/5101649) |
| Release date | July 14, 2026 |
| OS Build | 28000.2525 |
| Type | Cumulative security update (2026-07 B) |
| Highlights | 570 CVEs patched (3 zero-days); fixes CVE-2026-58634 (DWM elevation-of-privilege, high severity); SHA-2 thumbprint support for trusted RDP publishers; Secure Boot certificate deployment expansion. |

#### Non-Security Preview — July 28, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5101681](https://support.microsoft.com/help/5101681) |
| Release date | July 28, 2026 |
| OS Build | 28000.2608 |
| Type | Optional cumulative non-security preview (2026-07 D) |
| Highlights | Screen Tint accessibility overlay; voice typing in French/German/Spanish; Copilot quick actions for work/school in File Explorer; AI memory management for 32 GB+ RAM devices; Windows Update Calendar pause. |

---

### Windows 11 version 25H2 (OS build 26200)

_Available from 2025-09-30._  
End of updates — Home/Pro: **2027-10-12** · Enterprise/Education: **2028-10-10**

#### Patch Tuesday — July 14, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5101650](https://support.microsoft.com/help/5101650) |
| Release date | July 14, 2026 |
| OS Build | 26200.8875 |
| Type | Cumulative security update (2026-07 B) |
| Highlights | 570 CVEs (3 zero-days); SHA-2 RDP thumbprint support; curl upgraded to 8.21.0; Secure Boot certificate rollout; Point-in-time Restore enabled broadly; Windows Update Pause Calendar. |

#### Out-of-band — July 18, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5121767](https://support.microsoft.com/help/5121767) |
| Release date | July 18, 2026 |
| OS Build | 26200.8894 |
| Type | Out-of-band (OOB) update |

#### Non-Security Preview — July 28, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5101684](https://support.microsoft.com/help/5101684) |
| Release date | July 28, 2026 |
| OS Build | 26200.8973 |
| Type | Optional cumulative non-security preview (2026-07 D) |
| Highlights | Windows Hello ESS for peripheral fingerprint sensors; Start menu/taskbar performance improvements; file sizes in MB/GB in File Explorer; Secure Boot certificate updates; fixes for File History false credential errors, DFS mapped-drive Internet Zone misclassification, and newly-enrolled devices stuck in noncompliant state. |

---

### Windows 11 version 24H2 (OS build 26100)

_Available from 2024-10-01. Also serves as Windows 11 Enterprise LTSC 2024._  
End of updates — Home/Pro: **2026-10-13** · Enterprise/Education: **2027-10-12** · LTSC: **2029-10-09**

> 24H2 and 25H2 share the same cumulative update packages (KB5101650 and KB5101684) in July 2026.

#### Patch Tuesday — July 14, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5101650](https://support.microsoft.com/help/5101650) |
| Release date | July 14, 2026 |
| OS Build | 26100.8875 |
| Type | Cumulative security update (2026-07 B) |
| Highlights | Same as 25H2 above (shared package). |

#### Out-of-band — July 18, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5121767](https://support.microsoft.com/help/5121767) |
| Release date | July 18, 2026 |
| OS Build | 26100.8894 |
| Type | Out-of-band (OOB) update |

#### Non-Security Preview — July 28, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5101684](https://support.microsoft.com/help/5101684) |
| Release date | July 28, 2026 |
| OS Build | 26100.8973 |
| Type | Optional cumulative non-security preview (2026-07 D) |
| Highlights | Same as 25H2 above (shared package). |

---

### Windows 11 version 23H2 (OS build 22631) — Enterprise/Education only

_Home/Pro: end of servicing 2025-11-11. Enterprise/Education: **2026-11-10**._

#### Patch Tuesday — July 14, 2026

| Field | Detail |
|---|---|
| KB Article | [KB5099414](https://support.microsoft.com/help/5099414) |
| Release date | July 14, 2026 |
| OS Build | 22631.7376 |
| Type | Cumulative security update (2026-07 B) — Enterprise/Education only |
| Highlights | Security fixes aligned with July Patch Tuesday; fixes for Office and OneDrive regressions introduced in June. |

_No optional non-security preview update was published for 23H2 in July 2026._

---

*Sources: [Microsoft Learn — Windows 11 release information](https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information) · [KB5101650](https://support.microsoft.com/help/5101650) · [KB5101649](https://support.microsoft.com/help/5101649) · [KB5101684](https://support.microsoft.com/help/5101684) · [KB5101681](https://support.microsoft.com/help/5101681) · [KB5099414](https://support.microsoft.com/help/5099414) · [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5101650-and-kb5099414-cumulative-updates-released/) · [Windows Central](https://www.windowscentral.com/microsoft/windows-11/windows-11s-massive-july-2026-update-shows-how-ai-is-changing-patch-tuesday)*

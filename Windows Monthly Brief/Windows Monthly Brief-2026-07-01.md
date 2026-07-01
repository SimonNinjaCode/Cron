# Windows Monthly Brief — June 2026
_Generated 2026-07-01_

## Section 1 — Windows Roadmap Features

Features that appeared or changed status in **June 2026** (Platform: Windows 11 PC · Feature type: Feature · Edition: Retail).

Source: [Microsoft Windows Roadmap](https://www.microsoft.com/en-us/windows/business/roadmap)

### Rolling Out

| Feature | Status | Description | Target Version |
|---|---|---|---|
| **Low Latency Profile** | Rolling out | Temporarily boosts processor frequency for 1–3 s during interactive tasks (opening apps, Start menu, File Explorer, context menus), delivering up to 40% faster app launch and 70% faster interaction times with system features. | June 2026 Update |
| **Shared Audio (Bluetooth LE)** | Rolling out | Allows two Bluetooth devices to connect simultaneously to the same Windows 11 PC via Bluetooth LE Audio broadcast technology, so two users can share audio from a single device. | June 2026 Update |
| **Multi-App Camera** | Rolling out | Enables multiple applications to access and use the same camera stream simultaneously, allowing concurrent video calls alongside recording or streaming apps without blocking each other. | June 2026 Update |
| **Improved NPU Monitoring** | Rolling out | Adds per-app Neural Processing Unit (NPU) usage tracking in the Task Manager Processes section, providing granular visibility into AI-accelerated workloads. | June 2026 Update |
| **Enhanced Windows Hello** | Rolling out | Optimises the Windows Biometric (WinBio) service to reduce authentication latency when the PC resumes from Modern Standby. | June 2026 Update |
| **Secure Boot Certificate Refresh** | Rolling out | Replaces expiring 2011-era Secure Boot certificates with 2023-issued certificates ahead of their June 2026 expiry date. | June 2026 Update |

### In Preview

| Feature | Status | Description | Target Version |
|---|---|---|---|
| **Point-in-Time Restore** | In preview | Lets users quickly roll back their PC to a recent automatic restore point while preserving installed apps, settings, and personal files. | 26H2 (Experimental) |
| **Screen Tint** | In preview | System-wide colour overlay accessibility feature designed to reduce eye strain on bright or highly saturated displays. | 26H2 (Experimental) |
| **Improved Search (typo tolerance)** | In preview | Enhanced search algorithm that better handles typos, missing letters, extra characters, and partial app names for more accurate results. | Build 26300.8687+ |
| **Custom Account Folder Naming** | In preview | Allows users to set a custom name for their account folder during the out-of-box experience (OOBE) setup. | June 2026 Update |

---

## Section 2 — Patch Information

Covers the three currently supported Windows 11 retail versions as of June 2026: **26H1** (newest, released February 2026), **25H2** (released September 2025), and **24H2** (released October 2024).

> **23H2 status note:** Windows 11 23H2 Home/Pro reached end of support before June 2026. Enterprise/Education support continues until November 10, 2026. The June 9 security update KB5093998 (OS Build 22631.7219) was issued for Enterprise/Education customers on that version.

### Windows 11 26H1 (OS Build 28000.x)

_Released: February 10, 2026 · End of support (Home/Pro): March 14, 2028 · (Enterprise/Education): March 13, 2029_

| Update Type | Release Date | KB Number | OS Build | Link |
|---|---|---|---|---|
| Security (Patch Tuesday) | 2026-06-09 | KB5095051 | 28000.2269 | [support.microsoft.com/help/5095051](https://support.microsoft.com/help/5095051) |
| Non-security preview | 2026-06-23 | KB5095091 | 28000.2340 | [support.microsoft.com](https://support.microsoft.com/en-us/topic/june-23-2026-kb5095091-os-build-28000-2340-preview-255237ff-1236-4ad7-a087-251eb0cf8869) |

**June Patch Tuesday security highlights:** 200 CVEs addressed across Microsoft products, including 3 actively exploited zero-days — *GreenPlasma* and *YellowKey* (both BitLocker bypass vulnerabilities). The Secure Boot certificate rotation was also bundled into this update. Additional quality improvements include shared audio over Bluetooth LE, multi-app camera support, and Windows Search returning results from 2 characters instead of 3.

**June preview highlights:** Point-in-time restore, calendar experience in Windows Update Settings (allows pausing updates up to 35 days), and GIPHY integration in the emoji panel.

_Update history page: [Windows 11 version 26H1 update history](https://support.microsoft.com/en-us/topic/windows-11-version-26h1-update-history-253c73cd-cab1-4bfd-94dc-76c452273fc9)_

---

### Windows 11 25H2 (OS Build 26200.x)

_Released: September 30, 2025 · End of support (Home/Pro): October 12, 2027 · (Enterprise/Education): October 10, 2028_

| Update Type | Release Date | KB Number | OS Build | Link |
|---|---|---|---|---|
| Security (Patch Tuesday) | 2026-06-09 | KB5094126 | 26200.8655 | [support.microsoft.com](https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737) |
| Non-security preview | 2026-06-23 | KB5095093 | 26200.8737 | [support.microsoft.com](https://support.microsoft.com/en-us/topic/june-23-2026-kb5095093-os-builds-26200-8737-and-26100-8737-preview-0e2a20f2-cf9e-46f8-9f08-e6996220882d) |

---

### Windows 11 24H2 (OS Build 26100.x)

_Released: October 1, 2024 · End of support (Home/Pro): October 13, 2026 · (Enterprise/Education): October 12, 2027 · Also available as LTSC_

| Update Type | Release Date | KB Number | OS Build | Link |
|---|---|---|---|---|
| Security (Patch Tuesday) | 2026-06-09 | KB5094126 | 26100.8655 | [support.microsoft.com](https://support.microsoft.com/en-us/topic/june-9-2026-kb5094126-os-builds-26200-8655-and-26100-8655-1a9bcba6-5f53-4075-8156-fe11ac631737) |
| Non-security preview | 2026-06-23 | KB5095093 | 26100.8737 | [support.microsoft.com](https://support.microsoft.com/en-us/topic/june-23-2026-kb5095093-os-builds-26200-8737-and-26100-8737-preview-0e2a20f2-cf9e-46f8-9f08-e6996220882d) |

> **Note:** 25H2 and 24H2 share KB numbers (KB5094126 for Patch Tuesday; KB5095093 for the preview). The OS build base differentiates the two versions (26200.x vs 26100.x). The linked KB articles cover both versions in a single page.

> **24H2 Home/Pro approaching EOS:** Home and Pro editions of 24H2 reach end of support on **October 13, 2026** — organisations on these editions should plan to upgrade to 25H2 or 26H1 before then.

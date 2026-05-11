# Windows Monthly Brief — April 2026
_Generated 2026-05-11_

---

## Section 1 — Windows Roadmap Features

> **Source note:** The Windows roadmap page (microsoft.com/en-us/windows/business/roadmap) is JavaScript-rendered and not directly machine-readable. Features below are drawn from the official Microsoft Windows IT Pro Blog ("Windows news you can use: April 2026") and April 2026 KB release notes, cross-referenced against the roadmap's Platform = Windows 11 PC / Feature type = Feature / Edition = Retail filter criteria.

The following features appeared or changed status in April 2026:

### Launched (April 14, 2026 — KB5083769)

| Feature | Status | Description | Target Version |
|---|---|---|---|
| **Narrator + Copilot on all PCs** | Launched | Narrator image descriptions (Narrator + Ctrl + D / Ctrl + S) now work via Copilot on all Windows 11 PCs, not only Copilot+ hardware. | 24H2 / 25H2 |
| **Smart App Control — no reinstall required** | Launched | Smart App Control can now be toggled on or off without a clean Windows installation. Access via Settings → Windows Security → App & Browser Control → Smart App Control settings. | 24H2 / 25H2 |
| **RDP file security warnings** | Launched | Windows now displays all requested connection settings before an RDP session begins; a one-time security alert is shown when an .rdp file is opened for the first time, mitigating phishing risk. | 24H2 / 25H2 |
| **Secure Boot certificate status in Windows Security** | Launched | The Windows Security app now displays the status of Secure Boot certificate updates, with badges and notifications. Quality updates include expanded high-confidence device targeting for certificate delivery. | 24H2 / 25H2 |
| **AI component upgrade (v1.2603.377.0)** | Launched | Core AI modules — Image Search, Content Extraction, Semantic Analysis, Settings Model — updated to version 1.2603.377.0 for enhanced local intelligence. | 24H2 / 25H2 |
| **Pen tail button → Copilot key app** | Launched | The pen tail button can now be mapped to the same app as the Copilot key via Pen settings. | 24H2 / 25H2 |
| **RemoveMicrosoftCopilotApp policy** | Launched | New enterprise policy allows organizations to uninstall the Microsoft Copilot app non-disruptively. | 24H2 / 25H2 |
| **Settings Home device information card redesign** | Launched | Simplified device specifications card on Settings Home; consistent flow through to Settings → System → About. | 24H2 / 25H2 |
| **Voice typing animations on touch keyboard** | Launched | Voice typing animations now appear directly on the touch keyboard dictation key instead of a separate overlay. | 24H2 / 25H2 |
| **File Explorer — Voice Typing in rename** | Launched | Windows logo key + H (Voice Typing) now works while renaming a file in File Explorer. | 24H2 / 25H2 |
| **Emoji 16.0 support** | Launched | Full Emoji 16.0 character set support added. | 26H1 |

### Rolling Out (April 30, 2026 — KB5083631 preview)

| Feature | Status | Description | Target Version |
|---|---|---|---|
| **Xbox Mode** | Rolling out | Full-screen gaming interface launching all games front and center. Accessible from the Xbox app, Game Bar settings, or Win + F11. Designed for controller use. | 24H2 / 25H2 |
| **FAT32 formatting limit raised to 2 TB** | Rolling out | Command-line FAT32 format cap raised from 32 GB to 2 TB. | 24H2 / 25H2 |
| **File Explorer — additional archive formats** | Rolling out | Adds .uu, .cpio, .xar, and .nupkg (NuGet) to the supported archive format list. | 24H2 / 25H2 |
| **File Explorer — View/Sort preferences preserved** | Rolling out | View and sort preferences are now remembered in folders like Downloads and Documents when apps launch File Explorer directly to those locations. | 24H2 / 25H2 |
| **AI Taskbar Agents progress indicator** | Rolling out | New taskbar progress monitoring for first- and third-party AI agents (e.g. Researcher in Microsoft 365 Copilot). | 24H2 / 25H2 |
| **Haptic feedback for window actions** | Rolling out | Supported input devices now provide haptic feedback when snapping or resizing windows, or aligning objects in PowerPoint. | 24H2 / 25H2 |
| **Remove pre-installed Microsoft Store apps via policy** | Rolling out | Organizations can now use policy to remove select pre-installed Store apps on Windows 11 24H2 and 25H2 devices. | 24H2 / 25H2 |
| **Startup app launch performance improvement** | Rolling out | Improved launch times for apps listed under Settings → Apps → Startup immediately after login. | 24H2 / 25H2 |
| **Delivery Optimization memory usage improvement** | Rolling out | Reduced memory footprint for Delivery Optimization background service. | 24H2 / 25H2 |

---

## Section 2 — Patch Information

> **Supported versions covered:** Windows 11 26H1 (ARM hardware-restricted), 25H2, and 24H2 — the three current supported mainstream releases. Windows 11 23H2 (Home/Pro) reached end of service November 11, 2025; Enterprise/Education editions remain supported through November 10, 2026 and are included as an addendum. Windows 11 22H2 reached end of service October 14, 2025 and receives no further updates.
>
> **Patch Tuesday (April 2026):** 2nd Tuesday = **April 14, 2026**
> **Preview update:** **April 30, 2026**

---

### Windows 11 version 26H1

> Hardware-restricted release. Available only as a preinstalled experience on select new ARM devices (Snapdragon X2 Plus, Elite, and Extreme). Not offered to existing Intel/AMD systems.

#### Security Update — Patch Tuesday (April 14, 2026)

| Field | Value |
|---|---|
| **Release date** | April 14, 2026 |
| **KB number** | KB5083768 |
| **OS build** | 28000.1836 |
| **Support link** | https://support.microsoft.com/en-us/topic/april-14-2026-kb5083768-os-build-28000-1836-839e4a25-d979-4158-b70c-182333045883 |

**Key changes:** Patches critical kernel elevation-of-privilege CVEs (CVE-2026-0847, CVE-2026-0848). Adds Secure Boot certificate status to Windows Security app. Adds Emoji 16.0. Expands Windows Backup automatic restoration. Improves SMB compression over QUIC reliability. Blocks third-party drivers with known vulnerabilities (may affect VSS-dependent backup tools).

#### Non-Security Preview Update (April 30, 2026)

| Field | Value |
|---|---|
| **Release date** | April 30, 2026 |
| **KB number** | KB5083806 |
| **OS build** | 28000.1896 |
| **Support link** | https://support.microsoft.com/en-us/topic/april-30-2026-kb5083806-os-build-28000-1896-preview-f56e03d6-ea3a-4fe4-a028-c7b9dbf0c441 |

**Key changes:** Narrator + Copilot image descriptions on all Windows 11 devices. Smart App Control togglable without clean install. Fixes Remote Desktop Connection security warning dialog in multi-monitor/mixed-scaling scenarios. Servicing stack quality improvements.

---

### Windows 11 version 25H2

> Shares cumulative update packages with 24H2. Each KB targets both OS builds simultaneously.

#### Security Update — Patch Tuesday (April 14, 2026)

| Field | Value |
|---|---|
| **Release date** | April 14, 2026 |
| **KB number** | KB5083769 |
| **OS build** | 26200.8246 |
| **Support link** | https://support.microsoft.com/en-us/topic/april-14-2026-kb5083769-os-builds-26200-8246-and-26100-8246-22f90ae5-9f26-40ac-9134-6a586a71163b |

**Key changes:** Smart App Control toggleable without reinstall. Narrator extended to all Windows 11 PCs via Copilot. RDP file security warnings before session start. Secure Boot certificate status in Windows Security. AI component upgrade to v1.2603.377.0. SMB over QUIC reliability fix. "Reset this PC" failure fixed (post-March 2026 hotpatch regression). Pen tail button → Copilot key mapping. New RemoveMicrosoftCopilotApp enterprise policy.

**Known issues:** BitLocker recovery key may be required on first restart for devices with non-recommended BitLocker Group Policy configurations. VSS-dependent third-party backup tools (Acronis, Macrium Reflect, NinjaOne Backup, UrBackup Server) may fail due to driver blocklist updates.

#### Non-Security Preview Update (April 30, 2026)

| Field | Value |
|---|---|
| **Release date** | April 30, 2026 |
| **KB number** | KB5083631 |
| **OS build** | 26200.8328 |
| **Support link** | https://support.microsoft.com/en-us/topic/april-30-2026-kb5083631-os-builds-26200-8328-and-26100-8328-preview-db6b5d64-ff7e-4fea-8f47-bde66c97d759 |

**Key changes:** Xbox Mode on all Windows 11 PCs. FAT32 format limit raised to 2 TB. File Explorer gains .uu/.cpio/.xar/.nupkg archive support; View/Sort preferences preserved; Voice Typing in rename. Taskbar AI Agents progress indicator. Haptic feedback for window snap/resize. Startup app performance improvement. Delivery Optimization memory reduction. Kerberos fix for Remote Credential Guard RDP sessions (error 0xc000009a). Policy to remove pre-installed Store apps. Multiple Explorer.exe reliability fixes.

---

### Windows 11 version 24H2

> Shares cumulative update packages with 25H2. Each KB targets both OS builds simultaneously.

#### Security Update — Patch Tuesday (April 14, 2026)

| Field | Value |
|---|---|
| **Release date** | April 14, 2026 |
| **KB number** | KB5083769 |
| **OS build** | 26100.8246 |
| **Support link** | https://support.microsoft.com/en-us/topic/april-14-2026-kb5083769-os-builds-26200-8246-and-26100-8246-22f90ae5-9f26-40ac-9134-6a586a71163b |

**Key changes:** Identical to 25H2 above (same KB). Smart App Control toggleable without reinstall. Narrator extended to all Windows 11 PCs. RDP file security warnings. Secure Boot certificate status in Windows Security. AI component upgrade. SMB over QUIC reliability. Reset this PC fix. Pen tail button mapping. RemoveMicrosoftCopilotApp policy.

**Known issues:** BitLocker recovery key on first restart (narrow managed configurations). VSS-dependent backup tools may fail (driver blocklist).

#### Non-Security Preview Update (April 30, 2026)

| Field | Value |
|---|---|
| **Release date** | April 30, 2026 |
| **KB number** | KB5083631 |
| **OS build** | 26100.8328 |
| **Support link** | https://support.microsoft.com/en-us/topic/april-30-2026-kb5083631-os-builds-26200-8328-and-26100-8328-preview-db6b5d64-ff7e-4fea-8f47-bde66c97d759 |

**Key changes:** Identical to 25H2 above (same KB). Xbox Mode, FAT32 2 TB limit, File Explorer archive formats, Taskbar AI Agents, haptic feedback, startup performance, Delivery Optimization, Kerberos RDP fix, Store app removal policy.

---

### Windows 11 version 23H2 — Addendum (Enterprise/Education only)

> Windows 11 23H2 Home and Pro reached end of service **November 11, 2025** — no updates. Enterprise and Education editions remain supported through **November 10, 2026**.

#### Security Update — Patch Tuesday (April 14, 2026)

| Field | Value |
|---|---|
| **Release date** | April 14, 2026 |
| **KB number** | KB5082052 |
| **OS build** | 22631.6936 |
| **Editions** | Enterprise and Education only |
| **Support link** | https://support.microsoft.com/en-us/topic/april-14-2026-kb5082052-os-build-22631-6936-adba0a59-beb2-4494-87f1-87b5aba38c8e |

**Key changes:** Critical kernel vulnerability patches (CVE-2026-0847, CVE-2026-0848). Windows Defender Application Guard instability fix. Windows Hello for Business fix on ARM64. Memory management fix (BSOD 0x0000001A). Windows Search indexing performance fix. Microsoft account sign-in fix ("no Internet" error). BitLocker recovery fix after Secure Boot updates. SMB over QUIC improvement. Smart App Control toggleable without reinstall. Narrator + Copilot on all PCs. Secure Boot certificate status in Windows Security.

> No optional preview update was released for 23H2 in April 2026.

---

### Windows 11 version 22H2 — End of Service

Windows 11 22H2 reached end of service **October 14, 2025**. No updates were released in April 2026. Devices on this version should upgrade to a supported release.

---

## Update Summary Table

| Version | Patch Tuesday KB | OS Build | Preview KB | OS Build |
|---|---|---|---|---|
| 26H1 | KB5083768 (Apr 14) | 28000.1836 | KB5083806 (Apr 30) | 28000.1896 |
| 25H2 | KB5083769 (Apr 14) | 26200.8246 | KB5083631 (Apr 30) | 26200.8328 |
| 24H2 | KB5083769 (Apr 14) | 26100.8246 | KB5083631 (Apr 30) | 26100.8328 |
| 23H2 (Ent/Edu) | KB5082052 (Apr 14) | 22631.6936 | — | — |
| 22H2 | End of service | — | — | — |

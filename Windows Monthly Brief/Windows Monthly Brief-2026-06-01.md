# Windows Monthly Brief — May 2026
_Generated 2026-06-01_

---

## Section 1 — Windows Roadmap Features

> **Note:** The Windows Roadmap page (`microsoft.com/en-us/windows/business/roadmap`) is JavaScript-rendered and could not be fetched directly. Feature statuses below are sourced from Microsoft's official Windows IT Pro Blog, Tech Community posts, and KB release documentation for May 2026.

The following features appeared or changed to **Rolling out** / **In preview** status during May 2026, targeting Windows 11 PC (Retail edition):

### Features Rolling Out

| # | Feature | Status | Description | Target Version |
|---|---------|--------|-------------|----------------|
| 1 | **Xbox Mode** | Rolling out (CFR) | Console-like full-screen gaming interface. Enter via the Xbox app, Game Bar settings, or Win + F11. Minimises background activity for games. Released via Controlled Feature Rollout — not all devices receive it simultaneously. | 25H2, 24H2 (KB5089549); 26H1 (KB5089548) |
| 2 | **Shared Audio** | Rolling out | Enables two people to listen simultaneously from a single PC using Bluetooth LE Audio broadcast technology. Activated via Quick Settings → Shared audio → select two paired LE Audio devices → Start sharing. | 25H2/24H2 (KB5089573 preview, ships June Patch Tuesday); 26H1 (KB5089570 preview) |
| 3 | **Multi-App Camera** | Rolling out | Multiple applications can access the same camera stream simultaneously. Includes a Basic Camera mode for simplified/troubleshooting scenarios. Configurable via Group Policy under Windows Components > Camera > Configure Camera Options. | 25H2/24H2 (KB5089573 preview); 26H1 (KB5089548) |
| 4 | **Task Manager — NPU Visibility** | Rolling out | On PCs with an NPU, new optional columns are available in Task Manager: *NPU*, *NPU Engine*, *NPU Dedicated Memory*, and *NPU Shared Memory* on the Processes, Users, and Details pages. Surfaces AI workload utilisation for diagnostics and monitoring. | 25H2/24H2 (KB5089573 preview); 26H1 |
| 5 | **Custom User Folder Name at Setup** | Rolling out | During Windows OOBE, users can now enter a custom `C:\Users\<name>` folder name instead of the previously auto-generated 5-letter abbreviation derived from the Microsoft account email. Applies to new setups only; cannot rename existing folders post-install. | 25H2/24H2 (KB5089573 preview) |
| 6 | **Windows Hello as Default Sign-in** | Rolling out | Windows Hello face or fingerprint authentication is now set as the default sign-in method on every login, both on the lock screen and sign-in screen, on devices enrolled with Windows Hello biometrics. | 25H2/24H2 (KB5089573 preview) |
| 7 | **Smart App Control Toggle (No Reinstall Required)** | Rolling out | Smart App Control can now be enabled or disabled without performing a clean OS reinstall. Previously required a full factory reset. | 26H1 (KB5089548) |
| 8 | **Display: Refresh Rates Above 1000Hz** | Rolling out | Display infrastructure now supports refresh rates exceeding 1000 Hz, enabling next-generation high-refresh gaming monitors. Also reduces USB4 display power usage during sleep and improves auto-rotation reliability after sleep. | 26H1 (KB5089548) |
| 9 | **Copilot+ Detailed Image Descriptions** | Rolling out | On Copilot+ PCs, Windows 11 adds detailed accessibility image descriptions powered by on-device AI. Also enables in-app Copilot collaboration across all Windows 11 devices. | 26H1 (KB5089548) |
| 10 | **File Explorer — Voice Typing on Rename & Archive Improvements** | Rolling out | File Explorer gains: Voice Typing (Win + H) when renaming files; expanded archive format support (reducing need for third-party tools); improved reliability when unblocking downloaded files for preview; sorting permissions by Principal in Advanced Security Settings. | 26H1 (KB5089548); 25H2/24H2 (KB5089573 preview) |
| 11 | **Performance: Start / Search / App Launch** | Rolling out | Shell performance improvements accelerating Start menu open, Search, Action Center, and application launch times. Includes a new Low Latency Profile option. | 25H2/24H2 (KB5089573 preview) |

---

## Section 2 — Patch Information

**Reporting month:** May 2026  
**Patch Tuesday date:** Tuesday, 12 May 2026  
**End-of-month preview date:** Tuesday, 26 May 2026  
**Covered versions:** 26H1, 25H2, 24H2 (the three currently serviced Windows 11 releases)

> Windows 11, version 26H1 (released 10 Feb 2026) targets new devices shipping in early 2026 and is **not** offered as an in-place upgrade from 24H2 or 25H2 on existing hardware. Pro: serviced 24 months; Enterprise: 36 months. Hotpatching is not available on 26H1.

---

### Windows 11, version 26H1 (OS Build 28000.x)

#### Patch Tuesday — 12 May 2026

| Field | Detail |
|-------|--------|
| **KB** | KB5089548 |
| **OS Build** | 28000.2113 |
| **Release Date** | 12 May 2026 |
| **Type** | Security (cumulative) |
| **Support Link** | https://support.microsoft.com/en-us/topic/may-12-2026-kb5089548-os-build-28000-2113-5c764ec5-ab8d-41ca-aad4-c3630305f6ac |

**Highlights:**
- Addresses the May 2026 Patch Tuesday security vulnerabilities (shared CVE set with 25H2/24H2 below), including Windows Kernel privilege escalation, DirectX graphics kernel memory corruption, and NTLM authentication vulnerabilities.
- SSDP notification reliability fix (prevents service becoming unresponsive).
- File Explorer: Voice Typing on rename, archive support, downloaded-file unblocking, Advanced Security sorting.
- Display: support for >1000 Hz refresh rates, USB4 sleep power reduction, HDR reliability improvements, WMI monitor size reporting fix.
- Smart App Control: can now be toggled without a clean reinstall.
- Copilot+ PCs: detailed image descriptions; Copilot collaboration on all Windows 11 devices.
- Hyper-V and Print Spooler reliability improvements.
- **Package size:** ~450 MB (x64), ~380 MB (ARM64). Requires ≥1 GB free disk space and a restart.

#### Non-Security Preview — 26 May 2026

| Field | Detail |
|-------|--------|
| **KB** | KB5089570 |
| **OS Build** | 28000.2179 |
| **Release Date** | 26 May 2026 |
| **Type** | Optional non-security preview |
| **Support Link** | https://support.microsoft.com/en-us/topic/may-26-2026-kb5089570-os-build-28000-2179-preview-89993979-7bd9-4e57-aa33-588c7780addb |

**Highlights:**
- Xbox Mode (CFR — phased rollout, device eligibility varies).
- Shared Audio (Bluetooth LE Audio; phased rollout).
- File Explorer: dark-mode polish, additional reliability and preference-preservation fixes.
- Secure Boot certificate preparation work (Secure Boot certificates begin expiring June 2026; this update ensures continued secure boot capability).
- Tighter driver trust policy and expanded policy-based app removal controls.
- AI component updates (Image Search, Content Extraction, Semantic Analysis, Settings Model at v1.2604.515.0) — Copilot+ PCs only; will not install on standard PCs or Windows Server.
- New batch file handling security controls for enterprise.

---

### Windows 11, version 25H2 (OS Build 26200.x) and version 24H2 (OS Build 26100.x)

> Microsoft ships a single cumulative update KB covering both 25H2 (build 26200.x) and 24H2 (build 26100.x).

#### Patch Tuesday — 12 May 2026

| Field | Detail |
|-------|--------|
| **KB** | KB5089549 |
| **OS Builds** | 26200.8457 (25H2) · 26100.8457 (24H2) |
| **Release Date** | 12 May 2026 |
| **Type** | Security (cumulative) |
| **Support Link** | https://support.microsoft.com/en-us/topic/may-12-2026-kb5089549-os-builds-26200-8457-and-26100-8457-28ec2a99-4bbe-481d-a340-5c6cf18d9acb |

**Highlights:**
- Addresses **120 CVEs** across Windows components. Notable critical/important fixes include:
  - **CVE-2026-41096** — Heap-based buffer overflow in Windows DNS (Critical, RCE potential).
  - **CVE-2026-34329** — Similar heap overflow in Windows Message Queuing (MSMQ).
  - Windows Kernel privilege escalation to SYSTEM via insufficient input validation in kernel-mode driver communication.
  - DirectX graphics kernel memory corruption enabling arbitrary code execution.
- Resolves known issue where some devices entered **BitLocker Recovery mode** after recent boot-file updates (TPM validation edge case).
- **Secure Boot certificate update**: Secure Boot certificates on most Windows devices expire starting June 2026; this update provisions renewed certificates to ensure continued secure boot capability.
- Xbox Mode: rolling out via CFR on eligible devices.

**Known Issue:**
> KB5089549 fails to install on some devices, returning **error 0x800f0922**, caused by insufficient free space on the EFI System Partition (ESP) — particularly when ≤10 MB is available. Workaround: free space on the ESP before applying the update.

#### Non-Security Preview — 26 May 2026

| Field | Detail |
|-------|--------|
| **KB** | KB5089573 |
| **OS Builds** | 26200.8524 (25H2) · 26100.8524 (24H2) |
| **Release Date** | 26 May 2026 |
| **Type** | Optional non-security preview |
| **Support Link** | https://support.microsoft.com/en-us/topic/may-26-2026-kb5089573-os-builds-26200-8524-and-26100-8524-preview-f378c8ae-0170-47c9-a1e9-dfef978c8e17 |

**Highlights:**
- **Performance improvements**: accelerated app launch, Start menu open, Search, Action Center, and startup apps. New Low Latency Profile option.
- **Shared Audio**: Bluetooth LE Audio broadcast for simultaneous two-listener sessions.
- **Multi-App Camera**: multiple apps can share a single camera stream; Basic Camera mode for simplified/troubleshooting use.
- **Task Manager NPU columns**: NPU, NPU Engine, NPU Dedicated Memory, NPU Shared Memory — visible on Processes/Users/Details pages on AI PCs.
- **Custom user folder name**: users can set their `C:\Users\<name>` folder name during setup (new installations only).
- **Windows Hello default sign-in**: biometric authentication set as the default method on every sign-in.
- Resolves the 0x800f0922 EFI System Partition error introduced in the May Patch Tuesday update.
- Dev Drive size now specifiable in GB rather than MB.

> All features in KB5089573 will be included in the **June 2026 Patch Tuesday** cumulative update (no action required if devices apply monthly security updates automatically).

---

## Summary of Update History URLs

| Version | Update History |
|---------|---------------|
| 26H1 | https://support.microsoft.com/en-us/topic/windows-11-version-26h1-update-history-253c73cd-cab1-4bfd-94dc-76c452273fc9 |
| 25H2 | https://support.microsoft.com/en-us/topic/windows-11-version-25h2-update-history-99c7f493-df2a-4832-bd2d-6706baa0dec0 |
| 24H2 | https://support.microsoft.com/en-us/topic/windows-11-version-24h2-update-history-0929c747-1815-4543-8461-0160d16f15e5 |

---
layout:
  width: wide
---

# Windows Monthly Brief — September 2026
_Generated 2026-10-01_

---

## Section 1 — Windows Roadmap Features

The following features appeared or changed status on the Windows roadmap (Platform: Windows 11 PC, Feature type: Feature, Edition: Retail) during September 2026. Source: [Windows business roadmap](https://www.microsoft.com/en-us/windows/business/roadmap).

> **Major event:** Windows 11, version **26H2** (the "Windows 11 2026 Update") reached General Availability on **September 29, 2026**, delivered as a small enablement package (KB5121794) to devices running 24H2 or 25H2 with the September 22 preview (KB5124010) installed.

| Title | Status | Description | Target Version |
|---|---|---|---|
| Taskbar Repositioning | Rolling out | Users can move the Taskbar to the top, left, right, or default bottom position. Tooltips, flyouts, animations, and customization all work in every position. | 26H2 |
| Smaller Taskbar option | Rolling out | A compact Taskbar mode reduces bar height and icon size while keeping Start, Search, and the system tray accessible. Configurable under Settings > Personalization > Taskbar > Taskbar behaviors. | 26H2 (previewed 26H1 Sept 22) |
| Start menu size customization | Rolling out | Start gains preset size options — Small, Large, or Automatic — via Settings > Personalization > Start > Start menu size. Independent toggles for Pinned, Recent, and All Apps sections. | 26H2 |
| Windows Search privacy controls | Rolling out | New options under Settings > Privacy & security > Search let users control whether web results and Microsoft Store suggestions appear alongside local files. Local results now prioritized by default. | 26H2 |
| File Explorer: HTML preview + section memory | Rolling out | Preview pane now shows a "Preview anyway" button for HTML files and auto-previews PDFs. The Home page remembers each section's expanded/collapsed state across sessions. Context menu reorganized to reduce top-level clutter. | 26H2 (previewed 25H2/24H2 Sept 22) |
| Remappable Copilot key | Rolling out | Users can reassign the Copilot keyboard key to function as Right Ctrl or the Context Menu key in Settings. | 26H2 (previewed 25H2 Sept 22) |
| Camera roll backup (OneDrive) | Rolling out | New setting in Settings > Accounts > Windows backup to automatically back up photos and videos from the device to OneDrive. | 26H2 / 25H2 |
| Emoji 17.0 | Rolling out | Adds new and updated emoji from the Unicode Emoji 17.0 standard across the emoji picker and throughout the OS. | 26H2 / 25H2 / 24H2 |
| Open apps maximized by default | Rolling out | A new accessibility/personalization setting automatically maximizes app windows as they open, reducing the need to manually resize windows. | 26H2 / 25H2 / 24H2 |
| Task Manager: NPU usage + memory panels | Rolling out | Task Manager now includes a dedicated NPU (Neural Processing Unit) performance graph and new memory information panels alongside existing CPU/GPU/Disk views. | 26H2 |
| Narrator: Braille Viewer | Rolling out | Narrator adds a Braille Viewer panel for users who rely on refreshable braille displays, showing the current Narrator output in real time on screen. | 26H2 |
| Copilot Search box (opt-in) | Rolling out | An optional Copilot-powered search box replaces the standard Taskbar Search and reads "Ask Copilot anything." Includes Copilot Vision and Voice access points. Not enabled by default; user opt-in required. | 26H2 |
| Windows settings backup enabled by default | Rolling out | Settings backup is now on by default for eligible 26H2 devices, allowing users to restore Windows settings and Microsoft Store app lists after a reset, upgrade, or device replacement. Manageable via Intune, Group Policy, or MDM. | 26H2 |

> **Most notable:** The **Windows 11 26H2 release** on September 29 is the headline event — it brings Taskbar Repositioning as the most visible consumer feature and layers NPU/AI-centric Task Manager tooling for enterprise visibility into Copilot+ PC workloads.

---

## Section 2 — Patch Information

Current supported retail versions covered: **26H2** (new), **26H1**, **25H2**.

> Note: 25H2 and 24H2 share the same cumulative update packages (same KB, separate OS build numbers). 26H1 is based on a different Windows core and ships separate KBs. 26H2 was released September 29, 2026 and did not receive a separate Patch Tuesday update — its initial builds already incorporate the September security payload.
>
> ⚠️ **Out-of-band (Sept 14):** Microsoft released emergency OOB updates for all versions to fix issues introduced by the September 8 Patch Tuesday update. These are KB5129194 (26H1) and KB5129195 (25H2/24H2).
>
> 📅 Windows 11, version 24H2 Home/Pro end-of-support date: **October 13, 2026** — now within two weeks. Enterprise/Education support continues to October 2027.

---

### Windows 11, version 26H2 (OS Build 26300.x)

> 26H2 was released September 29, 2026. There is no stand-alone Patch Tuesday entry for 26H2 in September — the release build (26300.9457, enablement package KB5121794) is immediately superseded by the September D preview (KB5124010), which ships simultaneously as a day-1 update.

#### Release + Day-1 Update

| Field | Detail |
|---|---|
| Release date | September 29, 2026 |
| KB | KB5124010 |
| OS Build | 26300.9550 |
| Support link | [KB5124010](https://support.microsoft.com/help/5124010) |

**Highlights:** Includes the full September security payload; Taskbar Repositioning; smaller Taskbar option; Start menu size controls; Windows Search privacy settings; File Explorer HTML preview + section memory; Remappable Copilot key; Task Manager NPU panels; Narrator Braille Viewer; Settings backup on by default.

---

### Windows 11, version 26H1 (OS Build 28000.x)

#### Patch Tuesday — Security Update

| Field | Detail |
|---|---|
| Release date | September 8, 2026 |
| KB | KB5124012 |
| OS Build | 28000.2954 |
| Support link | [KB5124012](https://support.microsoft.com/help/5124012) |

**Highlights:** Patches two actively exploited zero-days (CVE-2026-81963 Windows Update Stack EoP, CVSS 7.8; and CVE-2026-85880 ALPC EoP, CVSS 7.8). Adds ML-KEM support in TLS and Secure Boot certificate enhancements. Fixes ARM-device launch failures for Microsoft Teams and new Outlook introduced by the August Patch Tuesday (KB5121000).

#### Out-of-Band Emergency Update

| Field | Detail |
|---|---|
| Release date | September 14, 2026 |
| KB | KB5129194 |
| OS Build | 28000.2956 |
| Support link | [KB5129194](https://support.microsoft.com/help/5129194) |

**Note:** Emergency fix for regressions introduced by KB5124012 (September 8).

#### Non-Security Preview Update (end of month)

| Field | Detail |
|---|---|
| Release date | September 22, 2026 |
| KB | KB5124006 |
| OS Build | 28000.3086 |
| Support link | [KB5124006](https://support.microsoft.com/help/5124006) |

**Highlights:** Taskbar position customization (bottom/top/left/right); smaller Taskbar option; updated progress indicators; share-window app discovery for work/school accounts; Administrator Protection feature; smoother virtual desktop switching; prerequisite for receiving the 26H2 enablement on 26H1-based devices (not applicable — 26H2 upgrades from 24H2/25H2 only).

---

### Windows 11, version 25H2 (OS Build 26200.x)

#### Patch Tuesday — Security Update

| Field | Detail |
|---|---|
| Release date | September 8, 2026 |
| KB | KB5124008 |
| OS Build | 26200.9445 |
| Support link | [KB5124008](https://support.microsoft.com/help/5124008) |

**Highlights:** Same two zero-day patches as 26H1 (CVE-2026-81963, CVE-2026-85880). ML-KEM support in TLS; Secure Boot enhancements. Shared KB with 24H2 (build 26100.9445).

#### Out-of-Band Emergency Update

| Field | Detail |
|---|---|
| Release date | September 14, 2026 |
| KB | KB5129195 |
| OS Build | 26200.9457 |
| Support link | [KB5129195](https://support.microsoft.com/help/5129195) |

**Note:** Emergency fix for regressions introduced by KB5124008. Shared with 24H2 (build 26100.9457).

#### Non-Security Preview Update (end of month)

| Field | Detail |
|---|---|
| Release date | September 22, 2026 |
| KB | KB5124010 |
| OS Build | 26200.9550 |
| Support link | [KB5124010](https://support.microsoft.com/help/5124010) |

**Highlights:** File Explorer HTML preview; remappable Copilot key; camera roll OneDrive backup; Emoji 17.0; open apps maximized setting; WinRE remote management plug-in; Kiosk mode Win+Tab block. **Required prerequisite** for upgrading to Windows 11 26H2 via KB5121794. Shared KB with 24H2 (build 26100.9550).

---

_Sources: [Microsoft Windows Roadmap](https://www.microsoft.com/en-us/windows/business/roadmap) · [Windows 11 release information](https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information) · [KB5124012 (26H1 Sept B)](https://support.microsoft.com/help/5124012) · [KB5124008 (25H2/24H2 Sept B)](https://support.microsoft.com/help/5124008) · [KB5129194 (26H1 OOB)](https://support.microsoft.com/help/5129194) · [KB5129195 (25H2/24H2 OOB)](https://support.microsoft.com/help/5129195) · [KB5124006 (26H1 Sept D preview)](https://support.microsoft.com/help/5124006) · [KB5124010 (25H2/24H2/26H2 Sept D)](https://support.microsoft.com/help/5124010)_

---
layout:
  width: wide
---

# Microsoft 365 Message Center — Security & Compliance Digest
**Period:** 2026-08-24 → 2026-09-23 | **Generated:** 2026-09-23

---

## ⚠️ Action Required

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-09-01 | [MC1426371](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1426371) | Passkeys become default; SMS/voice MFA retirement notice | Microsoft Entra | Identity & Access | Action Required | Passkeys are the default authentication method for eligible users as of September 1, 2026. Microsoft-provided SMS and voice call MFA (as a second factor) is retiring February 1, 2027. Admins should audit user authentication method registrations and accelerate passkey adoption campaigns before the February deadline; users relying solely on SMS/voice MFA will need a replacement. |
| 2026-09-01 | [MC1422061](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1422061) | Custom Controls in Conditional Access — creation disabled | Microsoft Entra | Identity & Access | Plan for Change | Creating or modifying Custom Controls in Conditional Access has been disabled as of September 2026; existing controls continue to function until full retirement in May 2027. Admins must migrate third-party MFA integrations from Custom Controls to External Authentication Methods (EAM) before the May 2027 deadline to avoid Conditional Access policy failures. |
| 2026-09-22 | [MC1457836](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1457836) | Tenants auto-enabled into Defender Unified RBAC | Microsoft Defender XDR | Threat Protection | Action Required | Starting late September 2026, tenants using legacy RBAC in Defender for Office 365 and Microsoft Sentinel will be automatically transitioned to Unified RBAC approximately 30 days after receiving a notification (rollout completes December 2026). Existing roles are imported automatically; admins should review role assignments and validate custom role mappings in advance. An opt-out is available within the portal post-activation. |

---

## Data Protection & Compliance

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-25 | [MC1413308](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1413308) | Data Lifecycle Management: Insights for Copilot and AI interactions | Microsoft Purview | Data Protection & Compliance | Public Preview | Public Preview begins late August 2026 for Data Lifecycle Management insights that surface retention-policy and disposition context for Copilot and AI app interactions. Helps admins understand how existing retention policies apply to AI-generated content; GA expected mid-October 2026. No admin action required to access the preview. |
| 2026-09-01 | [MC1449180](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1449180) | DLP and auto-labeling for non-Microsoft applications | Microsoft Purview | Data Protection & Compliance | GA | DLP policies and auto-labeling now cover non-Microsoft cloud apps — Google Workspace (Drive, Gmail), Box, and Salesforce — via Microsoft Defender for Cloud Apps, with GA beginning early September 2026 and completing late October 2026. Extends Purview data protection to cross-platform content; requires a Defender for Cloud Apps app-governance license. |
| 2026-09-08 | [MC1469958](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1469958) | Auto-labeling simulation capacity expanded to 20 million items | Microsoft Purview | Data Protection & Compliance | Public Preview | Auto-labeling simulation mode capacity increases from 4 million to 20 million items, enabling policy testing across much larger SharePoint, OneDrive, and Exchange data sets. Public Preview early-to-mid September 2026; GA rollout targeted late October 2026. No admin action required to start using the expanded limit in simulation mode. |
| 2026-09-15 | [MC1470884](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1470884) | eDiscovery: SharePoint Embedded containers as data source | Microsoft Purview | Data Protection & Compliance | Rollout | eDiscovery in Purview can now target user-owned SharePoint Embedded containers — including Microsoft Loop workspaces, Copilot Pages, and OneNote Notebooks — as first-class data sources, rolling out mid-September 2026. Expands legal-hold and search coverage to Copilot-generated content storage. |
| 2026-09-15 | [MC1477181](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1477181) | Default SharePoint library sensitivity labels applied to existing files | Microsoft Purview | Data Protection & Compliance | Rollout | SharePoint document library default sensitivity labels now apply retroactively to existing unlabeled files at rest, not just newly uploaded content, rolling out September 2026. Admins with configured library defaults should review the resulting encryption and access-policy changes on previously unlabeled files. |
| 2026-09-15 | [MC1474107](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1474107) | Endpoint DLP: Archive file classification behavior change on Windows | Microsoft Purview | Data Protection & Compliance | Update | Endpoint DLP on Windows endpoints now classifies the individual contents of archive files (ZIP, RAR, etc.) rather than the archive itself, rolling out September 2026. Existing DLP policies targeting archive file types may trigger differently on uploads and transfers; admins should review and test impacted policies before the rollout completes. |
| 2026-09-15 | [MC1454399](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1454399) | Clipchamp sensitivity-label support extended to project files | Microsoft Purview | Data Protection & Compliance | Update | The `EnableSensitivityLabelForVideoFiles` PowerShell setting now covers Clipchamp project files (`.clipchamp`) in addition to exported MP4 files, rolling out mid-September 2026. Admins using this setting gain DLP and classification coverage over in-progress Clipchamp projects, not just published videos. |
| 2026-09-22 | [MC1473155](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1473155) | Purview: New permission-change operations in audit log | Microsoft Purview | Data Protection & Compliance | Rollout | Two new audit operations capturing permission changes are added to the Microsoft Purview audit log, rolling out late September 2026. Provides more granular evidence for compliance investigations involving changes to permissions on Purview-managed resources. |
| 2026-09-22 | [MC1477182](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1477182) | DLP extended to Microsoft Cowork | Microsoft Purview | Data Protection & Compliance | Rollout | Microsoft Purview DLP policies, sensitivity-label grounding, and web-search DLP enforcement extend to Microsoft Cowork (the new collaborative AI workspace), rolling out late September 2026. Includes prompt-blocking on content matching DLP rules and sensitivity-label awareness within Cowork AI interactions. |
| 2026-09-22 | [MC1472022](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1472022) | Outlook for Mac: Purview DLP support for Calendar Events | Microsoft Purview | Data Protection & Compliance | Rollout | Microsoft Purview DLP policies now apply to Calendar Events in Outlook for Mac, preventing users from sharing sensitive information through calendar invites and event details that violate DLP rules, rolling out late September 2026. Aligns Mac DLP coverage with existing Windows and web Outlook behavior. |

---

## Identity & Access

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-24 | [MC1411574](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1411574) | System-preferred authentication extends to first-factor sign-in | Microsoft Entra | Identity & Access | Update | Updated August 24, 2026: System-preferred authentication now applies to first-factor sign-ins for tenants in Microsoft-managed state, automatically selecting the most secure registered method (e.g., passkey over password). Rolling out late June–late September 2026; no admin action required. |
| 2026-08-25 | [MC1440968](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1440968) | Passkey registration experience optimizations | Microsoft Entra | Identity & Access | Update | Optimizations to passkey registration via Registration Campaigns, Authentication Strengths, and My Sign-Ins prioritize local device passkeys and streamline the registration flow, rolling out late August 2026. No UI changes visible to admins; supports the broader passkeys-as-default rollout. |
| 2026-09-08 | [MC1469555](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1469555) | Optimized passkey registration campaign experience | Microsoft Entra | Identity & Access | Rollout | Updated passkey registration campaigns deliver improved user prompts and clearer step-by-step guidance throughout the passkey registration flow, rolling out early-to-mid September 2026. Complements the September 1 passkeys-by-default change; no separate admin configuration required. |
| 2026-09-15 | [MC1474104](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1474104) | Follow-up guidance: SMS first-factor sign-in retirement | Microsoft Entra | Identity & Access | Update | Follow-up communication published September 2026 regarding the August 11 retirement of SMS first-factor sign-in for Entra ID Free tenants, providing additional guidance on identifying affected users and confirming that alternative method registration is complete. Admins in affected tenants should confirm remediation. |

---

## Email Security

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-09-02 | [MC1422060](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1422060) | MDO: Prompt injection protection for email (timeline update) | Microsoft Defender for Office 365 | Email Security | Rollout | Prompt injection protection in Microsoft Defender for Office 365 (Plan 2 / M365 E5) — detecting and quarantining malicious email content designed to manipulate Microsoft 365 Copilot — had its rollout timeline updated on September 2, 2026; rollout now completes October 2026. Already active in tenants reached during July–September; high-confidence threats are auto-quarantined by default. |

---

## Threat Protection

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-09-22 | [MC1474106](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1474106) | MDO: MessageContents table in Advanced Hunting for Teams | Microsoft Defender for Office 365 | Threat Protection | Rollout | A new `MessageContents` table is added to Microsoft Defender Advanced Hunting, enabling KQL queries against Teams message content for threat investigation, rolling out late September 2026 and completing mid-October 2026. Available to Defender for Office 365 Plan 2 and Microsoft 365 E5 customers. |
| 2026-09-22 | [MC1476237](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1476237) | MDO: Remediation actions from Teams message entity flyout | Microsoft Defender for Office 365 | Threat Protection | Rollout | Defenders can now take remediation actions directly from the Teams message entity flyout in the Defender portal — including submitting messages to Microsoft and blocking senders or domains — rolling out late September 2026. Available to Defender for Office 365 Plan 1 and Plan 2 customers; reduces time-to-contain in Teams-based threats. |

---

## Endpoint Security

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-09-15 | [MC1473156](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1473156) | Intune: Windows Health Attestation migrating to Azure Attestation | Microsoft Intune | Endpoint Security | Plan for Change | Microsoft Intune will migrate Windows Health Attestation compliance evaluation from the legacy Device Health Attestation (DHA) service to Microsoft Azure Attestation (MAA), announced September 2026 with migration targeted for end of Q1 2027. Intune compliance policies using health attestation will be re-evaluated automatically; no admin reconfiguration expected, but admins should monitor compliance policy results post-migration. |

---

## Platform Security

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-25 | [MC1458480](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1458480) | Edge management service: Security Update Alerts | Microsoft Edge | Platform Security | GA | Admins using the Edge management service can now configure a security-severity threshold and receive alerts when an Edge release includes security fixes at or above that level — including zero-day patches — enabling faster internal response to high-severity browser security updates. No policy change required; opt-in via Edge management service settings. |
| 2026-08-25 | [RM566871](https://www.microsoft.com/en-us/microsoft-365/roadmap?id=566871) | Edge Enhanced Security Mode Plus | Microsoft Edge | Platform Security | Public Preview | Enhanced Security Mode Plus adds admin-configurable protections on top of the existing Enhanced Security Mode: restricts legacy network protocols, compression behavior, hardware-access web APIs, WebGL usage, and external protocol launches. Available as a Public Preview in August 2026 for enterprise environments requiring tighter browser attack-surface controls. |
| 2026-08-27 | [MC1387532](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1387532) | Microsoft Edge moves to 2-week release cycle | Microsoft Edge | Platform Security | Update | Starting with Edge 152 (Stable channel August 27, 2026), Microsoft Edge shifts from a 4-week to a 2-week release cycle, enabling faster delivery of security patches and smaller, more targeted releases. Organizations on the Extended Stable channel are unaffected by the cadence change; no admin action required. |
| 2026-09-09 | [MC1469327](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1469327) | September 2026 Windows security update now available | Microsoft 365 suite | Platform Security | Update | The September 2026 cumulative Windows security update (Patch Tuesday) is available for all supported Windows versions. Organizations should apply the update promptly through their standard patch-management workflows; admins using Windows Autopatch or Intune will receive automatic deployment per their configured rings. |

---

## Summary by Category

| Category | Count |
|----------|-------|
| Data Protection & Compliance | 10 |
| Identity & Access | 4 |
| Email Security | 1 |
| Threat Protection | 2 |
| Endpoint Security | 1 |
| Platform Security | 4 |
| **Action Required (cross-category)** | **3** |
| **Total unique items** | **25** |

---

*Source data retrieved from [mc.merill.net](https://mc.merill.net/) via web search. Per-item details at `https://mc.merill.net/message/<ID>`. Admin portal links open directly in the Microsoft 365 admin center Message Center.*

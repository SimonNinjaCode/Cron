---
layout:
  width: wide
---

# Microsoft 365 Message Center — Security & Compliance Digest
**Period:** 2026-08-01 → 2026-08-31 | **Generated:** 2026-08-31

---

## ⚠️ Action Required

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-01 | [MC1192257](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1192257) | MDTI convergence with Defender and Sentinel | Microsoft Defender XDR | Threat Protection | Retirement | Microsoft Defender Threat Intelligence fully converged into Microsoft Defender and Microsoft Sentinel as of August 1, 2026. Post-transition, MDTI requires an active Defender or Sentinel license — tenants that haven't verified licensing face loss of MDTI access. |
| 2026-08-11 | [MC1448374](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1448374) | SMS first-factor sign-in retired for Entra ID Free | Microsoft Entra | Identity & Access | Retirement | SMS first-factor sign-in (phone number + SMS OTP, no password) was retired for Entra ID Free tenants on August 11, 2026 due to fraud risk. SMS as a second-factor MFA method is unaffected; admins must ensure affected users registered an alternative method before the deadline. |
| 2026-08-15 | [MC1303719](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1303719) | federatedTokenValidationPolicy default enforcement | Microsoft Entra | Identity & Access | Update | Stricter `federatedTokenValidationPolicy` defaults now enforced starting mid-August 2026, blocking federated sign-ins where `internalDomainFederation` does not match the user's UPN domain. Tenants with federated domains configured before December 2025 should have reviewed their federation configuration to prevent sign-in disruptions. |
| 2026-08-20 | [MC1457836](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1457836) | Tenants auto-enabled into Defender Unified RBAC | Microsoft Defender XDR | Threat Protection | Rollout | Existing tenants using legacy RBAC in Defender and Sentinel will be auto-transitioned to Unified RBAC approximately 30 days after notification (late September–December 2026). Existing roles are imported automatically; admins should review role assignments ahead of the transition. An opt-out is available post-activation. |
| 2026-08-01 | [MC1440701](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1440701) | MDO encrypted attachment protection (opt-in) | Microsoft Defender for Office 365 | Email Security | GA | New opt-in Safe Attachments policy setting that quarantines emails containing password-protected attachments that cannot be scanned. Designed to close an encrypted-attachment abuse vector; admins must explicitly enable the policy to gain protection. |

---

## Data Protection & Compliance

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-01 | [RM568217](https://www.microsoft.com/en-us/microsoft-365/roadmap?id=568217) | Sensitivity labels for Entra security groups | Microsoft Purview | Data Protection & Compliance | GA | Sensitivity labels (the same labels used for Microsoft 365 groups) can now be applied to Microsoft Entra cloud security groups, reaching GA in August 2026. On-premises synced, Exchange-managed, and dynamic membership groups are not supported at GA; no separate label configuration is required. |
| 2026-08-01 | [MC1185445](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1185445) | Purview classifier simulation mode | Microsoft Purview | Data Protection & Compliance | GA | Admins can now test and validate custom trainable classifiers against production data before publishing, using the new Classifier Simulation Mode (Health Monitoring). Rolling out July–August 2026; optionally enables automatic disabling of inefficient classifiers to reduce false positives and scanning latency. |
| 2026-08-01 | [MC1381121](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1381121) | Endpoint DLP policy sync and device health AI skill | Microsoft Purview | Data Protection & Compliance | GA | AI-powered Policy Sync and Device Health skills for Endpoint DLP reach GA in late August 2026 (Public Preview from late July). Provides real-time policy deployment visibility, automatic issue identification, root cause analysis, and remediation recommendations; no admin action required to enable. |
| 2026-08-15 | [MC1387682](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1387682) | DLP default protection when Exchange classification fails | Microsoft Purview | Data Protection & Compliance | GA | New Exchange Online DLP capability to detect and respond to classification failures — including timeouts, throttling, and scan errors — rolling out mid- to late August 2026. Gives admins a safety net policy action when content cannot be classified, improving coverage with no impact on existing policies. |
| 2026-08-15 | [MC1404319](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1404319) | Endpoint DLP support for FTP and SFTP | Microsoft Purview | Data Protection & Compliance | GA | Endpoint DLP now monitors and protects file transfers over FTP and SFTP on managed Windows devices, reaching GA in mid-August 2026 (Preview from late July). Extends DLP coverage to file-transfer protocols commonly used to exfiltrate data from endpoints. |
| 2026-08-01 | [MC1221453](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1221453) | eDiscovery advanced review set explorer | Microsoft Purview | Data Protection & Compliance | GA | The Advanced Review Set Explorer — enabling Kusto Query Language (KQL) analysis of eDiscovery review sets for insights into item types, patterns, and trends — reaches GA in late August 2026 (Public Preview since February 2026). Enabled by default; no impact to existing eDiscovery workflows. |
| 2026-08-01 | [MC1413308](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1413308) | Data Lifecycle Management insights for Copilot and AI | Microsoft Purview | Data Protection & Compliance | Rollout | New Data Lifecycle Management insights surface data-retention and disposition context for Copilot and AI app interactions, rolling out August 2026. Helps admins understand how retention policies apply to AI-generated content and interactions. |
| 2026-08-15 | [MC1311975](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1311975) | Purview compliance portal role groups UI enhancements | Microsoft Purview | Data Protection & Compliance | Update | Enhanced Role Groups UI in the Purview compliance portal allows admins to view role assignments by roles, by members, or by their own permissions, completing rollout by mid-August 2026. Enabled by default; existing assignments are unchanged. |
| 2026-08-15 | [MC1409303](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1409303) | Edge enforces screen capture restrictions for labeled PDFs | Microsoft Edge | Data Protection & Compliance | GA | Microsoft Edge now enforces "Do Not Allow Screen Capture" restrictions on sensitivity-labeled PDFs viewed in OneDrive and SharePoint web viewers, reaching GA mid- to late August 2026. Aligns web behavior with desktop enforcement; existing sensitivity label policies apply automatically. Other browsers and mobile web are not supported at GA. |
| 2026-08-17 | [MC1255406](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1255406) | Data Security Triage Agent DLP summaries — timeline update | Microsoft Purview | Data Protection & Compliance | Update | The AI-generated DLP alert summaries feature in Microsoft Defender XDR had its GA timeline updated on August 17, 2026 — now targeting August 2027 (previously August 2026). Admins planning for this feature should revise roadmap expectations; the agent is deployed from Defender XDR and managed in Purview. |

---

## Identity & Access

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-01 | [MC1287372](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1287372) | Entra ID Governance account discovery | Microsoft Entra | Identity & Access | GA | Entra ID Governance Account Discovery identifies local and orphaned application accounts (in Atlassian Cloud, Salesforce, SAP Cloud Identity Services, ECMA on-prem) that are outside Entra ID, reaching GA in August 2026. Off by default; requires admin opt-in and an Entra ID Governance add-on or Entra Suite license. |
| 2026-08-01 | [MC1395007](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1395007) | Conditional Access and ID Protection for agents | Microsoft Entra | Identity & Access | GA | New service plans — Conditional Access for Agents and Identity Protection for Agents — were added automatically to Microsoft Agent 365 and Microsoft 365 E7 licenses, completing rollout in early August 2026. Existing CA and ID Protection policies are unchanged; licensing is required to use these capabilities for AI agents. |
| 2026-08-01 | [MC1400824](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1400824) | SSPR CAPTCHA protection modernized | Microsoft Entra | Identity & Access | Update | The legacy CAPTCHA challenge in Self-Service Password Reset was removed during August 2026 and replaced with modern backend throttling and behavior-based abuse detection. Users experience no additional friction; the change is transparent and requires no admin action. |
| 2026-08-07 | [MC1450134](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1450134) | WHfB and macOS Platform SSO as standalone MFA factors | Microsoft Entra | Identity & Access | Plan for Change | Published August 7, 2026 (updated August 18): Windows Hello for Business and macOS Platform SSO will be recognized as standalone MFA factors beginning October–November 2026. Users will be able to satisfy Authentication Strength policies and sign-in frequency checks using WHfB or Platform SSO without a separate passkey; admins should update onboarding and MFA registration guidance. |
| 2026-08-01 | [MC1450133](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1450133) | Register passkey as first MFA method | Microsoft Entra | Identity & Access | Plan for Change | Announced in August 2026 for rollout October 2026–February 2027: users will be able to register a passkey or other passwordless method as their very first MFA method, eliminating the current requirement to set up a weaker method first and increasing adoption of phishing-resistant authentication. |
| 2026-08-24 | [MC1411574](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1411574) | System-preferred auth applies to first-factor sign-in | Microsoft Entra | Identity & Access | Update | Updated August 24, 2026: System-preferred authentication now also applies to first-factor sign-ins for tenants in Microsoft managed state, selecting the most secure registered method (e.g., passkey over password). Rolling out late June–late September 2026; no admin action required. |
| 2026-08-25 | [MC1440968](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1440968) | Passkey registration experience optimizations | Microsoft Entra | Identity & Access | Update | Optimizations to passkey registration via Registration Campaigns, Authentication Strengths, and My Sign-Ins rolling out late August 2026, prioritizing local device passkeys. No UI changes visible to admins; no action required, but supports broader passkey adoption initiatives. |

---

## Email Security

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-01 | [MC1422060](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1422060) | MDO prompt injection protection for email | Microsoft Defender for Office 365 | Email Security | GA | Prompt injection protection in Microsoft Defender for Office 365 (Plan 2/M365 E5) — detecting malicious content in email that attempts to manipulate Microsoft 365 Copilot — reached GA and default-on status in early July 2026 and is active across the August window. High-confidence threats are auto-quarantined; admins should review workflows and inform security teams. |

---

## Threat Protection

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-01 | [MC1381119](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1381119) | Defender for Endpoint updates via Microsoft Update | Microsoft Defender for Endpoint | Endpoint Security | Rollout | Microsoft Defender for Endpoint security updates are decoupled from monthly Patch Tuesday and delivered independently via Microsoft Update, expanding to Windows 11 and remaining versions through fall 2026 (Windows 10 from May 2026). No restart usually required; organizations using manual deployment must adjust their update workflows. |
| 2026-08-01 | [MC1446794](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1446794) | Teams: Report security concerns in meetings | Microsoft Teams | Threat Protection | GA | "Report a meeting" feature allowing users to flag suspicious activity (phishing, impersonation, social engineering, scams) during Teams meetings is rolling out August 2026. Reports are reviewable in Microsoft Defender and the Teams admin center; enabled by default with no action required. |
| 2026-08-01 | [MC1447673](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1447673) | Teams: Report security concerns in group calls | Microsoft Teams | Threat Protection | Rollout | "Report a call" feature for group calls from call history rolls out August–October 2026, enabling users to flag suspicious callers. Reports surface in Teams admin center and Microsoft Defender; enabled by default with no admin action required. |

---

## Platform Security

| Date | ID | Title | Service | Category | Type | Summary |
|------|----|--------|---------|----------|------|---------|
| 2026-08-01 | [MC1452953](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1452953) | August 2026 Windows security update | Microsoft 365 suite | Platform Security | Update | The August 2026 cumulative Windows security update is available for all supported versions. Notable inclusions: Secure Boot certificate expansion using high-confidence device targeting data, and servicing stack quality improvements. Some devices may experience one additional restart during installation for the Secure Boot certificate update. |
| 2026-08-27 | [MC1387532](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1387532) | Microsoft Edge moves to 2-week release cycle | Microsoft Edge | Platform Security | Update | Starting with Edge 152 (Stable on August 27, 2026), Microsoft Edge moves from a 4-week to a 2-week release cycle, enabling faster delivery of security updates and smaller individual releases. Organizations using Extended Stable are unaffected by the cadence change; no admin action required. |

---

## Summary by Category

| Category | Count |
|----------|-------|
| Data Protection & Compliance | 10 |
| Identity & Access | 7 |
| Email Security | 1 |
| Endpoint Security | 1 |
| Threat Protection | 3 |
| Platform Security | 2 |
| **Action Required (cross-category)** | **5** |
| **Total unique items** | **24** |

---

*Source data retrieved from [mc.merill.net](https://mc.merill.net/) via web search. Per-item details at `https://mc.merill.net/message/<ID>`. Admin portal links open directly in the Microsoft 365 admin center Message Center.*

# Microsoft 365 Message Center Digest — Security & Compliance

**Window:** 2026-05-16 → 2026-06-15 | **Run date:** 2026-06-15 | **Timezone:** Europe/Berlin (CEST)

---

## Overview

25 security and compliance items with published dates or key rollout milestones inside the 30-day window.
Services: Microsoft Purview (12), Microsoft Entra (6), Microsoft Intune (1), Microsoft Defender XDR (4), Microsoft Defender for Office 365 (1), Microsoft 365 suite (1).

---

## Data Protection & Compliance

### MC1191257 — New Purview DSPM experience goes GA

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1191257](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1191257) |

Microsoft Purview Data Security Posture Management (DSPM) reaches GA with a redesigned unified dashboard covering traditional workloads, AI environments, and third-party integrations, plus enhanced AI observability and reporting. Enabled by default for eligible tenants; rollout runs early–late May 2026.

---

### MC1185445 — Custom classifier simulation mode goes GA

| Field | Value |
|---|---|
| **Date** | 2026-05-27 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1185445](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1185445) |

Classifier Simulation Mode in the Purview compliance portal reaches GA late May 2026, letting admins test and validate custom sensitive-information-type (SIT) classifiers against production data before publishing. Reduces false positives and scanning latency; no end-user action required.

---

### MC1217155 — Data Security Posture Agent reaches GA

| Field | Value |
|---|---|
| **Date** | 2026-05-27 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1217155](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1217155) |

The Purview Data Security Posture Agent becomes GA in late May 2026, using large language models to proactively surface sensitive data exposure and associated risks across Microsoft 365 and multicloud sources. Enabled by default for eligible tenants; no end-user impact.

---

### MC1297982 — Sensitivity labels block connected experiences in Office apps

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1297982](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1297982) |

Sensitivity labels gain a new setting to block all connected experiences that analyze content (e.g., Copilot, grammar tools) in Word, Excel, and PowerPoint. GA rollout begins mid-May 2026 and the setting auto-applies to existing labels already configured to block content analysis — no admin reconfiguration required.

---

### MC1262572 — Endpoint DLP device health reporting dashboard

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | Rollout |
| **Link** | [MC1262572](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1262572) |

A new Device Health Reporting Dashboard in Microsoft Purview Endpoint DLP provides centralized, quick diagnosis of device configuration issues with no user impact. Enabled by default for eligible tenants during the May–June 2026 rollout.

---

### MC1263277 — DLP blocks Copilot external web search on sensitive data

| Field | Value |
|---|---|
| **Date** | 2026-05-26 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1263277](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1263277) |

Microsoft Purview DLP policies can now evaluate and block external web searches triggered by M365 Copilot and Copilot Chat in real time when sensitive data is detected. GA rollout accelerated to late May 2026 (brought forward from late June); rollout completes late June 2026.

---

### MC1261587 — DLM priority cleanup for hard-deleting SharePoint/OneDrive files

| Field | Value |
|---|---|
| **Date** | 2026-05-26 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1261587](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1261587) |

A new priority cleanup workflow in Purview Data Lifecycle Management lets admins permanently hard-delete specific OneDrive and SharePoint files on demand, bypassing standard retention queues. Rollout from late May to mid-June 2026; admin action required to initiate cleanup jobs.

---

### MC1262573 — Extended scoping for sensitivity label policies

| Field | Value |
|---|---|
| **Date** | 2026-06-01 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1262573](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1262573) |

Admins can now include dynamic and non-mail-enabled security groups—and exclude modern Microsoft 365 groups—in sensitivity label policy targeting. GA expected by early June 2026; no end-user impact.

---

### MC1234571 — Adaptive scopes for SharePoint DLP policies

| Field | Value |
|---|---|
| **Date** | 2026-06-01 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1234571](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1234571) |

Microsoft Purview DLP adaptive scopes now support SharePoint, enabling policies to automatically target sites based on attribute-based criteria (URL, site name, metadata) rather than manually maintained static lists. GA rollout begins June 2026; not enabled by default — admins must create and assign adaptive scopes.

---

### MC1279068 — Sensitivity label inheritance for Teams meeting artifacts

| Field | Value |
|---|---|
| **Date** | 2026-06-05 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1279068](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1279068) |

Teams meeting transcripts, recordings, and Loop meeting notes can now automatically inherit the sensitivity label applied to the parent meeting. GA rollout begins early June and completes mid-June 2026; requires admin configuration in the Purview portal — labels must cover both Meetings and Files scopes.

---

### MC1301714 — DLP restricts external emails as Copilot grounding data

| Field | Value |
|---|---|
| **Date** | 2026-06-05 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | Public Preview |
| **Link** | [MC1301714](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1301714) |

A new DLP policy control lets admins exclude emails from external senders from being used as grounding data when M365 Copilot and Copilot Chat generate responses, reducing risk from untrusted external content influencing AI outputs. Public preview rollout begins early June 2026; feature is off by default and requires admin configuration.

---

### MC1181769 — Purview DLP integrates with Entra GSA Internet Access

| Field | Value |
|---|---|
| **Date** | 2026-06-15 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1181769](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1181769) |

Microsoft Purview DLP integrates with Entra Global Secure Access Internet Access to intercept and enforce sensitive-file-filtering policies at the network layer, blocking exfiltration to untrusted cloud apps regardless of browser or application used. GA rollout begins mid-June 2026; requires enabling Purview pay-as-you-go billing.

---

## Identity & Access

### MC1243549 — SharePoint OTP retirement, transition to Entra B2B

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Retirement |
| **Link** | [MC1243549](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1243549) |

Beginning May 2026, new external SharePoint/OneDrive sharing invitations switch from One-Time Passcode (SPO OTP) to Microsoft Entra B2B; the `EnableAzureADB2BIntegration` setting no longer controls external sharing behavior. Full OTP retirement completes August 31, 2026 — admins must ensure Entra B2B email OTP is not disabled in Entra External ID settings.

---

### MC1279092 — Passkeys enabled in Entra registration campaigns

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Update |
| **Link** | [MC1279092](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1279092) |

Passkeys (FIDO2) are now a supported targeted authentication method in Microsoft Entra Authentication Methods Registration Campaigns in the Microsoft-Managed state. Rollout from mid-May to late June 2026; tenants with registration campaigns enabled should review campaign targeting to manage passkey enrollment prompts.

---

### MC1220751 — "Require approved client app" Conditional Access control retired

| Field | Value |
|---|---|
| **Date** | 2026-06-01 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Retirement |
| **Link** | [MC1220751](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1220751) |

The "Require approved client app" grant control in Microsoft Entra Conditional Access retires in June 2026; policies relying solely on this control will no longer enforce access restrictions after retirement. **Action required:** migrate affected CA policies to "Require application protection policy" before the retirement date.

---

### MC1282568 — Microsoft Entra passkeys on Windows reaches GA

| Field | Value |
|---|---|
| **Date** | 2026-06-01 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | GA |
| **Link** | [MC1282568](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1282568) |

Passkeys on Windows devices reach GA (rollout completing by mid-June 2026), enabling phishing-resistant sign-in via Windows Hello for Business or platform credentials. Admins must ensure the Passkeys (FIDO2) authentication method is enabled in the Entra admin center; no per-user action required.

---

### MC1300584 — App Instance Lock on by default for new Entra applications

| Field | Value |
|---|---|
| **Date** | 2026-06-05 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Update |
| **Link** | [MC1300584](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1300584) |

Starting early June 2026, all newly created Microsoft Entra application registrations have App Instance Lock enabled by default, preventing sensitive service principal properties from being modified outside the home tenant. Existing applications are unaffected; automation that modifies these properties cross-tenant must be updated before rollout to avoid 400 errors.

---

### MC1223829 — Conditional Access enforcement for policies with resource exclusions

| Field | Value |
|---|---|
| **Date** | 2026-06-15 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Action Required |
| **Link** | [MC1223829](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1223829) |

Starting June 15, 2026, Conditional Access policies targeting All Resources with exclusions begin enforcing for sign-ins that request only certain OIDC or directory scopes (previously exempted). Users signing in through custom apps requesting only these scopes may now receive MFA or device-compliance challenges where they previously did not. Review CA policies that use resource exclusions — most standard tenants require no action.

---

## Endpoint Security

### MC1248388 — Windows Autopatch enables hotpatch updates by default

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Intune |
| **Category** | Endpoint Security |
| **Type** | Update |
| **Link** | [MC1248388](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1248388) |

Starting May 2026, Windows Autopatch enables hotpatch security updates by default for eligible Intune-managed devices, delivering security fixes without requiring device restarts. Opt-out via Quality Update policies has been available since April 2026; non-Autopatch tenants are unaffected.

---

### MC1381119 — Defender for Endpoint EDR updates move to Microsoft Update

| Field | Value |
|---|---|
| **Date** | 2026-05-26 |
| **Service** | Microsoft Defender XDR |
| **Category** | Endpoint Security |
| **Type** | Update |
| **Link** | [MC1381119](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1381119) |

Microsoft Defender for Endpoint EDR updates for Windows 10 now ship through Microsoft Update (KB5005292) rather than bundled in monthly Windows security updates, starting late May 2026; Windows 11 follows by fall 2026. Updates typically do not require restarts; organizations using manual deployments must adjust processes to pull from the Microsoft Update channel.

---

## Threat Protection

### MC1239187 — Defender for Office 365 URL click alerts include Teams

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Defender for Office 365 |
| **Category** | Threat Protection |
| **Type** | GA |
| **Link** | [MC1239187](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1239187) |

Microsoft Defender for Office 365 URL click alerts now extend to Microsoft Teams links (chats and channels), providing visibility into potentially malicious URLs clicked within Teams in addition to email. GCC, GCCH, and DoD GA rollout completed late May 2026.

---

### MC1266905 — Secure Score: Block mshta.exe outbound traffic in MDE

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Defender XDR |
| **Category** | Threat Protection |
| **Type** | Update |
| **Link** | [MC1266905](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1266905) |

Microsoft Secure Score adds a new recommendation to block outbound traffic from mshta.exe (a commonly abused living-off-the-land binary) in Microsoft Defender for Endpoint, reducing risk from LOLBIN-based attacks. Rollout completes late May 2026; admin action is required to implement the recommendation.

---

### MC1293483 — Secure Score: Secure Boot 2023 certificate readiness in MDE

| Field | Value |
|---|---|
| **Date** | 2026-06-01 |
| **Service** | Microsoft Defender XDR |
| **Category** | Threat Protection |
| **Type** | Update |
| **Link** | [MC1293483](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1293483) |

Microsoft Secure Score in Defender for Endpoint adds a recommendation tracking device readiness for the Secure Boot 2023 certificate update before the Windows UEFI CA 2011 certificates expire in June 2026. Enabled by default in Defender for Endpoint; provides device-level visibility and tracks remediation progress.

---

## Platform Security

### MC1261596 — Security Copilot included in Microsoft 365 E5

| Field | Value |
|---|---|
| **Date** | 2026-05-16 |
| **Service** | Microsoft Defender XDR |
| **Category** | Platform Security |
| **Type** | Rollout |
| **Link** | [MC1261596](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1261596) |

Security Copilot (400 Security Compute Units per 1,000 users) is rolling out to Microsoft 365 E5 tenants from April 20 through June 30, 2026, with AI-powered security assistance embedded across Defender, Intune, Entra, and Purview, plus promptbooks and agentic scenarios. Tenants receive 7-day advance notification before activation; no admin action required for provisioning.

---

### MC1304290 — Microsoft 365 Packaging Update: Defender Plan 1 and Safe Links

| Field | Value |
|---|---|
| **Date** | 2026-06-15 |
| **Service** | Microsoft 365 suite |
| **Category** | Platform Security |
| **Type** | Update |
| **Link** | [MC1304290](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1304290) |

Starting mid-June 2026, Microsoft 365, Office 365, and EMS suite licenses gain Microsoft Defender for Office 365 Plan 1 by default, adding Safe Links, Safe Attachments, anti-phishing protections, and URL time-of-click protection applied to all users. Rollout completes August 1, 2026; built-in protection policies apply automatically and cannot be disabled, though they can be supplemented or overridden by custom policies.

---

*Items outside the security/compliance scope (meeting UX, reactions, Loop social features, non-security Intune updates, etc.) were reviewed and excluded. Sources: [mc.merill.net](https://mc.merill.net) message center archive.*

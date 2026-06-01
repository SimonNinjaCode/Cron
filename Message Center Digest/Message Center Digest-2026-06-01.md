# Microsoft 365 Message Center Digest — Security & Compliance
**Reporting period: May 2026 | Generated: 2026-06-01**

This digest covers **17 security and compliance items** from the Microsoft 365 Message Center with a published date or material rollout milestone (GA, preview, opt-out, enforcement start) in May 2026. Items are sorted by date ascending.

---

## Items

| Title | Service | Category | Type | Summary | Date | Link |
|-------|---------|----------|------|---------|------|------|
| Defender XDR: Email summary via Security Copilot | Microsoft Defender XDR | Threat Protection | GA | Security Copilot-powered AI email summaries reach GA on the email entity page in Defender XDR (early–mid May 2026). Requires Security Copilot access and SCUs; surfaces detections, timeline analysis, and URL/attachment assessments in one place to reduce investigation time. | 2026-05-01 | [MC1268924](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1268924) |
| Defender for Office 365 URL click alerts include Teams | Microsoft Defender for Office 365 | Threat Protection | GA | URL click alerts now capture malicious link clicks originating in Teams messages in addition to email. Commercial rollout completes May 2026; GCC/GCCH/DoD GA begins early May and completes late May 2026. No admin action required. | 2026-05-01 | [MC1239187](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1239187) |
| Retirement of SharePoint OTP, transition to Entra B2B | Microsoft Entra | Identity & Access | Retirement | SharePoint One-Time Passcode external sharing retires in May 2026; new external invitations and authentications switch automatically to Microsoft Entra B2B. Existing OTP-based links stop working — communicate change to external collaborators and helpdesk. | 2026-05-01 | [MC1243549](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1243549) |
| Entra passkeys on Windows GA | Microsoft Entra | Identity & Access | GA | Phishing-resistant passwordless sign-in via Entra passkeys is generally available for managed and unmanaged Windows devices. Worldwide rollout started late April and continues through mid-June 2026; controlled via Authentication Methods policies and Conditional Access. | 2026-05-01 | [MC1282568](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1282568) |
| Passkey profiles and FIDO2 migration GA | Microsoft Entra | Identity & Access | GA | Passkey (FIDO2) profiles reach GA with rollout beginning early May 2026. Existing FIDO2 passkey tenants are automatically migrated to profiles; registration campaign settings update automatically with no immediate admin action required. | 2026-05-01 | [MC1221452](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1221452) |
| Autopatch: Hotpatch updates enabled by default | Microsoft Intune | Endpoint Security | Plan for Change | Windows Autopatch enables hotpatch security updates by default for eligible Intune-managed Windows 11 devices starting with the May 2026 security update, eliminating restart requirements. Opt-out available via Quality Update policies; Virtualization-based Security must be enabled on devices. | 2026-05-01 | [MC1248388](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1248388) |
| Endpoint DLP Device Health Reporting Dashboard | Microsoft Purview | Data Protection & Compliance | GA | New consolidated Endpoint DLP Device Health Dashboard in Purview provides at-a-glance views of device health, policy sync status, endpoint activity, and Defender version distribution. Rollout begins May 2026 with no configuration required; access directly in the Purview portal. | 2026-05-01 | [MC1262572](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1262572) |
| Sensitivity label inheritance for Teams meeting artifacts | Microsoft Purview | Data Protection & Compliance | Public Preview | Sensitivity labels applied to Teams meetings automatically inherit to transcripts, recordings, and Loop meeting notes. Public preview begins early May 2026 and completes mid-May 2026; enabled by default for preview-eligible tenants with no admin action required. | 2026-05-01 | [MC1279068](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1279068) |
| DLP new policy options for inline network and Edge for Business | Microsoft Purview | Data Protection & Compliance | GA | GA for DLP policy options enabling label-based scoping for unmanaged cloud apps, URL-contains conditions in policy rules, and user email alerts when activities are blocked. Late April–May 2026 GA rollout; admin configuration required to activate new controls on existing policies. | 2026-05-01 | [MC1247881](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1247881) |
| Reminder: CA "Require approved client app" retires June 2026 | Microsoft Entra | Identity & Access | Plan for Change | The "Require approved client app" Conditional Access grant control retires June 30, 2026. After retirement the control is silently ignored — admins must migrate all affected CA policies to "Require app protection policy" before the deadline to maintain MAM enforcement. | 2026-05-01 | [MC1220751](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1220751) |
| Older Defender for Endpoint mobile apps retired | Microsoft Defender XDR | Endpoint Security | Retirement | Microsoft Defender for Endpoint app versions on iOS and Android released before February 2026 lost cloud connectivity and stopped functioning on May 10, 2026. Admins must ensure all managed devices are running a current version; no configuration changes needed beyond updating the app. | 2026-05-10 | [MC1276511](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1276511) |
| External access tokens for actionable messages retired | Microsoft Entra | Identity & Access | Retirement | External access tokens for Outlook Actionable Messages were retired on May 15, 2026. All integrations relying on external tokens fail after this date; migrate affected workflows to Microsoft Entra-based authentication immediately. | 2026-05-15 | [MC1189663](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1189663) |
| Passkeys in Entra registration campaigns GA | Microsoft Entra | Identity & Access | GA | Passkey (FIDO2) support reaches the Microsoft Managed state within Entra Registration Campaigns. Rollout begins mid-May 2026 and completes late June 2026; eligible tenants automatically receive passkey registration nudges after MFA completion. | 2026-05-15 | [MC1279092](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1279092) |
| Brand impersonation protection for Teams Calling | Microsoft Teams | Threat Protection | Rollout | Teams Calling shows a high-risk call warning overlay when inbound external calls exhibit brand impersonation signals, allowing users to accept, block, or end the call. Enabled by default with no admin action required; rollout begins mid-May and completes late May 2026. | 2026-05-15 | [MC1219793](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1219793) |
| Teams External domains anomalies report | Microsoft Teams | Threat Protection | Rollout | New External Domains Anomalies report in Teams admin center surfaces sudden spikes in first-time cross-tenant communication to help detect BEC, phishing, or data exfiltration attempts. Daily alert summaries available; rollout completes late May 2026 with no configuration required. | 2026-05-15 | [MC1219794](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1219794) |
| Sensitivity labels block all connected experiences | Microsoft Purview | Data Protection & Compliance | Public Preview | New sensitivity label setting lets admins block all connected experiences that analyze document content in Word, Excel, and PowerPoint, preventing data from leaving the tenant boundary. Public preview begins mid-May 2026 and completes late May 2026. | 2026-05-15 | [MC1297982](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1297982) |
| Extended scoping for sensitivity label policies GA | Microsoft Purview | Data Protection & Compliance | GA | Admins gain granular scoping controls to target sensitivity label policies to specific users, groups, or sites, reducing over-broad policy application. GA rollout accelerated to late May 2026 (from the originally planned mid-June); expected to complete early June 2026. | 2026-05-25 | [MC1262573](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1262573) |

---

## ⚠️ Action Required Items

The following items require admin action, ordered by urgency. Note that the May deadlines have now passed (today is 2026-06-01).

### PAST DEADLINE — Immediate attention needed

**MC1276511 — Older Defender for Endpoint mobile apps retired (deadline: May 10, 2026)**
- App versions on iOS and Android released before February 2026 are now non-functional.
- **Action:** Check all managed devices for outdated Defender for Endpoint app versions and update immediately. Use Intune app deployment to push the current version.
- Link: [MC1276511](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1276511)

**MC1189663 — External access tokens for actionable messages retired (deadline: May 15, 2026)**
- External access tokens for Outlook Actionable Messages are now retired. Any integration that has not yet migrated to Microsoft Entra authentication is broken.
- **Action:** Identify all Actionable Message integrations, update token validation logic to use Entra tokens, and re-test workflows.
- Link: [MC1189663](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1189663)

### UPCOMING DEADLINE

**MC1220751 — "Require approved client app" Conditional Access control retires June 30, 2026**
- After June 30, 2026, this CA grant control will be silently ignored, potentially leaving mobile devices without MAM enforcement.
- **Action:** Review all Conditional Access policies using this control and migrate to "Require app protection policy." Use the migration guide at [aka.ms/approvedclientappmigration](https://learn.microsoft.com/en-us/entra/identity/conditional-access/migrate-approved-client-app).
- Link: [MC1220751](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1220751)

### PLAN FOR CHANGE — Already active

**MC1248388 — Windows Autopatch hotpatch enabled by default (effective: May 2026 security update)**
- Hotpatch security updates are now being applied by default to eligible Autopatch-managed Windows 11 devices. Devices without Virtualization-based Security enabled will not receive hotpatches.
- **Action:** If your organization is not ready for this change, configure Quality Update policies to opt out specific device groups or the whole tenant. Verify VBS is enabled on target devices.
- Link: [MC1248388](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1248388)

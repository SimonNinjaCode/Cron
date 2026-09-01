# Microsoft 365 Message Center Digest — Security & Compliance
**Run date:** 2026-09-01 (Europe/Berlin)
**Coverage window:** 2026-08-02 → 2026-09-01

---

## Summary

| Category | Items |
|---|---|
| Data Protection & Compliance | 10 |
| Identity & Access | 8 |
| Email Security | 2 |
| Threat Protection | 2 |
| Platform Security | 2 |
| **Total** | **24** |

---

## Data Protection & Compliance

---

### 1. Purview Information Protection: Classifier Simulation Mode GA

| Field | Value |
|---|---|
| **Date** | 2026-08-01 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1185445](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1185445) |

**Summary:** Admins can now test and validate custom trainable classifiers against production data in Simulation Mode before publishing, enabling optimization to reduce false positives and noisy matches. GA rollout began end of July 2026 and completes end of August 2026; no action required but admins should leverage the new simulation controls in the Purview compliance portal.

---

### 2. Purview DLM: Retention Based on "Last Accessed" for OneDrive and SharePoint (GA)

| Field | Value |
|---|---|
| **Date** | 2026-08-12 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC999442](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC999442) |

**Summary:** Retention policies and labels can now be configured to trigger based on when a file was last accessed in OneDrive or SharePoint, helping delete stale data and improve Copilot response quality. Rollout began late July 2026 and completes mid-August; admins can use the new "When items were last accessed" condition when creating or editing retention settings. Applies to Microsoft 365 file types; non-Microsoft file types will follow in a future rollout.

---

### 3. Purview DLP: Default Protection Controls for Exchange Online When Classification Fails (GA)

| Field | Value |
|---|---|
| **Date** | 2026-08-12 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1387682](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1387682) |

**Summary:** Purview DLP gains new conditions to detect and act on classification failures—timeouts, throttling, and scan errors—in Exchange Online, surfacing failures that previously went undetected. GA rollout begins mid-August and completes late August 2026; admins should monitor Activity Explorer and DLP alerts for increased alert volume after enabling and communicate the change to security/compliance teams.

---

### 4. Purview Endpoint DLP: FTP and SFTP Transfer Monitoring (GA)

| Field | Value |
|---|---|
| **Date** | 2026-08-12 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1404319](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1404319) |

**Summary:** Endpoint DLP can now monitor and protect file transfers over FTP and SFTP on managed Windows devices, closing a data exfiltration channel not previously covered. Preview began late July 2026; GA rollout began mid-August 2026.

---

### 5. Microsoft Edge Enforces Screen Capture Restrictions for Sensitivity-Labeled PDFs

| Field | Value |
|---|---|
| **Date** | 2026-08-12 |
| **Service** | Microsoft Purview / Microsoft Edge |
| **Category** | Data Protection & Compliance |
| **Type** | Rollout |
| **Link** | [MC1409303](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1409303) |

**Summary:** Microsoft Edge now enforces "Do Not Allow Screen Capture" restrictions on sensitivity-labeled PDFs viewed in OneDrive and SharePoint web viewers, aligning web behavior with existing desktop enforcement. Targeted Release rollout began early August; worldwide rollout mid- to late August 2026. Admins should review sensitivity labels with screen-capture restrictions and update helpdesk documentation.

---

### 6. Purview Information Protection: Sensitivity Labels for Microsoft Entra Security Groups (GA)

| Field | Value |
|---|---|
| **Date** | 2026-08-15 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [RM568217](https://www.microsoft.com/en-us/microsoft-365/roadmap?id=568217) |

**Summary:** Sensitivity labels can now be applied to Microsoft Entra cloud security groups using the same labels already configured for Microsoft 365 groups and sites—no separate label configuration required. Public preview began May 28, 2026; GA reached August 2026. Requires at least one Entra P1 license; mail-enabled security groups are not supported.

---

### 7. Purview DLP: Data Security Triage Agent in Microsoft Defender XDR (GA Timeline Update)

| Field | Value |
|---|---|
| **Date** | 2026-08-17 |
| **Service** | Microsoft Purview / Microsoft Defender XDR |
| **Category** | Data Protection & Compliance |
| **Type** | Update |
| **Link** | [MC1255406](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1255406) |

**Summary:** Microsoft revised the GA timeline for the Data Security Triage Agent (AI-generated summaries and categorizations for DLP alerts in Defender XDR) from August 2026 to August 2027; the feature remains available to deploy from Defender XDR with management in Purview. Admins planning around this feature should adjust roadmap timelines accordingly; existing DLP policies and enforcement are unaffected.

---

### 8. Purview DLM: Hard Delete OneDrive and SharePoint Files with Priority Cleanup Workflow

| Field | Value |
|---|---|
| **Date** | 2026-09-01 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1261587](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1261587) |

**Summary:** Purview Data Lifecycle Management introduces a priority cleanup workflow that allows admins to permanently (hard) delete specific OneDrive and SharePoint content—even when retention policies or holds are active—subject to mandatory eDiscovery admin review and approval. Not enabled by default; admins must configure it in Purview portal > Data Lifecycle Management > Priority cleanup. Rollout begins early September 2026 and targets rapidly growing Copilot/AI-generated content.

---

### 9. Purview DLM: Insights for Copilot and AI App Interactions

| Field | Value |
|---|---|
| **Date** | 2026-09-01 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1413308](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1413308) |

**Summary:** A new insights dashboard in Purview Data Lifecycle Management surfaces data access patterns from Copilot and AI app interactions, helping admins understand what data AI accesses and improve retention governance. Rollout begins early September 2026.

---

### 10. Purview eDiscovery: Customer-Managed Key (CMK) for Direct Export (GA)

| Field | Value |
|---|---|
| **Date** | 2026-09-01 |
| **Service** | Microsoft Purview |
| **Category** | Data Protection & Compliance |
| **Type** | GA |
| **Link** | [MC1289726](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1289726) |

**Summary:** eDiscovery Direct Export packages are now automatically encrypted using the organization's customer-managed key (CMK) for tenants with Data Encryption Policies (DEPs) configured via MDEP. Preview was available from early May 2026; GA begins early September 2026. No change to the eDiscovery UX; encryption is applied automatically based on existing DEP configuration.

---

## Identity & Access

---

### 11. Microsoft Entra: New Service Plans for Conditional Access and ID Protection for Agents

| Field | Value |
|---|---|
| **Date** | 2026-08-02 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | GA |
| **Link** | [MC1395007](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1395007) |

**Summary:** New service plans are automatically added to Microsoft Agent 365 and Microsoft 365 E7 subscriptions to formally enable Conditional Access and ID Protection capabilities for AI agent identities. No existing policies or configurations are changed; admins using these capabilities without the qualifying license should review licensing requirements.

---

### 12. Microsoft Entra ID Governance: Account Discovery (GA)

| Field | Value |
|---|---|
| **Date** | 2026-08-04 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | GA |
| **Link** | [MC1287372](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1287372) |

**Summary:** Account Discovery in Entra ID Governance helps admins identify local, orphaned, and unmanaged application accounts in connected third-party apps (e.g., Salesforce, Atlassian) that exist outside of Entra ID, matching them to Entra users to bring access under centralized governance. Off by default; requires admin opt-in. GA rollout begins early August and completes late August 2026.

---

### 13. Microsoft Entra: SSPR CAPTCHA Replaced with Behavior-Based Protection

| Field | Value |
|---|---|
| **Date** | 2026-08-04 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Update |
| **Link** | [MC1400824](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1400824) |

**Summary:** Legacy CAPTCHA in self-service password reset (SSPR) is replaced with backend throttling and behavior-based abuse detection, improving both security and accessibility. No user or admin action required; SSPR flows continue unchanged. Rollout begins early August and completes late August 2026. Admins should update helpdesk documentation to note that CAPTCHA prompts will no longer appear.

---

### 14. Microsoft Entra: SMS First-Factor Sign-In Retired for Entra ID Free Tenants

| Field | Value |
|---|---|
| **Date** | 2026-08-11 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Retirement |
| **Link** | [MC1448374](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1448374) |

**Summary:** As of August 11, 2026, users in Entra ID Free tenants can no longer sign in using only a phone number and SMS OTP (first-factor); attempts are blocked due to fraud risk. SMS as a second-factor MFA method is unaffected. Admins should identify users relying exclusively on SMS first-factor and ensure they have registered an alternative authentication method.

---

### 15. Microsoft Entra: federatedTokenValidationPolicy Default Settings Change

| Field | Value |
|---|---|
| **Date** | 2026-08-18 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Plan for Change |
| **Link** | [MC1303719](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1303719) |

**Summary:** Entra updated federatedTokenValidationPolicy to block federated sign-ins where the internalDomainFederation object doesn't match the user's UPN domain, closing a potential cross-domain federation abuse vector. Rollout began mid-August and completes end of August 2026; affects federated domains configured before December 2025. Admins should verify federation configurations to prevent sign-in disruptions.

---

### 16. Microsoft Entra: System-Preferred Authentication Now Applies to First-Factor Sign-In

| Field | Value |
|---|---|
| **Date** | 2026-08-24 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Update |
| **Link** | [MC1411574](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1411574) |

**Summary:** System-preferred authentication in Entra ID now applies to first-factor sign-in (in addition to second-factor) for tenants in the Microsoft managed state, automatically presenting users with their highest-ranked registered authentication method. Tenants can override the managed state via authentication method policy settings; user guidance should be updated to reflect the new behavior. Rollout runs June–September 2026.

---

### 17. Microsoft Entra: Passkey Registration Experience Optimizations

| Field | Value |
|---|---|
| **Date** | 2026-08-26 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Update |
| **Link** | [MC1440968](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1440968) |

**Summary:** Microsoft is rolling out UX improvements to the passkey registration experience in Entra ID in late August 2026. No admin action or configuration changes required.

---

### 18. Microsoft Entra: Passkeys by Default; Microsoft-Provided SMS and Voice MFA Retirement (Action Required)

| Field | Value |
|---|---|
| **Date** | 2026-09-01 |
| **Service** | Microsoft Entra |
| **Category** | Identity & Access |
| **Type** | Action Required |
| **Link** | [MC1426371](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1426371) |

**Summary:** Effective September 1, 2026, passkeys are enabled by default for eligible users, and the Registration Campaign for passkeys moves to Microsoft Managed state—users are prompted at MFA sign-in to register a passkey (skippable). Microsoft-provided SMS and voice MFA authentication retires February 1, 2027; organizations that require telephony must configure a telecom provider via the Microsoft Security Store before that date or face sign-in disruptions. Admins should audit users still relying on SMS/voice MFA and begin passkey migration now.

---

## Email Security

---

### 19. Microsoft Defender for Office 365: Encrypted Email Attachment Protection

| Field | Value |
|---|---|
| **Date** | 2026-08-04 |
| **Service** | Microsoft Defender for Office 365 |
| **Category** | Email Security |
| **Type** | GA |
| **Link** | [MC1440701](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1440701) |

**Summary:** A new opt-in setting in Safe Attachments policies allows admins to quarantine emails containing password-protected or encrypted attachments that Defender cannot scan or detonate. Admins control release of quarantined messages; end users can self-release by supplying the attachment password. Worldwide rollout early to late August 2026; GCC/GCC High/DoD rollout follows late August–October 2026.

---

### 20. Microsoft Defender for Office 365: Prompt Injection Protection for Email

| Field | Value |
|---|---|
| **Date** | 2026-08-04 |
| **Service** | Microsoft Defender for Office 365 |
| **Category** | Email Security |
| **Type** | GA |
| **Link** | [MC1422060](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1422060) |

**Summary:** Defender for Office 365 Plan 2 and Microsoft 365 E5 tenants now receive built-in detection of malicious prompt injection content in emails designed to manipulate AI assistants and agents; high-confidence threats are automatically quarantined as High Confidence Phish using a new "Prompt Injection Protection" detection technology. Enabled by default; no admin action required. Admins should review quarantine workflows and use Tenant Allow/Block List for exceptions. GA completing early September 2026.

---

## Threat Protection

---

### 21. Microsoft Teams: Report Security Concerns in Meetings

| Field | Value |
|---|---|
| **Date** | 2026-08-10 |
| **Service** | Microsoft Teams |
| **Category** | Threat Protection |
| **Type** | GA |
| **Link** | [MC1446794](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1446794) |

**Summary:** Teams users can now report suspicious or malicious activity (phishing, impersonation, scams) during meetings via a "Report a meeting" option; reports are reviewed by admins in Teams admin center and Microsoft Defender. Enabled by default; rollout began August 2026.

---

### 22. Microsoft Teams: Report Security Concerns in Group Calls

| Field | Value |
|---|---|
| **Date** | 2026-08-10 |
| **Service** | Microsoft Teams |
| **Category** | Threat Protection |
| **Type** | Rollout |
| **Link** | [MC1447673](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1447673) |

**Summary:** Teams users can report suspicious group calls from call history, enabling admins to investigate potential scams, impersonation, and unwanted external calls via Teams admin center and Microsoft Defender. Enabled by default; rollout runs August–October 2026.

---

## Platform Security

---

### 23. The August 2026 Windows Security Update Is Now Available

| Field | Value |
|---|---|
| **Date** | 2026-08-11 |
| **Service** | Microsoft 365 suite |
| **Category** | Platform Security |
| **Type** | Update |
| **Link** | [MC1452953](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1452953) |

**Summary:** The August 2026 cumulative security update (including KB5120240 for Windows 11 23H2) is now available for all supported Windows versions; it includes Secure Boot certificate updates, expanded high-confidence device targeting for Autopatch, and a standalone update for hotpatch-enrolled devices. A limited number of devices may require one additional restart during installation. Admins should deploy promptly via Intune, WSUS, or Windows Update.

---

### 24. Microsoft Defender for Endpoint: EDR Security Updates Move to Microsoft Update on Windows

| Field | Value |
|---|---|
| **Date** | 2026-08-15 |
| **Service** | Microsoft Defender XDR |
| **Category** | Platform Security |
| **Type** | Update |
| **Link** | [MC1381119](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1381119) |

**Summary:** Defender endpoint detection and response (EDR) updates are now delivered via Microsoft Update (KB5005292) independently of the monthly Windows cumulative update, enabling faster security improvements without tying them to Patch Tuesday cycles. Rollout began with Windows 10 in late May 2026, expanding to Windows 11 and remaining supported versions through fall 2026. Organizations using manual deployment should add the new update package to their standard process; no action needed for Microsoft Update-connected devices.

---

*Sources: [mc.merill.net](https://mc.merill.net/) · [admin.microsoft.com Message Center](https://admin.microsoft.com/Adminportal/Home#/MessageCenter) · Microsoft 365 Roadmap*

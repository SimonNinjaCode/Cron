# Microsoft 365 Message Center Digest -- Security & Compliance

Period: 2026-07-14 through 2026-08-13 (Europe/Berlin)
Generated: 2026-08-13
Focus: Security, identity, data protection, threat protection, compliance, endpoint security

---

## Summary

32 security and compliance messages are in scope for this 30-day window.

- **Microsoft Purview** has 13 items. Endpoint DLP expands to FTP/SFTP and gains AI-powered skills, adaptive protection links to retention, and last-accessed-date retention reaches GA. A late-July reversion of the custom SIT capturing-group enforcement is worth noting.
- **Microsoft Entra** has 9 items. Passkeys go default from September, blocking dangerous legacy partner-tier roles from August 3, stricter federated-token validation from mid-August, and SSPR CAPTCHA replacement.
- **Microsoft Defender XDR / Defender for Office 365** has 4 items. Prompt injection protection is enabled by default, ZAP now cleans Deleted Items, Defender Threat Intelligence converges into Defender/Sentinel, and encrypted-attachment quarantine arrives.
- **Exchange Online** has 1 action-required item on transport rule reporting scripts.
- **Microsoft 365 Suite** has 1 item. The 2026 packaging update adds Defender Plan 1 and URL time-of-click protection.

---

## Items by Category

### Data Protection & Compliance -- Microsoft Purview

| Date | ID | Title | Service | Type | Summary | Link |
|------|----|-------|---------|------|---------|------|
| 2026-07-14 | MC1419797 | DLP: Network-layer protection via Entra Global Secure Access | Microsoft Purview | Public Preview | Extends Purview DLP policies to the network layer by integrating with Microsoft Entra Global Secure Access Internet Access, so sensitive files get blocked at the network level before traffic leaves the device. Requires coordination across Purview, Entra, and Defender admins. Rollout begins July 2026 and completes October 2026. | [MC1419797](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1419797) |
| 2026-07-15 | MC1301831 | Data Security Investigations: OCR support GA | Microsoft Purview | GA | Optical character recognition (OCR) support in Purview Data Security Investigations reaches GA mid-July 2026. Scans and classifies image-based content (screenshots, scanned documents) within investigations. No admin action required to enable. | [MC1301831](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1301831) |
| 2026-07-15 | MC1384412 | Data Lifecycle Management: Retention policies for Planner content | Microsoft Purview | GA | Admins can now apply retention and deletion policies to Microsoft Planner (Tasks by Planner) task content via Purview DLM. Rollout runs mid-July to early August 2026; no existing policies are impacted. | [MC1384412](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1384412) |
| 2026-07-15 | MC1387681 | Insider Risk Management: Policy recommendation panel | Microsoft Purview | Rollout | A new policy recommendation panel in Insider Risk Management shows coverage gaps for data leakage and AI-misuse risk scenarios. Helps admins fine-tune policies without disrupting existing workflows. Rollout completes late July 2026. | [MC1387681](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1387681) |
| 2026-07-15 | MC1384415 | Endpoint DLP: Pre-curated file extension list | Microsoft Purview | GA | Endpoint Data Loss Prevention policies now support a pre-curated list of high-risk file extensions, simplifying policy configuration and broadening file-type coverage out of the box. Rollout runs early to late July 2026. | [MC1384415](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1384415) |
| 2026-07-15 | MC1385588 | DLP: Enriched audit data for Exchange matched rules | Microsoft Purview | GA | DLP rule-match audit events for Exchange Online now include enriched matched-condition details (matched values, rule name, policy name), improving compliance investigation accuracy. Rollout completed late June to July 2026. | [MC1385588](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1385588) |
| 2026-07-25 | MC1381121 | Endpoint DLP: AI policy sync and device health skill | Microsoft Purview | Public Preview | New AI-powered skills in Purview enable automatic policy sync checks and device health diagnostics for Endpoint DLP. Preview available late July 2026; GA expected late August 2026. Admins get a single-pane-of-glass view of device compliance state. | [MC1381121](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1381121) |
| 2026-07-25 | MC791110 | Data Lifecycle Management: Adaptive protection integration | Microsoft Purview | Rollout | Adaptive protection now integrates with Data Lifecycle Management, so retention policies automatically tighten based on a user's calculated insider risk level. Rollout begins late July and completes mid-August 2026. | [MC791110](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC791110) |
| 2026-07-28 | MC999442 | Data Lifecycle Management: Last-accessed retention for OneDrive and SharePoint | Microsoft Purview | GA | Retention policies based on a file's last-accessed date reach GA for OneDrive and SharePoint files. Admins can now configure policies that extend the retention clock on actively used files, reducing accidental deletion of live content. Rollout late July to mid-August 2026. | [MC999442](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC999442) |
| 2026-07-28 | MC1404319 | Endpoint DLP: FTP and SFTP support | Microsoft Purview | Public Preview | Endpoint DLP can now monitor and enforce policies on file transfers over FTP and SFTP protocols on managed Windows devices, closing a data-exfiltration channel. Preview starts late July 2026; GA expected mid-August 2026. | [MC1404319](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1404319) |
| 2026-07-28 | MC1413309 | Custom SIT capturing-group limit enforcement reverted | Microsoft Purview | Update | Microsoft reverted the previously announced one-capturing-group limit for custom Sensitive Information Type regex patterns effective late July 2026, following customer feedback. Multiple top-level capturing groups are again permitted; admins do not need to update existing SITs. | [MC1413309](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1413309) |
| 2026-08-12 | MC1387682 | DLP: Default protection for Exchange when classification fails | Microsoft Purview | GA | Purview DLP now detects scan failures (timeouts, throttling, errors) in Exchange Online and can apply configurable default protection actions when content cannot be classified. Admins gain visibility into previously silent classification failures. GA rollout begins mid-August 2026. | [MC1387682](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1387682) |
| 2026-08-12 | MC1311975 | Purview compliance portal: Role groups UI enhancements | Microsoft Purview | Rollout | The Role Groups page in the Purview compliance portal is redesigned so admins can view role assignments filtered by roles, members, or their own permissions in a single view. Rollout completes mid-August 2026. | [MC1311975](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1311975) |

---

### Identity & Access -- Microsoft Entra

| Date | ID | Title | Service | Type | Summary | Link |
|------|----|-------|---------|------|---------|------|
| 2026-07-14 | MC1395007 | New service plans: Conditional Access and ID Protection for agents | Microsoft Entra | GA | Microsoft Entra adds Conditional Access for Agents and ID Protection for Agents service plans to Microsoft Agent 365 and Microsoft 365 E7, enabling secure identity management for AI agent workloads. GA rollout began early July and completes early August 2026. | [MC1395007](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1395007) |
| 2026-07-25 | MC1411574 | System-preferred authentication now applies to first-factor sign-in | Microsoft Entra | Rollout | For tenants where system-preferred authentication is in the Microsoft-managed state, Entra now selects the most secure registered method for first-factor sign-in (not just second-factor). Tenants in Enabled or Disabled state are not affected. Rollout completes late July 2026. | [MC1411574](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1411574) |
| 2026-07-28 | MC1426371 | Passkeys by default and retirement of Microsoft-provided SMS/voice auth | Microsoft Entra | Plan for Change | Starting September 1, 2026, passkeys become the default authentication experience in Microsoft Entra. Microsoft-provided SMS and voice MFA will retire February 1, 2027. Admins must configure a telecom provider via the Microsoft Security Store before February 2027 or face service disruption. | [MC1426371](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1426371) |
| 2026-08-01 | MC1400824 | SSPR CAPTCHA replaced with behavioral abuse detection | Microsoft Entra | Update | Legacy CAPTCHA prompts in the Self-Service Password Reset flow are being replaced with backend throttling and behavior-based abuse detection starting early August 2026. Users will no longer see CAPTCHA; no admin action required and no disruption to password reset flows. | [MC1400824](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1400824) |
| 2026-08-01 | MC1423108 | Improved restore experience for Authenticator passkeys on iOS | Microsoft Entra | GA | Microsoft Authenticator on iOS receives a redesigned, guided restore flow for passkeys when users migrate to a new device. Requires iCloud Keychain backup. Enabled by default; no admin configuration needed. Rollout August 2026. | [MC1423108](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1423108) |
| 2026-08-03 | MC1409305 | Blocking new assignments to Partner Tier1/Tier2 Support roles | Microsoft Entra | Action Required | Starting August 3, 2026, new assignments to Partner Tier1 Support and Partner Tier2 Support roles in Entra return HTTP 400 errors. Existing assignments continue to work, but admins must update scripts, CSP/GDAP workflows, and automation to use least-privilege alternatives (User Administrator, Helpdesk Administrator, or custom roles). | [MC1409305](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1409305) |
| 2026-08-05 | MC1437671 | Passwordless password change in My Sign-Ins | Microsoft Entra | GA | Users with passkeys, FIDO2 keys, or Windows Hello for Business can change their password from My Sign-Ins without knowing the current password and without SSPR. The setting is tenant-wide, off by default, and admins must opt in. Rollout planned late October 2026. | [MC1437671](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1437671) |
| 2026-08-11 | MC1450133 | Users can register passkey as their first MFA method | Microsoft Entra | Plan for Change | Microsoft will allow users to register a passkey or passwordless credential as their very first MFA method during sign-up flows, lowering adoption barriers for phishing-resistant authentication. No admin action required. Rollout begins January 2027, completing February 2027. | [MC1450133](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1450133) |
| 2026-08-12 | MC1303719 | Stricter federatedTokenValidationPolicy defaults | Microsoft Entra | Action Required | Entra will enforce stricter federatedTokenValidationPolicy by default starting mid-August 2026, blocking federated sign-ins where the internalDomainFederation object does not match the user's UPN domain. Tenants with federated domains configured before December 2025 should audit their federation configuration to avoid authentication disruption. | [MC1303719](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1303719) |

---

### Threat Protection -- Microsoft Defender XDR / Defender for Office 365

| Date | ID | Title | Service | Type | Summary | Link |
|------|----|-------|---------|------|---------|------|
| 2026-07-14 | MC1422060 | Defender for Office 365: Prompt injection protection for email | Microsoft Defender for Office 365 | GA | Microsoft Defender for Office 365 (Plan 2 / M365 E5) now includes prompt injection protection that detects and blocks malicious email content crafted to manipulate AI assistants (Copilot). Enabled by default from early July 2026; no admin configuration required. | [MC1422060](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1422060) |
| 2026-07-28 | MC1323263 | Defender for Office 365: ZAP expands cleanup to Deleted Items | Microsoft Defender for Office 365 | GA | Zero-hour Auto Purge (ZAP) now retroactively scans and remediates malicious messages in users' Deleted Items folders within the ZAP detection window, following existing policy actions (junk, quarantine). A new SourceLocation column in EmailPostDeliveryEvents (Advanced Hunting) shows the originating folder. Rollout completes late July 2026. | [MC1323263](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1323263) |
| 2026-08-01 | MC1192257 | Defender Threat Intelligence: Convergence with Defender and Sentinel | Microsoft Defender XDR | Update | Microsoft Defender Threat Intelligence capabilities are fully integrated into Microsoft Defender XDR and Microsoft Sentinel as of August 1, 2026. After this date, standalone MDTI access requires an active Defender or Sentinel license. Integrated threat intelligence is now available natively within the SecOps workflow. | [MC1192257](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1192257) |
| 2026-08-04 | MC1440701 | MDO: Encrypted email attachment quarantine protection | Microsoft Defender for Office 365 | GA | Admins can now configure Safe Attachments policies to quarantine emails containing password-protected attachments that Defender for Office 365 cannot scan or detonate. Off by default; users can self-release by providing the attachment password (triggering just-in-time detonation). Supports ZIP, GZIP, 7z, RAR, PDF, and Office formats. Rollout August 2026. | [MC1440701](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1440701) |

---

### Email Security -- Exchange Online

| Date | ID | Title | Service | Type | Summary | Link |
|------|----|-------|---------|------|---------|------|
| 2026-07-30 | MC1323250 | Action Required: Update transport rule reporting scripts | Exchange Online | Action Required | Starting July 30, 2026, `Get-MailDetailTransportRuleReport` and `Get-MailTrafficPolicyReport` return transport rule data only when the `-EventType` parameter (`TransportRuleHits` or `TransportRuleActionHits`) is explicitly specified. Any scripts or automation that call these cmdlets without `-EventType` will receive empty results. Update scripts before July 30. | [MC1323250](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1323250) |

---

### Platform Security -- Microsoft 365 Suite

| Date | ID | Title | Service | Type | Summary | Link |
|------|----|-------|---------|------|---------|------|
| 2026-08-01 | MC1304290 | 2026 Microsoft 365 Packaging Update: Security additions | Microsoft 365 suite | GA | The 2026 Microsoft 365 licensing repackaging includes security additions: Microsoft Defender for Office 365 Plan 1 (URL time-of-click protection), Intune device management improvements, and +50 GB Exchange Online storage are bundled into applicable plans. Rollout completes early August 2026. | [MC1304290](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1304290) |

---

## Action Required Items -- Deadline Summary

| Deadline | ID | Action |
|----------|----|--------|
| **2026-07-30 (PASSED)** | MC1323250 | Add `-EventType` parameter to transport rule reporting cmdlets |
| **2026-08-03 (PASSED)** | MC1409305 | Replace Partner Tier1/Tier2 Support role assignments in scripts and GDAP workflows |
| **2026-08-12** | MC1303719 | Audit federated domain configuration before stricter policy defaults enforce mid-August |
| **Before 2027-02-01** | MC1426371 | Configure SMS/voice telecom provider via Microsoft Security Store, or migrate users to passkeys |

---

## Items Approaching -- Key Upcoming Milestones

| Date | ID | Event |
|------|----|-------|
| 2026-08-12+ | MC1387682 | DLP classification-failure protection for Exchange Online GA begins rolling out |
| 2026-08-12+ | MC1303719 | Stricter federated-token validation policy enforced by default |
| Late Aug 2026 | MC1381121 | Endpoint DLP AI policy sync and device health skill reaches GA |
| Late Aug 2026 | MC1404319 | Endpoint DLP FTP/SFTP support reaches GA |
| 2026-09-01 | MC1426371 | Passkeys become the default authentication experience in Microsoft Entra |
| 2026-11-09 | MC1325414 | Entra SSPR will require registered authentication methods |
| 2027-02-01 | MC1426371 | Microsoft-provided SMS and voice MFA retired |

---

*Sources: [mc.merill.net](https://mc.merill.net) Microsoft 365 Message Center Archive. Admin portal links open in the Microsoft 365 Admin Center and require appropriate permissions.*

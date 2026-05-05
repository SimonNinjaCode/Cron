# Microsoft 365 Message Center Digest — Security & Compliance
## April 2026 | Run date: 2026-05-05

This digest covers **20 security and compliance items** from the Microsoft 365 Message Center for April 2026 — items whose published date or a material rollout milestone (GA, Public Preview, opt-out window, enforcement start, or retirement) falls within the month.

---

## Items Table

| Date | Title | Service | Category | Type | Summary | Link |
|------|-------|---------|----------|------|---------|------|
| 2026-04-01 | SharePoint legacy records management features retired | Microsoft Purview | Data Protection & Compliance | Retirement | Microsoft Purview is retiring SharePoint Online Information Management Policies, In-Place Records Management, and deletion-only document policies starting April 2026. Admins must manually migrate workloads to Purview DLM/Records Management (E5 required for auto-retention); Microsoft will not auto-migrate existing configurations. | [MC1211579](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1211579) |
| 2026-04-01 | DLP for Copilot prompts safeguard generally available | Microsoft Purview | Data Protection & Compliance | GA | Microsoft Purview DLP policies now block Microsoft 365 Copilot (including pre-built agents) from grounding responses in sensitive data or returning protected content; a default simulation-mode policy is created automatically, and admins enable enforcement from the Purview portal or MAC. | [MC1181998](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1181998) |
| 2026-04-01 | IRM pay-as-you-go billing for other AI app indicators | Microsoft Purview | Data Protection & Compliance | GA | Insider Risk Management introduces consumption-based billing for the "Other AI apps" indicator category under Generative AI apps; charged per user activity processed. An Azure subscription must be linked before April 1, 2026; Microsoft Copilot indicators remain license-based and unaffected. | [MC1242784](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1242784) |
| 2026-04-01 | Windows Autopatch hotpatch updates enabled by default | Microsoft Intune | Endpoint Security | Plan for Change | Starting with the May 2026 Windows security update, Windows Autopatch will automatically enable hotpatch (no-reboot) security updates for all eligible Intune-managed devices. An opt-out tenant setting became available April 1, 2026; admins who are not ready should configure Quality Update policies before the May Patch Tuesday. | [MC1248388](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1248388) |
| 2026-04-01 | Triage Agent DLP summaries surfaced in Defender XDR | Microsoft Purview | Threat Protection | Public Preview | The Purview Data Security Triage Agent now surfaces AI-generated DLP alert summaries and severity categorizations directly within the Defender XDR alert queue (public preview, completing mid-April; GA August 2026). Agent management—instructions, pause/deactivate, usage monitoring—remains in the Purview portal; no changes to existing DLP policies. | [MC1255406](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1255406) |
| 2026-04-01 | Label publishing policy sync status in Purview portal | Microsoft Purview | Data Protection & Compliance | Update | A new Policy sync status column appears on the Label publishing policies page and a summary card on the Reports landing page, giving Information Protection admins real-time visibility into how label policy changes are propagating across workloads. Enabled by default; no admin action required. | [MC1260706](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1260706) |
| 2026-04-01 | Auth Methods Policy audit logs show only changed fields | Microsoft Entra | Identity & Access | Update | Entra ID audit logs for Authentication Methods Policy Update events now list only the specific properties that changed (with old and new values) instead of the entire policy payload. Organisations with automated log parsers or SIEM rules that rely on the full payload format should update their parsing logic. | [MC1260708](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1260708) |
| 2026-04-01 | Authenticator blocks Entra credentials on jailbroken iOS | Microsoft Entra | Identity & Access | GA | Microsoft Authenticator began enforcing jailbreak/root detection on iOS in April 2026 (Android phase started February). In three phases—warn, block registration/login, then wipe existing Entra accounts—the app removes work/school credentials from compromised devices. The feature is automatic and cannot be disabled by admins or users. | [MC1179154](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1179154) |
| 2026-04-10 | New Purview DSPM experience with AI observability | Microsoft Purview | Data Protection & Compliance | Update | The unified Data Security Posture Management (DSPM) dashboard (public preview completing early April) now delivers outcome-based guided workflows, AI observability, Security Copilot agents for automated triage and policy management, and third-party signals from BigID, Cyera, OneTrust, and Varonis. GA moved to early May 2026. Classic DSPM and DSPM for AI remain accessible. | [MC1191257](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1191257) |
| 2026-04-15 | Auto-labeling can override and remove manual sensitivity labels | Microsoft Purview | Data Protection & Compliance | GA | Admins can now configure SharePoint/OneDrive auto-labeling policies to override manually applied sensitivity labels or remove a label entirely when content no longer meets policy conditions. Not enabled by default; admins should review existing auto-labeling policies and communicate to users that labels on files at rest may change automatically once configured. | [MC1249431](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1249431) |
| 2026-04-15 | Sensitivity labels with user-defined permissions in Office web | Microsoft Purview | Data Protection & Compliance | GA | Word, Excel, and PowerPoint on the web now fully support applying sensitivity labels with custom user-defined permissions (specific users or domains; Viewer/Editor/Owner rights), eliminating the need to switch to desktop apps. Requires coauthoring on encrypted files to be enabled in the tenant. | [MC1208688](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1208688) |
| 2026-04-15 | Recommended and auto sensitivity labels in Outlook mobile | Microsoft Purview | Data Protection & Compliance | GA | Outlook for iOS and Android now prompts users to apply recommended labels and silently applies automatic labels during email composition, matching the behaviour of desktop and web Outlook. On by default for tenants with existing Purview sensitivity labelling policies; no policy reconfiguration needed. | [MC1247891](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1247891) |
| 2026-04-15 | Defender XDR AI email summary via Security Copilot | Microsoft Defender XDR | Threat Protection | Public Preview | A Security Copilot–powered email summary panel appears on the Email entity page in Defender XDR, presenting natural-language threat context, timeline, URL/attachment assessments, and recommended actions. Public preview mid-April through late April; GA from early May. Requires active Security Copilot SCU entitlement; opt-in only. | [MC1268924](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1268924) |
| 2026-04-20 | Security Copilot included in Microsoft 365 E5 plans | Microsoft Defender XDR | Threat Protection | GA | Security Copilot is being auto-provisioned for all eligible M365 E5 and E7 tenants (400 SCUs per 1,000 paid users monthly, up to 10,000 SCUs). Phased rollout April 20–June 30, 2026; tenants receive a 7-day advance notice email before activation. Core Defender, Entra, Intune, and Purview agentic features are included; advanced capabilities may incur additional costs. | [MC1261596](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1261596) |
| 2026-04-25 | Edge for Business cross-tenant Intune MAM support GA | Microsoft Intune | Endpoint Security | GA | Microsoft Edge for Business now enforces Intune App Protection Policies for users authenticated with your tenant's credentials on devices managed by a different tenant, with no additional app enrollment or MDM required. GA rollout completes end of April 2026; admins configure policies in the Intune portal. | [MC1255405](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1255405) |
| 2026-04-25 | AI personal data examination in Data Security Investigations | Microsoft Purview | Data Protection & Compliance | GA | Purview Data Security Investigations gains an AI-powered personal data examination that identifies and extracts common PII (names, addresses, bank account numbers) within investigation datasets, complementing existing credential, risk, and mitigation analyses. Available by default; no admin action required; respects existing DSI permissions. | [MC1266016](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1266016) |
| 2026-04-25 | Teams call logs retention and deletion policies supported | Microsoft Purview | Data Protection & Compliance | GA | Purview DLM retention and deletion policies can now be applied to Microsoft Teams call logs (Call Detail Records stored in Exchange Online mailboxes), ending indefinite default retention. Admins should review regulatory requirements for call-log retention and create or update policies before the feature reaches their tenant. | [MC1261586](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1261586) |
| 2026-04-25 | Entra passkeys on Windows generally available | Microsoft Entra | Identity & Access | GA | Device-bound passkeys stored in the Windows Hello container enable phishing-resistant, passwordless Entra sign-in on Windows devices using face, fingerprint, or PIN. Admins no longer need to explicitly allow Windows Hello AAGUIDs in a passkey profile. Managed via Authentication Methods policies and Conditional Access; rollout completes mid-June 2026 (GCC/DoD: late July). | [MC1282568](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1282568) |
| 2026-04-25 | Cross-tenant security group synchronization GA | Microsoft Entra | Identity & Access | GA | Entra now supports synchronising security groups across tenants to centralise group management in multi-tenant environments. GA rollout begins late April, completes end of May 2026. Admins configure cross-tenant sync settings in the Entra admin center; existing inbound/outbound synchronisation policies are not changed. | [MC1198077](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1198077) |
| 2026-04-30 | Trust DigiCert Global Root G2 for Exchange Online TLS | Exchange Online | Platform Security | Action Required | Exchange Online uses TLS certificates chained to DigiCert Global Root G2. Organisations with custom certificate trust stores, on-premises SMTP gateways, or older application stacks must add and trust this root CA before **April 30, 2026** to avoid mail-flow disruption when third-party providers distrust the legacy DigiCert G1 root. No action needed for devices using Windows/macOS automatic root updates. | [MC1224565](https://admin.microsoft.com/Adminportal/Home#/MessageCenter/:/messages/MC1224565) |

---

## Action Required Items

The following items require explicit administrator action before their stated deadlines:

### 1. Trust DigiCert Global Root G2 for Exchange Online TLS — **Deadline: April 30, 2026**
**MC1224565** | Exchange Online | Platform Security

Organisations with custom certificate trust stores (on-premises SMTP relays, non-Windows mail gateways, custom PKI) must add the **DigiCert Global Root G2** certificate to their trusted root store before April 30, 2026. Failure to act may result in complete SMTP mail-flow failures with Exchange Online when DigiCert's legacy G1 root is distrusted by the broader ecosystem.

*Verify:* Check your SMTP gateway/connector certificate chain. If `DigiCert Global Root G2` appears as an intermediate or root, no action is needed. If you see only the legacy G1 root, update your trust store.

---

### 2. SharePoint Online Legacy Compliance Features Retired — **Action: Migrate now**
**MC1211579** | Microsoft Purview | Data Protection & Compliance | Retirement

SharePoint Online Information Management Policies, In-Place Records Management, and deletion-only document policies are being retired starting April 2026. Microsoft will **not** auto-migrate existing configurations. Admins must:
1. Inventory existing SharePoint IMP/Records Management policies.
2. Migrate to Microsoft Purview Data Lifecycle Management or Records Management.
3. Note licensing uplift: auto-retention requires M365/O365 E5; manual retention requires M365 Business Premium minimum.

---

### 3. IRM Pay-as-you-go Billing for AI App Indicators — **Action: Link Azure subscription before April 1, 2026**
**MC1242784** | Microsoft Purview | Data Protection & Compliance | GA

If your organisation uses Insider Risk Management "Other AI apps" indicators under Generative AI apps, an Azure subscription must be linked to your Purview tenant to continue receiving those signals from April 1, 2026. Without a linked subscription, those indicators will stop generating signals. Microsoft Copilot indicators (license-based) are unaffected.

---

### 4. Windows Autopatch Hotpatch Default Enrollment — **Opt-out by: Before May 2026 Patch Tuesday**
**MC1248388** | Microsoft Intune | Endpoint Security | Plan for Change

Starting with the May 2026 security update, hotpatch updates will be enabled **by default** for all eligible Intune-managed Windows devices. If your organisation is not ready to deploy hotpatch (e.g., devices with pending Virtualization-based Security enablement, or specific compliance testing requirements), configure opt-out via Quality Update policies in Intune. The opt-out setting became available April 1, 2026.

---

*Report generated: 2026-05-05 | Sources: Microsoft 365 Message Center via mc.merill.net*

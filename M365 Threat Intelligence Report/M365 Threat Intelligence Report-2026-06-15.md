# M365 Threat Intelligence Report — May 2026

**Run Date:** 2026-06-15  
**Target Month:** May 2026 (fallback applied where noted)  
**Analyst:** Delphi — AI Threat Intelligence Analyst  
**Audience:** Security Architects · SOC Leads · Cyber Leadership  
**Scope:** Microsoft 365 · Entra ID · Azure · Integrated SaaS

---

## Executive Summary

Five cross-source themes dominating the May 2026 Microsoft cloud threat landscape:

- **OAuth & Device Code Phishing Has Become Industrialized.** Multiple Phishing-as-a-Service platforms — Kali365 (April 2026), Tycoon2FA (rebuilt post-disruption), EvilTokens — have commoditized OAuth Device Authorization Grant abuse, enabling mass MFA bypass without ever capturing a victim's password. This is a structural shift: token theft has replaced credential theft as the primary Microsoft 365 attack mechanism.

- **AiTM Phishing at Unprecedented Scale.** The April 14–16 "code of conduct" campaign — 35,000+ users, 13,000+ organizations, 26 countries — established AiTM phishing as an industrialized, multi-wave capability. Healthcare, financial services, professional services, and technology sectors absorbed the majority of impact; 92% of targets were US-based.

- **Entra ID Is the Single Most Targeted Asset.** From SSPR abuse to session cookie theft (Cookie Bite) to OAuth token hijacking, every major attack chain in May 2026 passed through Entra ID. Standard MFA is now consistently defeated across all these vectors. Organizations relying on push-notification or TOTP MFA for cloud access are insufficiently protected.

- **Identity Compromise Escalates to Full Azure Tenant Breach.** Storm-2949's May 2026 case study demonstrated a systematic pivot: SSPR abuse → Entra ID control → Microsoft Graph API enumeration → Azure App Service, Key Vault, SQL, Storage, and VM compromise — with active Defender tampering and log clearing throughout. A single identity breach is now sufficient for complete cloud infrastructure takeover.

- **AI Brand Impersonation Is an Expanding and Persistent Attack Surface.** Storm-3075 and Fox Tempest are exploiting public enthusiasm for ChatGPT, Microsoft Copilot, Anthropic Claude, and DeepSeek as phishing lures, with AiTM-based credential harvest and infostealer delivery. This vector will remain persistent as AI adoption grows and shadow-AI risk expands the organizational attack surface.

---

## Source 1: [The Hacker News](https://thehackernews.com/)

### Insight 1 — AiTM "Code of Conduct" Phishing Campaign Hits 35,000+ M365 Users

| Field | Detail |
|-------|--------|
| **Title** | [Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries](https://thehackernews.com/2026/05/microsoft-details-phishing-campaign.html) — May 2026 |
| **Introduction** | Between April 14–16, 2026, a multi-stage adversary-in-the-middle (AiTM) phishing campaign impersonating internal compliance communications — "code of conduct" HR violations — targeted 35,000+ users across 13,000+ organizations in 26 countries. Attackers used PDF-delivered links, Cloudflare CAPTCHA gating to block automated analysis, and a real-time AiTM proxy to capture Microsoft 365 session tokens at the point of authentication. MFA was defeated entirely; victims' passwords were never exposed to the attacker. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Unattributed cybercriminal group (multiple coordinated waves, organized infrastructure). **TTPs:** T1566.001 Spearphishing Attachment (PDF lures); T1557 AiTM Proxy; T1539 Steal Web Session Cookie; T1078.004 Valid Cloud Accounts; display name spoofing ("Internal Regulatory COC", "Workforce Communications"); CAPTCHA evasion; attacker-controlled .de TLD domains; cloud-hosted VM for bulk email delivery. **Targets:** Healthcare & Life Sciences (19%), Financial Services (18%), Professional Services (11%), Technology (11%). **Region:** United States (92%), 25 additional countries across Europe, APAC, and LATAM. |
| **Affected Cybersecurity Domain** | Phishing / Identity & Access / Email Security / BEC |
| **Risk** | Session token compromise enabling persistent M365 access without re-authentication; BEC fraud via hijacked executive and finance mailboxes; lateral movement via Microsoft Graph API enumeration; data exfiltration from OneDrive and SharePoint; MFA rendered ineffective against AiTM relay. |
| **Strategic Initiative** | MCRA: Identity Plane, Email Security. Zero Trust: *Verify Explicitly* (phishing-resistant MFA), *Assume Breach* (automatic attack disruption, ZAP, anomaly detection). Defender XDR: Entra ID Protection (AnomalousToken, ImpossibleTravel risk detections), Defender for Office 365 (Safe Links real-time detonation, Safe Attachments), Defender XDR automatic attack disruption. |
| **Call to Action** | 1. **Enforce phishing-resistant MFA (FIDO2/passkeys, Windows Hello)** for all users — TOTP and push-notification MFA are bypassed by AiTM. 2. **Enable Continuous Access Evaluation (CAE)** to revoke tokens immediately on risk signals or sign-out. 3. **Deploy Defender for Office 365 Safe Links** with real-time URL detonation for PDF-embedded links, and enable Zero-hour Auto Purge (ZAP). 4. **Configure Entra ID Protection** risk-based Conditional Access: block or require step-up on High-risk sign-in (AnomalousToken, ImpossibleTravel). 5. **Threat hunt:** Query sign-in logs for authentications from `.de` domains not on organizational allowlist; look for AnomalousToken risk detections followed by O365 activity within 5 minutes. 6. **Enable automatic attack disruption** in Defender XDR to autonomously contain compromised accounts. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

---

### Insight 2 — Device Code Phishing Hits 340+ M365 Organizations via OAuth Abuse *(Fallback — March 2026)*

| Field | Detail |
|-------|--------|
| **Title** | [Device Code Phishing Hits 340+ Microsoft 365 Orgs Across Five Countries via OAuth Abuse](https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html) — March 2026 *(Fallback — 2 months prior to target month; ongoing relevance confirmed by May 2026 PhaaS campaigns building on this vector)* |
| **Introduction** | Active since February 19, 2026, a threat actor (tracked as Storm-237, assessed with possible Russian state nexus) has used OAuth 2.0 Device Authorization Grant flow abuse to compromise 340+ Microsoft 365 organizations in the US, Canada, Australia, New Zealand, and Germany. Attackers trick users — via Teams messages or email — into entering legitimate device codes at Microsoft's authentication portal, bypassing MFA entirely and obtaining persistent access and refresh tokens. No further victim interaction is required. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Storm-237 (possible Russian state nexus, assessed by Microsoft). **TTPs:** T1528 Steal Application Access Token; T1078.004 Valid Cloud Accounts; OAuth Device Code Grant flow abuse (RFC 8628); social engineering via Teams messages and email; token persistence without credential re-use; post-compromise email exfiltration. **Targets:** Construction, non-profits, real estate, manufacturing, financial services, healthcare, legal, government. **Region:** USA, Canada, Australia, New Zealand, Germany. |
| **Affected Cybersecurity Domain** | Identity & Access / Cloud Security / Email Security |
| **Risk** | Persistent OAuth tokens granting access to Outlook, Teams, OneDrive without re-authentication (30–90 day token lifespan); no indicator of compromise in traditional credential logs; BEC potential via mailbox access; espionage and intellectual property exfiltration. |
| **Strategic Initiative** | MCRA: Identity Plane, Cloud Security. Zero Trust: *Verify Explicitly* (Conditional Access blocking device code flow). SSPM: Restrict OAuth app consent and delegated permissions. Defender for Cloud Apps: OAuth app governance policy. |
| **Call to Action** | 1. **Block device code authentication flow via Conditional Access** — deny the `deviceCode` grant type for all users unless explicitly required for specific managed-device workflows. 2. **Alert on OAuth token generation from unrecognized device IDs** or countries of operation. 3. **Implement CAE** to continuously validate token validity against current risk posture. 4. **Threat hunt:** Filter Entra sign-in logs for `AuthenticationProtocol = DeviceCode` combined with geolocation anomalies or first-seen device IDs. 5. **Review and revoke legacy OAuth app registrations** with broad M365 delegated permissions (Mail.Read, Files.ReadWrite.All). 6. **Educate users** via attack simulation: they will never legitimately be asked to copy a code from a website and paste it into an authentication flow initiated by a third party. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

---

## Source 2: [Ars Technica — Security](https://arstechnica.com/security/)

> **⚠️ Source Access Limitation:** Ars Technica's domain (`arstechnica.com`) is not accessible to the web crawling and search tools used in this environment — the domain is blocked from external agent access and returned no URLs in any search query. The two insights below are drawn from the FBI/IC3 primary advisory and the Microsoft Security Blog on topics that align directly with Ars Technica's security coverage focus. The Source field links to Ars Technica's security section as the intended source; specific article URLs from that publication could not be confirmed. All intelligence is verified from primary or first-tier secondary sources.

---

### Insight 1 — FBI Warning: Kali365 PhaaS Enables Mass M365 OAuth Token Theft Without Credentials

| Field | Detail |
|-------|--------|
| **Title** | [Kali365 Phishing-as-a-Service Kit Hijacks Microsoft 365 Access Tokens](https://www.ic3.gov/PSA/2026/PSA260521) — FBI/IC3, May 21, 2026 *(Ars Technica not accessible; FBI/IC3 PSA used as primary source for the same story)* |
| **Introduction** | The FBI issued a Public Service Announcement on May 21, 2026 warning about Kali365, a PhaaS platform first observed in April 2026 and distributed via Telegram. Kali365 abuses Microsoft's OAuth 2.0 Device Authorization Grant flow to deliver persistent M365 access tokens — covering Outlook, Teams, and OneDrive — to the attacker without ever capturing the victim's password or MFA code. The platform democratizes sophisticated token theft with AI-generated lures, automated campaign templates, and real-time dashboards, putting M365 account takeover within reach of low-skilled threat actors. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Multiple financially motivated cybercriminals using the Kali365 platform (Telegram-distributed; platform operator not publicly attributed). **TTPs:** T1528 Steal Application Access Token; OAuth Device Code Authorization flow abuse; AI-generated spearphishing (T1566); automated token capture dashboards; persistent refresh token retention without credential re-use; real-time individual tracking of targeted entities. **Targets:** Manufacturing, education, government, financial services, healthcare. **Region:** North America and Europe (hundreds of confirmed attacks). |
| **Affected Cybersecurity Domain** | Phishing / Identity & Access / SaaS / BEC |
| **Risk** | Persistent M365 access with refresh token lifetimes of 30–90 days; BEC from compromised executive and finance mailboxes; internal phishing escalation via Teams and Outlook; mass-scale threat due to PhaaS commoditization; standard MFA rendered fully ineffective. |
| **Strategic Initiative** | MCRA: Identity Plane, Email Security. Zero Trust: *Verify Explicitly* (phishing-resistant MFA, device compliance), *Least Privilege* (OAuth scope restriction). Defender for Cloud Apps: OAuth app governance and anomalous consent detection. Entra ID Protection: anomalous token and new device registration alerts. |
| **Call to Action** | 1. **Disable device code authentication flow via Conditional Access** for all users unless specifically required for managed device scenarios. 2. **Enable Entra ID Protection risk-based policies** to block or remediate High-risk sign-in sessions automatically. 3. **Alert on** `deviceCode` grant type in Entra sign-in logs from unmanaged or unrecognized device IDs. 4. **Revoke all refresh tokens** for accounts exhibiting anomalous sign-in patterns using `Revoke-MgUserSignInSession`. 5. **Deploy Microsoft Defender for Cloud Apps** to detect anomalous OAuth app permissions and unauthorized new app consent grants. 6. **User education:** Employees will never be asked to enter a Microsoft-generated code on an external website to verify their identity. |
| **Source** | [Ars Technica — Security](https://arstechnica.com/security/) *(site inaccessible; IC3 PSA used as primary source)* |

---

### Insight 2 — AI Brand Impersonation Drives AiTM Credential Harvest Across 2,000+ Organizations

| Field | Detail |
|-------|--------|
| **Title** | [AI brands as bait: How threat actors are using the AI hype in social engineering](https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/) — Microsoft Security Blog, June 8, 2026 *(Ars Technica not accessible; Microsoft TI blog used; June 2026 — 1 month after target period, labeled as cross-period reference)* |
| **Introduction** | Storm-3075 and Fox Tempest are exploiting mass enthusiasm for AI platforms — ChatGPT, Anthropic Claude, Microsoft Copilot, DeepSeek V4 — as social engineering lures, deploying AiTM-based credential harvest campaigns impacting 2,000+ organizations. Attack chains include phishing emails with multi-stage legitimate redirectors (Bitrix24 CRM, Amazon awstrack.me), CAPTCHA gating to defeat sandbox analysis, and malvertising on free streaming sites. Some campaigns deliver Vidar infostealer; others harvest Azure/M365 authentication tokens via AiTM. |
| **Status** | **Stay Informed** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Storm-3075 (initial access broker / malware distributor); Fox Tempest (malware-signing-as-a-service operator). **TTPs:** AI brand impersonation (ChatGPT, Claude, DeepSeek, Copilot); T1566.002 Spearphishing Link; T1557 AiTM credential/token harvest; T1176 malicious GitHub repositories with SEO manipulation; T1036 Masquerading (stolen branding, fake plugin pages); multi-stage legitimate service redirectors (Bitrix24, awstrack.me, Rebrandly); CAPTCHA evasion; Vidar infostealer delivery (Trojan:Win32/Vidar). **Targets:** Broad consumer and enterprise (2,000+ organizations). **Region:** USA (62%), UK (18%), India (9%), South Africa, Japan, France; campaign volumes of 4,500–100,000 phishing emails per day. |
| **Affected Cybersecurity Domain** | Phishing / Identity & Access / Malware / Endpoint |
| **Risk** | Azure/M365 session token theft; infostealer-based credential and cookie exfiltration from endpoints; persistent cloud account compromise; shadow-IT and bring-your-own-AI expanding the M365-adjacent phishing surface; malicious extensions enabling ongoing session monitoring. |
| **Strategic Initiative** | MCRA: Identity Plane, Email Security, Endpoint. Zero Trust: *Verify Explicitly*, *Assume Breach*. Defender XDR: Entra ID Protection (AnomalousToken), Defender for Endpoint (Vidar/infostealer detection, SmartScreen URL blocking), Defender for Office 365 (AI-lure domain blocking). |
| **Call to Action** | 1. **Block AI platform impersonation domains** via Defender SmartScreen URL blocking and add known C2 indicators (brokeapt[.]com, pan.ssffaa19[.]xyz, pan.rongtv[.]xyz) to Sentinel watchlists. 2. **Restrict browser extensions via Intune/Endpoint Manager** — allow only policy-approved extensions to prevent malicious extension-based token and cookie theft. 3. **Train users on AI brand impersonation** as a distinct phishing vector — AI platforms will never request credentials via third-party links. 4. **Enable Defender for Endpoint** to detect Vidar infostealer behavior (credential store scraping, browser data exfiltration). 5. **Audit GitHub for AI-branded repositories** in your supply chain — attackers exploit stars and forks to build perceived legitimacy quickly (91 stars, 27 forks within 4 days in one documented case). |
| **Source** | [Ars Technica — Security](https://arstechnica.com/security/) *(site inaccessible; Microsoft TI blog used as primary source)* |

---

## Source 3: [Dark Reading](https://www.darkreading.com/)

### Insight 1 — 'Cookie Bite' Attack Bypasses M365 MFA via Browser-Stolen Entra ID Session Cookies *(Fallback — April 2025)*

| Field | Detail |
|-------|--------|
| **Title** | ['Cookie Bite' Entra ID Attack Exposes Microsoft 365](https://www.darkreading.com/remote-workforce/cookie-bite-entra-id-attack-exposes-microsoft-365) — Dark Reading, April 2025 *(Fallback — approximately 13 months prior to target month; no May 2026 Dark Reading article directly accessible. Continued relevance confirmed by active reporting and community discussion through June 2026.)* |
| **Introduction** | Varonis Threat Labs disclosed "Cookie Bite," a proof-of-concept attack exploiting ESTSAUTH and ESTSAUTHPERSISTENT — the two primary Azure Entra ID session cookies — through a malicious Chrome browser extension. By stealing these cookies, attackers can replay active M365 sessions across Outlook, Teams, and SharePoint, bypassing MFA entirely because the cookies already encode a completed authentication event. The attack requires no system-level compromise, operates entirely within the browser, and produces no anomalous sign-in event visible in standard Entra ID logs. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Unattributed (PoC demonstrated by Varonis Threat Labs; technique now considered an active adversarial capability). **TTPs:** T1539 Steal Web Session Cookie; T1176 Browser Extension (malicious Chrome extension deployment); T1550.004 Web Session Cookie reuse; ESTSAUTH (transient session token) and ESTSAUTHPERSISTENT (long-lived persistent token) exfiltration; MFA bypass via authenticated cookie replay; no anomalous sign-in event generated. **Targets:** Any organization using Microsoft 365 and Azure Entra ID with standard browser-based authentication. **Region:** Global. |
| **Affected Cybersecurity Domain** | Identity & Access / SaaS / Browser Security |
| **Risk** | Complete M365 session hijacking without triggering re-authentication or sign-in anomaly alerts; persistent access across Outlook, Teams, SharePoint for the lifetime of ESTSAUTHPERSISTENT cookie; BEC via hijacked executive sessions; invisible to most SOC monitoring that focuses on Entra sign-in events; renders MFA controls completely moot for an already-authenticated session. |
| **Strategic Initiative** | MCRA: Identity Plane, Endpoint. Zero Trust: *Verify Explicitly* (CAE, device compliance for all M365 access), *Device Health* (managed-only browser policies). Defender XDR: Defender for Endpoint (browser extension behavioral detection), Entra ID session token policies. |
| **Call to Action** | 1. **Enable Continuous Access Evaluation (CAE)** — forces token re-validation on network change, location change, or risk signal, limiting the utility of stolen session cookies. 2. **Enforce Entra ID Conditional Access requiring compliant Intune-managed device** for all M365 access, blocking sessions from unmanaged endpoints where malicious extensions could operate. 3. **Restrict browser extensions via Intune/Endpoint Manager** — allowlist only policy-approved extensions; block all Chrome extension installations from outside the managed extension list. 4. **Configure sign-in frequency and persistent browser session policies** in Entra ID to minimize the lifespan of ESTSAUTHPERSISTENT cookies (recommend ≤1 hour for privileged roles). 5. **Threat hunt:** Look for M365 activity from the same session token arriving from multiple source IPs within a short window; look for ESTSAUTHPERSISTENT cookie re-use from IPs inconsistent with the user's device fleet. 6. **Deploy Defender for Endpoint** browser protection with behavioral analysis to detect extension-based cookie exfiltration patterns. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

---

### Insight 2 — Russian Nation-State Actors Weaponize Microsoft Office Zero-Day Within 3 Days of Disclosure

| Field | Detail |
|-------|--------|
| **Title** | [Russian Hackers Weaponize Microsoft Office Bug in Just 3 Days](https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-weaponize-office-bug-within-days) — Dark Reading, 2026 *(Exact publication date not confirmed; article returned in May/June 2026 search context)* |
| **Introduction** | Russian state-aligned threat actors weaponized a Microsoft Office vulnerability within three days of public disclosure, demonstrating a near-zero-day exploitation capability targeting the Office suite — the foundational productivity layer of every Microsoft 365 deployment. Office-delivered initial access consistently transitions to Entra ID credential theft and M365 cloud compromise, making rapid Office patch lag a direct identity security risk. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Russian state-nexus threat actors (specific group not confirmed in available summary). **TTPs:** T1203 Exploitation for Client Execution (Office zero-day); T1566.001 Spearphishing Attachment (Office document delivery); rapid exploitation timeline (3 days from disclosure to weaponization); potential pivot from endpoint to M365/Entra ID credential theft. **Targets:** Organizations across sectors using Microsoft Office/M365; typical Russian APT focus on government, defense, energy, and critical infrastructure. **Region:** Eastern Europe emphasis; global spillover expected. |
| **Affected Cybersecurity Domain** | Endpoint / Vulnerability Management / Phishing / Identity & Access |
| **Risk** | Office-delivered malware enabling credential theft → M365/Entra ID session compromise; ransomware deployment as secondary payload; espionage via M365 mailbox and SharePoint/OneDrive data access; near-zero-day exploitation window makes standard patch cycles insufficient. |
| **Strategic Initiative** | MCRA: Endpoint, Identity, Vulnerability Management. Zero Trust: *Assume Breach* (Attack Surface Reduction rules, endpoint detection). Defender XDR: Defender for Endpoint (ASR rules, Office Protected View enforcement, macro blocking), Sentinel (Office exploitation hunting rules). |
| **Call to Action** | 1. **Establish a <24-hour emergency patch SLA for Critical Microsoft Office CVEs** — 3-day weaponization leaves no room for standard patch windows. 2. **Enable Attack Surface Reduction (ASR) rules:** block Office from creating child processes; block Office from injecting code into other processes; block Office from creating executable content. 3. **Configure Office Protected View and Application Guard** (Microsoft Defender Application Guard for Office) to sandbox document execution for files from external sources. 4. **Block macros in all documents not from trusted managed locations** via Intune/Group Policy — enforce for all users without exception. 5. **Alert on:** Office process spawning unusual child processes (cmd.exe, powershell.exe, wscript.exe); outbound network connections from Office applications to non-Microsoft endpoints. 6. Prioritize these patches in Defender Vulnerability Management (TVM) prioritization dashboard. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

---

## Source 4: [BleepingComputer](https://www.bleepingcomputer.com/)

### Insight 1 — FBI Warns Kali365 PhaaS Platform Industrializes Microsoft 365 Token Theft

| Field | Detail |
|-------|--------|
| **Title** | [FBI warns of Kali365 phishing service targeting Microsoft 365 accounts](https://www.bleepingcomputer.com/news/security/fbi-warns-of-kali365-phishing-service-targeting-microsoft-365-accounts/) — BleepingComputer, May 2026 *(URL confirmed via search index; direct site fetch returned HTTP 403)* |
| **Introduction** | BleepingComputer reported on the FBI's May 21, 2026 warning about Kali365, a phishing-as-a-service platform first observed in April 2026 and marketed through Telegram. Kali365 abuses Microsoft's OAuth Device Authorization Grant flow — a legitimate mechanism for authenticating devices without displays — to steal M365 access tokens and gain persistent access to Outlook, Teams, and OneDrive without ever needing the victim's password or MFA code. The platform includes AI-generated lures, automated campaign templates, real-time tracking dashboards, and OAuth token capture, making sophisticated M365 account takeover accessible to low-skilled actors at scale. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Multiple financially motivated actors (Telegram channel subscribers); platform operator unattributed. **TTPs:** T1528 Steal Application Access Token; OAuth 2.0 Device Authorization Grant flow abuse; AI-generated spearphishing (T1566); real-time OAuth token capture and dashboard monitoring; persistent refresh token retention (30–90 day lifetimes); post-compromise access to Outlook, Teams, OneDrive. **Targets:** Manufacturing, education, government, financial services, healthcare. **Region:** North America and Europe (hundreds of attacks documented within weeks of platform launch). |
| **Affected Cybersecurity Domain** | Phishing / Identity & Access / SaaS / BEC |
| **Risk** | Persistent M365 tenant access for weeks without re-authentication; BEC fraud from executive and finance mailboxes; internal escalation via Teams phishing using compromised accounts; mass-scale risk due to PhaaS accessibility; standard MFA entirely ineffective; low cost of entry for threat actors. |
| **Strategic Initiative** | MCRA: Identity Plane, Email Security. Zero Trust: *Verify Explicitly* (phishing-resistant MFA, Conditional Access device compliance), *Least Privilege* (OAuth scope restriction). Defender for Cloud Apps: OAuth governance. Entra ID Protection: anomalous token and device registration alerts. |
| **Call to Action** | 1. **Create a Conditional Access policy to block device code flow** (`urn:ietf:params:oauth:grant-type:device_code`) for all users not explicitly requiring it for managed-device use cases. 2. **Enable CAE** to shorten the effective window for stolen tokens by forcing re-evaluation on risk signals. 3. **Configure Entra ID Protection** with automated High-risk user remediation (require password reset + MFA re-registration). 4. **Revoke all refresh tokens** for accounts showing anomalous OAuth grant activity (`Invoke-MgInvalidateAllRefreshTokens`). 5. **Deploy Defender for Cloud Apps** OAuth app governance to alert on new delegated permissions granted to unrecognized applications. 6. **Threat hunt:** Query Entra sign-in logs for `ClientAppUsed = DeviceCode` from unmanaged devices, new countries, or device IDs not previously seen for the user. |
| **Source** | [BleepingComputer](https://www.bleepingcomputer.com/) |

---

### Insight 2 — Storm-2949 Abuses Entra ID SSPR to Launch Azure-Wide Data Theft Campaign

| Field | Detail |
|-------|--------|
| **Title** | [Microsoft Self-Service Password Reset abused in Azure data theft attacks](https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/) — BleepingComputer, May 2026 *(URL confirmed via search index; direct site fetch returned HTTP 403)* |
| **Introduction** | BleepingComputer reported on Storm-2949's exploitation of Microsoft Entra ID's Self-Service Password Reset (SSPR) feature as the initial access vector for a cloud-wide breach campaign. The attacker social-engineered employees — posing as IT support — to approve fraudulent MFA prompts during a fake password reset, then immediately enrolled their own Microsoft Authenticator device, gaining persistent control of the identity. Storm-2949 subsequently used Microsoft Graph API and custom Python scripts to enumerate the entire Azure tenant before pivoting through App Services, Key Vaults, SQL Databases, Storage accounts, and Virtual Machines. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Storm-2949 (emerging, sophisticated cloud threat actor; financially motivated). **TTPs:** T1078.004 Valid Cloud Accounts (SSPR abuse); T1621 MFA Request Generation (fraudulent MFA fatigue); T1098.005 Device Registration (attacker authenticator enrollment); T1526 Cloud Service Discovery (Microsoft Graph API); T1580 Cloud Infrastructure Discovery (Azure RBAC enumeration); T1619 Cloud Storage Object Discovery; T1567 Exfiltration to Cloud Service (OneDrive/SharePoint); T1059 Command and Scripting (custom Python scripts); Azure VM Run Command and VMAccess extension abuse; T1219 Remote Access Tools (ScreenConnect); T1562.001 Impair Defenses (Defender tampering); T1070.001 Clear Windows Event Logs. **Targets:** IT personnel and senior leadership specifically social-engineered. **Region:** Not specified. |
| **Affected Cybersecurity Domain** | Identity & Access / Cloud Security / BEC |
| **Risk** | Full Azure tenant compromise from a single identity breach; complete M365 data exfiltration (OneDrive, SharePoint); Azure Key Vault secret exposure enabling service-to-service lateral movement; VM credential harvesting enabling on-premises pivot; persistent remote access via ScreenConnect; active defense evasion (Defender tampering, log clearing) making forensic reconstruction extremely difficult. |
| **Strategic Initiative** | MCRA: Identity Plane, Cloud Security, Privileged Access. Zero Trust: *Verify Explicitly* (SSPR authentication controls, phishing-resistant MFA), *Least Privilege* (Azure RBAC hardening), *Assume Breach* (Defender for Cloud, Sentinel immutable logging). CSPM: VM extension policies, Key Vault access auditing. |
| **Call to Action** | 1. **Require phishing-resistant MFA and out-of-band manager/security verification** for all SSPR events — especially for IT staff and senior leadership. 2. **Alert on SSPR events for privileged roles** — these should be treated as high-severity events requiring immediate SOC review. 3. **Enforce Entra PIM (Privileged Identity Management)** for all Azure RBAC Owner/Contributor/User Access Administrator assignments — require justification and time-bound activation. 4. **Alert on:** Azure VM Run Command executions; VMAccess extension deployments; new Key Vault access policy assignments; ScreenConnect installation events on Azure VMs. 5. **Route Azure Monitor audit logs to Sentinel with immutable storage** — Storm-2949 actively clears local Windows Event Logs, making cloud-side logging the only reliable forensic source. 6. **Hunt for:** Microsoft Graph API enumeration sessions (high-volume `GET /users`, `GET /groups`, `GET /servicePrincipals`) from user-context access tokens; Python user-agent strings authenticating to Azure management plane. |
| **Source** | [BleepingComputer](https://www.bleepingcomputer.com/) |

---

## Source 5: [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/)

### Insight 1 — Storm-2949: From Compromised Identity to Cloud-Wide Azure Breach

| Field | Detail |
|-------|--------|
| **Title** | [How Storm-2949 turned a compromised identity into a cloud-wide breach](https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/) — Microsoft Security Blog, May 18, 2026 |
| **Introduction** | Microsoft Threat Intelligence published a detailed case study of Storm-2949, an emerging threat actor that chained SSPR abuse and fraudulent MFA authenticator enrollment to achieve persistent Entra ID access, then systematically pivoted through the entire Azure tenant over multiple phases — exfiltrating M365 content (OneDrive/SharePoint), stealing secrets from Azure Key Vault, modifying firewall rules on SQL and App Services, harvesting credentials from Virtual Machines via Azure extensions, and installing ScreenConnect for persistent remote access — all while actively tampering with Microsoft Defender and clearing event logs to evade detection. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Storm-2949 (sophisticated, multi-phase cloud attacker; financially motivated). **TTPs:** SSPR abuse (T1078.004); MFA fatigue / fraudulent prompt (T1621); attacker authenticator enrollment (T1098.005); Microsoft Graph API directory enumeration (T1526); Azure RBAC privilege escalation (T1580); Azure VM Run Command and VMAccess extension for credential harvesting (T1059); ScreenConnect RMM deployment (T1219); Defender tampering (T1562.001); Windows Event Log clearing (T1070.001); OneDrive/SharePoint data exfiltration (T1567); Key Vault secret exfiltration; SQL Server and Storage account compromise via firewall rule manipulation. **Targets:** IT administrators and senior leadership (social engineering targets); broad Azure tenant assets. **Region:** Not specified in published report. |
| **Affected Cybersecurity Domain** | Identity & Access / Cloud Security / Endpoint |
| **Risk** | Full Azure tenant takeover from a single compromised identity; complete M365 data exfiltration; Key Vault exposure enabling cascading service compromise (database credentials, API keys, certificates); VM compromise as stepping stone to on-premises network; active anti-forensic measures significantly hindering incident response; potential ransomware pre-positioning. |
| **Strategic Initiative** | MCRA: Identity Plane, Cloud Security, Privileged Access. Zero Trust: *Verify Explicitly* (phishing-resistant MFA, SSPR controls), *Least Privilege* (Azure RBAC, Entra PIM), *Assume Breach* (Defender for Cloud, Sentinel with immutable logging). CSPM: VM extension policies, network security group baselines, Key Vault access auditing, firewall rule change alerting. |
| **Call to Action** | 1. **Immediately audit SSPR configuration** — require phishing-resistant MFA and additional out-of-band verification (manager approval, security team confirmation) for all password resets targeting IT and executive roles. 2. **Deploy Entra PIM for all Azure privileged roles** — enforce time-bound activation with justification; alert on any direct Owner/Contributor assignments bypassing PIM. 3. **Configure Azure Policy to restrict VM extension deployments** — block Run Command and VMAccess on production VMs unless from approved change management automation. 4. **Enable Azure Key Vault soft delete with purge protection** and configure alerts for any new access policy additions or certificate/secret exports. 5. **Stream all Azure Monitor and Entra audit logs to Sentinel with immutable storage** (Storage Account with WORM policy) — Storm-2949 clears local logs, making this the only reliable forensic source. 6. **Hunt for:** Graph API enumeration patterns (`GET /users?$top=999`, `GET /servicePrincipals`) from user-context tokens; Python user agents on Azure management plane APIs; ScreenConnect process installation on cloud-hosted VMs. 7. **Enable Security Copilot** for accelerated incident triage given the complexity of multi-resource pivoting in cases like this. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

---

### Insight 2 — Multi-Stage AiTM 'Code of Conduct' Campaign Steals M365 Session Tokens at Industrial Scale

| Field | Detail |
|-------|--------|
| **Title** | [Breaking the code: Multi-stage 'code of conduct' phishing campaign leads to AiTM token compromise](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/) — Microsoft Security Blog, May 4, 2026 |
| **Introduction** | Microsoft Defender Security Research published a comprehensive technical analysis of the April 14–16, 2026 large-scale AiTM phishing campaign that hit 35,000+ users across 13,000+ organizations in 26 countries. The attack weaponized fake internal HR compliance emails ("code of conduct" violation notices), PDF-delivered malicious links, Cloudflare CAPTCHA gating to block automated sandbox analysis, and a real-time AiTM proxy to capture Microsoft 365 session tokens and MFA responses at the point of authentication — yielding fully authenticated cloud sessions without the attacker ever seeing the victim's password. Campaign infrastructure was hosted on attacker-controlled .de TLD domains and a cloud-hosted Windows VM for bulk email delivery. |
| **Status** | **Assess** |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Unattributed; coordinated multi-wave infrastructure suggests organized criminal operation. **TTPs:** T1566.001 Spearphishing Attachment (PDF); T1557 AiTM Proxy; T1539 Steal Web Session Cookie; T1078.004 Valid Cloud Accounts; display name spoofing ("Internal Regulatory COC", "Workforce Communications"); CAPTCHA evasion (Cloudflare); attacker-controlled .de domain infrastructure (compliance-protectionoutlook[.]de, acceptable-use-policy-calendly[.]de); cloud VM for bulk email delivery; multiple coordinated waves (06:51–03:54 UTC across 3 days). **Targets:** Healthcare & Life Sciences (19%), Financial Services (18%), Professional Services (11%), Technology & Software (11%). **Region:** United States (92%), 25 additional countries across Europe, APAC, and LATAM. |
| **Affected Cybersecurity Domain** | Phishing / Identity & Access / Email Security / BEC |
| **Risk** | Authenticated M365 session takeover bypassing MFA; BEC from compromised executive and finance mailboxes; Microsoft Graph API-based lateral movement and directory enumeration; data exfiltration from M365 collaboration services; complete authentication evasion — attack looks like normal user sign-in traffic to standard monitoring. |
| **Strategic Initiative** | MCRA: Identity Plane, Email Security. Zero Trust: *Verify Explicitly* (FIDO2/passkey MFA), *Assume Breach* (automatic attack disruption, continuous token re-validation). Defender XDR: Entra ID Protection (AnomalousToken, ImpossibleTravel, UnfamiliarSignInProperties risk detections), Defender for Office 365 (Safe Links real-time detonation for PDF-embedded URLs, Safe Attachments, ZAP), Defender XDR automatic attack disruption. Security Copilot: phishing triage automation. |
| **Call to Action** | 1. **Upgrade all MFA to phishing-resistant methods (FIDO2 security keys, passkeys, Windows Hello for Business)** — TOTP and push-notification MFA are fully defeated by AiTM. This is the single most impactful control for this class of attack. 2. **Enforce Conditional Access** requiring phishing-resistant MFA for all cloud applications; set sign-in risk policy to block or require step-up at High risk (AnomalousToken, ImpossibleTravel). 3. **Enable ZAP in Defender for Office 365** to retroactively remove phishing emails already delivered to inboxes. 4. **Configure Safe Links with real-time URL detonation** — PDF-embedded links are the primary delivery mechanism and must be scanned at click time, not just at delivery. 5. **Enable Entra ID Protection** with automatic remediation for AnomalousToken risk detections (auto-revoke session, require fresh phishing-resistant MFA sign-in). 6. **Threat hunt:** Query Entra sign-in logs for `RiskEventType = AnomalousToken` followed by M365 activity within 5 minutes; look for sign-ins from `.de` domains not on the organizational partner allowlist; correlate with ZAP actions in Defender for Office 365 to identify post-delivery impact. 7. **Enable automatic attack disruption in Defender XDR** — this feature autonomously contains compromised accounts by blocking lateral movement within the M365 environment before human analyst intervention. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

---

## Appendix: Source Access Notes

| Source | Access Status | Notes |
|--------|---------------|-------|
| The Hacker News | ⚠️ HTTP 403 | URLs confirmed via web search index; content synthesized from search result summaries and Microsoft primary sources covering the same stories |
| Ars Technica | ❌ Blocked | Domain not accessible to web crawling tools; not returned in any search query. Content drawn from IC3 PSA and Microsoft TI blog on equivalent topics. |
| Dark Reading | ⚠️ HTTP 403 | URLs confirmed via web search index; content synthesized from search result summaries and Varonis/secondary sources |
| BleepingComputer | ⚠️ HTTP 403 | URLs confirmed via web search index; content synthesized from search result summaries, FBI PSA, and Microsoft primary sources |
| Microsoft Threat Intelligence | ✅ Fully accessible | All four blog posts fetched successfully; full content used |

---

## IoC Quick Reference

| Indicator | Type | Campaign / Actor |
|-----------|------|-----------------|
| `compliance-protectionoutlook[.]de` | Domain | AiTM Code of Conduct campaign |
| `acceptable-use-policy-calendly[.]de` | Domain | AiTM Code of Conduct campaign |
| `brokeapt[.]com` | C2 Domain | Storm-3075 / AI brand impersonation |
| `pan.ssffaa19[.]xyz` | C2 Domain | Storm-3075 / AI brand impersonation |
| `pan.rongtv[.]xyz` | C2 Domain | Storm-3075 / AI brand impersonation |
| `DeviceCode` OAuth grant type from unmanaged devices | Behavioral | Kali365, Storm-237, Storm-2949, EvilTokens |
| SSPR events for IT/executive accounts | Behavioral | Storm-2949 |
| Graph API enumeration (`GET /users?$top=999`) from user-context tokens | Behavioral | Storm-2949 |
| Python user-agent on Azure management plane APIs | Behavioral | Storm-2949 |
| ScreenConnect installation on Azure VMs | Behavioral | Storm-2949 |
| `ESTSAUTHPERSISTENT` cookie replayed from multiple source IPs | Behavioral | Cookie Bite |
| `Trojan:Win32/Vidar` | Malware hash | Storm-3075 / AI brand impersonation |

---

*Report generated by Delphi — AI Threat Intelligence Analyst*  
*Run: 2026-06-15 08:00 CEST | Target Month: May 2026*

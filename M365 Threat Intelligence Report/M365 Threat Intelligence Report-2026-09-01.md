# M365 Threat Intelligence Report — August 2026

**Report Date:** 2026-09-01  
**Target Period:** August 2026  
**Analyst:** Delphi — Automated Threat Intelligence Collection  
**Audience:** Security Architects · SOC Leads · Cyber Leadership

---

## Executive Summary

- **PhaaS ecosystem maturation against M365 at crisis scale**: Kali365, Mirage2FA, and the Payroll Pirates cluster (Storm-2755) represent a mature, commercially available Phishing-as-a-Service ecosystem that systematically bypasses MFA through AiTM session hijacking and OAuth Device Code abuse, collectively affecting thousands of US and EU organizations throughout August 2026. These are no longer isolated campaigns — they are industrialized crime platforms available on Telegram.

- **Maximum-severity Entra ID RCE (CVE-2026-69836, CVSS 10.0)**: A deserialization-of-untrusted-data vulnerability in Entra ID's cloud backend was disclosed August 20, 2026, allowing unauthenticated remote code execution with potential for global tenant compromise — the highest-severity Entra ID flaw to date. Microsoft self-patched the cloud service; no customer action is required, but post-exploitation audit is warranted.

- **421 CVEs in August Patch Tuesday**: Including two near-maximum severity Entra ID and M365 Admin Center elevation-of-privilege flaws (CVE-2026-59115, CVSS 9.9; CVE-2026-62873, CVSS 9.8). Patch governance and SLA enforcement cannot be treated as optional in this velocity environment.

- **Microsoft Teams vishing surged 10× above mid-2025 baseline** (Q2 2026 telemetry): BEC volumes spiked 121% in April 2026; credential phishing constituted 94–96% of all monthly email-borne attack payloads targeting M365. Teams is now an active attack surface requiring the same protection posture as email.

- **TerminalFix hybrid network tunneling threatens Entra Connect environments**: An evolved ClickFix campaign deploys custom Python reverse-tunnel implants providing attackers SOCKS-level proxy access through corporate networks, specifically targeting AD enumeration — a critical risk for Entra hybrid-joined estates where a compromised endpoint can traverse identity synchronization paths to cloud tenants.

> **⚠️ Collection Note:** Ars Technica (Source 2) was inaccessible via the network egress proxy during this automated run. That section uses fallback articles covering the same August 2026 threat stories from The Hacker News; analysts should cross-reference directly at [arstechnica.com/security](https://arstechnica.com/security/).

---

## 1. [The Hacker News](https://thehackernews.com/)

### Insight 1

| Field | Details |
|-------|---------|
| **Title** | [Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution](https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html) |
| **Introduction** | On August 20, 2026, Microsoft disclosed CVE-2026-69836 — a CVSS 10.0 remote code execution vulnerability in Entra ID's backend caused by improper deserialization of untrusted data at unauthenticated service endpoints. Microsoft initially tagged the vulnerability as "Exploited in the Wild" before issuing a correction on August 21 confirming exploitation was **not** observed. The fully cloud-hosted service was patched server-side; no customer action is required. |
| **Status** | **Assess** |
| **Threat Actor including TTPs, Targets & Region** | No confirmed threat actor (exploitation not observed per Microsoft correction). If weaponized: unauthenticated HTTP POST with malicious serialized payload to Entra ID endpoints → RCE → potential backdoor account creation or token-signing key theft. Targets: any organization using Entra ID as IdP for M365, Azure, or federated third-party applications. Global scope — particularly government, critical infrastructure, and financial services. |
| **Affected Cybersecurity Domain** | Identity & Access Management |
| **Risk** | Unauthenticated cloud-side RCE within Entra ID's service plane could allow attackers to create backdoor Global Admin accounts, steal or rotate token-signing certificates, inject malicious federation trust configurations, or maintain silent persistent access across all connected M365 tenants and Azure subscriptions — effectively compromising an entire organization's identity plane with no on-premises footprint. |
| **Strategic Initiative** | MCRA: Identity Plane · Zero Trust Pillars: Verify Explicitly, Assume Breach. Cloud Posture Management (Entra hardening). Alignment: Microsoft Secure Score — Identity category. |
| **Call to Action** | 1. **Post-disclosure audit**: validate no anomalous Global Admin accounts were created or federation trusts modified between August 19–22. 2. **Audit Entra ID Audit Logs** for `OperationName == "Add user"`, `"Add owner to application"`, `"Set domain authentication"` within the disclosure window. 3. **Hunt in Sentinel/Defender XDR**: `AuditLogs \| where TimeGenerated between (datetime(2026-08-19) .. datetime(2026-08-22)) and OperationName contains "Add" and InitiatedBy.app.displayName != "Microsoft"`. 4. **Enable Entra ID Privileged Identity Management** with activation alerts for Global Admin and Privileged Role Administrator. 5. **Review Conditional Access policies** for unexpected new trusted named locations or exclusions added around the disclosure date. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

---

### Insight 2

| Field | Details |
|-------|---------|
| **Title** | [Kali365 Weaponizes Microsoft Authentication Against US Companies: New Enterprise Risk](https://thehackernews.com/2026/08/kali365-weaponizes-microsoft.html) |
| **Introduction** | Kali365, first identified by the FBI in April 2026 and distributed via Telegram, is a Phishing-as-a-Service platform that abuses Microsoft's legitimate OAuth 2.0 Device Authorization Grant flow to harvest M365 access and refresh tokens without ever intercepting user credentials. The platform provides AI-generated lures, 33+ campaign templates, real-time dashboards, and a desktop tool (OctoLink Live) that lets operators open compromised mailboxes using stolen tokens — completely bypassing MFA. August 2026 saw active FBI-warned expansion targeting US enterprise environments. |
| **Status** | **Assess** |
| **Threat Actor including TTPs, Targets & Region** | Actor: Kali365 operator network (financially motivated; distributed commercial PhaaS via Telegram). TTPs: OAuth Device Code phishing (T1078.004 / T1566.002) — victims directed to legitimate microsoft.com/devicelogin; attacker captures resulting access + refresh tokens; OctoLink Live opens mailboxes with stolen tokens; automated session refresh every ~8 hours; post-compromise email harvesting for BEC setup. Targets: US corporations — finance, technology, healthcare, manufacturing. Primary region: United States; secondary EU exposure. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / BEC |
| **Risk** | Persistent M365 access tokens obtained via device code abuse grant full access to Exchange Online, SharePoint, OneDrive, Teams, and Calendar without credential theft. BEC follow-on enables financial fraud, sensitive data exfiltration, and lateral movement through trusted internal communication channels. Automated 8-hour session refresh evades idle-timeout controls and persists for weeks undetected. |
| **Strategic Initiative** | MCRA: Identity Plane · Email & Collaboration Security · Zero Trust: Verify Explicitly (device trust, token binding). Defender for Office 365 P2 · Entra ID Identity Protection · Entra Conditional Access (authentication flows). |
| **Call to Action** | 1. **Block Device Code flow** via Conditional Access Authentication Flow policy for all non-exempted use cases — this is the single highest-impact control. 2. **Deploy phishing-resistant MFA** (FIDO2 passkeys or Certificate-Based Auth) for all users, eliminating token-based MFA bypass. 3. **Enable Entra ID Token Protection** to cryptographically bind tokens to compliant managed devices. 4. **Hunt for device code abuse**: `SigninLogs \| where AuthenticationProtocol == "deviceCode" \| where RiskLevelDuringSignIn in ("medium","high") or IPAddress in (external_suspicious_ranges)`. 5. **Implement Continuous Access Evaluation (CAE)** to revoke sessions in near-real-time upon risk signal. 6. **User education**: Microsoft will never request entry of a device code via email, Teams message, or phone call. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

---

## 2. [Ars Technica](https://arstechnica.com/) — ⚠️ Fallback: Source Inaccessible

> **Collection Limitation:** Ars Technica's domain was blocked by the network egress proxy during this automated run (both direct WebFetch and domain-restricted WebSearch returned access errors). The two insights below cover the identical August 2026 campaigns from The Hacker News as primary fallback sources. Analysts are strongly encouraged to review [arstechnica.com/security](https://arstechnica.com/security/) directly for Ars Technica's own editorial angle on these stories.

---

### Insight 1 — Fallback

| Field | Details |
|-------|---------|
| **Title** | [Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365 Login Flows](https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-eu.html) *(Fallback: The Hacker News, August 2026)* |
| **Introduction** | The Mirage2FA Phishing-as-a-Service kit — active since 2024 — reached a new operational peak in August 2026, compromising sessions across more than 4,500 US and EU organizations by proxying legitimate Microsoft 365 authentication flows. Researchers estimate 48% of targeted email accounts were potentially compromised, with over 9,000 documented session-theft events; the kit bypasses all non-phishing-resistant MFA implementations. |
| **Status** | **Assess** |
| **Threat Actor including TTPs, Targets & Region** | Actor: Mirage2FA operators (commercial PhaaS; multiple independent subscribers). TTPs: Adversary-in-the-Middle (AiTM) session proxying against M365 OAuth flows (T1557); session cookie hijacking (T1539); legitimate Microsoft branding abuse; post-compromise session reuse for email access and BEC setup. Targets: Enterprises across US and EU — financial services, professional services, technology. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / SaaS |
| **Risk** | At 9,000+ documented session-theft events, Mirage2FA represents systematic industrial-scale M365 session compromise. Captured sessions expose Exchange Online, Teams, SharePoint, and OneDrive. Downstream BEC, data exfiltration, and lateral SaaS movement are the primary post-compromise outcomes. Any non-phishing-resistant MFA (SMS, TOTP, push notification) is bypassed by design. |
| **Strategic Initiative** | MCRA: Identity Plane · Email & Collaboration Security · Zero Trust: Verify Explicitly, Assume Breach. Entra ID Identity Protection Sign-in Risk Policies · Conditional Access · Defender for Cloud Apps (MCAS) session control. |
| **Call to Action** | 1. **Enforce phishing-resistant authentication** (FIDO2 / Entra ID passkeys / Certificate-Based Auth) as the baseline for all users — the only reliable defense against AiTM. 2. **Enable Sign-in Risk Conditional Access policies** (auto-block/step-up for medium+ risk). 3. **Deploy Defender for Cloud Apps** to monitor and revoke anomalous active sessions. 4. **Enable Entra ID Continuous Access Evaluation** for token revocation propagation in <1 minute. 5. **Hunt for AiTM indicators**: `SigninLogs \| where NetworkLocationDetails contains "proxy" or IPAddress in (known_residential_proxy_ranges) and ResultType == 0`. 6. Verify your Secure Email Gateway inspects redirect chains within phishing emails at URL level. |
| **Source** | [Ars Technica](https://arstechnica.com/) *(inaccessible — fallback: The Hacker News)* |

---

### Insight 2 — Fallback

| Field | Details |
|-------|---------|
| **Title** | [New Passkey Attacks Can Recover Synced Private Keys or Bypass Phishing-Resistant MFA](https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html) *(Fallback: The Hacker News, August 2026)* |
| **Introduction** | Security researchers disclosed novel attack techniques in August 2026 against cloud-synced passkey implementations (Google, Apple, Microsoft), demonstrating that passkey private keys synced via vendor cloud backup mechanisms may be extractable under certain conditions, and that device-attestation spoofing can in some scenarios allow passkey authentication from an unregistered device. The disclosure carries critical timing implications: Microsoft began rolling out passkeys as the **default** Entra ID authentication method on September 1, 2026. |
| **Status** | **Assess** |
| **Threat Actor including TTPs, Targets & Region** | Actor: Security researchers (responsible disclosure); potential exploitation by APT-level or sophisticated financially motivated actors with access to target devices or cloud sync infrastructure. TTPs: Passkey private key extraction from cloud sync storage; attestation bypass; abuse of passkey sync metadata. Targets: High-value individuals (executives, admins) and enterprises with Entra ID passkey enrollment. Global scope. |
| **Affected Cybersecurity Domain** | Identity & Access / Endpoint |
| **Risk** | If cloud-synced passkey private keys are extractable, attackers can authenticate to M365 and Entra ID without possessing the registered physical device — directly negating the phishing-resistant MFA strategy Microsoft is deploying as default in September 2026. This would undermine a cornerstone control of enterprise Zero Trust identity policy at scale. |
| **Strategic Initiative** | MCRA: Identity Plane (Passkeys/FIDO2) · Zero Trust: Verify Explicitly. Entra ID Authentication Methods Policy · Conditional Access: Device compliance attestation for passkey authentication. |
| **Call to Action** | 1. **Monitor Microsoft's advisory track** for passkey sync vulnerability patches and apply immediately. 2. **Prefer hardware-bound passkeys** (non-exportable, AAGUID-attested hardware security keys like YubiKey) for privileged and high-value accounts instead of cloud-synced software passkeys. 3. **Enforce Compliant Device Conditional Access** alongside passkey MFA — require Intune-enrolled, MDM-managed devices for authentication. 4. **Monitor Entra ID risk detections** for anomalous passkey authentications from atypical device profiles or geolocations. 5. **Engage with Microsoft's passkey rollout communications** before assuming full September 2026 passkey deployment is risk-mitigated. |
| **Source** | [Ars Technica](https://arstechnica.com/) *(inaccessible — fallback: The Hacker News)* |

---

## 3. [Dark Reading](https://www.darkreading.com/)

### Insight 1

| Field | Details |
|-------|---------|
| **Title** | [Microsoft's Patch Tuesday Deluge Continues With August Updates](https://www.darkreading.com/application-security/microsofts-patch-tuesday-deluge-continues) |
| **Introduction** | Microsoft's August 2026 Patch Tuesday addressed 421 CVEs — among the largest monthly releases on record — including two actively concerning Entra ID and Microsoft 365 Admin Center elevation-of-privilege vulnerabilities (CVE-2026-59115, CVSS 9.9 and CVE-2026-62873, CVSS 9.8), two zero-days, and 44 critical-severity flaws. Dark Reading highlights the compounding governance challenge for enterprise security teams managing this scale of patching velocity. |
| **Status** | **Assess** |
| **Threat Actor including TTPs, Targets & Region** | Multiple threat actors. CVE-2026-68820 (EoP in Windows WinSock, CVSS 7.0) is confirmed actively exploited in targeted attacks to escalate to SYSTEM privileges. All unpatched Windows, Microsoft 365, and Entra ID environments globally are in scope. |
| **Affected Cybersecurity Domain** | Identity & Access / Endpoint / Vulnerability Management |
| **Risk** | CVE-2026-59115 (Entra Provisioning Service EoP, CVSS 9.9): allows an attacker with initial low-privilege access to the provisioning pipeline to escalate to administrative control, enabling mass user creation, permission assignment, or backdoor provisioning across all M365 connected applications. CVE-2026-62873 (M365 Admin Center EoP, CVSS 9.8): threatens tenant-wide administrative takeover. Combined with active exploitation of the Windows EoP zero-day, endpoint compromise can quickly chain into cloud identity escalation. |
| **Strategic Initiative** | MCRA: Governance & Risk Management · Identity Plane · Endpoint Security · Zero Trust: Assume Breach. Defender Vulnerability Management; Microsoft Secure Score — vulnerability management pillar; Intune patch compliance reporting. |
| **Call to Action** | 1. **Prioritize CVE-2026-59115 and CVE-2026-62873** for immediate patching within 24–48 hours — treat Entra and M365 Admin Center EoP flaws as P1 regardless of overall patch cycle timing. 2. **Audit Entra Provisioning Service** connectors and app provisioning logs for unauthorized role assignments or user creations. 3. **Deploy CVE-2026-68820 patch** via Intune/WSUS for all Windows endpoints as the actively exploited zero-day. 4. **Enable PIM just-in-time access** for M365 Admin Center roles — eliminate persistent standing admin access. 5. **Automate Sentinel alerts** for Entra provisioning anomalies: `AuditLogs \| where Category == "ProvisioningManagement" and OperationName in ("Add user to role", "Add app role assignment")`. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

---

### Insight 2

| Field | Details |
|-------|---------|
| **Title** | [Critical Azure Entra ID Flaw Highlights Microsoft IAM Issues](https://www.darkreading.com/cloud-security/critical-azure-entra-id-flaw-microsoft-iam-issues) |
| **Introduction** | Dark Reading's editorial analysis of CVE-2026-69836 goes beyond the patch notice to examine structural Identity and Access Management (IAM) architectural weaknesses in Microsoft's cloud identity stack — specifically the risk of insufficient input validation at authentication service boundaries, the security implications of a single-vendor cloud identity monopoly, and why organizations cannot rely solely on Microsoft's server-side remediation response as a risk management strategy. |
| **Status** | **Assess** |
| **Threat Actor including TTPs, Targets & Region** | No confirmed exploitation. Systemic risk relevant to nation-state APT actors with cloud identity compromise mandates (Cozy Bear/APT29, Volt Typhoon, APT41, Lazarus Group) and the technical capability to exploit service-layer vulnerabilities before emergency patching completes. Global scope: all Entra ID-dependent organizations across government, financial services, healthcare, and critical infrastructure. |
| **Affected Cybersecurity Domain** | Identity & Access / Cloud Security Architecture |
| **Risk** | Organizations that rely exclusively on Entra ID as their identity control plane face catastrophic tenant-level compromise if a cloud-side RCE is weaponized — affecting all federated applications, all Azure subscriptions, and all M365 data without any on-premises attacker footprint. The single-vendor dependency creates a systemic concentration risk that patch governance alone cannot fully address. |
| **Strategic Initiative** | MCRA: Identity Plane · Zero Trust Architecture: Assume Breach (blast radius reduction), Defense-in-Depth. Alignment: Microsoft Zero Trust Rapid Modernization Plan (RaMP) — privileged access workstations, Entra hardening, break-glass account controls. |
| **Call to Action** | 1. **Harden privileged admin access**: enforce Entra Private Access or Bastion hosts for all M365/Azure admin portal access, restricting to compliant managed devices. 2. **Enforce Conditional Access for all privileged roles**: phishing-resistant MFA + compliant device + named locations only. 3. **Implement PIM** with approval workflows and maximum 4-hour activation windows for Global Admin and Privileged Role Administrator. 4. **Configure break-glass account monitoring**: `SigninLogs \| where UserPrincipalName in (break_glass_accounts) \| where ResultType != "50126"` — alert immediately on any use. 5. **Run a tabletop exercise** for full Entra ID compromise scenario — test detection, containment, and recovery playbooks. 6. Evaluate whether critical workloads require a secondary identity provider or certificate-based fallback path. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

---

## 4. [BleepingComputer](https://www.bleepingcomputer.com/)

### Insight 1

| Field | Details |
|-------|---------|
| **Title** | [Entra Passkey Enrollment Vishing Targets Microsoft 365 Users](https://www.bleepingcomputer.com/news/security/entra-passkey-enrollment-vishing-targets-microsoft-365-users/) |
| **Introduction** | Since April 2026, an active vishing (voice phishing) campaign has targeted Microsoft 365 users across multiple sectors, with attackers calling individuals and socially engineering them to enroll attacker-controlled passkeys in their Entra ID accounts. By abusing Microsoft's legitimate passkey self-enrollment portal, threat actors gain phishing-resistant M365 access without ever possessing user credentials — a significant escalation in social engineering sophistication that weaponizes Entra's own identity hardening features. |
| **Status** | **Assess** |
| **Threat Actor including TTPs, Targets & Region** | Actor: Unnamed financially motivated threat cluster (potential operational overlap with UNC6671 vishing operations documented by Mandiant). TTPs: Voice phishing (T1566.004) impersonating IT helpdesk or Microsoft Security; social engineering to initiate Entra passkey self-enrollment (T1098.001); post-compromise access via attacker-registered passkey credential; persistent account access without credential knowledge. Targets: Healthcare, finance, technology, government organizations. US and EU primary regions. Campaign active April–August 2026. |
| **Affected Cybersecurity Domain** | Identity & Access / Social Engineering / Phishing |
| **Risk** | Attacker-registered passkeys provide persistent, effectively phishing-resistant (from the victim's defensive perspective) access to M365 with minimal detection signal. If registered through a legitimate Entra enrollment flow, the event generates standard audit logs rather than risk detections. Enables downstream BEC, data theft, Teams impersonation, and lateral M365 movement using a registered credential the victim is unaware of. |
| **Strategic Initiative** | MCRA: Identity Plane · Human Risk Management · Zero Trust: Verify Explicitly (device trust and approval for registration events). Entra ID Authentication Methods Policy · Conditional Access for authentication method registration. |
| **Call to Action** | 1. **Restrict passkey self-enrollment**: require IT helpdesk ticket and manager co-approval via Entra ID Authentication Methods Policy — disable open self-enrollment for passkeys until vishing campaign declines. 2. **Enforce Conditional Access for registration events**: require Intune-enrolled managed devices for any new passkey registration — block from unmanaged personal devices. 3. **Alert on passkey registration events**: `AuditLogs \| where OperationName == "User registered security info" and AuthenticationMethodType == "passkey" \| where InitiatedBy.user.displayName != (expected IT admin)`. 4. **User awareness training**: no legitimate IT or Microsoft call requests a user to approve or register a new passkey via phone — treat all such calls as social engineering attempts. 5. **Review registered passkeys monthly**: report all passkey registrations to users for self-verification. |
| **Source** | [BleepingComputer](https://www.bleepingcomputer.com/) |

---

### Insight 2

| Field | Details |
|-------|---------|
| **Title** | [Hackers Use AiTM Attack to Monitor Microsoft 365 Accounts for BEC Scams](https://www.bleepingcomputer.com/news/security/hackers-use-aitm-attack-to-monitor-microsoft-365-accounts-for-bec-scams/) |
| **Introduction** | BleepingComputer reported in depth on the Payroll Pirates campaign (Microsoft tracking ID: Storm-2755), an ongoing financially motivated AiTM operation first observed in July 2026 that hijacks Microsoft 365 executive and HR/finance accounts, then uses Microsoft Graph API automation to silently monitor payroll, finance, and HR email threads across US, Canadian, and European organizations. The campaign routes victims through trusted Google and Amazon infrastructure before proxying the Microsoft login — rendering most URL-inspection defenses ineffective. |
| **Status** | **Assess** |
| **Threat Actor including TTPs, Targets & Region** | Actor: Storm-2755 / Payroll Pirates (financially motivated; active since July 2026; tracked by Arctic Wolf and Microsoft). TTPs: AiTM phishing via fake Microsoft login proxy routed through Google/Amazon infrastructure (T1557); session cookie theft (T1539); Microsoft Graph API mailbox search automation to identify payroll/finance/HR staff (T1114.002); inbox rule creation for email redirection (T1564.008); BEC wire/payroll fraud; automated 8-hour session refresh for persistence. Targets: C-suite executives, CFOs, payroll administrators, HR directors. US (primary), Canada, EU. Sectors: healthcare, education, manufacturing, government, professional services. |
| **Affected Cybersecurity Domain** | Email Security / BEC / Identity & Access |
| **Risk** | Storm-2755 achieves persistent M365 session access, then uses Microsoft's own Graph API to surgically identify high-value financial email threads and insert itself at the precise moment of a payment authorization or payroll update — enabling salary diversion and fraudulent wire transfers worth hundreds of thousands to millions per incident. Session automation and residential proxy routing make detection extremely difficult without dedicated BEC-specific alerting. |
| **Strategic Initiative** | MCRA: Email & Collaboration Security · Identity Plane · Zero Trust: Assume Breach, Least Privilege. Defender for Office 365 Plan 2 (BEC detection engine) · Entra ID Identity Protection · Microsoft Sentinel Graph API monitoring · MCAS conditional access app control. |
| **Call to Action** | 1. **Deploy Defender for Office 365 Plan 2** BEC policies with payroll, finance, and wire transfer keyword alerting on executive and admin mailboxes. 2. **Alert on inbox rule creation**: `OfficeActivity \| where Operation in ("New-InboxRule","Set-InboxRule") \| where Parameters contains "ForwardTo" or Parameters contains "DeleteMessage"`. 3. **Alert on Graph API bulk mailbox search activity**: `CloudAppEvents \| where ActionType == "SearchMailboxes" and AccountObjectId !in (approved_service_accounts)`. 4. **Block legacy authentication** (Conditional Access: block all legacy auth protocols) — eliminates a common AiTM proxy fallback path. 5. **Implement dual-approval controls** for all wire transfers and payroll changes — remove email-only confirmation from financial workflows. 6. **Enable phishing-resistant MFA** for all finance, HR, and C-suite accounts as first priority cohort. |
| **Source** | [BleepingComputer](https://www.bleepingcomputer.com/) |

---

## 5. [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/)

### Insight 1

| Field | Details |
|-------|---------|
| **Title** | [TerminalFix Campaign Deploys a Reverse Tunnel Through Multistage Intrusion](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/) |
| **Introduction** | Published August 28, 2026, Microsoft Threat Intelligence's analysis of TerminalFix reveals an advanced evolution of the ClickFix social engineering family: fake Cloudflare CAPTCHA overlays inject PowerShell via Windows Terminal clipboard manipulation, followed by DLL sideloading and steganographic payload delivery, culminating in a custom Python-based reverse WebSocket tunnel that grants attackers full SOCKS-level TCP proxy access through victim networks. Domain controller enumeration and SQL server discovery confirm enterprise lateral movement as the primary objective. |
| **Status** | **Stay Informed** |
| **Threat Actor including TTPs, Targets & Region** | Actor: Unnamed financially motivated threat cluster (emerging; not attributed to a known APT). TTPs: Drive-by compromise via ClickFix CAPTCHA overlay (T1189); clipboard-injected PowerShell via Windows Terminal (T1059.001); DLL sideloading via LockScreenContentServer.exe (T1574.002); steganographic PNG payload (T1027); Registry Run key + Scheduled Task persistence (T1547.001, T1053.005); Active Directory enumeration (T1018); reverse WebSocket C2 tunnel → SOCKS proxy (T1572). Targets: Enterprise organizations across IT, manufacturing, transportation, hospitality; European and North American presence. |
| **Affected Cybersecurity Domain** | Endpoint / Network / Identity & Access (Hybrid Environments) |
| **Risk** | The reverse WebSocket tunnel (connecting to gitnow[.]dev:443) transforms compromised endpoints into persistent SOCKS proxy pivot points providing attackers full TCP access to internal network segments — including domain controllers, SQL servers, backup infrastructure, and Entra Connect sync servers. In Entra hybrid-join environments, this attack path can enable credential harvesting from synced AD accounts, compromise of Entra Connect Sync service accounts, and ultimately cloud identity hijacking without any direct cloud attack vector. |
| **Strategic Initiative** | MCRA: Endpoint Security · Identity Plane (Hybrid) · Network Security · Zero Trust: Assume Breach, Least Privilege Access. Defender XDR for multi-stage detection · Microsoft Sentinel for lateral movement hunting · AppLocker/WDAC hardening · Entra Connect hardening. |
| **Call to Action** | 1. **Enable Attack Surface Reduction rules**: particularly `Block credential stealing from the Windows local security authority subsystem (lsass.exe)` and DLL sideloading prevention rules. 2. **Deploy AppLocker or Windows Defender Application Control (WDAC)** to restrict unsigned DLL execution from non-standard paths. 3. **Monitor for reverse tunnel C2**: block or alert on outbound WebSocket connections to code-hosting domains (gitnow[.]dev and similar); enforce DNS filtering for uncategorized domains. 4. **Harden Entra Connect Sync**: isolate the sync server, use a dedicated low-privilege service account, and alert on any sign-in from the Entra Connect Sync account outside expected behavior: `SigninLogs \| where UserPrincipalName == "sync_account@domain" and IPAddress !in (entra_connect_server_IPs)`. 5. **Hunt for ClickFix IOCs**: PowerShell with `Set-Clipboard` followed by terminal execution; LockScreenContentServer.exe loading DLLs from `%AppData%` or `%Temp%`. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

---

### Insight 2 — Fallback: July 2026

| Field | Details |
|-------|---------|
| **Title** | [Email Threat Landscape: Q2 2026 Trends and Insights](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/) *(Fallback: July 23, 2026 — no additional M365-specific threat intelligence posts published in August 2026 beyond TerminalFix and DeadLock ransomware)* |
| **Introduction** | Microsoft's Q2 2026 Email Threat Landscape report — derived from analysis of 7.6 billion email-borne phishing threats — reveals Teams-based vishing attacks at nearly 10× their mid-2025 baseline, a 121% BEC spike in April 2026, and credential phishing comprising 94–96% of all monthly payloads targeting M365 users. The report also documents the impact of Microsoft's March 2026 disruption of the Tycoon2FA PhaaS platform (92% decline by June) and the sustained rise of QR code phishing. |
| **Status** | **Stay Informed** |
| **Threat Actor including TTPs, Targets & Region** | Multiple actors. Key clusters: Tycoon2FA operators (disrupted March 2026), QR code phishing groups, Teams-based vishing operators. TTPs: Teams vishing (T1566.004) at 10× baseline; QR code phishing in PDF attachments (T1566.001); credential phishing via spoofed Microsoft authentication redirects; automated BEC reaching 67,000 users across 42,000 organizations within a 3-hour campaign window. Targets: All M365 enterprise and education tenants globally. |
| **Affected Cybersecurity Domain** | Email Security / Phishing / BEC / Identity & Access |
| **Risk** | Teams-based vishing at 10× baseline represents an urgent, underprotected attack surface — most organizations have mature email defenses but limited Teams-specific vishing controls. BEC automation capable of targeting 42,000 organizations in 3 hours demonstrates that manual incident response cannot scale to match adversary speed. Credential phishing at 94–96% payload share means nearly all M365 email attacks target credentials or session tokens; every user is in scope. |
| **Strategic Initiative** | MCRA: Email & Collaboration Security · Human Risk Management · Zero Trust: Verify Explicitly. Defender for Office 365 P2 · Microsoft Teams security policies · Microsoft Secure Score (email + collaboration categories). |
| **Call to Action** | 1. **Restrict Teams external access**: limit or block Teams messages from unmanaged external tenants; enforce allow-list policies for external domain communication. 2. **Deploy Defender for Office 365 Safe Links and Safe Attachments for Teams** — not just Exchange Online — as an immediate gap closure. 3. **Configure Teams calling policies** with caller verification notifications to alert users when receiving calls from external identities. 4. **Update security awareness training** to include Teams-based vishing scenarios and QR code phishing recognition — most programs focus exclusively on email. 5. **Track BEC automation signals**: `OfficeActivity \| where Operation in ("New-InboxRule","Set-InboxRule") \| summarize count() by UserId, bin(TimeGenerated, 1h) \| where count_ > 5` — rapid-succession rule creation indicates automated post-compromise activity. 6. **Integrate Microsoft Threat Intelligence** directly into Sentinel to receive real-time campaign indicators. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

---

## Most Critical Finding

**CVE-2026-69836 (CVSS 10.0) — Entra ID Unauthenticated RCE + PhaaS Ecosystem Industrialization**: The combination of a maximum-severity cloud-side Entra ID remote code execution disclosure (now patched by Microsoft) with an operationally mature PhaaS market (Kali365, Mirage2FA, Storm-2755) targeting M365 via AiTM and Device Code abuse at industrial scale represents the most severe M365 threat posture month on record. Immediate priorities: disable Device Code flow via Conditional Access, enforce phishing-resistant MFA, audit post-disclosure Entra Global Admin changes, and deploy BEC-specific Graph API monitoring.

---

*Report generated automatically by Delphi on 2026-09-01. Intelligence is assessed based on open-source reporting and Microsoft-published telemetry. Verify all IOCs and CVE details against primary vendor advisories before operational use. Ars Technica source was inaccessible via network proxy — cross-reference directly at arstechnica.com/security.*

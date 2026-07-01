# M365 Threat Intelligence Report — 2026-07-01

**Report Period:** June 2026 (fallbacks to May/March 2026 where noted)
**Audience:** Security Architects · SOC Leads · Cyber Leadership
**Analyst Note:** Content gathered via automated web research on 2026-07-01. Ars Technica (Source 2) returned access errors for the Anthropic user agent on both WebFetch and WebSearch (`Claude Code is unable to fetch from arstechnica.com`; `API Error: domain not accessible to our user agent`). That section presents two June 2026 insights sourced from verified secondary coverage of the same stories; the URLs are primary sources (TechCrunch, Microsoft Security Blog) rather than Ars Technica article links, and are clearly labelled as such.

---

## Executive Summary

Five cross-source themes dominated the M365/Entra ID/Azure threat landscape in June 2026:

1. **AI attack surface expansion.** Microsoft 365 Copilot became an active threat vector. CVE-2026-42824 ("SearchLeak") chained a prompt injection, an HTML race condition, and a Bing SSRF to exfiltrate any user-accessible enterprise content in a single click — patched by Microsoft on 4 June. Concurrently, Storm-3075 and Fox Tempest exploited AI-brand hype (fake ChatGPT/Claude lures) to deliver AiTM credential/token theft at scale. The AI layer is now both a target surface and an attack delivery mechanism.

2. **Phishing-as-a-Service commoditisation of device code abuse.** EvilTokens (launched Feb 2026, 1,380% device-code phishing surge) and Kali365 (FBI IC3 advisory PSA260521, Apr 2026) have reduced OAuth device-code attacks to a subscription-priced turnkey service. Standard MFA is ineffective: victims complete the challenge themselves. Refresh tokens survive password resets.

3. **No-malware identity-to-cloud kill chains.** Storm-2949 converted one SSPR social-engineering call into full exfiltration of M365 (thousands of OneDrive/SharePoint files) and Azure (Key Vault secrets, VM credentials, SQL firewall bypass) — zero malware, all legitimate platform APIs. This confirms a structural shift to identity as the primary kill-chain entry point.

4. **Misconfigured Entra tenant as enterprise blast radius.** FIFA's public World Cup Agent Platform auto-provisioned accounts into its production Entra tenant, enabling any external registrant to access internal match management systems and TV broadcast controls. No credentials required beyond a free registration. Illustrates how tenant segmentation failures convert low-complexity attacks into critical impact.

5. **Infostealer-to-enterprise bridge.** The StealC/Amadey ecosystem and the Sapphire Sleet npm supply chain compromise both harvest session cookies and OAuth tokens from personal/developer devices, providing a direct bridge into corporate M365 and Azure environments. A single stolen SSO token can unlock cloud-wide access regardless of MFA posture.

---

## Source 1 — [The Hacker News](https://thehackernews.com/)

### Insight 1

| Field | Content |
|-------|---------|
| **Title** | [One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html) |
| **Introduction** | Varonis Threat Labs disclosed CVE-2026-42824 ("SearchLeak"), a three-stage vulnerability chain in Microsoft 365 Copilot Enterprise Search that silently exfiltrates emails, SharePoint documents, OneDrive files, Teams data, and MFA codes — all triggered by a single click on a crafted URL containing a malicious `q` parameter. The attack chains a parameter-to-prompt injection, an HTML rendering race condition, and a Bing SSRF/CSP bypass; no credentials, malware, or elevated permissions are required. Microsoft mitigated the flaw server-side on 4 June 2026 with no customer action needed, though Varonis' PoC demonstrates the threat model remains relevant for any AI Search integrated with sensitive enterprise data. |
| **Status** | Stay Informed |
| **Threat Actor incl. TTPs, Targets & Region** | No named threat actor; Varonis PoC (defensive research). **TTPs:** T1190 Exploit Public-Facing Application; T1059.003 Command/Scripting via prompt injection; T1537 Transfer Data to Cloud Account; T1556.006 Modify Authentication Process (CSP bypass). **Attack chain:** (1) Crafted URL with malicious `q` parameter passed directly to Copilot as an executable prompt → (2) `<img>` tag in AI response fires before output sanitizer → (3) Bing image-search endpoint (CSP-allowlisted) performs SSRF GET to attacker-controlled server exfiltrating enterprise content. **Targets:** Any M365 Copilot Enterprise tenant globally. No credential requirement for victim — just a link click. |
| **Affected Cybersecurity Domain** | SaaS / AI Security / Data Exfiltration |
| **Risk** | One-click exfiltration of all Copilot-accessible M365 content (executive email threads, MFA seed material, SharePoint documents, Teams conversations). Blast radius limited only by user's data access scope. No persistence, no lateral movement needed, no EDR/AV signal. Risk of targeted spear-phishing abuse remains if similar patterns surface in future AI Search implementations or third-party Copilot plugins. |
| **Strategic Initiative** | MCRA: SaaS Security + Data Protection. Zero Trust: **Data pillar** — Assume Breach posture for AI workloads; least-privilege Copilot data access; classify and label sensitive assets before enabling AI indexing. |
| **Call to Action** | (1) Verify your M365 Copilot Enterprise Search access controls and data scope. (2) Audit which users hold M365 Copilot E5/E3+AI Add-on licensing — reduce to least-privilege principle. (3) Hunt in Defender XDR Unified Audit Log for anomalous Copilot Search queries containing external URL patterns or unexpected image-load events. (4) Validate Copilot configuration against the Microsoft Copilot for M365 security baseline and Purview data classification policies. (5) Enforce Sensitivity Label policies on SharePoint/OneDrive to restrict Copilot indexing of confidential content. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

---

### Insight 2 — *(2-month fallback: March 2026)*

| Field | Content |
|-------|---------|
| **Title** | [Device Code Phishing Hits 340+ Microsoft 365 Orgs Across Five Countries via OAuth Abuse](https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html) |
| **Introduction** | The EvilTokens phishing-as-a-service (PhaaS) platform, launched February 2026 and sold via Telegram at $600–$1,500/month, compromised over 340 Microsoft 365 organizations across the US, Canada, Australia, New Zealand, and Germany within its first five weeks. It abuses the legitimate OAuth 2.0 Device Authorization Grant (RFC 8628): victims are socially engineered into entering attacker-supplied device codes at `microsoft.com/devicelogin` and completing their own MFA challenge on the attacker's behalf, handing over persistent refresh tokens scoped to mailbox, OneDrive, calendar, and contacts. Huntress reported a 1,380% increase in device-code phishing activity between late 2025 and early 2026. |
| **Status** | Assess |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** EvilTokens PhaaS operators (financially motivated, open Telegram marketplace). **TTPs:** T1078 Valid Accounts; T1550.001 Application Access Token; T1534 Internal Spearphishing (BEC follow-on); AI-generated role-specific lures that adapt in near-real-time; built-in webmail interface, email harvesting, and mailbox triage. Tokens survive password resets. **Targets:** M365 organizations across all sectors; US, Canada, Australia, New Zealand, Germany identified in the initial 5-week campaign. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / BEC |
| **Risk** | Standard MFA provides zero protection — victim completes the MFA challenge themselves. Resulting refresh tokens persist for weeks to months per tenant token lifetime policy. Attackers gain full M365 scope (mail, calendar, OneDrive, Teams) enabling BEC wire-fraud, intellectual property theft, and privilege escalation. Single token can serve as pivot into connected SaaS apps (Salesforce, Slack, Zendesk) via SSO. |
| **Strategic Initiative** | MCRA: Identity Security (OAuth / App Registration governance) + Zero Trust: **Identity pillar** — phishing-resistant MFA, token lifetime controls, Conditional Access on device authorization flows. |
| **Call to Action** | (1) **Block device code authentication** via Entra ID Conditional Access ("Block legacy authentication" policy → include Device Code flow) for all non-kiosk users. (2) Audit active OAuth grants in Entra ID Admin Center > Enterprise Applications. (3) Hunt: Entra ID Sign-in Logs → filter `Authentication Method = Device Code` and correlate with unfamiliar device/IP. (4) Configure **authentication transfer policies** to prevent session transfer across devices. (5) Enforce **Entra ID Token Protection** for Exchange, SharePoint, Teams. (6) Alert on refresh token reuse from new geolocation within 24 hours of initial grant. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

---

## Source 2 — [Ars Technica](https://arstechnica.com/) *(Source Inaccessible — Secondary Coverage Used)*

> **⚠️ Access Limitation:** Ars Technica has blocked the Anthropic web-crawler user agent. Both `WebFetch` and `WebSearch` with the `arstechnica.com` domain return hard errors. The two insights below are drawn from verified secondary sources (TechCrunch, Microsoft Security Blog) covering the same June 2026 stories that fall within Ars Technica's standard coverage brief. URLs reflect the primary accessible source for each story, not an Ars Technica article link.

### Insight 1 — *(Secondary source; Ars Technica inaccessible)*

| Field | Content |
|-------|---------|
| **Title** | [Microsoft's open source tools were hacked to steal passwords of AI developers](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/) *(TechCrunch — Ars Technica domain inaccessible)* |
| **Introduction** | On 5 June 2026, GitHub disabled 73 Microsoft-owned repositories across the Azure, Azure-Samples, Microsoft, and MicrosoftDocs GitHub organizations after attackers injected password-stealing malware into developer tools used by AI coding workflows (VS Code extensions, Azure SDKs, and AI agent frameworks). Security firms Cloudsmith and OpenSourceMalware confirmed the malware harvested credentials when developers opened the compromised packages in AI coding environments including Claude Code, Gemini CLI, and VS Code. This was identified as a "re-compromise" of the Durable Task repository, suggesting incomplete remediation from a May 2026 incident attributed to Sapphire Sleet (North Korean state-sponsored, financially motivated). |
| **Status** | Assess |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Sapphire Sleet (North Korean state-sponsored, financially motivated; previously focused on crypto theft and supply chain compromise). **TTPs:** T1195.002 Compromise Software Supply Chain; T1554 Compromise Client Software Binary (postinstall payload injection); T1552.001 Credentials In Files (browser credential harvesting); T1587.001 Develop Capabilities: Malware. **Targets:** AI/ML and Azure developers globally who use open-source tooling from Microsoft's GitHub organizations. **Regions:** Global; disproportionate impact on US, European, and APAC developer communities. |
| **Affected Cybersecurity Domain** | SaaS / Cloud Developer Toolchain / Supply Chain |
| **Risk** | Stolen Azure developer credentials provide direct access to Azure subscriptions, Entra ID tenants, and connected M365 environments. Compromised development pipelines can inject malicious code into production Azure workloads (App Services, ACI, AKS). Password and session-token theft from developer workstations bypasses corporate MFA because tokens are already authenticated. Cascading impact: Azure DevOps pipelines, GitHub Actions, and any CI/CD deploying from compromised repos are downstream blast radius. |
| **Strategic Initiative** | MCRA: DevSecOps + Supply Chain Security + Zero Trust: **Applications pillar** (secure code pipeline, least-privilege service principals). |
| **Call to Action** | (1) Audit all GitHub Actions and Azure DevOps pipelines consuming Microsoft open-source packages from the affected orgs; pin dependency versions and verify hashes. (2) Rotate all developer Azure service principal credentials and revoke stale OAuth tokens linked to affected repos. (3) Enable Entra ID Sign-in Risk policies to flag anomalous developer identity sign-ins. (4) Scan developer workstations for StealC/Amadey or "Miasma Worm" IOCs (see Microsoft DCU advisory). (5) Enforce Managed Identity over service principal credentials for Azure workloads. (6) Review GitHub Advanced Security secret scanning alerts across Azure-connected repositories. |
| **Source** | [Ars Technica](https://arstechnica.com/) *(inaccessible — insight sourced from TechCrunch cross-coverage)* |

---

### Insight 2 — *(Secondary source; Ars Technica inaccessible)*

| Field | Content |
|-------|---------|
| **Title** | [From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/) *(Microsoft Security Blog — Ars Technica domain inaccessible)* |
| **Introduction** | Microsoft Threat Intelligence published a detailed analysis of Sapphire Sleet's compromise of the Mastra npm package — an AI agent orchestration framework used in 140+ downstream Azure and cloud-native projects. The attack inserted a hidden `postinstall` script that executed a credential harvesting payload on package installation, targeting developer environments that include Azure authentication contexts, GitHub tokens, and M365 OAuth tokens stored in local credential caches. The incident is part of a broader campaign correlated with the June 5 Microsoft GitHub repository takeovers. |
| **Status** | Assess |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Sapphire Sleet (DPRK-nexus; ATT&CK cluster overlaps with Lazarus Group tradecraft for supply chain intrusion). **TTPs:** T1195.001 Compromise Software Dependencies and Development Tools; T1059.001 PowerShell postinstall execution; T1552.001 Unsecured Credentials; T1003.001 OS Credential Dumping. The threat actor weaponized the npm package lifecycle to execute in CI/CD and developer environments without any user-initiated action beyond `npm install`. **Targets:** Cloud-native development teams using AI agent frameworks; Azure/M365 developer ecosystems. **Regions:** Global; focus on technology, financial services, and crypto verticals aligned with Sapphire Sleet's historic targeting. |
| **Affected Cybersecurity Domain** | Supply Chain / SaaS / Cloud Developer Security |
| **Risk** | Credential exfiltration from developer machines provides Sapphire Sleet with Azure service principal tokens, M365 OAuth grants, and GitHub PATs — sufficient for lateral movement into production Entra tenants without any additional exploitation. Downstream npm consumers in 140+ projects amplify the blast radius beyond the initial compromise. Financial services organizations using Mastra-based AI agents for M365/Teams-integrated workflows face elevated risk of cloud-tenant takeover. |
| **Strategic Initiative** | MCRA: Supply Chain + Identity Security. Zero Trust: **Identity pillar** — service principal hygiene; **Applications pillar** — dependency integrity validation. |
| **Call to Action** | (1) Immediately audit npm dependency trees for `mastra` and related packages; check installed versions against known clean hashes. (2) Revoke and rotate all Azure service principal secrets and OAuth tokens present on developer machines during the exposure window (approx. May–June 2026). (3) Enable `npm audit` and npm provenance attestation in all CI/CD pipelines. (4) Restrict outbound network from build environments to prevent postinstall data exfiltration. (5) Enroll developer identity accounts in Entra ID Privileged Identity Management (PIM) with just-in-time access for Azure subscriptions. (6) Hunt for Sapphire Sleet IOCs (Microsoft MSTIC advisory) in Defender for Endpoint and Defender for Cloud telemetry. |
| **Source** | [Ars Technica](https://arstechnica.com/) *(inaccessible — insight sourced from Microsoft Security Blog cross-coverage)* |

---

## Source 3 — [Dark Reading](https://www.darkreading.com/)

### Insight 1

| Field | Content |
|-------|---------|
| **Title** | [FIFA Bug Exposes World Cup Streams to Remote Takeover](https://www.darkreading.com/application-security/fifa-bug-world-cup-streams-remote-takeover) |
| **Introduction** | Ethical hacker "BobDaHacker" disclosed on 14 June 2026 that an access control failure in FIFA's Microsoft Entra ID configuration allowed any external registrant on the public FIFA Agent Platform to receive an account in FIFA's single production Entra tenant — the same tenant controlling World Cup TV streams, match management systems, and internal operations. Despite receiving access-denied messages in the UI, the backend API respected the provisioned account's permissions, granting near-unrestricted internal access. FIFA had no security disclosure channel; the researcher was forced to contact CISA and the FBI to prompt remediation, which was completed within 24 hours. |
| **Status** | Educate |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** No malicious exploitation confirmed; disclosed by ethical researcher. **Applicable TTPs if weaponised:** T1078.004 Valid Accounts: Cloud Accounts (auto-provisioned); T1538 Cloud Service Discovery; T1530 Data from Cloud Storage Object; T1496 Resource Hijacking (broadcast stream manipulation). **Root cause:** Absent tenant segmentation — public-facing registration and internal enterprise systems shared a single Entra ID tenant with insufficient RBAC isolation. **Targets:** Organizations that operate externally-facing portals or partner onboarding within the same Entra tenant as internal production systems. **Region:** Global relevance; any multi-tier SaaS/partner integration using shared Entra tenancy. |
| **Affected Cybersecurity Domain** | Identity & Access / Cloud Misconfiguration / SaaS |
| **Risk** | An identical misconfiguration in a corporate M365 tenant would allow any partner onboarding workflow to auto-provision Entra accounts with implicit internal access. This enables unauthenticated (from a corporate credential perspective) access to SharePoint, Teams, Exchange, and Azure resources — a zero-cost tenant takeover requiring no phishing or credential theft. The absence of a VDP/bug bounty program in large critical-infrastructure operators substantially delays disclosure timelines. |
| **Strategic Initiative** | MCRA: Identity Security + Cloud Security Posture Management (CSPM). Zero Trust: **Identity pillar** — explicit tenant segmentation; **Network/Perimeter** — API authorization validation beyond UI-layer controls. |
| **Call to Action** | (1) **Audit Entra tenant architecture**: verify that external-facing registration portals (partner, vendor, customer) provision identities into a **separate B2B/external Entra tenant**, not the production corporate tenant. (2) Review Guest User settings in Entra ID — restrict external collaboration to explicitly-invited users (Block all external identities as default). (3) Enable Entra ID Access Reviews for all Guest and External accounts quarterly. (4) Test your Entra API authorization independently of UI: use raw API calls to verify backend enforcement matches front-end access-denied responses. (5) Establish a Vulnerability Disclosure Policy (VDP) and register with CISA VDP Platform for responsible disclosure intake. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

---

### Insight 2

| Field | Content |
|-------|---------|
| **Title** | [Copilot 'SearchLeak' Attack Allows 1-Click Data Theft](https://www.darkreading.com/application-security/copilot-searchleak-attack-1-click-data-theft) |
| **Introduction** | Dark Reading's technical deep-dive on Varonis Threat Labs' SearchLeak research (CVE-2026-42824) explains how a novel AI-specific attack class — Parameter-to-Prompt Injection (P2P) — combined with classic web vulnerabilities (HTML injection and SSRF) turns Microsoft 365 Copilot Enterprise Search into a data exfiltration pipeline. The attack requires no target credentials or malware: an attacker embeds a malicious URL in any medium the target might click (phishing email, Teams message, SharePoint link), triggering Copilot to exfiltrate all indexed enterprise content to the attacker's server via the Bing image-search endpoint. Microsoft silently patched the vulnerability on 4 June 2026. |
| **Status** | Stay Informed |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Varonis Threat Labs (research/PoC); no attributed threat actor exploitation observed. **TTPs (attack model):** T1190 Exploit Public-Facing Application; T1566.002 Phishing: Spearphishing Link; T1567 Exfiltration Over Web Service (via Bing SSRF); T1059 Command and Scripting Interpreter (prompt injection as execution proxy). **Differentiator:** Prompt injection now constitutes a credible T1059-class execution technique within AI-augmented SaaS environments — with no traditional malware footprint. **Targets:** Enterprise M365 Copilot users; most valuable against C-suite, finance, legal, and HR roles with broad data access. **Region:** Global. |
| **Affected Cybersecurity Domain** | SaaS / AI Security / Phishing |
| **Risk** | Attack model bypasses all traditional endpoint security and email filtering — the malicious payload is a standard HTTPS URL served through Microsoft's own domain. Any future P2P injection vulnerability in AI Search tooling (including third-party Copilot plugins and Microsoft Graph connectors) carries equivalent risk. Data exfiltrated can include MFA recovery codes stored in email, M&A-sensitive documents, legal privileged communications, and source code. |
| **Strategic Initiative** | MCRA: SaaS Security + Application Security. Zero Trust: **Data pillar** — AI data access boundaries; **Applications pillar** — AI plugin/extension governance. |
| **Call to Action** | (1) Enforce Microsoft Purview **Sensitivity Labels** and **Data Loss Prevention (DLP)** policies to restrict Copilot indexing of Highly Confidential content. (2) Review the list of approved Copilot plugins and Microsoft Graph connectors — remove any that grant broader data access than required. (3) Enable **Defender for Cloud Apps** CASB integration to monitor and alert on anomalous Copilot data-access patterns. (4) Configure **Safe Links** for internal Teams messages and SharePoint links to add a click-time detonation layer. (5) Conduct red-team exercise: test whether your tenant's Copilot instance can be prompted to retrieve sensitive content via crafted URL parameters. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

---

## Source 4 — [BleepingComputer](https://www.bleepingcomputer.com/)

### Insight 1 — *(1-month fallback: May 2026)*

| Field | Content |
|-------|---------|
| **Title** | [FBI Warns of Kali365 Phishing Service Targeting Microsoft 365 Accounts](https://www.bleepingcomputer.com/news/security/fbi-warns-of-kali365-phishing-service-targeting-microsoft-365-accounts/) |
| **Introduction** | The FBI Internet Crime Complaint Center (IC3) issued advisory PSA260521 on 21 May 2026 warning of Kali365, a Telegram-distributed phishing-as-a-service platform active since April 2026 that provides even low-skill attackers with two M365-targeted attack modes: OAuth device code phishing and an AiTM "Cookie Link" mode. Kali365 features AI-generated phishing lures, automated campaign templates, real-time victim-tracking dashboards, and a structured operator model (admins, resellers, affiliates). The FBI explicitly recommends blocking device code authentication flows via Conditional Access policies to mitigate the most common attack mode. |
| **Status** | Assess |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Kali365 platform operators and affiliate network (financially motivated, multi-tier criminal business model). **TTPs:** T1566 Phishing (AI-generated lures); T1528 Steal Application Access Token (device code grant); T1539 Steal Web Session Cookie (AiTM Cookie Link mode); T1110.003 Password Spraying (fallback module). Kali365 combines device code OAuth abuse with an AiTM proxy mode, giving operators flexibility to choose the attack vector with highest success probability per target. **Targets:** M365 commercial and government tenants globally; finance, professional services, healthcare. **Regions:** Global distribution; primarily English-speaking markets identified in initial campaigns. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / BEC |
| **Risk** | Kali365 makes enterprise-grade MFA bypass accessible to low-skill affiliates at commodity pricing. The dual-mode (device code + AiTM) design ensures that tenants hardened against one technique remain vulnerable to the other unless both are addressed. Stolen OAuth tokens grant persistent M365 access (email, Teams, SharePoint, OneDrive) that persists through password resets. AiTM cookie-theft mode additionally captures authenticated session state, enabling immediate post-compromise action without token re-issuance. |
| **Strategic Initiative** | MCRA: Identity Security + Email Security. Zero Trust: **Identity pillar** — Conditional Access; phishing-resistant MFA (FIDO2/passkeys); token binding. |
| **Call to Action** | (1) **Immediately restrict or block Device Code authentication flow** in Entra ID Conditional Access (Grant → Block for non-kiosk scenarios). (2) Enforce **phishing-resistant MFA** (FIDO2 hardware keys, Windows Hello for Business, Entra passkeys) for all privileged roles and remote workers. (3) Audit Entra ID sign-in logs for successful Device Code authentications over the past 90 days; investigate any anomalous grant-to-usage gaps. (4) Configure **Entra ID Token Protection** for Exchange, SharePoint, and Teams. (5) Hunt for Kali365 infrastructure IOCs (IC3 PSA260521) in email gateway and proxy logs. (6) Review Microsoft Authenticator settings — disable number-matching fatigue vectors and enforce context-aware MFA approval. |
| **Source** | [BleepingComputer](https://www.bleepingcomputer.com/) |

---

### Insight 2 — *(1-month fallback: May 2026)*

| Field | Content |
|-------|---------|
| **Title** | [Microsoft Self-Service Password Reset Abused in Azure Data Theft Attacks](https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/) |
| **Introduction** | BleepingComputer reported Microsoft's disclosure of Storm-2949, a threat actor that converted a single SSPR social-engineering call into a multi-phase Azure cloud breach — exfiltrating thousands of OneDrive/SharePoint files and dozens of Azure Key Vault secrets (database credentials, connection strings, certificates) without deploying any malware. Storm-2949 impersonated IT support staff, persuaded targeted users to approve fraudulent MFA prompts, enrolled their own Microsoft Authenticator device, then methodically moved through Entra ID, Azure RBAC, and M365 using only legitimate platform APIs. The incident represents the archetypal "living-off-the-cloud" attack pattern and was disclosed by Microsoft Threat Intelligence on 18 May 2026. |
| **Status** | Assess |
| **Threat Actor incl. TTPs, Targets & Region** | **Actor:** Storm-2949 (Microsoft designation; developing group with sophisticated multi-layered capability; financial motivation assessed). **Full attack chain TTPs:** T1078.004 Valid Accounts: Cloud; T1656 Impersonation (IT support vishing); T1621 MFA Request Generation (fraudulent prompt); T1098.005 Account Manipulation: Device Registration; T1087.004 Account Discovery: Cloud; T1530 Data from Cloud Storage Object (OneDrive/SharePoint exfiltration); T1552.004 Unsecured Credentials: Private Keys (Key Vault); T1578 Modify Cloud Compute Infrastructure (VM Run Command); T1070.001 Clear Windows Event Logs; T1489 Service Stop (Defender tampering). **Targets:** Enterprise Azure/M365 tenants; financial services sector. **Regions:** Primarily English-speaking regions; specific geography not confirmed. |
| **Affected Cybersecurity Domain** | Identity & Access / Cloud Security / Data Exfiltration |
| **Risk** | Demonstrates that a single compromised Entra identity with Azure RBAC roles can yield: (a) full M365 data exfiltration via OneDrive/SharePoint, (b) Azure Key Vault credential harvesting enabling database and API access, (c) VM takeover via Run Command, (d) SQL firewall bypass for production database access. No endpoint compromise or traditional malware required — entirely invisible to endpoint-centric security tools. SSPR represents a broadly deployed but often under-governed identity recovery mechanism. |
| **Strategic Initiative** | MCRA: Identity Security + Cloud Security (CSPM/CIEM). Zero Trust: **Identity pillar** — SSPR governance, privileged access; **Cloud Infrastructure** — Azure RBAC least-privilege, Key Vault access controls. |
| **Call to Action** | (1) **Audit SSPR configuration**: enable SSPR only with two or more authentication methods; require phishing-resistant methods for reset. (2) Enforce **Privileged Identity Management (PIM)** for all Azure RBAC roles with `listKeys`, `publishxml`, and `runCommand` permissions — JIT access with approval workflow. (3) Enable **Microsoft Defender for Key Vault, Storage, and Resource Manager** to detect bulk secret enumeration and access policy changes. (4) Deploy **Conditional Access on SSPR registration** (since July 6, 2026, Entra ID evaluates CA for credential registration — ensure policy is in place). (5) Hunt in `CloudAuditEvents` and `CloudStorageAggregatedEvents` tables in Defender XDR Advanced Hunting for bulk OneDrive downloads and Key Vault access policy modifications. (6) Enable **immutable storage** on Azure Storage accounts containing backup/archive data. |
| **Source** | [BleepingComputer](https://www.bleepingcomputer.com/) |

---

## Source 5 — [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/)

### Insight 1

| Field | Content |
|-------|---------|
| **Title** | [AI Brands as Bait: How Threat Actors Are Using the AI Hype in Social Engineering](https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/) |
| **Introduction** | Microsoft Threat Intelligence identified Storm-3075 and Fox Tempest conducting multi-stage campaigns that exploit widespread AI interest — using fake ChatGPT and Claude-themed lures, malvertising on streaming sites, and SEO-poisoned GitHub repositories — to deliver code-signed malware and AiTM credential/token interception. Two distinct campaigns targeted 2,000+ organizations (62% US, 18% UK, 9% India); the malvertising component infected 66,000+ devices globally. Fox Tempest's malware-signing-as-a-service enables bypass of Windows SmartScreen and Defender at initial execution, before AiTM stages intercept M365 authentication tokens. |
| **Status** | Assess |
| **Threat Actor incl. TTPs, Targets & Region** | **Actors:** Storm-3075 (initial access broker, phishing/lure delivery); Fox Tempest (malware signing as a service — fraudulently obtained code-signing certificates enabling SmartScreen bypass). **TTPs:** T1566 Phishing (AI-themed lures); T1195.002 Supply Chain via SEO-poisoned GitHub repos; T1204.001 Malicious Link (malvertising); T1553.002 Code Signing (fraudulent certs); T1557 AiTM (final credential/token harvest); T1539 Steal Web Session Cookie. **Targets:** IT sector (56%), business services (21%), finance (8%). ChatGPT campaign: 97% South Africa, Switzerland, Austria (education/professional services). Claude campaign: 2,000+ orgs, 62% US/18% UK/9% India. Malvertising: Japan, South Africa, US, France (66,000+ devices). **Regions:** Global; concentrated in US, UK, South Africa, India. |
| **Affected Cybersecurity Domain** | Phishing / Identity & Access / Endpoint |
| **Risk** | AI-branded lures exploit a universal trust vector — employees across all departments interact with AI tools daily. AiTM final stage bypasses standard MFA to harvest both credentials and authenticated session tokens, enabling immediate M365 account takeover. Code-signing bypass defeats first-line executable controls. Malvertising on legitimate streaming sites reaches users outside corporate email filtering scope. Combined broker/tool-provider model lowers operational cost and scales attack volume. |
| **Strategic Initiative** | MCRA: Email Security + Endpoint Security + Identity Security. Zero Trust: **Identity pillar** — phishing-resistant MFA for all users; **Endpoints pillar** — tamper protection, ASR rules; **Applications** — Safe Links, Safe Attachments. |
| **Call to Action** | (1) Deploy **Safe Links** with URL detonation for all M365 users, including internal Teams messages. (2) Enable **Safe Attachments** with dynamic delivery and **Zero-Hour Auto Purge (ZAP)** to retroactively pull AI-lure phishing emails. (3) Enforce **phishing-resistant MFA** (Entra passkeys, Windows Hello for Business, FIDO2) for all users — standard SMS/TOTP/app-push MFA does not stop AiTM. (4) Enable **Entra ID Protection** risk-based Conditional Access: require step-up MFA or block sign-in on medium/high-risk sign-in events. (5) Deploy **Attack Surface Reduction (ASR) rules** on all endpoints targeting malicious code-signed executables. (6) Enable **Microsoft Defender SmartScreen** with enhanced protection mode on all managed browsers. (7) Hunt for Storm-3075 IOCs (Microsoft MSTIC blog) in Defender XDR email and endpoint telemetry. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

---

### Insight 2

| Field | Content |
|-------|---------|
| **Title** | [StealC and Amadey: Breaking Down Infostealers and the Cybercrime Services That Deliver Them](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/) |
| **Introduction** | Microsoft's Digital Crimes Unit (DCU) facilitated takedown actions on 24 June 2026 against the infrastructure supporting the StealC and Amadey malware distribution network. StealC, an advanced credential harvester, targets browser-stored passwords and session cookies (including M365 OAuth tokens and Entra ID SSO tokens) across Chromium, Firefox, Outlook, and WinSCP. Amadey acts as a modular loader delivering StealC as a second-stage payload, with both families deployed via ClickFix social engineering, SEO poisoning, phishing, and malvertising. The critical finding: a single home-PC compromise yields corporate VPN credentials, SSO tokens, and session cookies that bypass enterprise MFA — creating a direct personal-to-enterprise threat bridge. |
| **Status** | Stay Informed |
| **Threat Actor incl. TTPs, Targets & Region** | **Actors:** Financially motivated cybercriminals; commodity MaaS (Malware-as-a-Service) model — no single attributed APT, multiple operators. **TTPs:** T1056.001 Input Capture: Keylogging; T1539 Steal Web Session Cookie; T1555.003 Credentials from Web Browsers; T1053.005 Scheduled Task (persistence); T1055 Process Injection; T1566 Phishing (ClickFix social engineering); T1036.005 Masquerading. StealC uses RC4 encryption for C2; both families deployed in two-stage chain (Amadey loader → StealC payload). **Targets:** Consumers and enterprise employees on personal or work devices; crypto wallet holders; gaming platform users (Steam). **Regions:** Global. |
| **Affected Cybersecurity Domain** | Endpoint / Identity & Access / Phishing |
| **Risk** | Stolen Entra ID SSO tokens and browser-cached M365 session cookies bypass MFA entirely and provide immediate cloud access equivalent to an authenticated session. Attackers need no corporate network access — a single compromised home PC used for M365 access via browser serves as the pivot. "A single working account can unlock many enterprise systems at once" (Microsoft DCU). Perpetual credential refresh cycles mean SSO token theft has impact measured in weeks, not hours. |
| **Strategic Initiative** | MCRA: Endpoint Security + Identity Security + Zero Trust: **Endpoints pillar** (device compliance, EDR); **Identity pillar** (token protection, continuous access evaluation). |
| **Call to Action** | (1) Enable **Entra ID Continuous Access Evaluation (CAE)** to enforce near-real-time token revocation on policy changes, user risk elevation, or IP anomalies. (2) Enable **Entra ID Token Protection** (sign-in session binding) for Exchange Online, SharePoint, and Teams — forces re-authentication when token is used from a different device. (3) Deploy **Microsoft Defender for Endpoint** with cloud-delivered protection and tamper protection enabled on all corporate devices; extend to BYOD via Intune MAM. (4) Enable **Attack Surface Reduction rules** targeting malicious ClickFix-style LOLBin execution (e.g., Block process creations originating from WScript/CScript). (5) Hunt for StealC/Amadey IOCs in Defender XDR `DeviceProcessEvents` and `DeviceNetworkEvents` tables (Microsoft blog includes YARA rules and C2 patterns). (6) Enforce **Conditional Access device compliance** requiring managed/compliant device for all M365 access — restrict access from unmanaged personal devices to Microsoft Authenticator app-based access only. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

---

## Appendix: Key Threat Indicators & Platform Mapping

| Threat | MITRE ATT&CK Key TTPs | Defender XDR Detection Surface | Zero Trust Pillar |
|--------|----------------------|-------------------------------|-------------------|
| SearchLeak / CVE-2026-42824 | T1190, T1537, T1059 | Defender for Cloud Apps, Unified Audit Log | Data |
| EvilTokens / Device Code PhaaS | T1078, T1550.001, T1534 | Entra ID Sign-in Logs, Defender for Identity | Identity |
| Storm-3075 / Fox Tempest AI lures | T1566, T1557, T1553.002 | Defender for O365, Defender for Endpoint | Identity + Endpoints |
| Kali365 PhaaS (FBI PSA260521) | T1528, T1539, T1110.003 | Entra ID Sign-in Logs, Defender for O365 | Identity |
| Storm-2949 SSPR abuse | T1078.004, T1098.005, T1530, T1552.004 | Defender for Identity, Defender for Cloud | Identity + Cloud |
| FIFA Entra misconfiguration | T1078.004, T1538, T1530 | Entra ID Access Reviews, CSPM | Identity |
| StealC / Amadey | T1539, T1555.003, T1053.005 | Defender for Endpoint, MDE IOC list | Endpoints + Identity |
| Sapphire Sleet npm supply chain | T1195.002, T1552.001, T1059.001 | Defender for Cloud, GitHub Advanced Security | Applications |

---

*Report generated automatically on 2026-07-01 by the Delphi scheduled routine. Target month: June 2026. Sources checked: The Hacker News, Ars Technica (inaccessible — see note), Dark Reading, BleepingComputer, Microsoft Threat Intelligence. Fallback articles labelled inline.*

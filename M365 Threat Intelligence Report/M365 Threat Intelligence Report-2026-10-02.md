---
layout:
  width: wide
---

# M365 Threat Intelligence Report — September 2026

**Report Date:** 2026-10-02 (Europe/Stockholm)
**Reporting Window:** 2026-09-01–2026-09-30
**Audience:** Security architects · SOC leads · cyber leadership

## Executive summary

September's strongest signal is identity compromise as an end-to-end service: phishing kits and threat clusters target Microsoft 365 sessions, abuse device-code authentication or AiTM proxies, and then use mailbox and cloud data to drive fraud or extortion. Separate reporting shows that compromised Azure service principals can enable rapid destruction of cloud resources. The defensive priority is to correlate identity, app, endpoint and data activity; restrict and monitor OAuth grants and workload identities; and make recovery controls resilient to privileged credential compromise.

The 10 selected items below were published in September 2026. The Microsoft passkey investigation describes activity observed since May; it is included because its September publication adds current operational detail, not because the activity began in September. Analyst mappings to MCRA and Zero Trust are recommendations based on each article's described behavior. ATT&CK techniques are named only where the source or observed behavior supports them.

## 1. [The Hacker News](https://thehackernews.com/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [US-Focused CSuite Phishing Steals Microsoft 365 Sessions and Deploys RMM Tools for Remote Access](https://thehackernews.com/2026/09/us-focused-csuite-phishing-steals.html) — published 2026-09-30 |
| **Introduction** | ANY.RUN traced a phishing campaign across 351 sandbox submissions. Lures can lead either to Microsoft 365 credential/device-code session theft or installation of legitimate remote-management tools, linking cloud identity compromise with endpoint persistence. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | CSuite campaign; credential harvesting/device-code phishing and BAT/VBS delivery of ScreenConnect or Action1. 51% of sampled submissions came from the US; activity also appeared in India, the UK, Canada, Australia and elsewhere. Technology, manufacturing, government and consulting were prominent in the sample. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / Endpoint |
| **Risk** | A stolen session can expose Exchange Online and support BEC; RMM installation can preserve endpoint access and widen incident scope. The article's sandbox sample does not establish prevalence across all organizations. |
| **Strategic Initiative** | Analyst alignment: MCRA Identity, Threat Protection and SecOps; Zero Trust Identity, Device and Visibility & Analytics. Correlate sign-in/session events with endpoint software installation and suspicious script execution. |
| **Call to Action** | Hunt device-code sign-ins and unusual session behavior alongside new or unapproved RMM deployments. Restrict device-code flow where it is not needed, use phishing-resistant authentication, and investigate mailbox and endpoint activity as one incident. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks](https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html) — published 2026-09-07 |
| **Introduction** | Arctic Wolf tracks PREY-0058 activity using help-desk impersonation, AiTM token theft and residential-proxy sign-ins against executives and SaaS accounts. The report describes subsequent data theft and extortion, with overlap in tradecraft—not confirmed identity—with UNC6671. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | PREY-0058; help-desk vishing, AiTM token theft and proxy-based access. Directors, VPs and other executives are emphasized. Attribution/relationship to UNC6671 is reported as tradecraft similarity; do not treat as confirmed common operators. |
| **Affected Cybersecurity Domain** | Identity & Access / Social Engineering / SaaS / Data Protection |
| **Risk** | Valid session access to M365 and connected SaaS can expose executive communications and files, enable impersonation, and support extortion. Residential proxies can make location-based review less reliable. |
| **Strategic Initiative** | Analyst alignment: MCRA Identity, Data Protection, Threat Protection and SecOps; Zero Trust Identity, Application, Data and Visibility & Analytics. Strengthen help-desk identity verification and detect session use across SaaS. |
| **Call to Action** | Require a trusted verification channel for help-desk authentication changes. Review new authentication methods, token/session anomalies, mailbox access and SaaS downloads after suspicious sign-ins; revoke sessions and credentials when compromise is confirmed. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

## 2. [Ars Technica — Security](https://arstechnica.com/security/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [Microsoft disrupts AI-assisted platform that compromised 12,000 accounts](https://arstechnica.com/security/2026/09/microsoft-disrupts-ai-assisted-platform-that-compromised-12000/) — published 2026-09-22 |
| **Introduction** | EvilTokens automated device-code phishing and post-compromise inbox analysis. Microsoft reported 12,000 compromised accounts across 10,000 organizations; the service used AI to identify valuable contacts and support BEC. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | EvilTokens PhaaS operators/users; phishing followed by abuse of the legitimate OAuth device authorization flow, then inbox analysis and tailored payment-fraud lures. Microsoft reported global victims, with the largest concentration in the US. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / BEC / SaaS |
| **Risk** | Device-code authorization can yield an attacker-controlled authenticated session without conventional password capture. Inbox access reveals payment workflows and trusted relationships, increasing BEC and data exposure risk. Microsoft seized infrastructure; that does not establish that every previously compromised session was remediated. |
| **Strategic Initiative** | Analyst alignment: MCRA Identity, Threat Protection, SIEM+XDR and SecOps; Zero Trust Identity, Application, Data and Visibility & Analytics. Treat device authorization and post-authentication mailbox behavior as one detection chain. |
| **Call to Action** | Disable or condition device-code authentication where operationally feasible. Investigate device-code sign-ins, new device/authentication registrations, inbox rules and unusual mailbox search/download activity; revoke active sessions and verify payment changes out of band. |
| **Source** | [Ars Technica — Security](https://arstechnica.com/security/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [Attackers have been exploiting critical Zimbra flaw to steal emails](https://arstechnica.com/security/2026/09/attackers-have-been-exploiting-critical-zimbra-flaw-to-steal-emails/) — published 2026-09-30 |
| **Introduction** | Microsoft reported exploitation of Zimbra Collaboration Suite CVE-2026-73570, which can permit unauthenticated command execution under specific configuration conditions. Observed activity included web shells, mailbox/authentication data collection and attempted transfer. This is relevant to M365 chiefly where Zimbra remains in a hybrid or connected mail estate. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | Microsoft did not attribute the activity. Exploitation requires the optional `zimbra-snmp` package and enabled SNMP notifications; observed follow-on behavior included web shells, reverse shells, privilege escalation and email archive creation. |
| **Affected Cybersecurity Domain** | Email Security / Vulnerability Management / Hybrid Cloud |
| **Risk** | A compromised adjacent mail server may expose credentials and correspondence or provide an attacker a foothold into connected identity and collaboration workflows. The article does not report compromise of Exchange Online or Entra ID. |
| **Strategic Initiative** | Analyst alignment: MCRA Threat Protection, Identity and Data Protection; Zero Trust Application, Data and Visibility & Analytics. Maintain asset ownership and telemetry for non-Microsoft mail systems that exchange data with M365. |
| **Call to Action** | For Zimbra operators, verify the vendor-fixed version and whether the vulnerable package/configuration is present; investigate web shells, reverse shells and mailbox archive activity. In hybrid estates, rotate potentially exposed credentials and review associated Entra sign-ins and mail-flow integrations. |
| **Source** | [Ars Technica — Security](https://arstechnica.com/security/) |

## 3. [Dark Reading](https://www.darkreading.com/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [Microsoft Disrupts EvilTokens Device Code Phishing Service](https://www.darkreading.com/identity-access-management-security/microsoft-disrupts-eviltokens-device-code-phishing-service) — published 2026-09-22 |
| **Introduction** | EvilTokens packaged device-code phishing into a PhaaS product, including AI-assisted lure creation and inbox analysis. Microsoft said the service compromised more than 12,000 inboxes in over 10,000 organizations and disrupted its infrastructure with partners. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | EvilTokens PhaaS users; lures prompt victims to enter a live device code at Microsoft's legitimate login portal, authorizing an attacker session. High-value targeting and post-compromise assistance were built into the service. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / BEC |
| **Risk** | Users may believe they are completing a normal sign-in while authorizing another party's session. Inbox access enables fraud and sensitive-data discovery; disruption of infrastructure does not by itself revoke extant sessions. |
| **Strategic Initiative** | Analyst alignment: MCRA Identity, Threat Protection and SecOps; Zero Trust Identity, Application and Visibility & Analytics. Monitor authentication flow and subsequent SaaS actions rather than relying solely on domain reputation. |
| **Call to Action** | Review device-code sign-in policy and conditional access; alert on unexpected device authorization and follow-on mailbox rules, app registrations or bulk access. For suspected compromise, revoke sessions and inspect mailbox and payment-change activity. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [MFA Won't Save You From OAuth Consent Abuse](https://www.darkreading.com/vulnerabilities-threats/mfa-oauth-consent-abuse) — published 2026-09-18; opinion article |
| **Introduction** | The author argues that MFA does not govern what an authenticated user can authorize. A deceptive OAuth consent can grant an application continuing API access, depending on provider policy, app type and scopes. This is general SaaS guidance, not a report of a specific M365 campaign. |
| **Status** | Educate |
| **Threat Actor including TTPs, Targets & Region** | No actor or campaign is identified. Described path: lure to a legitimate OAuth authorization flow, user grants excessive permissions, then attacker accesses data through the app's approved API permissions. |
| **Affected Cybersecurity Domain** | Identity & Access / SaaS / Data Protection |
| **Risk** | Excessive or unreviewed app grants can enable persistent email, file or workflow access even when interactive sign-in has satisfied MFA. Scope and persistence depend on the grant and tenant controls. |
| **Strategic Initiative** | Analyst alignment: MCRA Identity, Data Protection and SecOps; Zero Trust Identity, Application, Data and Visibility & Analytics. Apply least privilege and governance to delegated and application permissions. |
| **Call to Action** | Restrict user consent to vetted publishers/permissions; require admin review for high-impact scopes. Inventory enterprise app grants, monitor new consent and unusual API activity, and revoke grants/tokens when unauthorized access is found. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

## 4. [BleepingComputer](https://bleepingcomputer.com/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [BigBear Microsoft 365 phishing service bypassed MFA at 258 organizations](https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/) — published 2026-09-07 |
| **Introduction** | CloudSEK reported that BigBear 2.0 used an Evilginx2-based AiTM proxy to capture passwords and authenticated session cookies. Its research said 258 organizations had at least one completed MFA-bypass compromise; the panel had collected thousands of credentials and cookies. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | BigBear 2.0 PhaaS and affiliate operators; AiTM proxy, session-cookie replay, geo-matched residential proxies, and JavaScript interference with FIDO2/WebAuthn in the observed setup. CloudSEK's report is the underlying research; counts reflect its observed dataset. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / SaaS |
| **Risk** | Captured session cookies can permit account access after the user completes MFA, exposing Exchange, SharePoint, OneDrive and connected SSO apps. The reported numbers should not be interpreted as a complete census of victims. |
| **Strategic Initiative** | Analyst alignment: MCRA Identity, Threat Protection, SIEM+XDR and SecOps; Zero Trust Identity, Device and Visibility & Analytics. Use phishing-resistant authentication and session-aware detection. |
| **Call to Action** | Prefer phishing-resistant MFA; investigate suspicious session/token use and unfamiliar devices even after MFA success. Review sign-in risk, revoke sessions after suspected AiTM compromise, and assess whether users can be redirected to weaker methods. |
| **Source** | [BleepingComputer](https://bleepingcomputer.com/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [JadePuffer agentic AI attacks target Azure, destroy cloud resources](https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-ai-attacks-target-azure-destroy-cloud-resources/) — published 2026-09-28 |
| **Introduction** | Microsoft observed JadePuffer/Storm-3168 using compromised service principals for Azure discovery, credential collection and destructive operations. One sequence attempted to delete more than 100 storage accounts and also targeted Key Vaults, databases, Function Apps, VMs and App Services. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | JadePuffer, tracked by Microsoft as Storm-3168; compromised workload identities, resource enumeration, key collection and rapid destructive API operations. Microsoft observed two attacks in June; September is the report date, not the incident date. |
| **Affected Cybersecurity Domain** | Cloud Infrastructure / Identity & Access / Data Protection |
| **Risk** | Overprivileged service principals can enable fast deletion of data and workloads and tampering with recovery safeguards. Resource locks and storage deletion protection prevented some deletions in the reported case. |
| **Strategic Initiative** | Analyst alignment: MCRA Identity, Threat Protection, SIEM+XDR and Data Protection; Zero Trust Identity, Application, Data and Visibility & Analytics. Treat workload identities and recovery controls as security-critical assets. |
| **Call to Action** | Inventory service principals, rotate exposed secrets and reduce permissions to task scope. Alert on unusual enumeration, key retrieval, bulk deletion and attempts to alter recovery locks; protect backups with independent deletion safeguards and test restoration. |
| **Source** | [BleepingComputer](https://bleepingcomputer.com/) |

## 5. [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/) — published 2026-09-09 |
| **Introduction** | Microsoft describes help-desk impersonation and passkey/SSO-themed lures followed by suspicious sign-ins, attacker-added authentication methods, Microsoft Graph reconnaissance, SharePoint/OneDrive downloads and mailbox collection. Microsoft says activity has been observed since May 2026. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | Microsoft associates activity with several actors, including Storm-3121 and Storm-3032, while noting multiple operators in the ecosystem. TTPs include identity social engineering, cloud-account use, MFA-method registration, Graph discovery, cloud storage collection and email collection. Microsoft lists ATT&CK mappings including T1078.004, T1556.006, T1087.004, T1530 and T1114. |
| **Affected Cybersecurity Domain** | Identity & Access / Social Engineering / SaaS / Data Exfiltration |
| **Risk** | An initial identity compromise can become durable through new authentication methods, then expose tenant structure, SharePoint/OneDrive content and mailbox data across accounts. |
| **Strategic Initiative** | MCRA: Identity, Threat Protection, SIEM+XDR, Data Protection and SecOps; Zero Trust: Identity, Device, Application, Data and Visibility & Analytics. This is analyst alignment to Microsoft's described cross-service sequence. |
| **Call to Action** | Correlate anomalous sign-ins with new authentication-method/device registration, Graph enumeration, token issuance and bulk SharePoint/OneDrive or mailbox activity. Validate new methods with users, remove unauthorized ones, revoke sessions and investigate the full identity-to-data sequence. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/) — published 2026-09-25 |
| **Introduction** | Microsoft's investigation details Azure resource destruction and credential collection using two compromised service principals. A seven-minute destructive sequence followed extended resource discovery; resource locks and deletion protection blocked some actions. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | JADEPUFFER, tracked by Microsoft as Storm-3168. Compromised service principals performed Azure resource discovery, credential/key collection and destructive operations against storage, databases, Key Vaults, VMs, Function Apps and App Services. Reported activity occurred in early June 2026. |
| **Affected Cybersecurity Domain** | Cloud Infrastructure / Workload Identity / Data Protection |
| **Risk** | A compromised workload identity with broad permissions can destroy production resources and weaken recovery options at machine speed. Exposed credentials may remain usable until revoked or rotated. |
| **Strategic Initiative** | MCRA: Identity, Threat Protection, SIEM+XDR, Data Protection and SecOps; Zero Trust: Identity, Application, Data and Visibility & Analytics. Apply least privilege to nonhuman identities and separate recovery authority. |
| **Call to Action** | Protect workload secrets, review service-principal owners and permissions, and rotate credentials following exposure. Monitor unusual API enumeration and deletion bursts; use resource locks and independent recovery safeguards, and verify Defender for Cloud coverage relevant to the workload. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

## Source limitations and coverage

- All selected articles were published in September 2026 and their original pages were fetched. The report uses public reporting only; no tenant-specific telemetry or private indicators were available.
- Several outlets report on the same Microsoft disclosures (EvilTokens, Storm-3168). These are multiple publications of overlapping underlying events, not independent confirmations of every detail.
- Microsoft passkey and Storm-3168 articles were published in September but describe activity observed since May and June, respectively. Publication date and incident date are kept distinct.
- Ars Technica's Zimbra story is adjacent rather than direct M365 threat reporting. Its relevance is limited to organizations operating Zimbra alongside or connected to M365; the cited article does not report Exchange Online or Entra compromise.
- Dark Reading's OAuth consent piece is explicitly opinion, not incident reporting. It supports governance advice but no actor attribution or campaign claim.
- Vendor and researcher counts (including ANY.RUN sandbox samples and CloudSEK's BigBear dataset) reflect their stated collection and should not be generalized to total prevalence. Threat attribution is included only as the cited source presents it.

---

*Prepared 2026-10-02 for the September 2026 reporting window. Findings are based on the linked public sources; validate applicability against local configuration and telemetry.*

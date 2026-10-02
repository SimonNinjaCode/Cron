---
layout:
  width: wide
---

# Microsoft AI Brief — 12 August 2026

*Enterprise coverage of Microsoft AI developments. This edition covers the seven days to 12 August 2026.*

---

## Security & Safety

### Defender for Office 365 Now Blocks Prompt Injection Attacks in Email

Microsoft has added prompt injection protection to Defender for Office 365, targeting a class of attack that has grown alongside enterprise AI adoption. The protection detects and blocks malicious instructions embedded in email content — instructions crafted to manipulate Copilot or other AI assistants into exfiltrating data from a user's mailbox or SharePoint environment, exposing system prompts, or running unauthorised workflows.

When a high-confidence threat is detected, the email is quarantined before any AI-powered workflow can process it. It appears in investigation dashboards under a new detection technology label, "Prompt Injection Protection," and is classified as High Confidence Phish. Admins do not need to create new policies: the protection slots into existing pipeline checks.

The feature has been enabled by default for Defender for Office 365 Plan 2 and Microsoft 365 E5 tenants since early July. Worldwide general availability is expected to complete in early September 2026.

**Action required:** Verify that your Defender for Office 365 Plan 2 or E5 tenants have received the feature. Security teams should update incident response runbooks to account for the new "Prompt Injection Protection" detection technology label. Threat hunting queries that filter on detection categories will need updating.

---

### Domain Exclusion for M365 Copilot: Launched and Pulled Within Days

Microsoft announced Domain Exclusion for Microsoft 365 Copilot in late July — a control that would have let administrators block up to 1,000 web domains from influencing Copilot's web-grounded responses, uploaded via a CSV file through PowerShell. Four days after rollout, on 4 August, Microsoft quietly pulled the feature. No explanation was given publicly. The only statement: "We understand the importance of this capability and are actively evaluating next steps."

The abrupt withdrawal left IT administrators who had already begun building exclusion lists without the promised control. A common response in the community was that an allowlist approach — specifying permitted sources rather than blocked ones — would be more practical at scale.

**What this means:** Organisations that were relying on Domain Exclusion for Copilot governance have no equivalent control today. Microsoft has not committed to a revised timeline. Admins planning web-grounding guardrails should treat this capability as unavailable until a replacement announcement appears in the Microsoft 365 Message Center.

---

### Microsoft Defender Threat Intelligence Standalone SKU Retired

As of 1 August 2026, Microsoft retired the standalone Microsoft Defender Threat Intelligence (MDTI) SKU. All MDTI capabilities are now available at no additional cost through the Microsoft Defender portal to any customer with a Microsoft Defender or Microsoft Sentinel subscription.

**Action required:** If procurement or licensing records include a separate MDTI line item, update those records. Any workflows or playbooks that referenced MDTI as a separately-billable service should be reviewed, and teams should confirm access is intact through the portal.

---

## Enterprise Platform

### Multi-Tenant Agent Management Enters Public Preview

As of 10 August, administrators can manage agents across multiple customer or subsidiary tenants from a single experience in the Microsoft 365 admin centre. The feature is in public preview and targets CSP partners operating under Granular Delegated Admin Privileges (GDAP), though it applies equally to enterprises with subsidiary tenants.

From one pane, admins can view a consolidated agent inventory, install or block agents across eligible tenants, and switch directly into a governed tenant without signing out. Risk and activity insights per tenant require an Agent 365 licence assigned to the end user.

**Action required:** CSP partners and multi-tenant enterprise admins should explore the feature in the M365 admin centre now. Those who want agent-level risk visibility should confirm Agent 365 licences are assigned to relevant users before the feature reaches general availability.

---

### OpenAI Now Listed as Subprocessor in M365 Copilot — Auto-Enabled on 24 July

A change that went live on 24 July deserves attention for any organisation with data residency or subprocessor-consent requirements. OpenAI-operated models now run under OpenAI as a formal Microsoft 365 Copilot subprocessor. The admin toggle to permit this was auto-enabled on 24 July for all tenants where it had not already been explicitly set to "No users."

**Action required:** Data protection and legal teams should review whether this subprocessor relationship requires updates to privacy notices, data processing agreements, or records of processing activities. Admins can verify the toggle state in the Microsoft 365 admin centre under Copilot settings.

---

### M365 Copilot Platform Updates: Authoritative Sites, AEM Integration, Anthropic in Word

The 11 August release notes for Microsoft 365 Copilot carry several items that require admin attention.

SharePoint Authoritative Sites is now available for Windows and web. Admins can designate specific SharePoint sites as trusted, high-quality sources — policies, company news, procedure documents — so Copilot Search prioritises them over general content. This needs to be configured in the SharePoint admin centre; it does not activate automatically.

Adobe Experience Manager (AEM) asset libraries can now be connected to Microsoft 365 so Copilot in PowerPoint draws on enterprise image libraries when building presentations. This is an opt-in integration requiring setup work to link the AEM instance.

In Word on the web, users can now choose Anthropic models alongside OpenAI models for editing tasks — the first appearance of model selection at the document-editing layer in core M365 apps.

A Viva Insights consumption dashboard now tracks credit usage for Cowork and WorkIQ APIs. It requires usage-based billing to be configured in Cost Management and is scoped to managers with five or more direct reports, Insights analysts, and global admins.

**Action required:** SharePoint admins should audit and mark authoritative sites. Organisations using AEM should plan the connector setup. Data teams should configure Cost Management billing for WorkIQ/Cowork if they intend to use the usage dashboard.

---

### Microsoft 365 E7 Promotional Pricing Expires 1 October

Partners and enterprise procurement teams have a deadline: Microsoft 365 E7 promotional discounts — currently at 10–15% off for one- and three-year terms — expire on 30 September 2026. No new promotional transactions on E7 will be available from 1 October. Microsoft 365 E3 promotions, by contrast, have been extended through 31 December 2026.

**Action required:** Any active E7 opportunities in the pipeline should close before 30 September. Procurement teams that planned to consolidate Copilot, Agent 365, and advanced governance under E7 at a discount will need to move quickly.

---

## Agentic AI

### Copilot Cowork Now Generally Available Worldwide

Copilot Cowork, Microsoft's agentic system for multi-step task execution, reached general availability for commercial customers globally as part of the June 2026 M365 Copilot update. Users define the task; Cowork plans and carries it out end-to-end, including complex cross-application workflows like project tracking and resource allocation using internal organisational data.

Usage costs are tracked against Copilot Credits (the renamed message packs in Copilot Studio) and are now visible through the Viva Insights consumption dashboard described above.

---

### Azure Copilot Replaces Combined Agent Mode with Named Agents and Admin Center

From 1 August 2026, Microsoft retired the single "Agent mode" experience in Azure Copilot, replacing it with a roster of individually named, purpose-built agents. The Observability Agent is now generally available. Four agents — Deployment, Troubleshooting, Optimisation, and Resiliency — remain in public preview, with a Migration Agent also in preview.

A new Azure Copilot Admin Centre gives administrators direct control to enable or disable individual agents per tenant. The previous allowlisting process used to gate access has been removed entirely.

**Action required:** Azure platform teams should review which agents are enabled in the admin centre and confirm they match intended scope. Any processes built around the old combined agent mode should be tested against the named-agent structure.

---

## Infrastructure

### Microsoft Caps Internal Engineer Token Budgets — A Signal for Enterprise AI Cost Planning

An internal memo from Microsoft EVP Jay Parikh, circulated around 5 August, told engineering teams that maximising token consumption is not a performance measure. Microsoft is assigning per-division AI token budgets, setting GPT-5.6 (a cheaper model tier) as the default for internal tooling, and giving individual engineers a dashboard to monitor their own spending.

The move comes as Microsoft engineers reportedly spend anywhere from hundreds to several thousands of dollars monthly in tokens. The programme frames the change around business outcomes rather than usage volume.

This is relevant to enterprise customers for two reasons. First, it signals that AI infrastructure cost is a genuine management challenge even inside Microsoft, and that governance tooling (dashboards, budgets, default model tiers) is how the industry will address it. Second, it suggests enterprises running large Copilot or Azure OpenAI deployments should be instrumenting their own token usage now — ahead of the point where it becomes a board-level line item.

---

### Microsoft 365 Copilot Closes FY26 at 30 Million Paid Seats

Microsoft closed its fiscal year 2026 with over 30 million paid Microsoft 365 Copilot seats, with net additions more than doubling quarter over quarter and customers with 50,000 or more seats up more than seven times year over year. Azure revenue surpassed $100 billion annually for the first time.

---

## Developer Tools

### Microsoft Agent Framework 1.0 GA; Foundry Hosted Agents in Preview Across 20 Regions

The Microsoft Agent Framework (MAF) reached 1.0 general availability on 2 April 2026, consolidating AutoGen and Semantic Kernel into a single supported SDK and runtime for .NET and Python. Foundry Hosted Agents — Microsoft's managed execution environment for production AI agents combining identity, memory, security, and observability — are in public preview across 20 Azure regions globally.

Enterprises building custom agents on Azure have a stable, supported platform to target. Teams still on AutoGen or standalone Semantic Kernel should plan migration to MAF to stay on a supported path.

---

## Dates to Watch

| Date | What |
|------|------|
| Early September 2026 | Defender for Office 365 prompt injection protection reaches worldwide GA |
| 3 September 2026 | Windows 365 Frontline SKU renamed to Windows 365 Flex (branding only, no functionality change) |
| 30 September 2026 | Microsoft 365 E7 promotional discounts expire |
| 31 December 2026 | Microsoft 365 E3 promotional discounts expire; Purview Suite for Business Premium 50% offer ends |

---

*Sources: Microsoft 365 Copilot release notes (learn.microsoft.com, 11 Aug 2026); Partner Center announcements August 2026 (learn.microsoft.com); The Register (theregister.com, 5–6 Aug 2026); Neowin, Petri, Heise Online (Domain Exclusion, Aug 2026); CybersecurityNews, Office365ITPros (prompt injection, Aug 2026); Slashdot, AI Weekly (token budgets, Aug 2026); TechCommunity Microsoft (Security Copilot, Defender, monthly news Aug 2026); Petri.com (Copilot Cowork GA, E7 plan, DLP); Regroove.ca (Azure Copilot agents, Aug 2026).*

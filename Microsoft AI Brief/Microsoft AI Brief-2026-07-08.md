# Microsoft AI Brief
### 8 July 2026 | Coverage: 1–8 July 2026

Microsoft announced this week that it will consolidate every consumer and enterprise Copilot product into a single unified app by August 2026 — a strategic reset triggered by data showing fewer than 4.5% of its 450 million commercial Microsoft 365 customers actually pay for Copilot features, and that among those who do, only 20–30% use it weekly. The announcement, which came via a 1,200-word internal memo from Executive Vice President Jacob Andreou leaked on 3 July, frames the rebuild as the product needing to "earn the right to exist."

---

## Security & Safety

### Dynamic Threat Detection Agent: Free Ride Ending, SCU Billing Imminent

Microsoft's Dynamic Threat Detection Agent for Security Copilot has been in public preview since early 2026 at no cost. That changes at general availability — expected this month — when the agent transitions to the Security Copilot SCU (Security Compute Unit) consumption model. From that point, every query the agent runs draws down SCU capacity.

The agent operates continuously in the background across Microsoft Defender and Microsoft Sentinel, correlating alerts, events, anomalies, and threat intelligence to surface false negatives that rule-based detections miss. In tests, it has been positioned as an antidote to alert fatigue: rather than generating more alerts, it re-ranks and re-investigates existing signal to find threats that slipped through.

**Action required.** Security teams should audit their current SCU allocation before GA lands. Organisations that activated the agent during preview and intend to keep it running need to confirm they hold enough capacity — or a Security Copilot subscription that covers it. Admins who prefer to evaluate cost before committing can disable the agent from the Defender portal.

### Security Analyst Agent and the 70-Partner Ecosystem

Also reaching enterprise teams this month is the Security Analyst Agent, which Microsoft describes as capable of ingesting up to approximately 100 MB of security telemetry per investigation. It performs multi-step analysis across Defender and Sentinel data, surfaces anomalies and hidden risks, and delivers a prioritised findings report rather than a stream of raw alerts. This fits into a broader expansion of Security Copilot's agentic surface: the Security Triage Agent now covers identity and cloud alerts in addition to endpoint, and the Security Store lists more than 70 partner-built agents that connect additional data sources and investigation workflows to the platform.

For SOC teams already running Defender XDR, the integration is native. For those evaluating the ROI before committing, Microsoft has published a per-agent consumption breakdown in the admin portal.

### AI-Generated Content Watermarks Now Live in Microsoft 365

Between 17 June and 1 July, Microsoft activated watermarking for AI-generated and AI-altered content across Microsoft 365 Copilot on Windows, Mac, iOS, Android, and web. The feature is on by default and does not require admin configuration. Content produced or substantially modified by Copilot carries a metadata marker that is preserved through most export and sharing workflows.

For compliance and legal teams, this has immediate relevance: documents and outputs submitted as human-authored work can now be checked against the watermark. It also matters for organisations running Communication Compliance policies that cover AI-generated content.

---

## Enterprise Platform

### M365 Copilot Pricing Restructured: New SKUs Live as of 1 July

Several pricing changes took effect this week that IT and procurement teams should verify against current agreements.

For **business-tier** customers, two new permanent SKUs replace earlier promotional bundles: Microsoft 365 Business Standard with Copilot is now $23.50 per user per month, and Microsoft 365 Business Premium with Copilot is $32 per user per month. These are not add-ons but integrated plans. Separately, the standalone Copilot Business add-on — previously available at a promotional $18 per user per month through 30 June — moved to $21 per user per month on 1 July.

Base plan prices also increased: Microsoft 365 Business Basic rose from $6 to $7 (16%), and Business Standard from $12.50 to $14 (12%). Business Premium holds at $22. The **enterprise** standalone Copilot add-on remains at $30 per user per month on top of a qualifying E3/E5 base plan.

**Action required.** Organisations mid-renewal cycle or on month-to-month terms should reconcile invoices against the new rates. Partners buying through CSP have updated price lists in Partner Center effective this month.

### The Copilot App Merger: What IT Teams Need to Plan For

The July 3 Andreou memo confirms that by August 2026 Microsoft will ship a single Copilot application that unifies GitHub Copilot, Copilot Chat, Copilot Cowork, and a new paid agentic layer called AutoPilot. A handful of features that failed to gain traction — Copilot Podcasts and Copilot Labs among them — will be retired.

For enterprise IT, the immediate implications are endpoint management and identity. A unified app means a single deployment package, but also a single permission surface that now encompasses background agents with access to Microsoft Graph data including email, calendar, and documents. Organisations that have been licensing GitHub Copilot, M365 Copilot, and Copilot Chat under separate policies will need to reconcile those into a single governance model ahead of the August cutover.

The adoption numbers behind this move — fewer than one in twenty commercial users paying for Copilot features — also serve as a signal about where Microsoft's pricing and packaging strategy is heading. The new bundled SKUs introduced on 1 July, combined with the August app consolidation, represent a pivot toward justifying subscription value through embedded agentic capability rather than standalone AI chat features.

### Copilot Cowork Gains Full Purview Compliance Coverage at GA

Copilot Cowork, Microsoft's task-completion agent built in collaboration with Anthropic, reached general availability on 16 June. This week, the compliance surface that enterprise customers were waiting for has started to land. Data Lifecycle Management policies are rolling out globally this week, joining audit logging, Data Security Posture Management, eDiscovery, Insider Risk Management, sensitivity label inheritance, and Communication Compliance policies that went live at GA.

Data Loss Prevention for Cowork outputs is still listed as "coming soon." All Cowork processing runs within the organisation's Microsoft 365 trust boundary; task outputs do not leave the tenant without explicit policy permission.

On the cost side: Cowork is billed via Copilot Credits through a usage-based model. Administrators can manage credit allocation, set group-level spending limits, configure budget alerts and hard caps, and switch between prepaid and pay-as-you-go through the new Cost Management Dashboard in the Microsoft 365 admin centre. This dashboard also covers other AI experiences on the usage-based billing track.

**Action required.** Organisations that enabled Cowork during preview should confirm DLM policies are configured before wider rollout. Those still evaluating deployment should wait for DLP coverage if that control is a prerequisite under their information governance framework.

---

## Agentic AI

### AutoPilot: Microsoft's Always-On Agent Tier

The July 3 memo introduces AutoPilot as a distinct product category: background AI agents that operate continuously without user initiation. The first AutoPilot agent, Scout, monitors email, calendar, and organisational context through Microsoft Graph, and takes action — drafting, scheduling, routing, flagging — based on standing instructions rather than per-session prompts.

AutoPilot agents will be offered as paid add-ons inside the unified Copilot app. Specific pricing has not been published, but the structure places them above the base Copilot Chat tier and alongside Copilot Cowork in the usage-based billing layer.

The enterprise concern here is consent and scope. Unlike Copilot Chat, which responds to explicit prompts, AutoPilot agents act on standing permissions. IT and security teams should expect to develop policies around what Graph permissions AutoPilot agents can hold, which user groups can activate them, and how their actions are captured in audit logs.

---

## Infrastructure

### Foundry Hosted Agents Reach General Availability

Microsoft Foundry's Hosted Agents in Foundry Agent Service are reaching general availability in early July, following the Build 2026 announcement in June. The runtime is framework-agnostic: agents built with Microsoft Agent Framework, LangGraph, the GitHub Copilot SDK, or the OpenAI SDK can be deployed without rewriting for a proprietary API.

Key capabilities now available at GA include durable state and filesystem access for long-running autonomous agents, and framework-agnostic tracing and evaluation via OpenTelemetry. A Routines feature — which allows any agent to be triggered on a timer or schedule without a human in the loop — is in public preview alongside GA.

For enterprise development teams, the practical value is moving agents from development to production without re-platforming. The eval framework, which extends Microsoft's open trust stack to any agent regardless of the SDK used, means organisations can apply consistent quality and safety gates across a heterogeneous agent fleet.

---

## Dates to Watch

- **Mid-July 2026:** Dynamic Threat Detection Agent GA — SCU consumption begins, free preview ends.
- **This week:** Data Lifecycle Management for Copilot Cowork rolling out globally.
- **August 2026:** Unified Copilot app launches, replacing separate consumer and enterprise apps; feature retirement begins (Copilot Podcasts, Copilot Labs).
- **TBC:** Data Loss Prevention for Copilot Cowork; AutoPilot pricing published.

---

*Sources: Microsoft Tech Community (Security Copilot, M365 Copilot, Azure AI Foundry), Microsoft Foundry DevBlog, petri.com, TechTimes, WindowsNews.ai, teamascend.com, abouttmc.com, stmicro.net, hbs.net*

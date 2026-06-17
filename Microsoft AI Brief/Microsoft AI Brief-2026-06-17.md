# Microsoft AI Brief
**Week of 10–17 June 2026**

---

Two deadlines land on June 30 that enterprise teams cannot afford to miss: the Security Copilot E5 rollout completes, and the window to lock in current M365 Copilot pricing closes. Both are covered below, along with Microsoft's most consequential Build 2026 announcement — Scout, its first always-on autonomous agent.

---

## Security & Safety

### Security Copilot agents now embedded in E5 — rollout ends June 30

Microsoft's phased rollout of Security Copilot into Microsoft 365 E5 tenants began April 20 and completes June 30. Every tenant on the list receives seven days' advance notice before activation.

What's included in the E5 entitlement: conversational Copilot Chat in Defender (GA), the Phishing Triage Agent (GA), the Threat Intelligence Briefing Agent (GA), and two agents still in preview — the Security Alert Triage Agent (identity and cloud alerts beyond phishing) and the Security Analyst Agent (multi-step investigation across Defender and Sentinel, preview since March 26). More than 70 partner-built agents are also available in the Security Store.

The included pool is 400 Security Compute Units per 1,000 licensed users. SOC teams that exceed that pool pay $6 per SCU on a pay-as-you-go basis. One operational detail worth knowing: Security Copilot agents appear in the tenant as synthetic user accounts. Teams that monitor identity activity should account for this in their SIEM alert tuning to avoid spurious detections.

Governance spans Defender, Entra, Intune, Purview, and the standalone Security Copilot portal. Customers who want to stay on the free E5 tier without triggering consumption should review agent configuration before rollout completes.

**Action:** Review agent deployment settings in the Defender portal before June 30. Validate SCU monitoring and confirm your SIEM rules won't flag agent synthetic accounts as anomalous.

Sources: [Operational Notes — Security Copilot Agents in Defender XDR and Entra](https://techcommunity.microsoft.com/discussions/microsoftthreatprotection/operational-notes-on-microsoft-security-copilot-agents-in-defender-xdr-and-micro/4525826) · [Security Copilot Agents in Defender XDR: where things actually stand](https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689) · [E5 inclusion notice MC1261596](https://mc.merill.net/message/MC1261596)

---

### Security Dashboard for AI reaches general availability

Microsoft's Security Dashboard for AI — announced in public preview in February — is now generally available, with no additional licensing required.

The dashboard aggregates AI risk signals from Microsoft Defender, Entra, and Purview into a single view: an AI risk scorecard, an inventory of AI assets (agents, models, MCP servers, and third-party AI applications), posture drift alerts, and natural-language investigation via Security Copilot. It covers both Microsoft-managed AI services and external models connecting into your tenant.

For enterprise security teams, the timing is relevant. The rapid growth of Copilot Studio agents, MCP connectors, and now the first "Autopilot" agents (see below) makes AI asset sprawl a realistic governance problem. The dashboard is the most direct tool Microsoft has provided to get visibility across that estate before it becomes unmanageable.

**Action:** Enable in the Defender portal under the Security for AI section. No additional license required. Recommended first step: run the inventory report and cross-reference against your approved AI application list.

Sources: [Security Dashboard for AI — Now Generally Available](https://techcommunity.microsoft.com/blog/microsoft-security-blog/security-dashboard-for-ai---now-generally-available/4494637) · [Help Net Security](https://www.helpnetsecurity.com/2026/02/16/microsoft-security-dashboard-for-ai-tool/)

---

## Enterprise Platform

### M365 Copilot pricing increases July 1 — lock in rates by June 30

Microsoft is raising prices on Microsoft 365 base plans on July 1, 2026, while simultaneously making M365 + Copilot bundles permanent SKUs for SMBs. The increases:

| Plan | Current | July 1 |
|---|---|---|
| Business Basic | $6/user/mo | $7 |
| Business Standard | $12.50 | $14 |
| E3 | $36 | $39 |
| E5 | $57 | $60 |

Two new permanent SMB bundles launch on July 1: M365 Business Standard with Copilot at $23.50/user/month, and M365 Business Premium with Copilot at $32, both for up to 300 seats on annual billing. Copilot Business standalone currently carries a promotional rate of $18/user/month; that rises to $21 on July 1.

**Action:** Organizations renewing, expanding, or adding Copilot seats should complete transactions before June 30 to hold the lower rates. Procurement teams should be notified now.

Sources: [Act Now: Lock in Current Pricing on M365 Copilot Business Bundles](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/act-now-lock-in-current-pricing-on-microsoft-365-copilot-business-bundles/4502628) · [M365 Business Plans with Copilot Become Permanent (July 2026)](https://windowsnews.ai/article/microsoft-365-business-plans-with-copilot-become-permanent-for-smbs-starting-july-2026.425116)

---

### Copilot app auto-installs on Windows — Phase 2 underway

Microsoft resumed the phased auto-install of the Microsoft 365 Copilot app on commercial Windows devices. Phase 2 began June 15 and runs through July 1, targeting Current Channel tenants with active Copilot licenses. Phase 3 (July 2–20) covers Monthly Enterprise Channel and Semi-Annual Enterprise Channel.

The app installs silently alongside existing Microsoft 365 desktop apps. It does not activate or consume Copilot licenses on its own — the distinction matters for organizations that license selectively. The rollout does not apply to the European Economic Area.

Admins who want to suppress the install have three options: the tenant-wide toggle in M365 Admin Center under Settings > Org Settings > Microsoft 365 Copilot; Intune policies; or Group Policy using the May 2026 Administrative Templates (policy object: "Disable Microsoft 365 Copilot auto-install").

**Action:** Phase 2 is active now. If your organization has change control requirements or hasn't communicated the Copilot app rollout to end users, set the opt-out toggle today or configure Group Policy before the Phase 2 window closes July 1.

Sources: [M365 Copilot Default Install Returns: IT Governance Guide for June 2026](https://windowsnews.ai/article/microsoft-365-copilot-default-install-returns-it-governance-guide-for-june-2026.425281) · [MC1152323](https://mc.merill.net/message/MC1152323)

---

### May 2026 M365 Copilot updates: Claude Opus 4.8 and MCP connectors

Two May 2026 additions that enterprise teams should evaluate:

**Claude Opus 4.8 in M365 Copilot.** Anthropic's Opus 4.8 is now selectable alongside OpenAI models in Word, Excel, PowerPoint, and Copilot Chat. This is the first time a non-OpenAI frontier model has been surfaced as a user-selectable option in core M365 applications. Organizations with specific requirements around model behavior, output style, or cost allocation now have a meaningful alternative.

**Federated Copilot Connectors (MCP).** Federated connectors built on the Model Context Protocol bring live third-party data into Copilot Chat and Researcher without requiring data to be preprocessed into Microsoft's graph. The first wave includes LSEG, Moody's, HubSpot, and Notion, with native security controls preserved at the connector layer. Organizations can also build custom federated connectors for internal systems.

The practical implication of MCP connectors is that Copilot can now reference data from authoritative source systems in real time, rather than from a potentially stale SharePoint or OneDrive copy. For teams doing financial analysis, CRM-grounded summaries, or knowledge management, this changes how well Copilot responses can be grounded.

Sources: [What's New in M365 Copilot — May 2026](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%e2%80%99s-new-in-microsoft-365-copilot--may-2026/4522010) · [M365 Copilot May 2026 Recap: 53 Updates](https://www.aguidetocloud.com/blog/microsoft-365-copilot-may-2026-updates/)

---

## Agentic AI

### Microsoft Scout: the first "Autopilot" agent

Microsoft's most significant Build 2026 announcement for enterprise customers is Scout, introduced by Satya Nadella on June 2 as the first product in a new category called Autopilots.

Where previous Copilot agents respond to prompts, Scout is designed to run continuously without being asked. It joins Teams group chats as a participant, monitors Outlook threads, manages calendar requests, manipulates files in OneDrive and SharePoint, and can adjust system settings — all on behalf of a user, within the tenant's compliance and governance envelope. Microsoft describes Autopilots as "always-on, enterprise-grade, long-running agents" running in your tenant, not as an external service.

The capability is built on OpenClaw, Microsoft's in-house reasoning infrastructure. Governance controls — the specific policies and permission scopes admins will be able to set — are still being developed as part of the Frontier private preview.

The rollout timeline is deliberately slow: a waitlist is open for private preview, activations are expected to begin in Q4 2026, and general availability is not expected before mid-2027. That gives enterprise organizations time to develop agent governance frameworks before the technology becomes broadly available — time that should be used.

**Action:** Register for the private preview waitlist if your organization wants early access. More practically, use the 12+ months before GA to define your agent authorization policies: which workflows can be delegated, what permission scopes are acceptable, how agent actions will be audited.

Sources: [Microsoft Scout Autopilot Agent: Turning Copilot Into Governed Enterprise Action](https://windowsnews.ai/article/microsoft-scout-autopilot-agent-turning-copilot-into-governed-enterprise-action.422881) · [TechRadar: Microsoft reveals Scout, its first Autopilot](https://www.techradar.com/pro/a-new-category-of-agents-microsoft-reveals-scout-its-first-autopilot-which-wants-to-change-how-you-work-for-good) · [The Register: No longer just a Copilot](https://www.theregister.com/ai-and-ml/2026/06/03/no-longer-just-a-copilot-microsofts-ai-wants-to-take-the-wheel/5250718)

---

## Developer Tools

### Microsoft Agent Framework Build 2026: CodeAct, Agent Harness, Hosted Agents

The Microsoft Agent Framework (MAF), which reached 1.0 GA on April 2 by converging AutoGen and Semantic Kernel into a single platform, shipped three meaningful additions at Build 2026.

**Agent Harness** addresses the gap between a working local agent and a production-ready one. It adds context compaction, instruction merging, task tracking, and human-in-the-loop approval flows to the execution layer. For enterprise developers, the approval flow support is the relevant part: it provides a structured way to require human sign-off before agents take irreversible actions.

**CodeAct** changes how agents use tools. Rather than calling tools one by one in a loop, the model writes a short Python program, executes it once inside a Hyperlight micro-VM sandbox (isolated per call), and returns a consolidated result. The claimed benefit is fewer round-trips to the model and more predictable execution. CodeAct is currently in alpha (`agent-framework-hyperlight` package).

**Hosted Agents in Foundry Agent Service** provides a managed path from local development to production: Microsoft handles scaling, session persistence, and observability. The tracing and evaluation layer now covers agents built on LangChain, LangGraph, OpenAI SDK, or any custom framework via OpenTelemetry — not just MAF. This framework-agnostic observability is significant for enterprise teams with mixed agent stacks.

Sources: [Microsoft Agent Framework at Build 2026](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/) · [Build and run agents at scale with Microsoft Foundry](https://devblogs.microsoft.com/foundry/agent-service-build2026/) · [Build agents you can trust — open evals and control standard](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/)

---

## Dates to Watch

| Date | What |
|---|---|
| **June 30** | Security Copilot E5 rollout completes — review agent config now |
| **June 30** | M365 Copilot pricing lock-in deadline |
| **July 1** | M365 base plan and Copilot bundle prices increase |
| **July 1** | Copilot app auto-install Phase 2 ends (Phase 3 begins July 2) |
| **July 20** | Copilot app auto-install Phase 3 ends (Semi-Annual Enterprise Channel) |
| **Q4 2026** | Scout Autopilot private preview activations begin |
| **Mid-2027** | Scout Autopilot general availability (earliest estimate) |

---

*Microsoft AI Brief is published weekly. Coverage period: 10–17 June 2026.*

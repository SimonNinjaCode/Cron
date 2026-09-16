# Microsoft AI Brief — 16 September 2026

*Enterprise intelligence on Microsoft AI | Week of 9–16 September 2026*

---

## Security & Safety

### Copilot Goes Dark for 100 Minutes — and a Resilience Test Is to Blame

On the night of 9 September, copilot.microsoft.com dropped off the internet from 22:25 UTC until 00:05 UTC on the 10th, returning a Cloudflare Error 1016 to everyone who tried to reach it. That is not a routing quirk — it is the error code for an origin server that Cloudflare cannot contact, which means the backend behind the Copilot web surface was unreachable for the duration.

Microsoft acknowledged that the Microsoft 365 Copilot team ran a resilience test during the same window that produced unintended consequences. Some users who retained access to the portal lost the suggested prompts inside Copilot Chat. The service restored without a customer-facing incident declared, but the overlap between a deliberate test and a full outage on a production endpoint will draw scrutiny from enterprise reliability teams.

**What this means for you:** If your organisation uses copilot.microsoft.com as a direct entry point — rather than the Teams or Microsoft 365 apps — this is a reminder that the web surface carries no separate SLA language from the core service. Review whether your user-facing runbooks call out the Teams-embedded Copilot Chat as the failover path when the web URL is unreachable. The event also surfaces a governance question: resilience testing on shared production infrastructure requires better isolation.

---

### Microsoft Defender Now Scores Risk for Every AI Agent in Your Estate

A significant capability has quietly reached operational status: Microsoft Defender assesses posture risk for AI agents across the enterprise — including agents built in Copilot Studio, Microsoft Foundry, and those discovered running locally on endpoint devices. Risk levels factor in configuration, access scope, runtime activity, and other signals, giving security teams a ranked list of agents to investigate.

This matters because most organisations that have adopted Copilot Studio or Foundry over the past year have accumulated a long tail of agents with undocumented permissions and data access. Defender's posture scoring is the first platform-native tool that makes that inventory visible alongside a risk signal, rather than requiring manual auditing.

**Licensing note:** As of 1 July 2026, AI agent security capabilities for Copilot Studio and Foundry agents require a **Microsoft Agent 365** licence. Customers who assumed these controls were included in their existing Defender or E5 subscription should verify their licence position. Agents created before that date did not automatically inherit the new controls; a deliberate enrolment step is required.

**Action required:** Run the AI agent inventory report in Defender now. Prioritise any agent rated high or critical risk. Cross-reference your Copilot Studio and Foundry deployments against the inventory to identify agents that have never been reviewed. If you lack Agent 365 licences, request a scoping call with your Microsoft account team before the next renewal cycle.

---

### Security Copilot Agents — Where Things Stand Heading into Autumn

The **Phishing Triage Agent** is generally available for customers with Defender for Office 365 Plan 2. It handles the full triage loop for user-reported phish — classification, enrichment, remediation recommendation — without analyst intervention. Measured time-to-triage has dropped by a reported 30% on average across early adopters.

The **Security Alert Triage Agent**, which extends the same autonomous approach to identity and cloud alerts beyond the phishing use case, remains in preview. The **Dynamic Threat Detection Agent** runs continuously in the Defender backend, correlating across Defender and Sentinel telemetry to generate hypotheses and emit alerts when evidence converges — useful for threat hunters who want proactive surfacing rather than reactive triage.

More than 70 partner-built agents are listed in the Security Store. The quality varies significantly; treat third-party agents as you would any external tool and review their data access requirements before deployment.

**Licensing context:** Security Copilot moved into E5 product terms on 1 January 2026. The phased tenant rollout ran from 20 April to 30 June. If your tenant was not activated by the end of June, contact licensing support — activation is not retroactive.

---

## Enterprise Platform

### Copilot Cowork: Generally Available, Compliance Controls Now Shipping

Copilot Cowork — Microsoft's autonomous multi-step task runner, developed in collaboration with Anthropic — reached general availability for commercial customers in July and has been accumulating governance tooling since. September's focus is squarely on making autonomous AI activity auditable.

Administrators now have a **Cost Management Dashboard** in the Microsoft 365 admin centre that shows credit consumption per user, supports budget caps, and can flag usage spikes. On the compliance side, Microsoft Purview's Data Security Posture Management for AI provides the front door: it discovers Cowork activity, applies existing sensitivity labels and DLP policies, and surfaces compliance gaps before they become incidents.

Practically, this means Cowork now has the same kind of admin surface that Teams and SharePoint acquired over years — but compressed into a few months. The controls are present; the question is whether your Purview policies are mature enough to be meaningful. An organisation that still has large volumes of SharePoint content with no sensitivity label applied will find that Cowork can read and act on that content without restriction.

**Action required:** Before expanding Cowork access beyond your pilot group, review your Purview information protection baseline. At minimum, auto-labelling policies should be applied to the document libraries Cowork is likely to touch. Enable audit logging for Cowork sessions from day one — the audit trail is what regulators and legal teams will ask for first.

---

### Excel's COPILOT() Worksheet Function Has Been Retired

Effective 14 September 2026, the `=COPILOT()` worksheet function is no longer available in Excel. Users who built workbooks that called the function directly will find those formulas returning an error. Microsoft's stated position is that all Copilot capability in Excel is now accessed through the **Copilot side pane**, which offers the same underlying intelligence through a conversational interface rather than a formula.

This is a workflow change, not a capability removal — but it will break any workbook that embedded the function, including templates distributed to end users and any automation that relied on Excel's calculation engine to invoke Copilot programmatically.

**Action required:** Identify workbooks in your estate that contain `=COPILOT()` calls. The Search in SharePoint and OneDrive can find files by keyword; a Power Automate flow that scans site collections is the more thorough approach for large deployments. Communicate the change to Excel power users and finance teams who commonly built self-service models using the function.

---

### Copilot in SharePoint: September 2026 Updates

SharePoint's Copilot integration has picked up meaningful administrative scope this month. Users can now ask natural language questions across site content, trigger simple workflows, and create new sites through conversational prompts — capabilities that were previously limited to the M365 Chat surface. The September release also adds site-level admin controls allowing owners to scope what Copilot can read within their site, which addresses the content oversharing concern that came up repeatedly in enterprise pilots.

A separate article dated 15 September from Petri specifically examined **SharePoint Advanced Management** as a Copilot readiness instrument. SAM's site access review and restricted access control policies are now presented as prerequisites rather than optional hardening steps — a signal that Microsoft is positioning governance readiness as a gating condition for full Copilot deployment, not an afterthought.

**Action required:** If SharePoint Advanced Management is not yet licensed in your tenant (it requires Microsoft 365 E5 or a standalone SAM licence), assess whether the new Copilot site controls are sufficient for your risk posture. Sites containing HR, legal, or financial data should have restricted access control policies applied before those sites are in scope for Copilot.

---

### Microsoft 365 "AI at Work" Roadmap — Single Pane for AI Features

Microsoft has consolidated its scattered product roadmap entries into a unified **AI at Work Roadmap**, providing a single destination for upcoming features across Microsoft 365, Copilot, agents, Dynamics 365, Power Platform, and Dataverse. The change took effect in late August and September is the first month in which Dynamics 365 and Power Platform features appear alongside M365 entries.

For IT planning teams, this is genuinely useful: the previous arrangement required monitoring three or four separate roadmap views to build a complete picture of what was shipping. The consolidated view also includes estimated rollout dates by ring, which makes it easier to schedule training and change management activities. The roadmap is available at microsoft.com/en-us/microsoft-365/roadmap.

---

## Agentic AI

### Agent 365 Licensing Transition for Copilot Studio and Foundry Agents

As noted in the Security section, the July 1 transition to Microsoft Agent 365 licensing for AI agent security capabilities marks a broader shift in how Microsoft is packaging agentic AI for enterprise. Agent 365 is positioned as the governance and management layer for agents running across Microsoft 365, Foundry, and Copilot Studio — analogous to Intune for devices.

The practical implication for organisations that deployed Copilot Studio agents during the wave of adoption in late 2025 and early 2026 is that those agents now need to be assessed against the Agent 365 licence model. Agents used purely for productivity workflows with no elevated data access may not trigger the requirement; agents with access to sensitive data stores or external connectors almost certainly will.

---

### What's New in M365 Copilot (July Update — Now Operational)

The July 2026 M365 Copilot update is now fully rolled out to commercial tenants and worth noting for IT teams who have been managing the rollout:

- **GPT-5.6 family** is now the default model in M365 Copilot, replacing the earlier GPT-5 baseline. Expect measurably better performance on complex document summarisation and multi-document synthesis tasks.
- Users can now **@mention Word, Excel, and PowerPoint agents** directly in Copilot Chat, reducing the friction of context-switching between the chat surface and individual Office applications.
- **Copilot Cowork** is now the default autonomous mode when users ask Copilot to complete multi-step tasks, having replaced the earlier "agent mode" branding.

The GPT-5.6 upgrade is a background change — tenants do not need to take action — but it may produce different outputs for workflows that had been tuned against specific model behaviour. If your organisation has documented expected Copilot outputs for compliance or quality-control purposes, a brief review is warranted.

---

## Developer Tools

### Microsoft Foundry: Multimodal Application Layer Expanding

**GPT-Live-1** and **GPT-image-2.5** are available in Microsoft Foundry, enabling applications that can simultaneously process audio, generate speech, create images, and edit visual content within a single model context. This is primarily relevant to teams building customer-facing applications on Azure, but enterprise intranet and productivity tooling use cases are emerging — narrated document summaries, accessible content generation, and real-time meeting visualisation being the clearest examples.

Foundry's observability and evaluation tooling (shipping since Build 2026) now surfaces ROI metrics alongside technical traces, making it easier to demonstrate business value from AI investments — something that has been missing from enterprise AI reporting frameworks.

---

## Dates to Watch

| Date | Event |
|------|-------|
| 14 Sep 2026 | `=COPILOT()` function retirement **effective now** — audit Excel workbooks |
| Rolling (now) | Copilot Cowork compliance controls shipping — review Purview policies |
| Rolling (now) | AI agent posture risk available in Defender — run first inventory |
| 1 Jul 2026 (passed) | Agent 365 licence required for agent security features — verify licence position |
| TBC | Security Alert Triage Agent GA (currently in preview) |

---

*Sources: Microsoft Tech Community (Azure AI Foundry Blog, M365 Copilot Blog, Security Copilot Blog, SharePoint Blog), Microsoft DevBlogs (Agent Framework, Foundry), The Register, Petri.com, Practical365, Microsoft Learn.*

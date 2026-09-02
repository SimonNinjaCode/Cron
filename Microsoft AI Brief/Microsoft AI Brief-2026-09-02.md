# Microsoft AI Brief — 2 September 2026

*Enterprise intelligence on Microsoft AI. Covers the seven days ending 2 September 2026.*

---

## Security & Safety

### CoSnitch (CVE-2026-24301): The third Copilot vulnerability of the year — and the most instructive

Varonis Threat Labs disclosed a critical flaw in Microsoft Copilot Personal on 18 August, a week after reporting it triggered a patch. The vulnerability, tracked as CVE-2026-24301 and named CoSnitch, let an attacker silently siphon data from a victim's connected accounts with a single click on a malicious link. What makes it stand out is how it was found: researchers repeatedly asked Copilot why automatic data exfiltration "wasn't possible," reframing each refusal as a follow-up question. The model's own explanations about why the attack couldn't work eventually mapped its internal architecture and surfaced the undocumented parameter needed to execute it. Varonis calls this technique meta-hacking — social-engineering the AI's reasoning process rather than attacking its code.

Microsoft says it found no evidence of active exploitation before the patch shipped. The fix is live.

**Why it matters for enterprise IT and security teams:** CoSnitch is the third Copilot-class vulnerability Varonis has published this year, following Reprompt (guardrail bypass via repeated questioning) and SearchLeak (covert data exfiltration through M365 Copilot Enterprise). The pattern suggests systematic research pressure on Copilot's agentic connectors — the same integrations that make Copilot useful are expanding its attack surface. Organisations running Copilot Personal alongside work accounts should verify that all users are on the latest app version. More broadly, security teams should track the Varonis Threat Labs disclosure stream as a leading indicator of Copilot-class risks.

**Action required:** Confirm Copilot Personal app updates have propagated to managed devices. Review any connected app permissions granted to Copilot Personal; CoSnitch operated through those connections.

---

### Security Copilot now included in E5 — 40+ new agents in scope

Security Copilot's inclusion in Microsoft 365 E5 and E7 reached full tenant rollout by the end of June. The E5 entitlement covers Copilot Chat in Defender, promptbooks, agentic scenarios across Defender, Entra, Intune, and Purview, the standalone Security Copilot portal, Agent Builder, and Graph APIs.

The agentic layer has expanded substantially. Over 40 new Microsoft and partner-built agents were introduced across the first half of 2026: 12 Microsoft-built agents spanning Defender, Entra, Intune, and Purview, plus more than 30 partner-built agents accessible through the Security Store. Key agents include the Phishing Triage Agent (GA in Defender for Office 365 P2), the Security Alert Triage Agent extending automated triage to identity and cloud alerts, and the Security Analyst Agent for multi-step investigation across Defender and Sentinel.

**Why it matters:** Any E5 customer who hasn't activated Security Copilot is leaving a capability they're already paying for unused. The agent catalogue has also grown past the point where individual review is practical — IT and security teams need a policy governing which agents can be deployed and by whom, rather than case-by-case approval.

**Action required:** If your tenant hasn't been activated, follow the E5 activation path in the admin centre. Establish a Security Store agent governance policy before end-users begin deploying agents independently.

---

## Enterprise Platform

### The Microsoft 365 Roadmap is now the AI at Work Roadmap

On 25 August, Microsoft renamed the Microsoft 365 Roadmap to the AI at Work Roadmap, expanding its scope to include Dynamics 365, Power Platform, and Dataverse updates starting September 2026. The Register flagged the change two days later, noting the rebranding also adds a layer of AI-category filtering that makes it harder to browse features without a Copilot lens.

Two substantive feature changes landed alongside the rename. The M365 Admin Agent reached general availability — it handles user management, licence assignment, service health monitoring, and troubleshooting natively within the admin centre using natural language. Separately, Anthropic's Claude Opus 5 was added to Microsoft 365 Copilot (Claude Sonnet 5 was added in July), with both models manageable per-user or per-group through the admin centre.

**Why it matters:** The Admin Agent GA is operationally significant — it shifts routine admin tasks from scripted queries or portal navigation to conversational interaction, and it will catch the attention of help-desk and IT operations teams. The multi-model capability (GPT-5.6 family, Claude Sonnet 5, Claude Opus 5) is now a real procurement and governance question: which model is appropriate for which use case, and who controls the defaults?

**Action required:** Review Admin Agent scopes and permissions before enabling broadly — the agent has write access to user and licence records. Establish a model governance policy in the Copilot admin centre specifying which models are permitted for which user groups.

**Date to watch:** October 2026 — SharePoint Framework Copilot Components are targeting general availability.

---

### Microsoft's two Copilot apps became one

The consumer Copilot app and the Microsoft 365 Copilot app began merging into a single application in mid-August, with mobile and web rolling out worldwide from 13 August and Windows and macOS apps following in mid-September. The unified app retains the Microsoft Copilot name with a new icon; work and personal account data remain separated by design with account switching available in-app.

Two features did not survive the consolidation: group chat threads and the Podcasts feature were both retired on 18 August.

**Why it matters:** For enterprise IT, the relevant question is endpoint management. The Windows and macOS unified app arrives in mid-September, which means MDM and MAM policies configured for two separate apps will need review. Data separation between accounts is Microsoft's stated guarantee, but security teams should verify this through their own testing, particularly for tenants where users also hold personal Microsoft accounts.

**Action required:** Review Intune and third-party MDM policies for Copilot app management ahead of the mid-September Windows/macOS rollout. Confirm conditional access policies cover the unified app correctly.

---

### Microsoft 365 E7: The all-in AI bundle since May

The Microsoft 365 E7 "Frontier Suite" reached general availability on 1 May 2026 at $99 per user per month. It bundles Microsoft 365 E5, Microsoft 365 Copilot, the Entra Suite, and Agent 365 into a single SKU. Buying the components separately costs approximately $117, making E7 roughly a 15% discount for organisations intending to deploy all four. CSP promotional pricing extends to 31 December 2026 (10–15% off depending on seat count and term).

The critical caveat: agent consumption costs — building and running AI agents in Copilot Studio or Microsoft Foundry — sit outside the per-seat price entirely.

**Why it matters:** For enterprise agreements renewing in the second half of 2026, E7 is the relevant benchmark. The bundle pricing makes Copilot and Agent 365 look inexpensive at the SKU level, which may underestimate total cost of ownership once agent consumption is factored in. Procurement and FinOps teams should model agent consumption costs separately before committing.

**Action required:** If your EA or MCA-E renewal falls before 31 December 2026, request an E7 quote and run a total cost comparison including projected agent consumption. Use the Cost Management Dashboard (see Agentic AI section) to baseline current consumption if any agentic workloads are already live.

---

## Agentic AI

### Copilot Cowork is generally available — with a compliance framework to match

Copilot Cowork — Microsoft's agentic productivity layer that plans, executes, and delivers multi-step work tasks autonomously — reached general availability on 16 June 2026 for all Microsoft 365 Copilot commercial subscribers outside GCC (FedRAMP compliance not yet in scope). The feature was co-developed with Anthropic.

The compliance surface at GA is broader than many expected: audit logs, Data Security Posture Management, eDiscovery, Insider Risk Management, sensitivity label inheritance end-to-end, and Communication Compliance policies are all supported. All Cowork activity runs inside your existing Microsoft 365 compliance boundary. Administrators manage access, budgets, and credit consumption through a Cost Management Dashboard in the M365 admin centre; billing is usage-based.

**Why it matters:** Copilot Cowork is the first generally available agentic layer in M365 that operates across multiple apps and steps autonomously. The compliance infrastructure is better than comparable first-generation agentic features, but "supported" is not the same as "configured." Most tenants will need to actively connect their existing IRM and eDiscovery policies to Cowork activity rather than assuming inheritance is automatic.

**Action required:** Before enabling Cowork for any production user group, verify that audit log coverage, sensitivity label inheritance, and IRM policies are correctly applied to Cowork activity in your tenant. Set budget caps in the Cost Management Dashboard; usage-based billing without caps can produce unexpected spend. Confirm GCC timeline with your Microsoft account team if applicable.

---

## Sources

- [Copilot tricked into telling researchers how to hack itself — The Register](https://www.theregister.com/research/2026/08/18/copilot-tricked-into-telling-reseachers-how-to-hack-itself/5288857)
- [CoSnitch CVE-2026-24301 — Varonis Threat Labs](https://www.varonis.com/blog/cosnitch)
- [Critical Microsoft Copilot CoSnitch Vulnerability — Cybersecurity News](https://cybersecuritynews.com/copilot-cosnitch-vulnerability/)
- [CoSnitch Flaws Turned Microsoft Copilot Into a One-Click Data Theft Tool — Redmond Mag](https://redmondmag.com/articles/2026/08/19/cosnitch-flaws-turned-microsoft-copilot-into-a-one-click-data-theft-tool.aspx)
- [Microsoft slaps a fresh coat of AI paint on the Microsoft 365 Roadmap — The Register](https://www.theregister.com/software/2026/08/27/microsoft-slaps-a-fresh-coat-of-ai-paint-on-the-microsoft-365-roadmap/5292865)
- [Moving beyond release waves with the AI at Work roadmap — Microsoft Dynamics 365 Blog](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/)
- [What's New in Microsoft 365 Copilot — July 2026 — Microsoft Tech Community](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%e2%80%99s-new-in-microsoft-365-copilot--july-2026/4538332)
- [Microsoft's dueling Copilot apps have combined into a single entity — The Register](https://www.theregister.com/ai-and-ml/2026/08/13/microsofts-dueling-copilot-apps-have-combined-into-a-single-entity/5287512)
- [Security Copilot Is Free in E5 Starting April 20 — myabt.com](https://www.myabt.com/blog/security-copilot-e5-free-april-activate)
- [Security Copilot Comes Included with Microsoft 365 E5 — LogicV](https://logicv.com/blog/security-copilot-comes-included-with-microsoft-365-e5-what-this-really-means-for-socs-in-2026/)
- [From alert overload to decisive action: How Security Copilot agents are transforming security and IT — Microsoft Tech Community](https://techcommunity.microsoft.com/blog/securitycopilotblog/from-alert-overload-to-decisive-action-how-security-copilot-agents-are-transform/4504213)
- [Microsoft 365 E7: $99 Bundle Breakdown — SAMexpert](https://samexpert.com/microsoft-365-e7-licensing-guide/)
- [M365 licensing changes July 2026: E7, Agent 365, Copilot explained — Orchestry](https://www.orchestry.com/insight/m365-licensing-changes-july2026)
- [Microsoft Brings Copilot Cowork to General Availability with New Compliance Controls — Petri](https://petri.com/microsoft-copilot-cowork-compliance-controls/)
- [Copilot Cowork GA June 16 2026: Metered Agent Billing, Credits, and IT Governance — Windows Forum](https://windowsforum.com/threads/copilot-cowork-ga-june-16-2026-metered-agent-billing-credits-and-it-governance.426989/)

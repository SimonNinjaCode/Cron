# Microsoft AI Brief — 15 July 2026

*Enterprise intelligence on Microsoft AI. Week of 8–15 July 2026.*

---

## Security & Safety

### Security Copilot Is Now Bundled Into M365 E5 — And the Meter Is Running

The most consequential licensing change in Microsoft's security stack took effect on 1 July, and many IT teams are still catching up. Microsoft 365 E5 now includes an allocation of Security Copilot usage as part of the subscription — 400 Security Compute Units (SCUs) per 1,000 licensed users per month, capped at 10,000 SCUs across a tenant. Additional consumption beyond that allocation is billed through Azure at the standard SCU rate.

The E5 price increased from $57 to $60 per user per month (a 5.3% rise) and now bundles Security Copilot alongside Intune Endpoint Privilege Management, Enterprise Application Management, and Cloud PKI. For organisations that have been running Security Copilot as a separately purchased product, the consolidation simplifies procurement but requires a review of existing SCU contracts to avoid double-paying.

What this means in practice: the Phishing Triage Agent is generally available and handles user-reported phishing through Defender for Office 365 P2 without analyst intervention. The Security Alert Triage Agent — extending the same autonomous triage logic to identity and cloud alerts — is in preview. The Security Analyst Agent, which runs multi-step investigations, entered preview in March and is still rolling out. Together these represent a meaningful shift toward autonomous, agent-driven SOC workflows.

**Action required:** Audit existing standalone Security Copilot purchases before the next renewal. Review the SCU consumption model against your tenant size and agent usage expectations. SOC teams should prioritise enabling the Phishing Triage Agent, which is production-ready and has the clearest ROI case.

---

### Nadella Issues a Sharp Warning on AI Data Sovereignty

In a blog post published 13 July, Microsoft CEO Satya Nadella framed what he called the "reverse information paradox" — the idea that enterprises using large, closed-source AI models are paying twice: once with money, and again with the proprietary business knowledge they feed into those models. The concern is that model providers can learn from customer data in ways that eventually commoditise what makes each business distinct.

Nadella's public stance represents a significant rhetorical departure from Microsoft's long-standing partnership with OpenAI. Major customers including T-Mobile, SAP, and ADP are already moving toward flexible, open-source alternatives hosted on-premises or in controlled cloud environments rather than sharing workloads with frontier labs.

Microsoft's pitch is Foundry and the enterprise-hosted Frontier Company offering, where Microsoft guarantees that customer data and IP are never harvested to train foundational models. The message is aimed squarely at enterprises still evaluating where to land after the AI hype cycle: take data sovereignty seriously before you are locked in.

**What to watch:** Whether Microsoft's own ongoing investment in OpenAI's commercial API creates a contradiction here — or whether this signals a longer-term decoupling of Microsoft's enterprise products from OpenAI-hosted inference.

---

### Security Dashboard for AI Is Generally Available

The Security Dashboard for AI, which entered public preview in February, is now generally available. It aggregates posture and real-time risk signals from Microsoft Defender, Entra, and Purview into a single executive and practitioner view covering AI applications and agents across the tenant.

The dashboard inventories Microsoft-hosted AI assets (M365 Copilot, Copilot Studio agents, Foundry apps) alongside third-party AI tools including Google Gemini, OpenAI ChatGPT, and MCP servers. No additional licensing is required — any organisation already using eligible Defender, Entra, or Purview products has access.

For CISOs who have been fielding board questions about AI risk without a coherent answer, this is the most practical tool Microsoft has shipped. It does not yet cover shadow AI deployments that bypass corporate controls, but the MCP server inventory is a genuine addition given how quickly those connectors have proliferated.

**Action required:** Security and compliance teams should activate the dashboard now and establish a baseline inventory of AI assets before the next audit cycle.

---

## Enterprise Platform

### Copilot Cowork Is Live — Admins Need to Set Spending Controls

Copilot Cowork reached general availability worldwide on 16 June, and billing on consumed Copilot Credits began 1 July. The feature executes complex, long-running, multi-tool tasks end-to-end and returns a completed result rather than a draft — closer to a delegated project than an assisted search.

The GA release ships with audit log support, Data Security Posture Management, eDiscovery, Insider Risk Management, and sensitivity label inheritance. Data Loss Prevention integration is still to come. Cowork runs within the Microsoft 365 trust boundary and applies existing tenant policies, but enterprise admins need to explicitly choose who can use it and at what cost.

Critically: **Cowork is off by default.** Admins enable it through the Cost Management Dashboard in the M365 admin centre, where they can set spending policies, hard caps, and per-group or per-user limits. Both prepaid Copilot Credits and pay-as-you-go billing are available. Tenants where at least one user participated in the Frontier preview (March 30–June 16) received a billing grace period through 30 June — that window has now closed.

**Action required:** If your organisation has not yet reviewed Cowork's admin controls, do so before usage accrues. Configure spending limits before end of July. Establish data sensitivity guidelines for tasks submitted to Cowork given the multi-step autonomous execution model.

---

### Work IQ APIs Are Generally Available: Power BI, Dataverse, and Copilot Grounding

On 16 June, Microsoft made the Work IQ APIs generally available, enabling developers and IT administrators to build enterprise agents that reason over Microsoft 365 data at scale. The most notable enterprise-ready integration is Power BI: Copilot can now query Power BI reports and semantic models in natural language and return grounded answers without users or developers needing to build separate query layers.

Dataverse integration — allowing Copilot to search and query line-of-business records — entered public preview in June, with general availability targeted for September. The Work IQ APIs also underpin the Vision capability in M365 Copilot, which processes a stream of images from screen or camera sharing. Admins now have a dedicated control to govern where Vision can be used, which matters for regulated environments where screen content must be controlled.

For enterprise teams evaluating how to extend Copilot with internal data sources, the Work IQ APIs represent the most direct path into Microsoft's supported grounding infrastructure, ahead of custom RAG builds.

---

## Infrastructure

### GPT-Realtime-2.1 Arrives in Microsoft Foundry With Reasoning and Lower Pricing

Microsoft Foundry this week added GPT-realtime-2.1 and GPT-realtime-2.1-mini to the Azure OpenAI collection. The key architectural change from the previous generation is native reasoning: the model works through a problem internally before responding, making it suited for voice applications that need to handle complex, multi-step queries without routing through a separate text pipeline.

Enterprises can tune the trade-off between cost and response latency by setting reasoning effort explicitly (minimal / low / medium / high). The GA release also includes a 20% reduction in per-token costs versus the prior realtime model, new voices (Marin and Cedar), improved instruction following, and production-ready telephony features including SIP/PSTN support. For contact-centre, compliance-recording, and real-time meeting-intelligence use cases, this is the most capable speech-to-speech model available in the Azure stack.

**Date to watch:** Check your existing Azure OpenAI realtime deployments for the new model version. The cost reduction takes effect immediately on new deployments; existing deployments need to be updated manually.

---

## One Sentence

The most significant development this week is the activation of Security Copilot within Microsoft 365 E5 subscriptions, representing the first time autonomous SOC AI has been pushed to every E5 seat by default — with billing now live and admin action required to manage consumption.

---

*Sources: [The Register (13 Jul)](https://www.theregister.com/ai-and-ml/2026/07/13/microsoft-chief-turns-hostile-on-frontier-ai-labs-warns-companies-to-guard-their-ip/5270628) · [TechCommunity: Security Copilot Scale](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/microsoft-security-copilot-ai-driven-security-operations-at-greater-scale/4528912) · [TechCommunity: Security Dashboard for AI](https://techcommunity.microsoft.com/blog/microsoft-security-blog/introducing-security-dashboard-for-ai-now-in-public-preview/4494637) · [TechCommunity: M365 Copilot June 2026](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--june-2026/4529572) · [Microsoft 365 Blog: Cowork GA](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/) · [TechCommunity: Realtime AI](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/a-new-chapter-for-realtime-ai-reasoning-translation-and-real-time-transcription/4517124) · [Sourcepass: E5 July 2026 Changes](https://sourcepassmcoe.com/articles/what-is-changing-in-microsoft-365-e5-on-july-1-2026-sourcepass-mcoe) · [Petri: Copilot Cowork](https://petri.com/copilot-cowork-task-automation-microsoft-365/) · [TechCrunch: Nadella Warning](https://techcrunch.com/2026/07/13/satya-nadella-has-issued-a-shocking-warning-to-companies-using-ai/)*

---
layout:
  width: wide
---

# Microsoft AI Brief — 23 September 2026

*Enterprise intelligence on Microsoft AI | Week of 16–23 September 2026*

---

## Security & Safety

### Foundry IQ Gets Encryption, Permissions Sync, and Sensitivity-Label Controls — in Preview

Microsoft has moved three governance capabilities for AI agents into preview inside Foundry IQ: encryption of knowledge content at rest and in transit through customer-managed keys, permissions sync that enforces SharePoint and Entra access controls when agents query the knowledge layer, and sensitivity-label governance that carries Microsoft Purview labels through to content an agent reads or surfaces. Together, these close a gap that compliance teams flagged during enterprise pilots: agents could retrieve and relay content that the requester had no permission to see directly, because the agent's service identity held broader access than the end user.

The practical effect is that Foundry IQ now participates in the same policy enforcement chain as Microsoft 365 — a labelled document that is restricted to a specific security group should remain restricted when an agent summarises it, and these preview controls are the mechanism.

Access activity is routed into existing Purview and Microsoft Sentinel monitoring workflows rather than creating a separate log silo, which should reduce the operational overhead of auditing AI activity.

**What this means for you:** If you have deployed Foundry-based agents against internal knowledge bases, the permissions sync preview is the control most worth testing first. It is the clearest protection against the oversharing scenario regulators and internal audit teams raise most often. Enrol a non-production environment in the preview, then validate that users outside the permitted group cannot receive content through the agent that they could not access directly. Enable customer-managed keys if your data classification policy requires them — this is the prerequisite for bringing AI workloads into scope for regulated data handling.

---

### Azure Credit Discrepancy Triggers $16K Bill — a Cautionary Tale for AI Workloads

A case documented in The Register on 22 September illustrates a risk that enterprise finance and cloud operations teams should treat as a live concern. A customer running AI workloads on Azure continued provisioning services after their Azure credit balance had been exhausted — because Microsoft's Founders Hub portal showed a healthy credit balance while the billing portal had already zeroed the account. The discrepancy ran for five weeks, accumulating $16,000 in charges driven primarily by AI workload costs.

The underlying problem is not unique to this customer. Microsoft operates multiple portal surfaces — Azure Portal, Founders Hub, admin.microsoft.com, Cost Management — that pull billing data from different back-end systems on different refresh cycles. For general workloads this rarely causes harm. For AI workloads, where per-hour costs for GPU inference can run to hundreds of dollars and agents can sustain high utilisation autonomously, even a short period of unchecked spending produces significant charges.

**Action required:** If your AI workloads run under an Azure credit arrangement (MACC drawdowns, promotional credits, or startup programme grants), verify that your cost alerting is anchored to the billing API, not a portal summary. Set budget alerts at 50%, 75%, and 90% of your credit envelope through Azure Cost Management — these trigger against actual spend, not portal-rendered balances. Review whether any Foundry-hosted agents are configured to scale-to-zero when idle; agents left running at low utilisation accumulate costs without producing value.

---

## Enterprise Platform

### Copilot Deep Citations Reaches General Availability

Copilot Deep Citations is now generally available for Microsoft 365 commercial tenants on desktop, Mac, and web. The feature links each Copilot response directly to the specific passage in the source document that informed it — not just a file reference, but a highlighted excerpt that lets users verify the claim without reading the whole document.

The initial scope covers Word and PowerPoint references, with support for meeting transcripts, web content, and PDFs confirmed for a later rollout date. No admin action is required; the feature activates automatically for licensed users.

For regulated industries where Copilot adoption has stalled over concerns about citation accuracy and auditability, this addresses the most concrete objection directly. A compliance officer can open a document, see exactly which paragraph the agent cited, and judge whether the citation is appropriate — rather than accepting the output on faith.

The roadmap entry (RM523223) has been tracking since August preview. Tenants already in the August preview will see no change; those outside it should expect the feature to appear in the coming days if not already visible.

**What this means for you:** Deep citations transform Copilot from a summarisation tool into a verifiable research assistant in the eyes of most legal, finance, and compliance functions. The feature does not change what Copilot can access — it only makes the access visible. If your deployment has been waiting on a trust signal before expanding Copilot to sensitive document libraries, this is it.

---

### SharePoint Copilot Citation Analytics Now Live for Most Commercial Tenants

SharePoint has quietly added a metrics layer showing how often each document, page, or news post has been cited by Microsoft 365 Copilot across the tenant. The feature is rolling out to tenants with fifty or more Copilot licences and requires no admin configuration.

In practice, administrators and content owners can now see a Total citations card on site analytics pages, a Popular content view ranked by citation frequency, and a per-file AI citations metric alongside the existing views and viewers columns. The data reveals which SharePoint content is actually being fed into AI responses — a question that previously had no answer.

This matters operationally because it inverts the information security problem. Rather than trying to prevent all content from reaching Copilot, teams can identify exactly which documents are being cited and audit whether they should be. High-citation documents that carry no sensitivity label become an immediate governance priority. Low-quality or outdated documents that Copilot is citing frequently become a content governance priority.

**Action required:** Once the analytics surface in your tenant, pull the first citation report and filter for content with high citations but no sensitivity label applied. This is your highest-priority labelling backlog for Copilot readiness. Share the data with site owners — many will not know their content is being cited and will have strong opinions about whether it should be.

---

### Copilot in Excel — Finance Skills and Trusted Data Connectors

A September 17 update to Excel's Copilot integration adds capability aimed specifically at finance teams: structured skills for planning, forecasting, valuation, and reporting workflows; trusted data connectors that let Copilot pull from approved finance systems without manual data import; plan-before-action guidance that shows users what Copilot intends to do before it modifies a model; and change tracking that records what Copilot altered and why.

The change tracking and plan-before-action elements address the control failure mode that enterprise finance teams raised most persistently: Copilot modifying a complex financial model in ways that were hard to audit or reverse. The answer Microsoft has landed on is explicit confirmation steps and a change log, rather than limiting what Copilot can do.

**What this means for you:** If your finance team has avoided Copilot in Excel because of concerns about model integrity, the September update is the right time to restart the pilot conversation. The controls are not perfect — the change log is per-session and does not integrate with Excel's existing version history — but they represent a meaningful improvement over the previous state. Budget templates and forecasting workbooks are the highest-value starting point.

---

### Copilot Cowork Comes to iOS and Android

Microsoft has extended Copilot Cowork's autonomous task delegation to mobile. Users on iOS and Android can now hand off multi-step tasks, monitor progress, and receive completed outputs through the Microsoft 365 Copilot mobile app. The mobile release also introduces reusable skills — saved task templates that users can invoke with a single tap — and an expanded plugin library covering Microsoft 365 apps and selected third-party tools.

**What this means for you:** The mobile release primarily affects knowledge workers who spend significant time away from a desk — field sales, operations managers, executives. The compliance controls that shipped with the June GA still apply to mobile-originated tasks (audit logging, sensitivity label inheritance, eDiscovery), so the governance posture does not change. GCC and GCC High tenants should note that Cowork GA for those environments is targeted for November 2026.

---

## Agentic AI

### Foundry Hosted Agents Gain Resilience Controls in Preview

Long-running Foundry hosted agents can now survive two scenarios that previously caused silent failure: an agent working through a multi-hour process no longer disappears if the originating request disconnects, and agents can recover automatically if the hosting process stops unexpectedly mid-task. The mechanism is a durable work identity and lease-based recovery system — the agent holds a lease on its in-progress state, and if the process drops, a new instance picks up the lease and continues from where it stopped.

Each agent session also receives a sandboxed persistent file system for its duration, meaning agents that generate intermediate files do not lose that work on process restart. Microsoft published sample code for resilient workflow patterns on 21 September, giving developers a concrete starting point.

The scale-to-zero model remains in place: agents that are idle consume no compute resources. This means the cost and failure-recovery profiles are now both addressed — a combination that significantly improves the case for running production agents against long-horizon tasks.

**What this means for you:** The practical unlocked use case is overnight agents: an agent set to process a backlog of documents or perform a multi-system reconciliation overnight no longer requires a babysitting process to monitor it. Before deploying any long-running agent to production, review the durable identity documentation to understand how lease expiry interacts with your existing job-monitoring and alerting patterns. The resilience model is in preview, so treat it as appropriate for testing and staged rollout rather than tier-1 production workloads.

---

## Infrastructure

### GPT-Live-1 Enters the Foundry Model Catalog

GPT-Live-1 is now listed in the Microsoft Foundry model catalog (model version dated 9 September 2026), with broad availability rolling out across regions this week. The model is designed for continuous, full-duplex audio interaction — it processes incoming speech while generating its response simultaneously, unlike turn-based voice models that must finish listening before they begin speaking.

This sits alongside GPT-image-2.5, which reached Foundry availability on 8 September and added a Sketch capability (turning user drawings into AI-generated images) alongside a 50% reduction in generation latency compared to image-2. Two variants are available: Flare (optimised for speed) and Sunburst (optimised for detail).

For most enterprise teams, these are platform infrastructure updates rather than immediate deployment decisions. The more relevant signal is the direction of travel: Microsoft Foundry is acquiring the full stack of frontier multimodal models, giving enterprise developers access to capabilities that previously required direct OpenAI API contracts.

**Licensing note:** GPT-Live-1 is provisioned through Foundry's standard token consumption model. Audio tokens are priced differently from text tokens — review the Foundry pricing page before building cost models for any voice application.

---

## Dates to Watch

| Date | Event |
|------|-------|
| Now (rolling) | Copilot Deep Citations GA — activating for commercial tenants, no admin action needed |
| Now (rolling) | SharePoint Copilot citation analytics — visible for tenants with 50+ Copilot licences |
| Now (rolling) | GPT-Live-1 available in Foundry model catalog |
| Now (preview) | Foundry hosted agents resilience — enrol non-production workloads |
| Now (preview) | Foundry IQ permissions sync and sensitivity-label controls — test against restricted content |
| November 2026 | Copilot Cowork GA for GCC and GCC High (FedRAMP compliance pending) |
| TBC | Deep citations support for meetings, web, and PDF references |

---

*Sources: Microsoft Tech Community (Azure AI Foundry Blog, M365 Copilot Blog, Security Copilot Blog, SharePoint Blog), Microsoft DevBlogs (Foundry), Microsoft Learn, Petri.com, The Register, SharePoint Stuff (roadmap roundup 21 September), Microsoft Roadmap (RM523223, MC1247902).*

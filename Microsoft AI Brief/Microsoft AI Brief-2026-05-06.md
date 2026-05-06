# Microsoft AI Brief — 6 May 2026

**Period covered: 30 April – 6 May 2026**

---

## Security & Safety

### Security Copilot Lands in Every E5 Tenant — But the Agents Are Still Metered

The phased rollout of Security Copilot to Microsoft 365 E5 tenants started April 20 and runs through June 30, 2026. Most enterprise security teams are now encountering Copilot inside Defender XDR whether they actively provisioned it or not. The licensing change was written into product terms from January 1, but tenant enablement is only materialising now.

What is actually shipping — and what still costs extra — varies by capability:

**Copilot Chat in Defender** went GA with the April update. It provides conversational Q&A inside the Defender XDR portal sidebar, grounded in incident and entity data. This is covered under E5 with no additional billing.

**Phishing Triage Agent** is also GA. It handles user-reported phishing through Defender for Office 365 Plan 2, classifying submissions and drafting remediation steps autonomously.

**Security Alert Triage Agent** entered preview in April. It extends agentic triage beyond phishing into identity and cloud alerts.

**Security Analyst Agent** has been in preview since March 26. It performs multi-step investigations across Defender and Sentinel telemetry, processing up to around 100 MB of security data per session.

The distinction matters for budgets: Copilot Chat in Defender is included in E5. The autonomous agents — Alert Triage and Analyst in particular — still consume Security Copilot Units (SCUs), billed separately at consumption rates.

**Action required:** SOC leads should audit which agents are active in their tenants before the June 30 rollout completes. Enabling autonomous agents without a governance review introduces both scope risk and unexpected SCU spend.

---

### Security Copilot Email Summary Reaches GA This Month

Public preview launched mid-April; general availability is expected to complete by mid-May 2026. The feature adds an AI-generated narrative directly to the Email entity page inside Defender XDR. Rather than analysts manually correlating metadata, URL verdicts, and attachment analysis, the summary surfaces a coherent natural-language account of what happened, what automated actions were taken, and where residual risk remains.

The capability draws on email metadata, timeline events, URLs, and attachments and presents findings in the same Copilot right-side pane used for other Defender investigations. Access requires Security Copilot licensing (SCU-based).

Email remains the dominant initial access vector in enterprise incidents. Faster triage at the email entity level reduces mean-time-to-understand for analysts processing high volumes. Security teams reviewing SCU budget for Q3 should include this feature when modelling consumption.

---

## Enterprise Platform

### Microsoft 365 E7 Goes GA at $99 Per User Per Month

Microsoft's new top-tier SKU, Microsoft 365 E7, reached general availability through CSP partners on May 1, 2026. At $99 per user per month on annual commitment, it bundles Microsoft 365 E5, Microsoft 365 Copilot, the Microsoft Entra Suite, and the newly GA Microsoft Agent 365 into a single line item.

Purchased separately, the same components total roughly $117 per user per month, so the bundle represents approximately a 15% saving. Introductory volume discounts extend that further: 10% off for 10 or more seats and 15% off for 100 or more seats, available through December 31, 2026.

Agent 365 — which provides the governance and management plane for AI agents deployed across Microsoft 365 — also reached general availability independently on May 1. It was previously accessible only through the Microsoft Frontier early-access programme, so this is its first broadly available release.

For organisations already on E5 that are actively evaluating Copilot licences, E7 is worth modelling against the cost of separate Copilot and Agent 365 add-ons. The Agent 365 governance tooling — audit logs, agent lifecycle management, deployment controls — has operational value beyond the base Copilot capability, particularly for regulated industries.

**Date to watch:** E7 introductory pricing expires December 31, 2026.

---

### Federated Copilot Connectors Bring Live External Data via MCP

Microsoft began rolling out Federated Copilot Connectors to the Microsoft 365 admin center from April 20, with user availability expected to complete by late May 2026. These represent a meaningfully different architecture from the existing synced Graph connectors.

Federated connectors use Model Context Protocol (MCP) to retrieve data from external systems in real time, without indexing that data into Microsoft Graph. For IT teams, the practical difference is the absence of an ingestion pipeline: no crawl scheduling, no Graph index storage overhead, and no lag between source updates and what Copilot sees. Each query goes live to the source system, authenticated through the individual user's own OAuth 2.0 identity and permissions.

The first GA wave covers HubSpot, LSEG, Moody's, and Notion, available inside M365 Copilot and Copilot Researcher. Excel integration is planned for summer 2026.

Federated connectors are **enabled by default** for all tenants once they roll out. Admins can manage and disable individual connectors through the Microsoft 365 admin center.

**Action required:** The default-enabled stance is a change from the indexed connector model, where IT controlled provisioning. Tenant admins should review which connectors are appearing in their environment and determine whether the default-on posture fits their data governance policy, particularly where external financial data providers (LSEG, Moody's) are concerned.

---

## Agentic AI

### Microsoft Agent 365 and Agent Framework 1.0: Two Pieces of the Production Agentic Story

Two related but distinct milestones landed this week and last, and they are easy to conflate.

**Microsoft Agent 365** (GA May 1) is the enterprise management control plane for AI agents deployed across Microsoft 365. It handles governance, audit logging, lifecycle management, and deployment policy for Copilot agents. It ships as part of E7 or as a standalone add-on.

**Microsoft Agent Framework 1.0** (GA April 3) is the open-source developer SDK for building those agents in the first place — available for both .NET and Python. It emerged from merging the enterprise foundations of Semantic Kernel with the orchestration patterns of AutoGen.

Key capabilities at 1.0 that matter for enterprise development teams:

**Orchestration patterns** include Sequential (linear handoffs between specialised agents), Group Chat (collaborative multi-agent reasoning), and Magentic-One (task-oriented planning with goal decomposition).

**MCP integration** lets agents dynamically discover and invoke external tools without custom integration code for each source.

**Middleware pipeline** allows cross-cutting concerns — content safety filters, compliance logging, audit hooks — to be injected into the agent execution loop globally, without modifying individual agent prompts. This is the responsible AI affordance that was largely missing from earlier experimentation-phase frameworks.

**Agent-to-Agent (A2A) protocol** provides standardised communication between agents built on different systems.

A browser-based debugger gives developers a real-time visual view of message flows and tool invocations during local development.

The 1.0 designation signals API stability. Teams that held off building production systems because of breaking-change risk between releases now have a stable surface to commit to.

---

## Infrastructure

### GPT-5.5 Generally Available in Microsoft Foundry

OpenAI's GPT-5.5 reached general availability in Microsoft Foundry in late April, with GPT-chat-latest (the faster, chat-optimised variant) rolling out concurrently. Measured improvements over GPT-5.3-chat include:

- 52.5% fewer hallucinations on benchmark evaluations; 37.3% reduction in hallucinated claims on conversations previously flagged for factual errors
- 25–30% fewer output words across common prompts while preserving response quality
- More structured and context-aware function invocation for tool-calling and RAG workflows
- Improved computer-use accuracy and long-context reasoning for sustained agentic tasks

GPT-5.5 is available in Microsoft Foundry for Azure customers and now powers Microsoft 365 Copilot and Copilot Studio as well.

The word-efficiency improvement translates directly to lower output token costs on the same workloads. Teams running GPT-5.3-based production pipelines should benchmark GPT-5.5 for both quality and cost before the next budget cycle — gains of 25–30% on output tokens represent meaningful savings at scale.

---

## Developer Tools

### GitHub Copilot Moves to Metered Billing on June 1

GitHub announced that all Copilot plans switch to usage-based billing on June 1, 2026. Plan prices remain unchanged, but the billing structure underneath them shifts: fixed monthly request allocations (Premium Request Units) are replaced by GitHub AI Credits, consumed based on actual token usage across input, output, and cached tokens.

What changes in practice:

**Code completions and Next Edit suggestions** remain included in all plans and do not consume credits. Core developer flows are unaffected.

**Agentic features** — Copilot Workspace, multi-file agent edits, agent-initiated pull requests — consume AI Credits proportional to compute. Teams that have adopted agent-mode workflows will very likely see cost increases relative to the fixed-allocation model.

**Enterprise baselines**: Copilot Business ($19/user/month) includes $19 in monthly AI Credits per user; Copilot Enterprise ($39/user/month) includes $39. A transitional credit boost runs from June 1 through September 1, 2026 — 3,000 credits for Business users and 7,000 for Enterprise — to cushion the migration.

**Code review** will consume both AI Credits and GitHub Actions minutes.

**Action required:** Enterprise GitHub admins should pull current usage data from the Copilot billing dashboard before June 1 and model projected spend under the credit structure, with particular attention to teams using agent-mode features. The September 1 date is when transitional credits expire and spend could step up noticeably.

---

## Context: UK Government Signals Enterprise Confidence in Copilot

HMRC, the UK's tax authority, this week confirmed it is rolling out Microsoft 365 Copilot to 28,000 staff following a trial that estimated savings of roughly 26 minutes per user per day. The deployment makes HMRC one of the largest single-agency Copilot rollouts in the public sector globally. For enterprise IT decision-makers still in evaluation mode, a regulated government agency of this scale clearing Copilot for broad deployment carries some weight.

---

*Sources: Microsoft Tech Community Hub, Microsoft DevBlogs, Microsoft Azure Blog, Microsoft Security Blog, Petri.com, The Register, GitHub Blog, Windows Forum, Visual Studio Magazine*

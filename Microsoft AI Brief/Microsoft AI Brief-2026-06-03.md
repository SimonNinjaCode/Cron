# Microsoft AI Brief — 3 June 2026

*Enterprise intelligence on Microsoft AI. Coverage: 27 May – 3 June 2026.*

---

## Security & Safety

### Security Copilot is now live in your E5 tenant — check before June 30

The most consequential licensing shift of the year is quietly completing. Since 1 January 2026, Microsoft Security Copilot has been included within Microsoft 365 E5 and Microsoft 365 E5 Security at no additional charge, covering chat, promptbooks, agentic scenarios across Defender, Entra, Intune, Purview, and the standalone portal, plus the Agent Builder and Graph APIs. Microsoft is rolling out tenant activation in phases, with the window running from 20 April through 30 June 2026.

That deadline matters because many E5 tenants have not yet been provisioned. Security teams should confirm their activation status now rather than discovering it after the window closes and needing to raise a support ticket.

What they gain access to is substantial. Three agents are now available or imminent in Microsoft Defender:

**Phishing Triage Agent** (GA) handles user-reported phish through Defender for Office 365 Plan 2, classifying submissions and taking action autonomously. Early data suggests it identifies 6.5× more malicious alerts than human analysts working unaided. St. Luke's University Health Network reports saving more than 200 analyst hours a month.

**Security Alert Triage Agent** (preview, rolled out April 2026) extends the same autonomous triage model beyond phishing into identity and cloud alerts. The longer-term direction is a single consolidated agent covering phishing, identity, and cloud workloads.

**Security Analyst Agent** (announced at RSA Conference 2026) takes a different approach: rather than triaging at alert volume, it performs deep multi-step investigations across Defender and Sentinel telemetry, surfacing high-impact risks with prioritised findings and reasoning in minutes. Microsoft positions this for the analyst who needs breadth — feeding context into incidents rather than reacting to them.

For organisations already on E5, the practical question is change management, not licensing. Deploying autonomous triage agents requires updated runbooks, tuned exclusion lists, and analyst buy-in. Sovereign-cloud and GCC tenants should check regional availability timelines, as activation schedules differ.

**SCU note:** Sentinel-connected scenarios still consume Security Compute Units. The E5 inclusion covers the embedded Defender and Purview workloads; Sentinel usage is metered separately.

---

### Purview DLP now reaches directly into Copilot interactions

Microsoft has extended Purview Data Loss Prevention to cover prompts and responses in Microsoft 365 Copilot and Copilot Chat directly, not just the files that Copilot touches. In May 2026, a major revision to Data Security Posture Management (DSPM) for AI landed with unified AI observability, posture reporting, and embedded Security Copilot agents that can surface and summarise DLP and insider-risk alerts without leaving the Purview console.

For compliance teams this closes a gap that has caused procurement friction: organisations that held back Copilot deployment over concerns that sensitive data could leak through AI responses now have a technically-auditable control layer. DLP policies written for SharePoint and Exchange apply to the Copilot interaction itself.

The Copilot Governance Dashboard, now generally available, provides a single view of who is using which Copilot capabilities, what data is being referenced, and whether any DLP events have fired. Admins can pull this data via the `aiInteractionHistory` Graph API for integration into SIEM pipelines.

**Action:** Compliance and security teams running Copilot in production should review their DLP policies against the new Copilot location type and configure governance dashboards before broad rollout.

---

## Enterprise Platform

### M365 Copilot gets a full redesign and 53 new features — and a July pricing deadline

Microsoft shipped a redesigned Microsoft 365 Copilot on 28 May 2026, the most visible change to the product since launch. The new interface consolidates entry points across the app suite into a single consistent workspace, applies progressive disclosure so users see a focused prompt surface that expands rather than a panel cluttered with options, and loads more than twice as fast (50%+ reduction in load time). Complex chat response times are down 10% as well.

Alongside the redesign, the May 2026 monthly update brought 53 new capabilities. The ones most relevant to enterprise deployments:

**Multi-model choice.** Anthropic's Claude Opus 4.8 is now available inside M365 Copilot for long-running, multi-step tasks — document drafting, data analysis, presentation building. OpenAI's GPT-5.5 Instant is also available, tuned for concision: fewer follow-up questions, less verbosity, better STEM reasoning. Users in Word can select between model families from the compose pane.

**Federated MCP Connectors.** Copilot can now query external systems live at prompt time — Canva, HubSpot, Linear, LSEG, Moody's, Notion — rather than relying on a pre-indexed snapshot. This matters for financial and sales teams whose data freshness requirements the previous connector model could not meet.

**Copilot Notebooks + Teams meetings.** Notebooks now accept individual Teams meetings as knowledge sources, pulling in transcripts, shared files, chat, and notes. Project-based notebooks can accumulate meeting context over time, making it materially easier to onboard someone mid-project.

**Pricing deadline — 1 July 2026.** Microsoft has confirmed that M365 + Copilot Business Bundle pricing increases on 1 July 2026. Organisations renewing or expanding seats before that date can lock in current pricing. Procurement teams should model whether accelerating a renewal makes sense given their planned Copilot seat growth.

---

## Agentic AI

### Build 2026: Microsoft Agent Framework hits 1.0 and the agentic stack goes production-ready

Microsoft Build 2026 (2–3 June, San Francisco) is the clearest signal yet that Microsoft is treating agents as a primary product category rather than a Copilot feature. The headline deliverable is Microsoft Agent Framework 1.0, now generally available in both .NET and Python, with a consistent API surface across both runtimes.

The framework ships with a production-ready agent harness as a first-class concept: skills, context, procedural memory, and middleware are no longer experimental. Graph-based orchestration supports everything from single-agent automations to complex multi-agent workflows where agents delegate to each other.

**Hosted Agents in Foundry Agent Service** reach GA by end of June 2026. Each session runs in its own sandboxed environment with dedicated compute, memory, and filesystem access. The runtime is framework-agnostic, so teams are not locked into the Microsoft Agent Framework to use the hosting layer.

**Foundry Toolkit for VS Code** is now GA: create agents from templates or from a GitHub Copilot prompt, trace runs locally with full visualisation, and deploy directly to Foundry Agent Service from VS Code. Tracing and evaluation for hosted agents follow in late June 2026.

**Publishing to Teams and M365 Copilot** is GA in June 2026, meaning developer teams can ship agents their organisation's users access through the M365 Copilot interface without separate App Store submissions or Teams admin portal workarounds.

**Trust and evaluation framework.** Microsoft published an open trust standard and evaluation harness for agents at Build, covering safety, grounding accuracy, and tool-call reliability across any underlying framework. This matters for enterprise governance: procurement and IT risk teams increasingly require evals before approving agentic tools for production.

For organisations still in proof-of-concept mode on agents, the GA of the hosting layer and the VS Code toolkit removes the main operational blocker. The question shifts from "can we build this" to "how do we govern it."

---

## Infrastructure

### GPT-5.4 mini and GPT-5.4 nano land in Azure AI Foundry for latency-sensitive workloads

Two new models from OpenAI are now available in Microsoft Foundry: GPT-5.4 mini and GPT-5.4 nano. Both are positioned for high-volume, low-latency scenarios — agent pipelines that need fast tool-call execution, classification tasks, and real-time customer interactions that do not require the full capability of GPT-5.4.

The nano tier in particular fills a gap for organisations running agents at scale where token cost and round-trip latency are the binding constraints. Enterprises building large agentic orchestrations can now route commodity reasoning steps to nano and reserve frontier model capacity for tasks that warrant it.

Also rolling out this week: GPT-realtime-translate and GPT-realtime-2 in Foundry, enabling real-time translation and transcription at the API level. Both are relevant for contact-centre and meeting-intelligence applications.

---

## Developer Tools

### GitHub Copilot billing went usage-based on June 1 — and developers are not happy about it

Effective 1 June 2026, GitHub moved all Copilot plans from premium-request counting to token-based AI Credits. Every interaction now consumes credits based on input tokens, output tokens, and cached tokens at published model rates; 1 AI credit equals $0.01 USD.

Seat pricing itself is unchanged: Copilot Business at $19/user/month, Copilot Enterprise at $39/user/month. But the substance of what those prices buy has shifted. Developers quickly noted that switching from a flat request budget to a token budget means certain workflows — long context completions, multi-turn agent sessions, code review on large files — now consume disproportionately more.

Microsoft/GitHub is softening the transition with elevated credit allotments for enterprise customers from 1 June through 1 September 2026, after which allotments return to standard levels. Budget controls are available at user, cost centre, and enterprise levels.

**What IT and FinOps teams need to do now:** Review which developer workflows generate the highest token volumes (generally: agent mode, large-file review, chat with long context). Set cost centre budgets before the grace period ends in September. The token billing model also means model choice matters more than before — switching a workflow from a premium model to a standard model has a direct, visible cost impact.

---

## To Watch

- **June 30, 2026** — Final date for E5 tenant activation for Security Copilot. Confirm status in the Microsoft 365 admin centre.
- **June 2026** — Hosted Agents (Foundry Agent Service) and tracing/evaluation reach GA. Final production-readiness milestone for the agentic developer stack.
- **July 1, 2026** — M365 + Copilot Business Bundle pricing increases. Last opportunity to lock in current pricing on new or expanded seats.
- **September 1, 2026** — GitHub Copilot AI Credit grace period ends. Enterprise allotments revert to standard levels; FinOps teams should have budgets and controls in place before this date.

---

*Sources: Microsoft Tech Community (Azure AI Foundry Blog, M365 Copilot Blog, Security Copilot Blog, Microsoft Defender Blog), Microsoft DevBlogs (Foundry), Microsoft 365 Blog, GitHub Blog, The Register, Petri.com, Practical365, Visual Studio Magazine, InfoWorld.*

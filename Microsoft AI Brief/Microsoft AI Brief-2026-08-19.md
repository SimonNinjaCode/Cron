---
layout:
  width: wide
---

# Microsoft AI Brief — August 19, 2026

*Enterprise-focused coverage of Microsoft AI developments. Week ending August 19, 2026.*

---

## Security & Safety

### Copilot "CoSnitch" vulnerability patched after eight months, but the discovery method raises new questions

The biggest Microsoft security story of the week arrived on August 18, when Varonis Threat Labs disclosed a critical one-click data exfiltration vulnerability in Microsoft Copilot Personal. Dubbed CoSnitch (CVE-2026-24301), Microsoft patched it the same day, closing a flaw Varonis privately reported in December 2025.

The attack chained three linked weaknesses. An undocumented URL parameter, combined with Copilot's standard query function, let an attacker-crafted prompt execute automatically on page load with no user interaction. Once triggered, Copilot could query any connected app and funnel stolen data to an attacker-controlled server through its own URL-fetching capability. One click, no warning.

The discovery method is what makes this operationally significant. Varonis used "meta-hacking": instead of reverse-engineering the system, they socially engineered the AI itself. By reframing questions to look like natural follow-ups, they coaxed Copilot into describing its own attack surface. The AI surfaced the vulnerability during what appeared to be a normal session.

Varonis confirmed no evidence of in-the-wild exploitation, and the patch is server-side so no admin action is needed. Security teams should audit which third-party apps are connected to Copilot Personal accounts across their environment and review what data those connections can reach.

Using an AI to map its own weaknesses will not stay a one-off. Expect similar disclosures as researchers adopt this approach across other AI products.

---

### Security Copilot in Defender moves from assistive to autonomous

At RSA Conference 2026 in March, Microsoft announced the Security Analyst Agent for Microsoft Defender. The agent handles multi-step alert investigations that would typically require senior analyst time and produces natural-language verdicts with transparent decision graphs that walk teams through its reasoning. The companion Security Alert Triage Agent, also in preview, applies dynamic reasoning across evidence to classify and prioritise alerts at scale.

Both agents integrate with third-party tools through Defender's Agents library, including XBOW's Pentest Analysis Agent for vulnerability validation, and run across Microsoft Defender XDR and Sentinel telemetry.

Security teams running Defender XDR with Sentinel should evaluate these agents in a preview tenant now. Autonomous triage requires explicit enablement, and administrators retain full control over scope and action limits. Licensing falls under Security Copilot, included in E5 product terms since January 1, 2026.

---

## Enterprise Platform

### One Copilot app, two identities

Microsoft started rolling out a unified Copilot application this week, folding the consumer app and the Microsoft 365 enterprise experience into a single shell. Mobile and web versions began their worldwide rollout on August 13; Windows and Mac desktop apps follow in mid-September.

Users sign in with a personal account, a work or school account, or both simultaneously and switch between them within the app. Data stays separated: work account content does not mix with personal, and vice versa. The consolidated product keeps the "Microsoft Copilot" name and ships a new icon.

Three features retire on August 18 as part of the transition: Group Chat, Podcasts, and Deep Research. Organisations whose users relied on Deep Research should validate the Researcher agent inside Microsoft 365 Copilot as a replacement before the September desktop rollout.

This is the first structural step toward what Microsoft has called a "super app" planned for later in 2026.

Admin action, time-sensitive. The new unified app carries a different application ID from the standalone Microsoft 365 Copilot app. Conditional access policies, Intune app protection configurations, and app allowlisting rules that reference the old app ID need updating before the desktop rollout in mid-September.

---

### Microsoft 365 E7: Copilot, Agent 365, and Entra Suite in one SKU at $99

Microsoft 365 E7 "Frontier Suite" reached general availability on May 1, 2026, at $99 per user per month. It bundles Microsoft 365 E5, Microsoft 365 Copilot, the Entra Suite, and Agent 365 into a single SKU, roughly $18 per user per month less than buying the components separately.

Agent 365 deserves the most scrutiny. It is a governance control plane for AI agents, integrating with Defender, Entra, and Purview to apply existing security and data policies to every agent running in your environment. For organisations rolling out agentic workflows, this is the policy enforcement layer Microsoft has been promising.

One important caveat for budget planning: the $99 subscription does not cover agent compute costs. Running agents through Copilot Studio or Microsoft Foundry consumes capacity billed separately.

Licensing teams evaluating Copilot or agent deployments should model total cost of ownership against E7, particularly where organisations are already on E5 and considering the $30 Copilot add-on. The break-even depends on planned agent workload volume and Entra Suite utilisation.

---

### Purview DLP policies now reach inside Copilot prompts

Microsoft shipped a governance update that regulated-industry administrators have been waiting for: Data Loss Prevention policies in Microsoft Purview can now target the content of Copilot prompts. If a prompt contains a sensitive information type defined in an existing DLP policy, Copilot can detect and block the interaction before any data reaches the model or a connected web search.

Alongside the DLP update, the Copilot Analytics Dashboard gained expanded access for non-admin roles, per-user satisfaction tracking, and CSV export capability. A new bulk oversharing remediation tool lets administrators identify and disable overly permissive file-sharing links at scale instead of working through them individually.

Regulated industries should map existing Purview DLP sensitive information types to Copilot scopes now. Organisations that have not run a file permission audit ahead of Copilot deployment should use the new oversharing remediation tools before broader rollout.

---

## Agentic AI

### Copilot Cowork is now available to all M365 Copilot licensees

Copilot Cowork, Microsoft's autonomous task-completion agent for Microsoft 365, became generally available worldwide on June 16. It is open to all Microsoft 365 Copilot licence holders without a separate Frontier programme enrolment.

Cowork handles long-running, multi-tool workflows across Microsoft 365 apps, files, and data, planning and executing a task from start to finish and returning a completed deliverable rather than a draft requiring the user to do the remaining work. As of the July 2026 M365 Copilot update, Word, Excel, and PowerPoint agents can be invoked directly inside Copilot Chat by @mentioning them, tightening the integration with familiar Office workflows.

Billing runs on Copilot Credits. Sentinel agent visibility is included, giving enterprise IT and security teams a monitoring trail for Cowork activity alongside other agent workloads in Defender.

Multiple AI models now power the stack. Anthropic Claude Opus 4.8 and Claude Sonnet 5 are available inside Microsoft 365 Copilot for complex multi-step tasks, alongside OpenAI's GPT-5.6 family. Organisations running regulated workflows should confirm which model their agents are using and whether that aligns with their data residency commitments.

Before broad internal deployment, administrators should set Copilot Credits allocations and define usage policies for Cowork, particularly for any workflows that touch regulated or classified data. Enabling Sentinel monitoring from the outset will make future audit requirements easier to meet.

---

## Infrastructure

### Azure crosses $100 billion as Foundry reaches 1,900 models

Microsoft's fiscal Q4 2026 earnings (reported July 30) confirmed Azure revenue surpassed $100 billion for the first time. Microsoft 365 Copilot reached over 30 million paid seats. Azure AI Foundry now catalogues more than 1,900 models, spanning OpenAI, Meta Llama, Mistral, Cohere, Anthropic Claude, and Microsoft Phi.

Hosted agents in the Foundry Agent Service moved to public preview at Build 2026, available across 20 Azure regions globally. The Microsoft Agent Framework reached 1.0 GA in April, merging AutoGen and Semantic Kernel into a single supported SDK for .NET and Python. Organisations building custom agent pipelines should review the new MAF 1.0 documentation before continuing development on legacy AutoGen or Semantic Kernel codebases.

---

*Most significant development this week: Varonis disclosed and Microsoft patched the CoSnitch one-click data exfiltration vulnerability in Copilot Personal (CVE-2026-24301), closing an eight-month window between discovery and fix. The "meta-hacking" technique Varonis used, getting an AI to surface its own weaknesses, will produce further disclosures across the industry.*

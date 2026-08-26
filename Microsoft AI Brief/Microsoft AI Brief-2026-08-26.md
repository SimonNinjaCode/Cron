# Microsoft AI Brief — 26 August 2026

*Enterprise coverage of Microsoft AI developments, week ending 26 August 2026.*

---

## Security & Safety

### Copilot Personal Vulnerability Exposed — and Patched — After Eight Months

Researchers at Varonis disclosed a chained vulnerability in Microsoft Copilot Personal on 18 August, the same day Microsoft shipped the patch. The attack, internally named CoSnitch by the researchers, worked by feeding Copilot a sequence of carefully worded questions until the model progressively revealed details about its own internal architecture and undocumented URL parameters. The final piece — an `autorun=1` parameter that triggers automatic query execution — enabled a full attack chain: memory poisoning, prompt injection via a crafted URL, and data exfiltration from connected personal apps, all with a single malicious link sent to the victim.

Microsoft assigned CVE-2026-24301, scoring it 8.8 under CVSS 3.1 (high severity). The disclosure timeline is notable: Varonis reported the issue in December 2025, meaning it sat unpatched for nearly eight months.

**What this means for enterprise IT:** Microsoft has confirmed that Copilot Personal is the affected surface — the Microsoft 365 Copilot commercial service is not affected, and no customer action is required for enterprise tenants. However, the case exposes a broader concern: employees who use personal Microsoft accounts alongside work accounts may have had personal data at risk. With the unified Copilot app rollout now separating personal and Entra-managed accounts at the data layer (see below), IT teams should confirm users understand which account context they are operating in. The eight-month patch delay also warrants scrutiny when evaluating Microsoft's AI security response posture.

### Security Copilot Agents Expanding Across the SOC

Microsoft's Security Copilot is pushing deeper into daily SOC operations with a growing set of autonomous agents embedded directly in Defender XDR. The Phishing Triage Agent now handles user-reported phishing at scale, classifying alerts and resolving false positives autonomously — St. Luke's Healthcare reports savings of nearly 200 hours per month. The Threat Intelligence Briefing Agent generates daily, tailored threat summaries in the Defender portal to help teams move from reactive to anticipatory posture. A third agent, the Conditional Access Optimization Agent, identifies missing Zero Trust policy gaps and reportedly delivers 204% greater accuracy than manual review.

Sentinel is also evolving. Microsoft's Sentinel MCP Server enables agents to reason across identity, endpoint, cloud, and network signals through a shared data graph, rather than querying each product separately. A new Analyst Notes feature lets security admins control when incident summaries are auto-generated — always, on demand, or by severity threshold — configured directly in the Defender portal.

KuppingerCole's 2026 AI Security Operations Centre report named Microsoft an overall leader, citing Security Copilot's depth of integration across Sentinel and Defender.

**Action required:** Teams evaluating the Phishing Triage Agent and Conditional Access Optimization Agent should assess readiness against their Sentinel licensing. The Sentinel MCP Server integration may require updated connector configuration. Verify that Analyst Notes controls are tuned to your incident response SLAs.

---

## Enterprise Platform

### Unified Copilot App Begins Rollout — Work and Personal in One Shell

Microsoft started the worldwide rollout of a unified Microsoft Copilot app in mid-August 2026, merging the consumer Copilot experience and the Microsoft 365 Copilot app into a single application. The new home is `copilot.cloud.microsoft`. Mobile and web apps are rolling out globally now; Windows and Mac desktop clients follow in mid-September.

The account model matters: users can sign in with a personal Microsoft account, a work or school Entra account, or both simultaneously via an account switcher. Data does not cross the boundary — work data managed by Entra stays separate from personal account data. Consumer-only features being retired from 18 August include Copilot Podcasts and the consumer version of Deep Research. Image creation and consumer chat move into the shared shell.

**What this means for enterprise IT:** The visual separation between consumer and commercial AI surfaces is collapsing into a single app. While Microsoft maintains a data isolation boundary at the Entra layer, the user experience no longer makes that boundary obvious. Teams with policies around personal AI tool use — or managing shared devices — should update acceptable-use guidance and confirm that sensitivity label enforcement and Purview DLP controls are active before the Windows/Mac rollout hits in September. Branding, URL, and support documentation will also need updating in internal IT portals.

### Purview DLP Controls for M365 Copilot — October GA Date to Watch

Microsoft has introduced Purview Data Loss Prevention policy enforcement inside Microsoft 365 Copilot, allowing admins to block regulated data from appearing in Copilot prompts or AI-assisted searches. The Admin Centre now surfaces oversharing risk indicators, counts of DLP-protected Copilot interactions, and a direct toggle to enable Copilot DLP without navigating into the full Purview portal. Admins can detect and remediate overly permissive file access links in bulk.

A further capability — tracked as Microsoft 365 Roadmap ID 559617 — is in development with general availability targeted for October 2026.

**Action required:** Compliance and IT teams should audit existing Purview DLP policies for coverage gaps in Copilot interactions now, ahead of the October release. The new Admin Centre controls remove the previous barrier of requiring Purview portal access, so DLP enablement for Copilot is now a realistic first step even for organisations that have not deeply configured Purview. Check that sensitivity labels are applied to documents in SharePoint and OneDrive — Copilot's label inheritance only works where labels exist.

### Microsoft 365 E7 "Frontier Suite" — What Enterprise Buyers Need to Know

Microsoft's M365 E7 plan, priced at $99 per user per month on an annual commitment, has been generally available since 1 May 2026. It bundles Microsoft 365 E5 ($60), Microsoft 365 Copilot ($30), the Entra Suite ($12), and Agent 365 ($15). Buying those components separately lists at roughly $117, so the bundle represents approximately 15% savings. Introductory promotional pricing applies through existing Enterprise Agreement, MCA-E, and CSP channels — 10% off for 10+ seats, 15% off for 100+ seats.

Agent 365, the newest component in the bundle, is a governance and control layer for AI agents running in the Microsoft 365 environment. It is not an agent-building platform; its purpose is visibility, policy enforcement, and spend management for agents deployed by others.

**What this means for enterprise buyers:** Organisations already running E5 and Copilot should model whether E7 is a better commercial vehicle than separate licensing, particularly if they plan to adopt Agent 365 governance controls as agentic deployments scale. Procurement teams renewing EAs in the next two quarters should request E7 pricing comparisons. Security teams should evaluate whether Agent 365's governance controls meet internal AI risk requirements before assuming a bundle is a straightforward upgrade.

---

## Agentic AI

### Copilot Cowork at General Availability — Compliance Controls in Place, DLP Still Coming

Copilot Cowork — Microsoft's agentic AI service that plans, executes, and delivers completed multi-step work across Microsoft 365 — reached general availability worldwide in June 2026. At GA, the service flows prompts, responses, and generated artifacts through existing Microsoft 365 compliance controls: audit logging, Data Security Posture Management, eDiscovery, Insider Risk Management, and sensitivity label inheritance are all supported. Data Loss Prevention support is listed as coming later.

Billing runs through usage-based Copilot Credits. Administrators manage spend through a Cost Management Dashboard in the M365 Admin Centre, with per-user budget controls and agent visibility through Sentinel integration.

**What this means for enterprise IT:** The compliance control set at GA is workable for many regulated organisations, but the absence of DLP support is a gap worth tracking — particularly for sectors where data classification at the generation layer is a compliance requirement, not an option. Before enabling Cowork for users who handle regulated data, confirm that sensitivity labels are in place and that the eDiscovery and IRM scope covers Cowork-generated artifacts. Set explicit credit budgets at rollout; the usage-based model can produce unexpected spend at scale.

---

## Infrastructure

### Azure AI Foundry Model Roster Broadens — Vercel AI SDK Support Added

Azure AI Foundry (operating under the Microsoft Foundry brand) continues expanding its model catalogue. New Azure OpenAI additions include GPT-realtime-2.1 and GPT-realtime-2.1-mini, targeting low-latency conversational and real-time transcription workloads. Anthropic's Claude is now generally available in Foundry.

Microsoft also extended Vercel AI SDK compatibility beyond Azure OpenAI's chat surface to include Llama, DeepSeek, Mistral, Phi, and Anthropic models, giving teams that already use the Vercel SDK a lower-friction path to model diversity without rewriting provider logic. The recommended architecture for agentic workloads is GPT-5.x as the orchestrator, GPT-5-mini for sub-tasks, and Phi-4 or fine-tuned models for domain-specific components.

**For development teams:** The Vercel AI SDK extension reduces vendor lock-in for TypeScript-based agentic apps. Teams evaluating multi-model architectures on Azure now have a supported, provider-agnostic surface rather than managing separate SDKs per model family.

---

## Regulatory Watch

### UK Competition Probe into Copilot Price Bundling

The UK's Competition and Markets Authority opened an investigation in late July into whether Microsoft misled enterprise customers by adding Copilot features into Microsoft 365 subscriptions and subsequently raising subscription prices. Microsoft disputes the characterisation. The outcome could influence how Copilot is licensed and disclosed in EU and UK enterprise contracts.

**Date to watch:** The investigation is ongoing. UK and EU procurement and legal teams should monitor for any interim findings that affect contract terms or renewal negotiations.

---

*Most significant development this week: Microsoft patched CVE-2026-24301 (CoSnitch), a high-severity Copilot Personal vulnerability that sat unpatched for eight months after disclosure — confirming that enterprise organisations must not assume AI surface vulnerabilities receive the same response priority as traditional software flaws.*

---

*Sources consulted: [The Register](https://www.theregister.com), [Dark Reading](https://www.darkreading.com), [Petri](https://petri.com), [Microsoft Tech Community](https://techcommunity.microsoft.com), [Microsoft DevBlogs](https://devblogs.microsoft.com), [Windows Central](https://www.windowscentral.com), [Redmond Magazine](https://redmondmag.com), [Practical365](https://practical365.com), [4sysops](https://4sysops.com), [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog).*

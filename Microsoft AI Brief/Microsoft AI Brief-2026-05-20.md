# Microsoft AI Brief — 20 May 2026

**Period covered: 14 May – 20 May 2026**

---

## Security & Safety

### Security Copilot Agents in Defender XDR: The Full Picture Ahead of the June E5 Deadline

With the phased E5 Security Copilot rollout running until June 30, 2026, this week brought renewed focus on exactly which agents are production-ready and which remain in preview. The picture is more fragmented than Microsoft's marketing suggests, and that gap matters for SOC teams trying to baseline capacity and SCU consumption before the rollout completes.

The Phishing Triage Agent, the Threat Intelligence Briefing Agent, and Copilot Chat in Defender are all generally available. The Phishing Triage Agent requires Defender for Office 365 P2 and handles user-reported phishing autonomously — classifying, investigating, and closing the low-confidence cases without analyst intervention. The Threat Intelligence Briefing Agent generates tenant-tailored intel summaries on a regular cadence using Microsoft's threat intelligence feeds. Both consume SCUs.

Still in preview: the Security Alert Triage Agent (identity and cloud alerts, rolling from April), the Security Analyst Agent (multi-step autonomous investigation, preview since late March), and the Threat Hunting Agent (natural-language-driven hunting). The Dynamic Threat Detection Agent is the most consequential in this cohort — it runs continuously in the background, correlating across Defender and Sentinel telemetry without requiring an analyst to start an investigation. During public preview it runs free; at GA, currently targeted for late 2026, it moves onto the SCU consumption model and can be disabled by administrators who want to manage spend.

The E5 rollout deadline is the immediate pressure point. Eligible tenants receive a 7-day notification before Security Copilot activates. Organizations that haven't yet modelled SCU consumption against agent usage patterns are running out of runway.

**Action required:** Verify your tenant notification status and model SCU consumption for the GA agents before June 30. Preview agents, particularly Dynamic Threat Detection, are free now but will not remain so at GA — document their usage today to avoid billing surprises.

---

### Purview DLP Guided Diagnostics for Copilot Now Available

Microsoft's Purview Data Loss Prevention integration for Microsoft 365 Copilot added a guided diagnostics experience in mid-May, making it materially easier to troubleshoot why a DLP policy is or isn't blocking a specific Copilot interaction. For teams that deployed DLP-for-Copilot at GA and found policy behaviour opaque, this closes a real visibility gap.

The underlying capability arrived in waves: DLP policies that inspect Copilot prompts before processing are generally available, covering scenarios where a user pastes or references sensitive data in a prompt. The protection for Copilot-assisted web queries — where a prompt triggers an external search that could inadvertently leak data in the query string — remains in public preview.

The diagnostics experience surfaces in the Purview portal and, for tenants with eligible Security Copilot access, generates AI-powered insights about policy gaps. The Copilot Dashboard also gained a CSV export capability this week, which gives compliance teams a straightforward way to pull interaction data for audits or for feeding into existing reporting infrastructure.

**Date to watch:** DLP for web queries is in public preview now; watch for GA announcement in the July–August timeframe. Compliance teams in regulated industries should test the web query protection in preview before relying on it for audit evidence.

---

## Enterprise Platform

### GPT-5.5 Instant Arrives in Microsoft 365 Copilot and Foundry

The most significant model update of the week: OpenAI's GPT-5.5 Instant is now rolling out to Microsoft 365 Copilot users and is available in Microsoft Foundry via the API as `gpt-chat-latest`. Microsoft's own evaluation data shows a 52.5% reduction in hallucinations compared to GPT-5.3-chat, with hallucinated claims in previously-flagged conversations down 37.3%. For enterprise deployments where Copilot is handling document summarisation, meeting recaps, or financial data extraction, those numbers are meaningful — not because hallucinations disappear, but because the frequency drops enough to change how much human review is warranted in steady-state workflows.

The model brings stronger tool calling, deeper long-context reasoning for lengthy documents and threads, and improved agentic execution — the ability to take sequential steps reliably without requiring user intervention at each stage. Microsoft 365 Copilot users with priority access get the upgrade first; standard Copilot Chat users follow on a rolling basis. In Foundry, the model is available through both the Responses API and Chat Completions API, with support for structured outputs, parallel tool calling, and computer use.

For teams running custom agents on Foundry, the switch from a pinned GPT-5.3 or GPT-5.4 deployment to `gpt-chat-latest` is the shortest path to GPT-5.5, but requires accepting that the underlying model will change again when Microsoft updates the alias. Teams with strict versioning requirements should pin to `gpt-5.5-instant` explicitly.

**Action required:** Review any Copilot or Foundry workflows that depend on consistent output formatting — improved tool calling behaviour can shift JSON structures in agentic pipelines. Regression test before promoting to production.

---

### Microsoft Embeds Copilot More Deeply in Word, Excel, and PowerPoint

Starting this week and completing by early June, Microsoft is rolling out a persistent Copilot button at the bottom-right corner of the canvas in Word, Excel, and PowerPoint on Windows and Mac, along with two new keyboard shortcuts: Alt+C to open the Copilot pane from anywhere in the document, and F6 to shift focus to the button from the keyboard. On Mac, Cmd+Control+I does the same. The previous entry points — scattered across the ribbon, context menus, and the floating bar — are being consolidated into this unified model.

The Register framed this as Microsoft making Copilot "harder to ignore," which captures the practical reality: users who have avoided Copilot by not looking for it will now have a permanent visual anchor in every document they open. For enterprises that haven't completed their AI governance and acceptable-use rollout, this accelerates the timeline. When the button appears and employees start clicking it, IT and compliance teams will face questions about data access, whether it can be disabled, and whether usage is covered under existing licensing terms.

The button can be suppressed through Microsoft 365 admin controls for unlicensed tenants, but the default for licensed Copilot environments is on. Admins deploying via Intune or Group Policy should audit their current Copilot feature policies before the June rollout completes.

**Date to watch:** General availability in Word, Excel, and PowerPoint on Windows and Mac targeted for early June 2026. Verify admin policy state before then.

---

### Agent 365 Reaches General Availability; E7 SKU Bundles the Stack

Agent 365 — Microsoft's control plane for managing AI agents across Microsoft 365 — reached general availability on May 1, and its implications are still filtering through enterprise licensing discussions this week. Priced at $15 per user per month, Agent 365 provides the governance layer for deploying, monitoring, and retiring Copilot Studio and third-party agents at scale. It includes audit logging for agent actions, per-agent permission scopes, and integration with Entra ID for identity-based access control on what agents can see and do.

More significant for larger organisations is the new E7 SKU, priced at $99 per user per month, which bundles Microsoft 365 E5, Copilot, Agent 365, and the Entra Suite into a single agreement. For customers currently running E5 plus Copilot licenses separately, E7 is worth modelling: depending on how Entra Suite add-ons are currently licensed, the bundle can be cost-neutral or better.

The governance features in Agent 365 are also the enterprise answer to what analysts have been calling "agent sprawl" — the accumulation of autonomous tools across M365, CRM, and ERP platforms with no unified audit trail. Without a control plane, security teams have limited visibility into what agents are accessing on behalf of users.

**Action required:** If your organisation has more than 50 Copilot licenses, compare current E5 + Copilot spend against E7 pricing. Also assess whether Agent 365 governance features address outstanding requirements from your AI risk register.

---

## Agentic AI

### New Realtime AI Models Roll Out in Microsoft Foundry

Three new OpenAI realtime models entered the Foundry model catalogue from May 6 and have been completing their rollout this week: GPT-realtime-translate, GPT-realtime-2, and GPT-realtime-whisper. The three are designed to operate together for live multilingual scenarios.

GPT-realtime-translate takes live audio input and produces translated speech plus a transcript in the target language — end to end, without a separate speech-to-text step. GPT-realtime-whisper runs in parallel to capture a verbatim transcript of the original speech for archival or captioning purposes. GPT-realtime-2 extends the realtime audio model with adjustable reasoning effort — you can specify minimal, low, medium, or high reasoning at call time — which lets developers tune cost and latency for the complexity of each query rather than paying for full reasoning on every exchange.

The practical use cases are narrow but high-value: live call centres serving multilingual customer bases, international board calls where compliance requires transcription of both the source and translated audio, and voice-driven AI assistants in industries where a text intermediary would introduce unacceptable latency. For most enterprise M365 deployments, these models won't be directly relevant yet — but they are the infrastructure layer that makes future Teams AI meeting features possible.

**Date to watch:** No GA date announced for GPT-realtime-translate; currently in rolling preview in the Foundry catalogue. Developers building voice-first workflows should pilot now to get ahead of the GA demand curve.

---

### Windows 11 Copilot Key Remapping Expands After Backlash

Microsoft confirmed this week that Windows 11 will expand Copilot key remapping options following persistent feedback that the dedicated key — introduced on Copilot+ PCs in 2024 — breaks established keyboard workflows. Administrators and power users who rely on Right Ctrl or the Context Menu key for accessibility tools, terminal shortcuts, or developer environments have had no official reassignment path. Microsoft confirmed the expanded remapping capability will arrive later in 2026.

The announcement is modest in scope but relevant for enterprise device management: organisations deploying Copilot+ hardware at scale have been fielding user complaints about involuntary Copilot activations, and there is currently no MDM policy to reassign the key. Until the remapping feature ships, the only mitigation is disabling Copilot at the OS level entirely, which removes the key behaviour but also removes Copilot access.

**Date to watch:** No specific date given; "later in 2026." IT teams managing Copilot+ PC fleets should document the workaround in their hardware deployment guides and revisit when the update ships.

---

*Sources: [Microsoft Tech Community – Azure AI Foundry Blog](https://techcommunity.microsoft.com/category/azure-ai-foundry), [Microsoft Tech Community – Security Copilot Blog](https://techcommunity.microsoft.com/category/security-copilot/blog/securitycopilotblog), [Microsoft Tech Community – Microsoft 365 Copilot Blog](https://techcommunity.microsoft.com/blog/microsoft365copilotblog), [Microsoft 365 Insider Blog](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/new-copilot-entry-points-smart-suggestions-and-keyboard-first-design/4517930), [Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/), [Azure Blog – GPT-5.5 in Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/), [The Register – Copilot in Office](https://www.theregister.com/personal-tech/2026/05/12/microsoft-makes-copilot-easier-to-summon-harder-to-ignore-in-office/5238612), [Petri – Copilot Purview DLP](https://petri.com/microsoft-365-copilot-purview-dlp-analytics/), [4sysops – Purview DLP for Copilot](https://4sysops.com/archives/microsoft-365-copilot-security-purview-dlp-oversharing-controls-and-dashboard-analytics/), [TechTimes – Windows 11 Copilot Key](https://www.techtimes.com/articles/316815/20260518/microsoft-expands-windows-11-copilot-key-customization-after-user-backlash.htm), [Nerd Level Tech – Agent 365 GA](https://nerdleveltech.com/microsoft-agent-365-ga-ai-agent-control-plane)*

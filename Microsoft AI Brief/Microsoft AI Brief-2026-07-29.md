# Microsoft AI Brief — 29 July 2026

*Enterprise-focused coverage of Microsoft AI developments. Period: 22–29 July 2026.*

---

## Security & Safety

### Microsoft launches its first in-house cybersecurity AI model — and a new agentic security platform

The week's biggest story landed on 27 July when Microsoft announced **MAI-Cyber-1-Flash**, its first AI model designed and built specifically for cybersecurity work. The model is a security-specialised fine-tune of MAI-Code-1-Flash — the lightweight coding model already embedded in GitHub Copilot and VS Code — and draws on more than 100 trillion daily signals across Microsoft's identity, endpoint, cloud, and network telemetry.

MAI-Cyber-1-Flash isn't deployed standalone. It sits inside **MDASH**, Microsoft's multi-agent vulnerability identification and remediation harness, where it works in combination with OpenAI's GPT-5.4. Together they score 95.95% on the CyberGym benchmark — about 12 percentage points above the next best-performing competitor configuration — while running at roughly 50% of the cost of Microsoft's previous production setup. Mustafa Suleyman, CEO of Microsoft AI, framed the economics plainly: "We have world-leading performance at 50% of the cost."

Above MDASH sits **Project Perception**, a higher-order agentic security platform coordinating three classes of specialised agents. Red team agents model adversary movement through an environment; blue team agents investigate signals and prioritise risk; green team agents write patches and harden defences. The system enters **public preview on 3 August**.

**What it means for enterprise security teams:** If Project Perception delivers on its benchmarks in production, it represents a meaningful shift in automated vulnerability management — shifting from periodic scans to continuous, agentic remediation. The August preview is worth evaluating for organisations running Defender Vulnerability Management or Azure Defender workloads. The model was reviewed by Microsoft's AI Red Team, put through adversarial testing, and independently assessed by a third party before release.

**Action:** Register interest in the public preview launching 3 August. Review whether current vulnerability management workflows (including any MDASH integrations) need to be updated to accommodate the new agent-based architecture.

---

### Open Secure AI Alliance: 37 companies unite on open AI security standards

On 27 July, NVIDIA led the launch of the **Open Secure AI Alliance**, a 37-member consortium building shared, open-source cyber-defence tools for AI systems. Microsoft is a founding member alongside IBM, Cisco, Cloudflare, CrowdStrike, Hugging Face, Salesforce, Palantir, Red Hat, ServiceNow, and others. OpenAI, Anthropic, and Google are not members.

The Alliance builds on the Linux Foundation's Akrites initiative and the Open Source Security Foundation. Rather than creating new AI models, it focuses on the security infrastructure surrounding them: open testing frameworks, agent harnesses, and defensive tooling that organisations can inspect, customise, and deploy on their own infrastructure. NVIDIA is open-sourcing the NOOA framework as the technical foundation.

**What it means for enterprise security teams:** The Alliance's open-source orientation is significant. Organisations that can't or won't depend on proprietary vendor security tooling will have a vendor-backed alternative set of frameworks to work from. Given Microsoft's founding membership and CrowdStrike's participation, expect integration with Defender and Falcon workflows over time.

**Action:** No immediate action required. Watch for Alliance framework releases over Q3/Q4 2026 and assess whether any components replace or supplement existing AI security tooling.

---

### Agent 365 license enforcement: AI agent security is no longer included in existing Defender licences

This one is already in effect and organisations may already be experiencing the impact. Since **1 July 2026**, AI agent security capabilities for Microsoft Copilot Studio and Microsoft Foundry agents require a dedicated **Microsoft Agent 365 licence** ($15/user/month standalone, or included in M365 E7 at $99/user/month). These capabilities are no longer covered by existing Defender for Cloud Apps or Defender for Cloud licences. Tenants without an eligible Agent 365 licence lost access on 1 July.

The capabilities now behind the Agent 365 licence include:

- Agent discovery and posture management for Copilot Studio agents
- Agent threat detection and real-time protection
- Advanced Hunting queries over agent activity (now in the new `AgentsInfo` table — the old `AIAgentsInfo` table is deprecated)
- Foundry agent discovery, posture assessment, and threat protection

The Defender portal continues to surface these experiences for licensed tenants. But organisations that had blocking rules in legacy Agent 365 real-time protection will find those rules **stopped enforcing on 1 July**. New rules must be defined under Settings > Security for AI > Policies & rules > Real-time protection.

Third-party cloud agents previously discovered through Defender for Cloud connectors are also no longer discoverable through that path — registry sync must be reconfigured through the Microsoft 365 agent registry.

**Action (if not already completed):** Confirm Agent 365 licence coverage. Update any saved Advanced Hunting queries, custom detections, or workbooks that reference `AIAgentsInfo` to use `AgentsInfo`. Redefine any real-time protection blocking rules. Migrate alert workflows from legacy Defender alerts to Agent 365 observability logs. If unlicensed, a 25-seat, 30-day admin-led trial is available through the Microsoft Admin Center.

---

## Enterprise Platform

### SharePoint Copilot rolls out new capabilities in July 2026

Microsoft published its July 2026 SharePoint Copilot update this week, covering features now rolling out to all users with a Microsoft 365 Copilot licence:

- **Default enablement**: Copilot in SharePoint is now on by default across all licensed tenants — no manual opt-in required.
- **Office document creation from SharePoint content**: Users can ask Copilot to generate a Word document, Excel workbook, or PowerPoint deck directly from site content, turning existing knowledge bases into finished deliverables.
- **Interactive HTML dashboards**: Excel can turn SharePoint list and library data into shareable HTML dashboards.
- **Conversational library management**: Users can reorganise folders, move files, add columns, and create views through natural language commands.
- **AI Skills discoverability**: Typing /Skills in any site surfaces available custom skills in context, making automation more accessible to non-technical users.
- **Natural-language sharing and approvals**: One-command sharing and approval flow configuration.

**What it means for enterprise IT teams:** Default enablement is the most operationally significant change. Admins who have not already reviewed and configured Copilot governance policies in SharePoint should do so now — sensitivity labels, citation controls, and admin toggles are all available but may require configuration.

**Action:** Review SharePoint admin centre settings for Copilot governance. Confirm data loss prevention and sensitivity label policies apply correctly to Copilot-generated content before users begin creating documents from site data.

---

### Copilot Cowork reaches general availability with compliance controls

Microsoft's **Copilot Cowork** — the AI-driven productivity agent that plans, executes, and delivers multi-step work tasks — reached general availability in June 2026, and the accompanying compliance and governance controls are now in full effect. Cowork uses Anthropic's Claude Opus 4.8 and Sonnet 4.6 at launch, with GPT-5.5 available to Frontier programme participants.

The GA release added compliance controls designed for regulated industries: data residency options, audit logging of agent actions, and integration with Microsoft Purview for supervision and content classification. The system was developed in close collaboration with Anthropic, and Microsoft has positioned it as the centrepiece of the "agentic M365" experience.

**What it means for enterprise IT teams:** With Cowork now generally available, governance and audit logging questions that were deferred during preview should be addressed. The Purview integration means organisations with existing information governance policies can extend them to Cowork-generated outputs — but this requires configuration, not just licensing.

**Action:** Review Purview integration setup for Cowork. Confirm audit logging is enabled and routed to your existing SIEM or compliance workflows.

---

## Agentic AI

### Foundry Agent Service adds memory and optimiser in preview

Microsoft Foundry's hosted agent service now offers two new capabilities in preview, published in the June/July documentation cycle:

- **Agent memory**: Persistent memory across agent sessions, allowing agents to accumulate context over time rather than starting fresh each interaction. Memory is configurable per agent and scoped to tenant data boundaries.
- **Agent optimiser**: An automated feedback loop that adjusts agent behaviour based on evaluation results — effectively letting production agents tune themselves against defined quality metrics.

Both capabilities build on the Foundry observability stack announced at Build 2026, which provides end-to-end tracing and evaluation tooling for agents running on any framework.

**What it means for enterprise developers:** Persistent memory is the capability that closes the gap between Copilot-style chat interactions and genuinely agentic workflows. The optimiser is directionally interesting for reducing the manual iteration cycle in production agent deployments, though it requires well-defined evaluation criteria to be useful.

**Action:** Review the new `memory-usage` and `agent-optimizer` documentation on Microsoft Learn. Assess whether memory scoping and retention policies meet your data governance requirements before enabling in production.

---

## Developer Tools

### New OpenAI models land in Microsoft Foundry

Several new models became available in Microsoft Foundry this month:

- **GPT-chat-latest** (GPT-5.5 Instant): Microsoft's newest general-purpose chat model in Foundry, built on GPT-5.4 and GPT-5.3-chat. Delivers improvements in factual accuracy, tool-calling reliability, and response efficiency.
- **GPT-realtime-2.1 and GPT-realtime-2.1-mini**: Updated real-time voice models with expanded context windows and internal reasoning before speaking, enabling more coherent voice agent responses. Added to the Azure OpenAI model catalogue as of early July.

The Foundry model catalogue now spans more than 11,000 models across OpenAI, Anthropic, Meta, Google, xAI, and Hugging Face, accessible through a single endpoint and credential set.

**What it means for enterprise developers:** GPT-realtime-2.1's internal reasoning step is particularly relevant for contact centre and voice assistant deployments where coherence under ambiguous queries has historically required workarounds. GPT-chat-latest's tool-calling improvements reduce prompt engineering overhead in agentic workflows.

**Action:** Review model availability in your Azure region. Update deployment configurations if you're pinned to earlier GPT versions and want to test the new variants.

---

## One to Watch

**Microsoft chief on AI IP risk (13 July):** In a public statement that landed just outside this week's window, CEO Satya Nadella warned enterprise customers to guard their intellectual property carefully when sharing data with frontier AI labs. The comments were interpreted as a competitive signal — Microsoft wants customers running sensitive workloads through its own Azure infrastructure, not third-party providers. Enterprise legal and security teams who haven't reviewed their AI data-sharing agreements in the context of where model training boundaries sit should do so before deploying agentic systems that touch proprietary data.

---

*Sources: [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/), [SecurityWeek](https://www.securityweek.com/microsoft-unveils-mai-cyber-1-flash-its-first-cybersecurity-ai-model/), [The Hacker News](https://thehackernews.com/2026/07/microsoft-says-new-cybersecurity-ai.html), [TechCrunch](https://techcrunch.com/2026/07/27/microsoft-launches-its-first-cyber-model-and-a-new-agentic-cybersecurity-system/), [Petri](https://petri.com/microsoft-project-perception-ai-security-platform/), [NVIDIA Blog](https://blogs.nvidia.com/blog/open-secure-ai-alliance/), [SecurityWeek — Open Secure AI Alliance](https://www.securityweek.com/nvidia-and-tech-giants-launch-ai-security-alliance/), [Microsoft Learn — Agent 365 transition](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365), [TechCommunity — SharePoint Copilot July 2026](https://techcommunity.microsoft.com/blog/spblog/what%e2%80%99s-new-in-copilot-in-sharepoint-july-2026/4535420), [Petri — Copilot Cowork compliance](https://petri.com/microsoft-copilot-cowork-compliance-controls/), [Microsoft Foundry docs — What's new June 2026](https://learn.microsoft.com/en-us/azure/foundry/whats-new-foundry), [TechCommunity — GPT-chat-latest](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-openais-newest-chat-model-in-microsoft-foundry/4516848), [The Register — Microsoft IP warning](https://www.theregister.com/ai-and-ml/2026/07/13/microsoft-chief-turns-hostile-on-frontier-ai-labs-warns-companies-to-guard-their-ip/5270628)*

# Microsoft AI Brief — 9 September 2026

*Enterprise-focused intelligence on Microsoft AI developments. Coverage period: 2 September – 9 September 2026.*

---

## Security & Safety

### Microsoft Releases August Security Roundup — AI Agent Risk Now a Core Defender Signal
*Published 27 August 2026 — Microsoft Security Blog*

Microsoft's August 2026 security roundup formalises AI agents as a first-class risk surface inside Defender. Defender now evaluates posture risk for every agent based on live indicators: configuration gaps, access levels, runtime activity, endpoint and user context, and active alerts. Security teams get a ranked view of which agents deserve immediate attention, not a raw inventory.

Two other retirements land in this roundup with enterprise action windows. Microsoft Defender Threat Intelligence (MDTI) as a standalone product was retired on 1 August 2026; teams that built workflows or SIEM integrations against its dedicated portal need to shift those to Microsoft Defender and Microsoft Sentinel, where the threat intelligence feed continues. Separately, Data Loss Prevention inside Defender for Cloud Apps (MDA) will be deprecated on 31 December 2026, with DLP consolidated into Microsoft Purview. Organisations running MDA DLP policies should begin their Purview migration now to avoid a scramble at year-end.

On a more positive note, auto-labeling policies in Microsoft Purview can now process 500,000 SharePoint and OneDrive files per day, up from 100,000. For large estates, that is a meaningful acceleration of sensitivity-label coverage before Copilot surfaces data at scale. Defender for Identity sensor migration from v2.x to v3.x is also generally available.

**Action required:** Review MDA DLP policy dependencies before 31 December. Begin MDTI portal integration migrations to Defender/Sentinel. Audit Defender's new AI agent risk panel for your tenant.

---

### New Security Copilot Agents Target Threat Detection and Compliance Automation
*Sources: petri.com, Microsoft Security Blog*

Microsoft has continued expanding the Security Copilot agent catalogue. The current lineup spans Microsoft Defender, Microsoft Entra, Microsoft Intune, and Microsoft Purview, with agents handling alert triage, identity governance, device management, and compliance workflows including Data Subject Request automation and policy enforcement.

The Security Analyst Agent is the headline addition: it performs multi-step investigations across Defender and Sentinel telemetry, processes up to roughly 100 MB of security data per session, and surfaces anomalies and high-impact threats with context-rich narratives. For SOC teams drowning in alert queues, the design intent is fewer analyst hours spent on initial triage and more on validated threats. The agent ecosystem in the Security Store now exceeds 70 partner-built agents, broadening the signal sources available without custom integration work.

Licensing note: Security Copilot became part of the Microsoft 365 E5 core entitlement earlier this year and should be active in eligible tenants. Administrators who have not yet enabled it or configured agent policies should check the Security Copilot admin portal.

---

### Microsoft Purview DSPM Gets Renewed Focus as Copilot Deployment Widens
*Sources: petri.com (2 September 2026), Microsoft Learn*

With Copilot Cowork now in general availability and the unified Copilot app moving to desktops this month, Microsoft and third-party analysts are renewing attention on Data Security Posture Management for AI. The core premise: Copilot does not create oversharing problems, it exposes permissions problems that already existed but went unnoticed because no tool queried across the estate that quickly.

DSPM for AI sits in Microsoft Purview and provides a ranked list of issues — overshared content, unprotected sensitive data, missing sensitivity labels, excessive permissions — before those issues become AI-assisted data incidents. Organisations that have not run a DSPM assessment before their Copilot rollout are accepting risk that is discoverable without it. Microsoft Security Copilot integrates with DSPM to allow natural-language investigation of flagged assets and risky user activities.

**Recommended action:** Run a DSPM for AI assessment in the Purview portal before expanding Copilot seat coverage. Prioritise remediation of the highest-exposure findings before the mid-September desktop Copilot app rollout reaches your users.

---

## Enterprise Platform

### GPT-6 Astra Lands on Azure — Early Access Open for Enterprise Customers
*Source: industry reporting, 3 September 2026*

Microsoft announced GPT-6 Astra on 3 September 2026, positioning it as OpenAI's most capable workplace model and making early customer access available through Azure AI Foundry. Astra is framed as a model purpose-built for complex, multi-step agentic tasks at enterprise scale, rather than a general-purpose upgrade to earlier GPT generations.

Details on context windows, pricing tiers, and enterprise SLAs have not been formally published at time of writing. Organisations in Microsoft's enterprise agreement programmes should contact their account team for early-access nomination. For teams already building on Azure OpenAI, Astra will appear in the Foundry model catalogue as it becomes broadly available.

---

### The Unified Copilot App Begins Its Desktop Rollout This Week
*Sources: The Register (13 August 2026), Windows Central, GeekWire*

The consumer Copilot app and the Microsoft 365 Copilot app are now a single application. The mobile and web merger completed in mid-August; the Windows and macOS desktop rollout is beginning in mid-September — meaning it is arriving in managed tenants now. The unified app carries a new icon, keeps the "Microsoft Copilot" name, and consolidates consumer chat and image creation alongside enterprise M365 work experiences in one shell.

This is the first structural step toward a broader "super app" Microsoft has signalled for later in 2026. For enterprise IT, the immediate concern is endpoint management: the merged app behaves differently from the standalone Microsoft 365 Copilot desktop clients some organisations have deployed. Administrators should review Intune or equivalent MDM policies to confirm the unified app is permitted and that enterprise data policies apply cleanly to the new client. The change does not alter licensing; entitlements from existing Microsoft 365 Copilot seats carry forward.

**Watch date:** Mid-September 2026 for broad Windows/macOS desktop rollout completion.

---

## Agentic AI

### HydraFusion Brings Multi-Model Orchestration to GitHub Copilot
*Source: industry reporting*

Microsoft has introduced HydraFusion inside GitHub Copilot, an orchestration architecture that coordinates multiple models across distinct roles — planning, building, critiquing, and completing — for a single coding task. The claimed outcome is coding task completion at up to 67% lower cost compared to routing the same task to a single frontier model.

For engineering organisations managing GitHub Copilot consumption, this is material: complex tasks that previously hit expensive single-model calls may now complete within a cheaper multi-agent pipeline, without developers changing their workflow. There is no opt-in required; the routing happens inside the Copilot runtime.

---

### Copilot Cowork — What the GA Release Means for Compliance Teams
*Sources: petri.com, Microsoft 365 Blog (16 June 2026)*

Copilot Cowork — the agentic feature that executes multi-step tasks from start to finish, including producing artefacts, without requiring the user to manage each step — reached general availability in June. The story that matters for compliance teams is what the GA release included: audit logs, eDiscovery, Insider Risk Management, sensitivity label inheritance, and Data Security Posture Management integration. Data Loss Prevention support is listed as coming later.

Cowork runs on usage-based billing and is administered through the Microsoft 365 admin centre, which now includes a Cost Management Dashboard for monitoring credit consumption and setting budgets. Prompts, responses, and generated artefacts flow through existing Microsoft 365 data governance controls. Sensitivity labels are inherited end-to-end.

For organisations that had been holding Cowork deployment pending compliance answers, the GA controls remove most blockers. DLP support remains outstanding; teams in regulated industries that need DLP coverage on Cowork-generated content should treat that gap as a known limitation until Microsoft confirms availability.

---

## Developer Tools

### Excel's =COPILOT() Function Retires 14 September — Workbook Owners Need to Act
*Sources: The Register (17 August 2026), Office Watch, Neowin*

Microsoft has confirmed that the COPILOT() worksheet function will be disabled in Excel on 14 September 2026. The function never reached general availability — it sat in Frontier and Insider preview for roughly a year — and Microsoft's rationale is straightforward: the Copilot side pane already handles the same capabilities (summarising text, classifying data, generating content, web retrieval) and does so through a conversational interface rather than a cell formula.

The deadline is five days away. Any workbook that contains live =COPILOT() formula calls should be opened, the formula outputs converted to static values, and the formulas removed before the 14th. Microsoft has not clarified whether existing formulas will return errors silently or explicitly after cutoff. Treat them as breaking changes.

The broader lesson here: the side-pane paradigm is winning over worksheet-formula AI in Microsoft's roadmap. Teams that have been waiting on formula-based AI integration for Excel automation should plan around the Copilot pane or the Excel agent rather than further formula functions.

**Action required by 14 September 2026:** Identify and convert any =COPILOT() formulas in shared or automated workbooks.

---

## Key Dates to Watch

| Date | Event |
|------|--------|
| **14 September 2026** | Excel =COPILOT() function disabled — workbook remediation deadline |
| **Mid-September 2026** | Unified Copilot app desktop rollout (Windows/macOS) — review MDM policies |
| **31 December 2026** | MDA DLP deprecated — Purview migration deadline |
| **Ongoing** | GPT-6 Astra early access via Azure AI Foundry — contact account team |

---

*Sources: [Microsoft Security Blog — August 2026](https://www.microsoft.com/en-us/security/blog/2026/08/27/whats-new-in-microsoft-security-august-2026/) · [Security Dashboard for AI GA](https://techcommunity.microsoft.com/blog/microsoft-security-blog/security-dashboard-for-ai---now-generally-available/4494637) · [Security Copilot at Greater Scale](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/microsoft-security-copilot-ai-driven-security-operations-at-greater-scale/4528912) · [Copilot Cowork GA](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/) · [Petri — Copilot Cowork Compliance](https://petri.com/microsoft-copilot-cowork-compliance-controls/) · [Petri — Security Copilot Agents](https://petri.com/security-copilot-agents-threat-detection-compliance/) · [Petri — Purview DSPM](https://petri.com/microsoft-purview-data-security-posture-management/) · [The Register — Unified Copilot App](https://www.theregister.com/ai-and-ml/2026/08/13/microsofts-dueling-copilot-apps-have-combined-into-a-single-entity/5287512) · [The Register — Excel COPILOT function](https://www.theregister.com/ai-and-ml/2026/08/17/excels-copilot-function-is-headed-for-the-recycle-bin/5288327)*

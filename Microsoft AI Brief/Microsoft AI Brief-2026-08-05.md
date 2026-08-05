# Microsoft AI Brief — 5 August 2026

*Enterprise intelligence on Microsoft AI. Covering 30 July – 5 August 2026.*

---

## Security & Safety

### AI Worm Spreads Through Word Documents Via Copilot — Not Yet Fully Fixed

The most significant security story of the week is also one of the first of its kind in a mainstream productivity suite. Norwegian researcher Håkon Måløy publicly disclosed a self-propagating AI worm targeting Copilot for Word on 28 July, 144 days after he first reported it to Microsoft on 6 March.

The attack works by hiding malicious instructions as white text on a white background inside a Word document. When a user feeds that document to Copilot to assist with drafting or editing, Copilot strips the formatting, reads the hidden text as instructions, and follows them — including embedding the same hidden payload into the output document. A market analysis downloaded from a compromised site, included in a Copilot-assisted financial report, can silently alter figures in the report and pass itself along to anyone who receives that report and does the same.

Reworded versions of the attack still worked as of late July, meaning the underlying vulnerability class has not been closed. Microsoft has not issued a patch or advisory.

**What IT and security teams should do now:** Audit which external documents employees are routing through Copilot for Word. Restrict the use of Copilot with documents from untrusted sources where possible. Brief SOC and communications teams — the data-integrity risk (silent alteration of financial or contractual content) is as serious as the propagation risk. Monitor the Microsoft Security Response Center for an advisory.

---

### UK's CMA Opens Bait-and-Switch Probe Into Copilot Price Bundling

Britain's Competition and Markets Authority opened a formal investigation into Microsoft on 27 July over whether consumer Microsoft 365 customers were given adequate information before being moved onto a more expensive subscription tier when Copilot features were added to their plans.

The background: in January 2025, Microsoft folded Copilot into its Personal and Family consumer subscriptions. At renewal, customers were automatically migrated to the Copilot-equipped tier — priced at £84.99 a year versus £59.99 for the now-renamed "Classic" plan — unless they actively opted down or cancelled. The CMA is examining whether customers had clear enough information to make that choice before it was made for them.

Similar investigations are underway in Australia and Italy. The CMA has indicated it may expand scope to cover enterprise bundling practices. One analysis put the maximum penalty exposure at up to 10% of global revenue.

**What enterprise teams should watch:** The outcome of this probe has real implications for how Microsoft structures future AI feature bundling in commercial M365 agreements. Procurement and vendor management teams should track the CMA timeline and consider what opt-out or tiering rights current contracts provide.

---

### Security Copilot: New Defender Capabilities, Licensing Change Takes Effect

Microsoft published its July 2026 security update on 30 July, including several developments worth noting in combination.

A new prompt injection protection feature entered preview in Microsoft Defender. It identifies and quarantines emails containing malicious AI instructions before delivery — a direct complement to the Word worm story above, and a signal that Microsoft is treating prompt injection as a systematic threat class rather than isolated incidents.

The autonomous SOC agent picture also expanded. New multi-agent workflows in Defender pair red team agents (exposing weaknesses), blue team agents (investigating threats), and green team agents (hardening what's found) in continuous loops, executing end-to-end security workflows without manual handoffs between stages.

A licensing change that took effect 1 July is also worth flagging: AI agent security capabilities for Microsoft Copilot Studio and Azure Foundry agents now require a Microsoft Agent 365 license. Organizations that had been relying on existing Defender for Cloud Apps or Defender for Cloud licenses to cover these capabilities are now out of compliance unless they have upgraded. Check your license estate.

---

## Enterprise Platform

### Microsoft Closes FY2026: Azure Crosses $100B, Copilot Reaches 30 Million Paid Seats

Microsoft reported Q4 FY2026 earnings on 29 July. The headline numbers: total quarterly revenue of $90 billion (beating estimates), EPS of $4.81, and Azure growth of 43% year-over-year — the highest quarterly rate in several years. For the full fiscal year, Azure crossed $100 billion in annual revenue for the first time.

Microsoft 365 Copilot reached 30 million paid seats in the quarter, up from roughly 20 million at the end of Q3 — a 50% jump in three months. Daily active usage rose tenfold year-over-year, and the number of enterprise customers deploying Copilot at significant scale (Microsoft's internal threshold) tripled.

For Q1 FY2027, CFO Amy Hood guided to 45% Azure growth at constant currency, above both Q4's rate and analyst consensus.

Two contextual notes that matter for enterprise buyers. First, The Register reported this week that only 3.3% of users who access Copilot Chat actually hold paid Copilot licenses — a reminder that free-tier exposure is substantial and data governance policies should cover both. Second, the class action filed earlier this year alleging Microsoft made misleading statements about Copilot adoption is still active.

---

### M365 Copilot July Update: GPT-5.6, Claude Sonnet 5, and 40+ Feature Rollouts

The July 2026 M365 Copilot release is unusually large. Two new foundation models arrived: OpenAI's GPT-5.6 family, positioned for knowledge work with stronger multi-step reasoning, and Anthropic's Claude Sonnet 5, aimed at agentic tasks including document drafting, spreadsheet analysis, and presentation creation. Both are available now for licensed M365 Copilot users; model switching is not currently exposed to end users.

Feature highlights with enterprise relevance:

- **App agents in Copilot Chat:** Users can now @mention the Word, Excel, or PowerPoint agent directly in Copilot Chat to create deliverables without leaving the conversation surface.
- **Copilot in Outlook now reasons across the full inbox and calendar**, not just single threads — useful for summarisation and action extraction at scale.
- **SharePoint content creation:** Copilot can now generate Word, Excel, and PowerPoint files directly from SharePoint content, reducing copy-paste workflows.
- **PowerPoint Agent Mode** builds decks grounded in the user's own files, meetings, and email through Work IQ.
- **Copilot Notebooks** can now export to Word, Excel, or PowerPoint and generate mind maps from note content.

Admins: review the updated sensitivity label and data loss prevention controls before enabling Agent Mode features in regulated environments. Microsoft published updated compliance documentation alongside this release.

---

## Agentic AI

### Copilot Cowork: Compliance Controls Land as Enterprise Adoption Accelerates

Copilot Cowork went generally available on 16 June for M365 Copilot customers, and the compliance control set that arrived with it deserves a closer look now that deployments are scaling.

Cowork is Microsoft's agentic AI layer for Microsoft 365 — it plans, executes, and tracks multi-step work across the M365 surface using organisational context. Think of it as an autonomous workflow runner that operates within your existing Microsoft 365 tenant rather than a separate system.

The compliance architecture at GA includes sensitivity label inheritance and display on all Cowork outputs, full audit logging, interaction content in the Data Security Posture Management Activity Explorer, support for eDiscovery and Data Lifecycle Management, Insider Risk Management integration, and Communication Compliance coverage of Cowork interactions. This brings Cowork broadly in line with the compliance posture of other M365 workloads.

Licensing: Cowork requires an M365 Copilot license and charges usage-based billing through Copilot Credits. Administrators can monitor credit consumption and set budgets through the new Cost Management Dashboard in the M365 admin centre. Microsoft reports Cowork has been adopted by more than half the Fortune 500 companies that have deployed M365 Copilot.

**Admin action:** If you enabled Cowork during preview, verify that your Communication Compliance and eDiscovery policies have been updated to cover Cowork interactions. These are not automatically inherited from existing policies.

---

## Infrastructure

### Microsoft 365 E7 and the Agent 365 Licensing Layer

For teams still working through the licensing implications of Microsoft's AI push, the E7 (Frontier Suite) SKU is the consolidation point to understand. Available since 1 May at $99 per user per month, it bundles Microsoft 365 E5, Microsoft 365 Copilot, Agent 365, and the Microsoft Entra Suite — saving approximately $18 per user per month against buying the components separately.

Agent 365 — also available standalone at $15/user/month — is the control plane Microsoft has built for managing AI agents as organisational entities. It gives agents their own identities, permissions, and security guardrails within Entra, and is now the required license for AI agent security capabilities in Copilot Studio and Foundry (as noted above in the Security section). Organisations that are building or deploying autonomous agents and have not yet evaluated whether they need Agent 365 should do so before the end of Q3.

---

## Dates to Watch

| Date | What |
|------|------|
| **Ongoing** | Word/Copilot AI worm — no patch issued; monitor MSRC |
| **Q3 2026** | CMA investigation timeline; watch for statement of objections |
| **1 July 2026** (already in effect) | Agent security capabilities require Agent 365 license |
| **FY27 Q1 guidance** | Azure 45% growth at constant currency — next earnings Oct 2026 |

---

*Sources: Microsoft Tech Community, Microsoft Security Blog, The Register, CybersecurityNews, Petri.com, Practical365, Microsoft Investor Relations, Malwarebytes, GBHackers, Futurum Group, TechTimes.*

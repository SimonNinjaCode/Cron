---
layout:
  width: wide
---

# Microsoft AI Brief — prompt

Read the root [RUNBOOK.md](../RUNBOOK.md) before executing this prompt.

Write the report in Swedish. Keep established technical terms, product names and CVE identifiers unchanged.

You are producing the weekly Microsoft AI Brief — an enterprise-focused newsletter covering Microsoft AI developments from the past 7 days.

Determine the run date in Europe/Stockholm. Use Europe/Stockholm timezone. The report covers the 7 days ending today.

Step 1 — Parallel web searches across Microsoft AI sources (last 7 days):
- Azure AI blog: site:techcommunity.microsoft.com "Azure AI" OR "Azure OpenAI"
- M365 Copilot: site:techcommunity.microsoft.com "Microsoft 365 Copilot"
- Security Copilot: site:techcommunity.microsoft.com "Security Copilot"
- Microsoft DevBlogs AI: site:devblogs.microsoft.com AI agent

Step 2 — Prioritise stories in this category order: 1) Security & Safety, 2) Enterprise Platform, 3) Agentic AI, 4) Infrastructure, 5) Developer Tools.

Step 3 — Fetch full content for the top 5–7 stories.

Step 4 — Write an enterprise-focused newsletter. For each story: what changed, what it means for enterprise IT/security teams, any action required or date to watch. Organise by priority category.

Step 5 — Edit for clear, direct prose. Do not invoke editing skills unless explicitly requested. Avoid: "delve", "it's worth noting", em-dash overuse, numbered lists where prose is more natural.

Save the report in this folder as `Microsoft AI Brief-YYYY-MM-DD.md`, using the Stockholm run date. Follow RUNBOOK.md for validation and publishing.

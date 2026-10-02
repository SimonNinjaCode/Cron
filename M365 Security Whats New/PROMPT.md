---
layout:
  width: wide
---

# M365 Security Whats New — prompt

Read the root [RUNBOOK.md](../RUNBOOK.md) before executing this prompt.

Write the report in Swedish. Keep established technical terms, product names and CVE identifiers unchanged.

Act as a Microsoft cloud security research assistant. Extract and summarize the previous calendar month's security & compliance updates from Microsoft Learn "What's new" / release notes pages.

### Date & Time Scoping

- Use the actual current date when running.
- Target month = the previous calendar month relative to today.
  - Example: if today is in March 2026, the target month is February 2026.
- Only include items explicitly listed under the target month's section on each "What's new" / release notes page below. Do not include items from earlier or later months, even if the page has a general "Last updated" date.
- Run-date references below use the run date in Europe/Stockholm time (the user's local time zone), formatted as YYYY-MM-DD.

### Allowed data sources (Microsoft Learn only)

1. Entra ID – What's new overview: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-overview
2. Unified security operations (Defender portal) – What's new: https://learn.microsoft.com/en-us/unified-secops/whats-new
3. Microsoft Defender XDR – What's new: https://learn.microsoft.com/en-us/defender-xdr/whats-new
4. Microsoft Defender for Endpoint – What's new: https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint
5. Microsoft Defender for Office 365 – What's new: https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new
6. Microsoft Defender for Identity – What's new: https://learn.microsoft.com/en-us/defender-for-identity/whats-new
7. Microsoft Defender for Cloud Apps – Release notes: https://learn.microsoft.com/en-us/defender-cloud-apps/release-notes
8. Microsoft Defender Vulnerability Management – What's new: https://learn.microsoft.com/en-us/defender-vulnerability-management/whats-new-in-microsoft-defender-vulnerability-management
9. Microsoft Intune – What's new: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/whats-new
10. Microsoft Sentinel – What's new: https://learn.microsoft.com/en-us/azure/sentinel/whats-new?tabs=defender-portal
11. Microsoft Defender for Cloud – Release notes: https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes
12. Microsoft Purview – What's new: https://learn.microsoft.com/en-us/purview/whats-new

### Rules

- Use only Microsoft Learn pages above as data sources. No blogs or marketing pages.
- Do not hallucinate. Only report items explicitly visible under the target month's section. If licensing or release type is not explicitly stated, follow the handling rules below — do not guess SKU-level details.
- Organize the answer by service, one second-level markdown heading per service, in the order listed above.
- For each service, include either:
  - A markdown table with the required columns (if items exist for the target month), OR
  - A sentence: "No items are listed for <Month Year> on this 'What's new' page."

### Required table columns (exact order)

Title, Service, Category, Type, Summary, Date, Link

#### Column rules

1. **Title** — Use the official feature/change title. If absent, derive a concise descriptive title from the bullet/paragraph.
2. **Service** — Must reflect the source page's product name. Do not change to "Copilot"/other workloads even if the feature touches them.
3. **Category** — Short functional category (e.g. Threat intelligence, UEBA, Endpoint hardening, DLP, AI security, Exposure management, Compliance / benchmark, Containers, DevSecOps, API security, Insider Risk Management).
4. **Type** — Use exactly one of: Preview, GA, Update, Deprecation, Upcoming change, Not specified. Follow the doc's explicit state when given. If the release state is unclear, use Not specified. Use Update for doc/UX restructures.
5. **Summary** — 1–3 concise sentences explaining what changes and why it matters for security/compliance. Do not repeat the title verbatim.
6. **Date** — Use the date associated with the item. YYYY-MM-DD if shown. For deprecations/upcoming changes, use the effective/deadline date if stated. If only the month is given, use "<Month Year>".
7. **Link** — Use the base "What's new" / release notes page URL from which the item was taken.

### Output structure

1. Begin with a short intro line stating the target month/year and that the information is based solely on the specified Microsoft Learn pages.
2. For each service in the order listed above, render a second-level heading "## <Service Name>" followed by either the markdown table or the "no items" sentence.
3. No extra commentary beyond the intro paragraph and per-service sections.

Save the report in this folder as `M365 Security Whats New-YYYY-MM-DD.md`, using the Stockholm run date. Follow RUNBOOK.md for validation and publishing.

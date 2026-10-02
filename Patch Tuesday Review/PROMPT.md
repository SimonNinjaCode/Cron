---
layout:
  width: wide
---

# Patch Tuesday Review — prompt

Read the root [RUNBOOK.md](../RUNBOOK.md) before executing this prompt.

Write the report in Swedish. Keep established technical terms, product names and CVE identifiers unchanged.

Generate the monthly Microsoft Patch Tuesday review for the current month and deliver it to Simon.

1. The "patch month" — typically the current calendar month, since Patch Tuesday falls on the 2nd Tuesday.

2. Gather data via parallel web_search queries. Issue these in parallel, substituting the current month and year:
   - "Microsoft Patch Tuesday {Month} {Year} summary total CVEs zero-day"
   - "Microsoft Patch Tuesday {Month} {Year} critical RCE CVE list"
   - "Microsoft Patch Tuesday {Month} {Year} exploited in the wild publicly disclosed"
   - "Microsoft Patch Tuesday {Month} {Year} BleepingComputer Qualys CrowdStrike breakdown by type"
   - "CISA KEV {Month} {Year} Microsoft CVE deadline"
   Pull from BleepingComputer, CrowdStrike, Qualys, Absolute Security, The Hacker News, Tenable, Rapid7, MSRC release notes when surfaced. Cross-reference at least two sources for every CVE listed.

3. Synthesize into the structured report. Required sections, in order:
   - Title: "# Microsoft Patch Tuesday Review — {Month} {Year}"
   - "_Generated {YYYY-MM-DD}_" (no caveats, no dry-run banners)
   - "## Summary" with bullets: total CVEs patched, zero-days (exploited + publicly disclosed), critical-severity count, Edge/Chromium count if separately released
   - "### Breakdown by type" markdown table: Elevation of Privilege, Remote Code Execution, Information Disclosure, Security Feature Bypass, Denial of Service, Spoofing, Edge–Chromium
   - "## Exploited in the Wild" table: CVE | CVSS | Criticality (Critical/Important/Moderate/Low) | Title | Customer Action | Link. Use "Required" for customer-deployed patches and "Vendor-managed" only where the official source confirms it. Do not mark a customer patched without tenant or device evidence.
   - "## Publicly Disclosed" table: same columns
   - "## Highest Rated — CVSS ≥ 8.0 or Critical" table: same columns. Include any CVE with CVSS ≥ 8.0 OR labeled Critical by Microsoft, even if CVSS isn't published.
   - "## Exploitation More Likely" — list CVEs Microsoft tagged with this exploitability assessment when sources name them; otherwise note that secondary sources don't enumerate them all.
   - "## Notable themes from this month" — 3–5 bullets covering attack surface patterns, infrastructure exposure, attack-chain compositions
   - "---"
   - "## Sources" — bulleted list of every source URL consulted, formatted as `[Publisher — Article title](URL)`. Include the MSRC release-notes link as the last source.
   For any CVE where CVSS or criticality could not be confirmed, write "n/a" in that column. Never fabricate a value.

4. FINAL SUMMARY (chat): one or two sentences naming the patch month, total CVE count, zero-day count.

This runs at 08:00 Stockholm on the Wednesday immediately after the second Tuesday. Verify the current-month release is available before writing. If it is unavailable, report a blocked run rather than relabeling the previous month.

Save the report in this folder as `Patch Tuesday Review-YYYY-MM-DD.md`, using the Stockholm run date. Follow RUNBOOK.md for validation and publishing.

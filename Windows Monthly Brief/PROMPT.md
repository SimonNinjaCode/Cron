---
layout:
  width: wide
---

# Windows Monthly Brief — prompt

Read the root [RUNBOOK.md](../RUNBOOK.md) before executing this prompt.

Write the report in Swedish. Keep established technical terms, product names and CVE identifiers unchanged.

Compile a monthly Windows update brief.

**Section 1 — Windows roadmap features:**
Check the Windows roadmap at https://www.microsoft.com/en-us/windows/business/roadmap with filters set to: Platform = Windows 11 PC, Version = All, Status = All, Feature category = All, Channels = Retail. These are the current public controls; Retail is a channel, not an edition. List only features that are NEW since the previous run of this task (compare the most recent prior report and roadmap-state.json in this folder). For each new feature include: title, status (e.g. Rolling out, In preview), short description, and any version it targets. If nothing is new since last run, say so explicitly.

**Section 2 — Patch information:**
Cover the current Windows 11 version plus the two prior supported versions (verify the currently supported versions and editions against official Microsoft lifecycle documentation). For each version, include both the security update (Patch Tuesday — 2nd Tuesday of the previous month) and the non-security preview update (end of previous month). For each patch list: release date, KB number, OS build, and the support.microsoft.com link. Source from each version's update history page (discover and fetch the real links; never construct a guessed update-history URL).

Keep a complete roadmap snapshot in roadmap-state.json, including the observation date, feature IDs or stable titles, status, target version and source URL. Compare stable feature IDs (or titles when no ID is exposed) to the prior snapshot. On the first run without a snapshot, record a baseline and state that newly added features cannot yet be identified reliably. Read and write this state only in this job folder; include it in the report commit. If a supported version has no applicable preview update, say so with the source. Do not replace a baseline from an incomplete fetch.

Save the report in this folder as `Windows Monthly Brief-YYYY-MM-DD.md`, using the Stockholm run date. Follow RUNBOOK.md for validation and publishing.

For the roadmap baseline, complete means all results exposed by the public roadmap under those filters, with pagination/lazy loading handled and the extracted count checked against the displayed result count. Missing newer versions in the version-filter options do not make an All-version snapshot incomplete. State the source's version coverage limit separately. Do not apply the three-version patch-selection rule to roadmap discovery.

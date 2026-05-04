# Windows Monthly Brief

**Cadence:** Monthly — 1st of month at 09:00 Stockholm  
**Cron:** `0 7 1 * *` (07:00 UTC)  
**Output:** `Windows Monthly Brief-YYYY-MM-DD.md`  
**Status:** Active — remote routine

## Description

Monthly brief covering two areas: new features appearing on the Windows roadmap since the previous run, and patch release details for the current supported Windows 11 versions (security update on 2nd Tuesday + non-security preview update at end of month).

## Sections

- Section 1 — Windows roadmap features (new since last run)
- Section 2 — Patch information for current + two prior supported Windows 11 versions

## Process

No dedicated flow diagram — see prompt below.

## Prompt

Compile a monthly Windows update brief.

**Section 1 — Windows roadmap features:**
Check the Windows roadmap at https://www.microsoft.com/en-us/windows/business/roadmap with filters set to: Platform = Windows 11 PC, Channel/Status fields 2 and 3 = All, Feature type = Feature, Edition = Retail. List only features that are NEW since the previous run of this task (use prior run memory to compare). For each new feature include: title, status (e.g. Rolling out, In preview), short description, and any version it targets. If nothing is new since last run, say so explicitly.

**Section 2 — Patch information:**
Cover the current Windows 11 version plus the two prior supported versions (e.g. 26H1, 25H2, 24H2 — adjust as Microsoft updates the supported list). For each version, include both the security update (Patch Tuesday — 2nd Tuesday of the previous month) and the non-security preview update (end of previous month). For each patch list: release date, KB number, OS build, and the support.microsoft.com link. Source from each version's update history page (e.g. https://support.microsoft.com/en-gb/topic/windows-11-version-26h1-update-history-... and equivalents for the other versions).

### Output file

Save the report as `Windows Monthly Brief-YYYY-MM-DD.md` where the date is today's run date.

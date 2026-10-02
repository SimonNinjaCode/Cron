---
layout:
  width: wide
---

# M365 Security Whats New

Föregående månads säkerhetsnyheter från tolv Microsoft Learn-sidor.

**Codex-jobb:** `Cron - M365 Security Whats New`  
**Modell:** Luna 6.0 (`gpt-6-luna`), medium reasoning  
**Schema:** Monthly — 1st at 07:00, `Europe/Stockholm`  
**Rapport:** `M365 Security Whats New-YYYY-MM-DD.md`

- [Prompt](PROMPT.md)
- [Exempel](EXAMPLES.md)
- [Gemensamma körinstruktioner](../RUNBOOK.md)
- [Mermaid-källfil](diagram.mmd)

## Process

```mermaid
flowchart TD
    A["Monthly — 1st at 07:00 - Europe/Stockholm"] --> B["Read RUNBOOK.md and PROMPT.md"]
    B --> C["Read 12 Microsoft Learn release-note pages"]
    C --> D["Select only previous calendar month"]
    D --> E["Write one table per service"]
    E --> F["Save dated Markdown report"]
    F --> G["Register in SUMMARY.md"]
    G --> H{"GitBook validation passes?"}
    H -- No --> I["Fix report or report failure"]
    H -- Yes --> J["Commit job files and SUMMARY.md; push to Cron main"]
    J --> K["GitBook Git Sync imports main when connected"]
```

---
layout:
  width: wide
---

# Windows Monthly Brief

Windows-roadmap och föregående månads säkerhets- och previewuppdateringar.

**Codex-jobb:** `Cron - Windows Monthly Brief`  
**Modell:** Luna 6.0 (`gpt-6-luna`), medium reasoning  
**Schema:** Monthly — 1st at 09:00, `Europe/Stockholm`  
**Rapport:** `Windows Monthly Brief-YYYY-MM-DD.md`

- [Prompt](PROMPT.md)
- [Exempel](EXAMPLES.md)
- [Gemensamma körinstruktioner](../RUNBOOK.md)
- [Mermaid-källfil](diagram.mmd)

## Process

```mermaid
flowchart TD
    A["Monthly — 1st at 09:00 - Europe/Stockholm"] --> B["Read RUNBOOK.md and PROMPT.md"]
    B --> C["Read Windows roadmap and supported release histories"]
    C --> D["Compare prior roadmap baseline and verify KB details"]
    D --> E["Write roadmap changes and update tables"]
    E --> F["Save dated Markdown report"]
    F --> G["Register in SUMMARY.md"]
    G --> H{"GitBook validation passes?"}
    H -- No --> I["Fix report or report failure"]
    H -- Yes --> J["Commit job files and SUMMARY.md; push to Cron main"]
    J --> K["GitBook Git Sync imports main when connected"]
```

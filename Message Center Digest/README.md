---
layout:
  width: wide
---

# Message Center Digest

Publik sammanställning av Message Center-ändringar inom säkerhet och compliance.

**Codex-jobb:** `Cron - Message Center Digest`  
**Modell:** Luna 6.0 (`gpt-6-luna`), medium reasoning  
**Schema:** Monthly — 1st at 06:00, `Europe/Stockholm`  
**Rapport:** `Message Center Digest-YYYY-MM-DD.md`

- [Prompt](PROMPT.md)
- [Exempel](EXAMPLES.md)
- [Gemensamma körinstruktioner](../RUNBOOK.md)
- [Mermaid-källfil](diagram.mmd)

## Process

```mermaid
flowchart TD
    A["Monthly — 1st at 06:00 - Europe/Stockholm"] --> B["Read RUNBOOK.md and PROMPT.md"]
    B --> C["Read public Message Center aggregator"]
    C --> D["Filter security and compliance in rolling 30-day window"]
    D --> E["Sort changes and highlight action deadlines"]
    E --> F["Save dated Markdown report"]
    F --> G["Register in SUMMARY.md"]
    G --> H{"GitBook validation passes?"}
    H -- No --> I["Fix report or report failure"]
    H -- Yes --> J["Commit job files and SUMMARY.md; push to Cron main"]
    J --> K["GitBook Git Sync imports main when connected"]
```

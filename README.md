---
layout:
  width: wide
---

# Cron

Sju schemalagda Codex-jobb för Microsoft 365, säkerhet och AI. Alla använder **Luna 6.0** (`gpt-6-luna`) med medium reasoning och tider i **Europe/Stockholm**.

Rapporter skrivs som Markdown, valideras och pushas till [SimonNinjaCode/Cron](https://github.com/SimonNinjaCode/Cron). GitBook läser `main` när Git Sync är anslutet. `.gitbook.yaml` anger innehållsstruktur; den skapar inte anslutningen.

## Jobb

| Codex-jobb | Schema i Stockholm |
|---|---|
| [Cron - Generative AI Brief](<Generative AI Brief/README.md>) | Weekly — Wednesday 08:00 |
| [Cron - Microsoft AI Brief](<Microsoft AI Brief/README.md>) | Weekly — Wednesday 09:00 |
| [Cron - Message Center Digest](<Message Center Digest/README.md>) | Monthly — 1st at 06:00 |
| [Cron - M365 Security Whats New](<M365 Security Whats New/README.md>) | Monthly — 1st at 07:00 |
| [Cron - M365 Threat Intelligence Report](<M365 Threat Intelligence Report/README.md>) | Monthly — 1st at 08:00 |
| [Cron - Windows Monthly Brief](<Windows Monthly Brief/README.md>) | Monthly — 1st at 09:00 |
| [Cron - Patch Tuesday Review](<Patch Tuesday Review/README.md>) | Monthly — day after second Tuesday at 08:00 |

Patch Tuesday-granskningen körs onsdagen efter den andra tisdagen. Microsofts släpp och analyser måste finnas före granskningen.

## Struktur

```text
TOPIC/
  README.md                 # syfte, schema och diagram
  PROMPT.md                 # jobbets instruktioner
  diagram.mmd               # Mermaid-källa
  EXAMPLES.md               # länkar till historiska exempel
  TOPIC-YYYY-MM-DD.md        # rapportarkiv och nya resultat
RUNBOOK.md                  # gemensam källkontroll och publicering
jobs.json                   # avsedda Codex-inställningar
SUMMARY.md                  # GitBook-navigation
.gitbook.yaml               # GitBook-innehållskonfiguration
scripts/                    # registrering och validering
```

## Drift

Codex-jobbens inställningar hanteras i Scheduled. De läser aktuell RUNBOOK.md och respektive PROMPT.md vid varje körning. jobs.json dokumenterar inställningarna, men ändringar där aktiveras inte automatiskt i Codex. Datorn måste vara vaken och Codex igång när lokala jobb körs.

[Gemensamma körinstruktioner](RUNBOOK.md) · [GitBook-anslutning](GITBOOK.md)

Historiska rapporter är bevarade från den tidigare miljön. De är exempel, inte omverifierade faktaunderlag eller bevis på lyckade Codex-körningar.

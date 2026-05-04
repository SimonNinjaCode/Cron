# Cron

Automated intelligence pipeline for Microsoft 365 security, threat intelligence, and AI news. Seven scheduled remote agents run on claude.ai and push their output back to this repo as dated markdown files.

## Jobs

| Job | Cadence | Schedule |
|-----|---------|----------|
| [Generative AI Brief](Generative%20AI%20Brief/README.md) | Weekly | Wednesday 08:00 Stockholm |
| [Microsoft AI Brief](Microsoft%20AI%20Brief/README.md) | Weekly | Wednesday 09:00 Stockholm |
| [Message Center Digest](Message%20Center%20Digest/README.md) | Monthly | 1st of month 06:00 Stockholm |
| [M365 Security Whats New](M365%20Security%20Whats%20New/README.md) | Monthly | 1st of month 07:00 Stockholm |
| [M365 Threat Intelligence Report](M365%20Threat%20Intelligence%20Report/README.md) | Monthly | 1st of month 08:00 Stockholm |
| [Windows Monthly Brief](Windows%20Monthly%20Brief/README.md) | Monthly | 1st of month 09:00 Stockholm |
| [Patch Tuesday Review](Patch%20Tuesday%20Review/README.md) | Monthly | 14th of month 08:00 Stockholm |

Each job folder contains:
- `README.md` — description, schedule, prompt, and process diagram
- `diagram.mmd` — Mermaid workflow diagram
- `TOPIC-YYYY-MM-DD.md` — dated output files written by the remote agent

## Dashboard

A local Flask dashboard for browsing job configs and reading outputs.

```bash
cd dashboard
python app.py
# opens at http://127.0.0.1:8080
```

Remote routine status and run logs: https://claude.ai/code/routines

## Structure

```
<Job Name>/
  README.md          # job docs, prompt, cron
  diagram.mmd        # mermaid workflow
  TOPIC-YYYY-MM-DD.md  # outputs (committed by remote agent)

dashboard/
  app.py             # Flask app
  templates/         # Jinja2 templates

prompts.md           # source prompts (reference)
```

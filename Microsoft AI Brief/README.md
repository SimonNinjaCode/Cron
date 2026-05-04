# Microsoft AI Brief

**Cadence:** Weekly — every Wednesday at 09:00 Stockholm  
**Cron:** `0 7 * * 3` (07:00 UTC)  
**Output:** `Microsoft AI Brief-YYYY-MM-DD.md`  
**Status:** Active — remote routine

## Description

Weekly newsletter covering Microsoft AI developments from the past 7 days, focused on enterprise-relevant updates across Azure AI, M365 Copilot, Security Copilot, and the Microsoft developer ecosystem. Prioritises by category and applies humanised prose to the final output.

## Priority categories

1. Security & Safety
2. Enterprise Platform
3. Agentic AI
4. Infrastructure
5. Developer Tools

## Sources

Azure AI blog, M365 Copilot blog, Security Copilot blog, Microsoft Tech Community, DevBlogs, Learn blog, practical365, petri, The Register

## Process

```mermaid
graph TD
    A([Wednesday 08:00]) --> B[WebSearch Microsoft AI sources — last 7 days]
    B --> B1[Azure AI, M365 Copilot, Security Copilot blogs]
    B --> B2[Tech Community, DevBlogs, Learn blog]
    B --> B3[practical365, petri, The Register]
    B1 & B2 & B3 --> C[Prioritise by category]
    C --> C1[1. Security & Safety]
    C --> C2[2. Enterprise Platform]
    C --> C3[3. Agentic AI]
    C --> C4[4. Infrastructure]
    C --> C5[5. Developer Tools]
    C1 & C2 & C3 & C4 & C5 --> D[Fetch full content for top stories]
    D --> E[Write enterprise-focused newsletter]
    E --> F[Apply humaniser: remove AI writing patterns]
    F --> G[Write to Microsoft AI Brief-YYYY-MM-DD.md]
    G --> H[Append row to runs.md]
```

## Prompt

> Prompt not yet written. See diagram for process description.

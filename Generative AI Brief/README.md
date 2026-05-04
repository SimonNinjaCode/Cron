# Generative AI Brief

**Cadence:** Weekly — every Wednesday at 08:00 Stockholm  
**Cron:** `0 6 * * 3` (06:00 UTC)  
**Output:** `Generative AI Brief-YYYY-MM-DD.md`  
**Status:** Active — remote routine

## Description

Weekly newsletter covering enterprise-relevant generative AI developments from the past 7 days. Searches nine AI sources, filters for enterprise relevance, fetches full content for the top 5–7 stories, and writes a structured newsletter with humanised prose.

## Sections

- This Week in AI (overview)
- Top Stories with enterprise implications
- Safety & Governance
- Enterprise Features & APIs
- Security Risks
- Numbers That Matter

## Sources

Anthropic, OpenAI, DeepMind, Google AI, Azure AI blog, HuggingFace, MIT Tech Review, Ars Technica, The Register

## Process

```mermaid
graph TD
    A([Wednesday 08:00]) --> B[WebSearch 9 AI sources — last 7 days]
    B --> B1[Anthropic, OpenAI, DeepMind, Google AI]
    B --> B2[Azure AI blog, HuggingFace]
    B --> B3[MIT Tech Review, ArsTechnica, The Register]
    B1 & B2 & B3 --> C[Filter: enterprise-relevant content only\nExclude consumer, gaming, trivial UI updates]
    C --> D[Fetch full content for top 5–7 stories]
    D --> E[Write newsletter]
    E --> E1[This Week in AI overview]
    E --> E2[Top Stories with enterprise implications]
    E --> E3[Safety & Governance]
    E --> E4[Enterprise Features & APIs]
    E --> E5[Security Risks]
    E --> E6[Numbers That Matter]
    E1 & E2 & E3 & E4 & E5 & E6 --> F[Apply humaniser: remove AI writing patterns]
    F --> G[Write to Generative AI Brief-YYYY-MM-DD.md]
    G --> H[Append row to runs.md]
```

## Prompt

> Prompt not yet written. See diagram for process description.

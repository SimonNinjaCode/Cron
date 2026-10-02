---
layout:
  width: wide
---

# GitBook-anslutning

Repository: [SimonNinjaCode/Cron](https://github.com/SimonNinjaCode/Cron)  
Branch: `main`  
Konfiguration: `.gitbook.yaml` med `root: ./`, `readme: README.md` och `summary: SUMMARY.md`.

## Anslut Git Sync

1. Öppna avsett GitBook Space och välj Git Sync → GitHub.
2. Ge GitBook GitHub-integrationen åtkomst till SimonNinjaCode/Cron.
3. Välj Cron, main och repositoryroten.
4. Gör den första synkroniseringen från GitHub till GitBook. Repositoryt är källan för detta importerade innehåll.
5. Kontrollera att startsidan, sju jobb och rapportarkivet visas och att en senare push synkroniseras.

Anslutningen konfigureras i GitBook. YAML-filen och en lyckad GitHub-push bevisar inte att GitBook är anslutet. GitBook publicering av en webbplats är ett separat steg från innehållssynkronisering.

Dokumentation: [GitBook Git Sync](https://gitbook.com/docs/docs-as-code/git-sync) och [Content configuration](https://gitbook.com/docs/docs-as-code/git-sync/content-configuration).

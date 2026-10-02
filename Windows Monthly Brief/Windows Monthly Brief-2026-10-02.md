---
layout:
  width: wide
---

# Windows Monthly Brief — oktober 2026
_Rapportdatum: 2 oktober 2026 (Europe/Stockholm)_

**Rapporteringsfönster:** 1–30 september 2026.

## 1. Windows roadmap

Jag kan inte fastställa vilka roadmap-funktioner som tillkommit sedan föregående rapport. Mappen saknar `roadmap-state.json`, så detta är första körningen med en tillförlitlig jämförelsebaseline. Den tidigare rapporten räcker inte som komplett snapshot.

Roadmapen gav 127 träffar med Platform = Windows 11 PC och Channel = Retail. Microsofts versionsfilter visade 23H2, 24H2 och 25H2, men saknade 26H1 och 26H2 trots att officiell livscykeldokumentation listar båda som stödda GA-versioner. Därför går det inte att verifiera att resultatet är en komplett snapshot för de begärda filtren. Jag har inte skrivit en ofullständig `roadmap-state.json`.

**Utfall:** Nya funktioner kan inte identifieras tillförlitligt i denna körning. Nästa körning behöver en komplett, sparad baseline för att kunna visa faktiska förändringar. Källa: [Windows roadmap](https://www.microsoft.com/en-us/windows/business/roadmap).

## 2. Windows 11-uppdateringar

Microsofts stödsida, senast uppdaterad 29 september 2026, listar 26H2, 26H1 och 25H2 som de tre senaste versionerna i General Availability Channel. 26H1 är begränsad till utvalda nya enheter och är inte en uppgradering för befintliga datorer. [Supported versions of Windows client](https://learn.microsoft.com/en-us/windows/release-health/supported-versions-windows-client)

### Windows 11, version 26H2 (build 26300)

Version 26H2 blev tillgänglig 29 september. Den fick därför ingen separat B-uppdatering på Patch Tuesday den 8 september. Septemberförhandsversionen omfattade redan build 26300 och är den första tillämpliga uppdateringen i den publicerade uppdateringshistoriken.

| Typ | Releasedatum | KB | OS-build | Supportartikel |
|---|---|---|---|---|
| Säkerhetsuppdatering (B) | Ingen separat septemberutgåva | — | — | [Uppdateringshistorik för 26H2](https://support.microsoft.com/en-au/servicing/os/windows-11/2026/09/windows-11-version-26h2-update-history) |
| Icke-säkerhetsrelaterad förhandsversion (D) | 22 september 2026 | KB5124010 | 26300.9550 | [KB5124010](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124010-windows-11-24h2-25h2-update) |

### Windows 11, version 26H1 (build 28000)

| Typ | Releasedatum | KB | OS-build | Supportartikel |
|---|---|---|---|---|
| Säkerhetsuppdatering (B) | 8 september 2026 | KB5124012 | 28000.2954 | [KB5124012](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124012-windows-11-26h1-security-update) |
| Icke-säkerhetsrelaterad förhandsversion (D) | 22 september 2026 | KB5124006 | 28000.3086 | [KB5124006](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124006-windows-11-26h1-update) |

### Windows 11, version 25H2 (build 26200)

| Typ | Releasedatum | KB | OS-build | Supportartikel |
|---|---|---|---|---|
| Säkerhetsuppdatering (B) | 8 september 2026 | KB5124008 | 26200.9445 | [KB5124008](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124008-windows-11-24h2-25h2-security-update) |
| Icke-säkerhetsrelaterad förhandsversion (D) | 22 september 2026 | KB5124010 | 26200.9550 | [KB5124010](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124010-windows-11-24h2-25h2-update) |

KB5124010 gäller 26H2, 25H2 och 24H2. Microsoft anger att septemberversionen var den sista förhandsversionen för 24H2; versionen upphör inte att få säkerhetsuppdateringar förrän enligt respektive editions livscykel. [KB5124010](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124010-windows-11-24h2-25h2-update)

## Källor och begränsningar

- Versionsurval och editionslivscykler: [Supported versions of Windows client](https://learn.microsoft.com/en-us/windows/release-health/supported-versions-windows-client). Versionerna ovan är GA-servicing; LTSC behandlas inte som en av de tre senaste GA-versionerna.
- Versionshistorik: [26H2](https://support.microsoft.com/en-au/servicing/os/windows-11/2026/09/windows-11-version-26h2-update-history), [26H1](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/02/windows-11-version-26h1-update-history), [25H2](https://support.microsoft.com/en-us/servicing/os/windows-11/2025/07/windows-11-version-25h2-update-history).
- Roadmapens publika vy var dynamisk och saknade 26H1/26H2 i versionsfiltret. Det förhindrar en komplett snapshot och säker jämförelse. Ingen roadmap-state-fil har därför skapats.
- B- och D-utgåvorna har hämtats från Microsoft Support-artiklarna länkade ovan. För 26H2 redovisas uttryckligen att ingen separat september-B-utgåva fanns; 26H2 nådde GA den 29 september.

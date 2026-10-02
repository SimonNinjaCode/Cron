---
layout:
  width: wide
---

# Windows Monthly Brief — oktober 2026
_Rapportdatum: 2 oktober 2026 (Europe/Stockholm)_

**Rapporteringsfönster:** 1–30 september 2026.

## 1. Windows roadmap

Roadmapen visade **127 resultat** med Platform = Windows 11 PC, Version = All, Status = All, Feature category = All och Channel = Retail. Jag hämtade samtliga 127 resultatkort; extraherat antal matchar sidans visade antal. En fullständig snapshot finns i [`roadmap-state.json`](roadmap-state.json), med titel, status, beskrivning, målversion, kategori, plattform, kanal och källadress för varje resultat.

Det finns ingen tidigare `roadmap-state.json` att jämföra med. Den föregående rapporten är inte en verifierad fullständig snapshot. Därför går det inte att avgöra vilka poster som tillkommit sedan föregående körning, och inga funktioner anges som nya. Den här körningen etablerar baslinjen för nästa jämförelse.

**Täckningsbegränsning:** Versionsväljaren erbjuder All, 23H2, 24H2 och 25H2; 26H1 och 26H2 saknas. Snapshoten använder ändå Version = All och omfattar alla 127 resultat som den publika vyn visar under de begärda filtren. Avsaknaden av 26H1/26H2 i väljaren är en begränsning i källans versionsmetadata, inte skäl att utelämna den tillgängliga resultatmängden. [Windows roadmap](https://www.microsoft.com/en-us/windows/business/roadmap)

## 2. Windows 11-uppdateringar

Microsofts livscykelsida, uppdaterad 29 september 2026, listar 26H2, 26H1 och 25H2 som de tre senaste stödda versionerna i General Availability Channel. Version 26H1 är avsedd för vissa nya enheter och erbjuds inte som uppgradering på befintliga enheter. [Supported versions of Windows client](https://learn.microsoft.com/en-us/windows/release-health/supported-versions-windows-client)

### Windows 11, version 26H2 (build 26300)

| Typ | Releasedatum | KB | OS-build | Supportartikel |
|---|---|---|---|---|
| Säkerhetsuppdatering (B) | Ingen separat utgåva den 8 september | — | — | [Versionshistorik för 26H2](https://support.microsoft.com/en-au/servicing/os/windows-11/2026/09/windows-11-version-26h2-update-history) |
| Icke-säkerhetsrelaterad förhandsversion (D) | 22 september 2026 | KB5124010 | 26300.9550 | [KB5124010](https://support.microsoft.com/en-us/help/5124010) |

26H2 blev tillgänglig 29 september, efter månadens Patch Tuesday. KB5124010 gäller 26H2, 25H2 och 24H2. [Livscykelöversikt](https://learn.microsoft.com/en-us/windows/release-health/supported-versions-windows-client) · [KB5121794, enablement package för 26H2](https://support.microsoft.com/en-gb/servicing/os/windows-11/2026/09/kb5121794-feature-update-to-windows-11-version-26h2)

### Windows 11, version 26H1 (build 28000)

| Typ | Releasedatum | KB | OS-build | Supportartikel |
|---|---|---|---|---|
| Säkerhetsuppdatering (B) | 8 september 2026 | KB5124012 | 28000.2954 | [KB5124012](https://support.microsoft.com/en-us/help/5124012) |
| Icke-säkerhetsrelaterad förhandsversion (D) | 22 september 2026 | KB5124006 | 28000.3086 | [KB5124006](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5124006-windows-11-26h1-update) |

[Versionshistorik för 26H1](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/02/windows-11-version-26h1-update-history)

### Windows 11, version 25H2 (build 26200)

| Typ | Releasedatum | KB | OS-build | Supportartikel |
|---|---|---|---|---|
| Säkerhetsuppdatering (B) | 8 september 2026 | KB5124008 | 26200.9445 | [KB5124008](https://support.microsoft.com/en-us/help/5124008) |
| Icke-säkerhetsrelaterad förhandsversion (D) | 22 september 2026 | KB5124010 | 26200.9550 | [KB5124010](https://support.microsoft.com/en-us/help/5124010) |

[Versionshistorik för 25H2](https://support.microsoft.com/en-gb/servicing/os/windows-11/2025/07/windows-11-version-25h2-update-history)

**Driftsnotering:** Microsoft dokumenterar ett problem där vissa Credential Guard-skyddade maskinkonton kan tappa sin säkra domänkanal efter KB5124012, KB5124008 eller senare uppdateringar när Machine Identity Isolation är konfigurerat i en miljö som inte uppfyller kravet på Windows Server 2025 Domain Functional Level. Microsoft beskriver också separata USB Audio Class 1.0-problem; OOB-uppdateringarna KB5129194 för 26H1 och KB5129195 för 25H2/24H2 åtgärdar vissa ljudlägen. Läs respektive KB innan bred utrullning. [KB5124012](https://support.microsoft.com/en-us/help/5124012) · [KB5124008](https://support.microsoft.com/en-us/help/5124008)

## Källor och begränsningar

- Roadmap-snapshoten fångar samtliga 127 resultat som visades med de valda filtren. Den publika versionsväljaren listar inte 26H1 eller 26H2. Inget påstående om nya roadmapfunktioner görs utan en tidigare tillförlitlig baseline.
- Patchurvalet bygger på Microsofts stödda GA-versioner och varje versions uppdateringshistorik. För 26H2 saknas separat B-uppdatering i rapporteringsfönstret eftersom versionen blev tillgänglig 29 september, efter Patch Tuesday den 8 september.
- Septemberförhandsversionen KB5124010 var den sista preview-uppdateringen för 24H2. 24H2 ingår inte bland rapportens tre versionsrader, men KB5124010:s 24H2-build är 26100.9550. [KB5124010](https://support.microsoft.com/en-us/help/5124010)

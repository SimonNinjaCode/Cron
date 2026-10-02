---
layout:
  width: wide
---

# Microsoft Patch Tuesday Review — September 2026

_Detta är en historisk replay för pipelinevalidering; patchmånaden september 2026 åsidosätter den normala spärren för en ännu inte tillgänglig månadsrelease._

_Generated 2026-10-02_

## Summary

- **Totalt antal CVE:** ej fastställt. BleepingComputer räknar 966 CVE i Patch Tuesday-utgåvan. CrowdStrike räknar 972. Båda skiljer sig från komplett månadstäckning och använder egna avgränsningar; MSRC:s JavaScript-baserade release notes gav ingen läsbar export av hela listan i denna körning.
- **Zero-days:** 2 aktivt utnyttjade; 0 separat bekräftade som offentligt kända före patch. CVE-2026-81963 och CVE-2026-85880.
- **Critical:** ej fastställt; BleepingComputer anger 105 och CrowdStrike 113.
- **Edge/Chromium:** inget separat totalantal verifierat. BleepingComputer exkluderar uttryckligen 204 tidigare publicerade sårbarheter från Patch Tuesday-totalen, inklusive Edge Chromium-fixar.

### Breakdown by type

Sekundärkällornas uppdelningar för själva Patch Tuesday-utgåvan. Totalsumman av kategorierna följer BleepingComputers uppskattning om 960 och inte deras rapporterade total 966; därför lämnas totalen obestämd.

| Typ | Antal |
|---|---:|
| Elevation of Privilege | 438 |
| Remote Code Execution | 258 |
| Information Disclosure | 173 |
| Security Feature Bypass | 19 |
| Denial of Service | 56 |
| Spoofing | 16 |
| Edge–Chromium | ej fastställt; utanför rapporterad Patch Tuesday-avgränsning |

## Exploited in the Wild

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---:|---|---|---|---|
| CVE-2026-81963 | 7.8 | Important | Windows Update Stack Elevation of Privilege Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963) |
| CVE-2026-85880 | 7.8 | Important | Windows Advanced Local Procedure Call (ALPC) Elevation of Privilege Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880) |

MSRC beskriver båda som lokala privilege escalation-fel där angriparen behöver en etablerad körmöjlighet. BleepingComputer bekräftar aktiv exploatering, teknisk typ och att Microsoft inte publicerat detaljer om hur intrången genomfördes. CVSS 7.8 rapporteras av sekundärkällor; MSRC:s sårbarhetssidor kunde inte läsas av webbklienten.

## Publicly Disclosed

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---:|---|---|---|---|
| Inga bekräftade | n/a | n/a | Ingen separat offentligt känd före patch rapporteras för de två zero-day-felen | n/a | [MSRC September release notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep) |

## Highest Rated — CVSS ≥ 8.0 or Critical

Verifierade exempel från sekundärkällor. Tabellen är inte en fullständig CVSS ≥ 8.0-inventering: MSRC:s release notes kunde inte exporteras till en läsbar CVE-lista i den här körningen. BleepingComputer identifierar 105 Critical-poster men att lista enbart dem skulle ändå missa CVSS ≥ 8.0-poster klassade Important.

| CVE | CVSS | Criticality | Title | Customer Action | Link |
|---|---:|---|---|---|---|
| CVE-2026-69579 | n/a | Critical | Windows Message Queuing Remote Code Execution Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69579) |
| CVE-2026-72981 | 8.1 | Critical | IP Helper Remote Code Execution Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72981) |
| CVE-2026-72986 | 8.8 | Critical | Graphic Fonts Remote Code Execution Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72986) |
| CVE-2026-73018 | 8.8 | Critical | Graphic Fonts Remote Code Execution Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-73018) |
| CVE-2026-72960 | 8.8 | Critical | Windows Media Player Remote Code Execution Vulnerability | Required | [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72960) |

Källorna ger inte stöd för kund- eller enhetsstatus. “Required” betyder att uppdateringen är en kundinstallerad Microsoft-produktfix, inte att någon viss miljö redan har patchats.

## Exploitation More Likely

Microsofts risketiketter kunde inte hämtas systematiskt från Security Update Guide i denna körning. Sekundärkällornas genomgångar nämner bland annat **CVE-2026-69676** (Kerberos RCE) som “Exploitation More Likely”; den etiketten är inte verifierad mot läsbar primärdata här. Övriga poster redovisas inte utan verifierbart MSRC-underlag.

## Notable themes from this month

- De två bekräftat utnyttjade bristerna är lokala EoP-fel. De är relevanta för post-compromise privilege escalation, inte som självständiga externa ingångar.
- RCE-volymen är hög: BleepingComputer räknar 258 RCE-poster, varav 81 klassade Critical.
- Windows Update Stack och ALPC visar värdet av att säkra klientens och serverns interna privilegiegränser efter första fotfästet.
- Patch Tuesday-siffror blir svårjämförbara när rapportörer blandar datumavgränsning och redan tidigare publicerade produktuppdateringar. En enda odifferentierad månadstotal döljer den skillnaden.
- MSRC rekommenderar att Windows-baselineuppdateringarna installeras; de kräver omstart. Exchange Server har separat distributionsvägledning från Exchange-teamet.

---

## Sources

- [BleepingComputer — Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/) — publicerad 8 september 2026; total, kategorier, aktiv exploatering och CVE-titlar.
- [CrowdStrike — September 2026 Patch Tuesday: Two Exploited Zero-Days and 113 Critical Vulnerabilities Among 972 CVEs](https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/) — publicerad 8 september 2026; alternatif total och CVSS-exempel.
- [SANS Internet Storm Center — September 2026 Microsoft Patch Tuesday](https://isc.sans.edu/diary/September%2B2026%2BMicrosoft%2BPatch%2BTuesday/33320) — publicerad september 2026; bekräftar exploatering av CVE-2026-81963.
- [Microsoft Learn — Release notes for Microsoft Edge Security Updates](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) — Edge-uppdateringshistorik; ingen separat verifierbar septembertotal erhölls.
- [Microsoft MSRC — CVE-2026-81963](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963) — primär sårbarhetspost; webbvisaren kräver JavaScript.
- [Microsoft MSRC — CVE-2026-85880](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880) — primär sårbarhetspost; webbvisaren kräver JavaScript.
- [Microsoft MSRC — September 2026 Security Update Release Notes](https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep) — primär månadspost; sistnämnda MSRC-release notes-länk. Webbvisaren gav ingen läsbar postlista.

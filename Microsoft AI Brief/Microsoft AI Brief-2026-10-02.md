---
layout:
  width: wide
---

# Microsoft AI Brief — 2 oktober 2026

*Enterprise intelligence om Microsoft AI | 26 september–2 oktober 2026*

Veckans tydligaste förflyttning är från enskilda Copilot-funktioner till styrning av agenter och deras anslutningar. Microsoft presenterar gemensam pluginhantering i Copilot, fler modeller i Microsoft 365 och Foundry samt ett ökat fokus på affärskontext, utvärdering och reproducerbar driftsättning. Inga nya Security Copilot-annonseringar i de angivna officiella flödena kunde verifieras för perioden.

## Security & Safety

### Agentutvärdering: en bra medelpoäng räcker inte som releasebeslut

I ett Microsoft Foundry-inlägg den 1 oktober beskriver Microsoft ett arbetssätt för att koppla agenters körspår till beteendekrav och konsekvensbaserade releasegrindar. Exemplet är en agent som ger ett välformulerat svar men ändå utför en återbetalning utanför sin behörighet. En sammanvägd utvärderingspoäng kan dölja sådana enstaka men allvarliga fel. Artikeln kallar mönstret *Consequence-Aware Agent Release Contract* och är uttryckligen ett praktiskt förslag, inte en Microsoft-produktstandard.

**Vad det betyder:** Sätt separata, blockerande tester för förbjudna verktygsanrop och otillåtna beslut. Granska spår och konsekvenser, inte bara språkmodellens svar eller ett genomsnittligt eval-resultat. Behåll misslyckade scenarier som regressionstester. [Microsoft Foundry Blog, 1 oktober](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/beyond-agent-scores-building-consequence-aware-release-gates-with-microsoft-foun/4559709)

**Att bevaka:** Mönstret är vägledning och kräver att organisationen själv definierar kontrakt, allvarlighetsnivåer och releasetrösklar.

## Enterprise Platform

### Gemensamt pluginregister för Copilot samlar upptäckt och åtkomststyrning

Microsoft presenterade den 30 september ett pluginregister för flera Copilot-upplevelser och Microsoft 365-appar. Ett plugin kan paketera agent, skill och connector. Användare ska hitta godkända funktioner via en gemensam Plugins-yta; administratörer ska kunna granska Microsoft-, partner- och organisationsbyggda plugins samt aktivera, inaktivera, blockera eller tilldela dem via Microsoft 365 admin center och Agent 365. Utrullningen har inletts. Microsoft anger att vissa connectors fortfarande rullas ut och att Copilot Studio, GitHub Copilot och Foundry är framtida utökningar.

**Vad det betyder:** Detta ger en centralare kontrollpunkt för vilka datakällor och åtgärder Copilot kan använda. Det ersätter inte granskning av enskilda connectors, deras behörigheter eller den information de exponerar. Inventera befintliga agenter och connectors, bestäm godkännandekriterier och uppdatera instruktioner som hänvisar till gamla Agents-menyer. [Microsoft Copilot Blog, 30 september](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-the-plugin-registry---one-place-to-discover-and-govern-plugins-for-m/4559682)

**Att bevaka:** Utrullningen pågår; bekräfta vilka registerfunktioner som faktiskt syns i tenant innan processer skrivs om. Microsoft uppger att grundläggande register- och hanteringsfunktioner ingår i kvalificerade Microsoft-molnprenumerationer.

### Fabric IQ kopplar Copilot till styrda Power BI-definitioner

Microsoft uppgav den 28 september att Fabric IQ i Copilot Chat och Cowork nått generell tillgänglighet. Funktionen använder Power BI:s semantiska modeller, mått och affärsdefinitioner som kontext för svar. Microsoft säger att befintliga åtkomstkontroller och styrning bevaras. Integrationen i Code kommer via Frontier-programmet. Samma artikel beskriver IQ Sharing för Fabric i preview samt nya Fabric-funktioner för observability och agentisk data engineering.

**Vad det betyder:** En styrd semantisk modell kan minska motstridiga definitioner av exempelvis försäljning eller prognos mellan rapporter och Copilot-svar. Det gör kvaliteten och ägarskapet för Power BI-modeller ännu viktigare. Bekräfta att mått, definitioner och åtkomstregler är aktuella innan användare förlitar sig på svaren i verksamhetsbeslut. [Official Microsoft Blog, 28 september](https://blogs.microsoft.com/blog/2026/09/28/new-microsoft-data-innovations-unlock-what-only-your-business-knows/)

**Att bevaka:** GA gäller enligt Microsoft för Copilot Chat och Cowork. Code-integrationen är kommande via Frontier; IQ Sharing är preview.

## Agentic AI

### Microsoft 365 Copilot får fler modeller och nya administrativa möjligheter

I septemberöversikten, publicerad den 30 september och uppdaterad 1 oktober, samlar Microsoft ändringar som rullat ut under månaden. Bland dem finns centralt hanterade auktoritativa SharePoint-källor för Copilot Search: administratörer kan markera upp till 100 SharePoint-webbplatser som officiella källor. Artikeln beskriver också att Copilot kan anropa agenter och skills i prompten, nya Teams Phone-agentfunktioner och Copilot-stöd i SharePoint och OneDrive.

**Vad det betyder:** Auktoritativa källor ger IT och innehållsägare ett konkret sätt att styra vilka SharePoint-sajter Copilot Search ska betrakta som verifierade. Börja med en avgränsad uppsättning välskötta kunskapskällor och följ upp sökträffar och innehållsansvar. Inventera även var agenter och skills kan anropas från användarpromptar.

**Att bevaka:** Microsoft beskriver flera funktioner som utrullade i september, men vissa andra anges som kommande i oktober eller som Frontier-utrullning. Roadmap-datum är preliminära. [Microsoft Copilot Blog, 30 september, uppdaterad 1 oktober](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--september-2026/4559107)

### GPT-6.1 Sol blir GA i Microsoft Foundry

Microsoft meddelade den 29 september att GPT-6.1 Sol är generellt tillgänglig i Foundry. Microsoft lyfter förbättringar för agentisk kodning, datoranvändning och professionella arbetsuppgifter samt ett kontextfönster på upp till en miljon tokens. Standardkapacitet debiteras efter användning; Provisioned Throughput finns vid lansering i Global- och US Data Zone-distributioner. Microsoft beskriver även lager av skydd, inklusive innehållsfilter, skydd för verktygsanrop, identitets- och åtkomstkontroller samt Purview-policyer och mänskliga kontrollpunkter.

**Vad det betyder:** En ny modell ger ett alternativ för återkommande agentflöden, men modellens egenskaper är inte bevis på att en viss arbetslast blir säkrare eller billigare. Jämför på egna uppgifter med kvalitet, felutfall, latenstid och kostnad per genomförd uppgift. Kontrollera stödda regioner och distributionsalternativ mot krav på dataplacering; utvärdera även verktygsbehörigheter och mänskliga godkännanden separat.

**Att bevaka:** Tillgänglighet och kapacitet skiljer sig mellan distributionslägen och regioner. Granska aktuella priser före budgetering. [Microsoft Foundry Blog, 29 september](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-gpt-6-1-sol-in-microsoft-foundry-advanced-intelligence-optimized-for/4560811)

## Infrastructure

### Hosted agents kan tas in i Terraform-flöden

Ett Microsoft Foundry-inlägg den 1 oktober visar hur containerbaserade hosted agents kan distribueras med Terraform och Azure AzAPI. Mönstret använder Azure Resource Manager för Foundry-konto, projekt och anslutningar men skapar den logiska agenten genom Foundrys data-plane-API med `azapi_data_plane_resource`. Inlägget rekommenderar att produktionsflöden även hanterar remote state, godkännanden, image-versionering och verifiering av att en agentversion blivit aktiv före trafikstyrning.

**Vad det betyder:** Plattformsteam kan lägga agentkonfiguration närmare befintlig IaC- och CI/CD-styrning, även när applikationsteam äger agentkoden. Det blir en delad kontrollkedja, inte en anledning att ge pipeline-identiteter bredare rättigheter. Börja med en icke-produktionsmiljö och lägg in godkännande, artefaktfrämjande och återställningsväg.

**Att bevaka:** Artikeln är en implementationsexempel och använder data-plane-resursen `Microsoft.Foundry/agents@v1`. Bekräfta API-version, behörigheter och aktuella krav mot Microsoft Learn innan införande. [Microsoft Foundry Blog, 1 oktober](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/deploying-hosted-agents-in-foundry-agent-service-via-terraform/4560435)

## Källäge och begränsningar

Rapporten bygger på offentliga Microsoft-källor: Microsoft Copilot Blog, Microsoft Foundry Blog och Official Microsoft Blog. Jag fann inget nytt Security Copilot-inlägg inom perioden i de angivna Microsoft TechCommunity-sökningarna. Därför finns ingen Security Copilot-produktnyhet i denna utgåva. Källorna är huvudsakligen Microsofts egna lanserings- och vägledningstexter; utlovade förbättringar är inte oberoende effektmätningar. Utrullning, licens, region och status kan skilja mellan tenants och förändras efter publicering. Kontrollera länkad dokumentation och tenantens faktiska release-status före planering.

*Källor verifierade 2 oktober 2026. Publiceringsdatum anges per artikel; där en status skiljer mellan GA, preview och successiv utrullning redovisas det i respektive avsnitt.*

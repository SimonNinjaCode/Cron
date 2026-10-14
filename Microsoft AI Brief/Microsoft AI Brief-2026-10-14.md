---
layout:
  width: wide
---

# Microsoft AI Brief — 14 oktober 2026

*Enterprise intelligence om Microsoft AI | 8–14 oktober 2026*

Veckans tydligaste besked gäller två risklager för Microsoft 365 Copilot: Purview DLP kan stoppa externa e-postmeddelanden från att användas som underlag, och Microsoft beskriver ett nytt trust-aware skydd vid modellens inferens. På plattformssidan visar Foundry hur SharePoint-behörigheter kan följa användaren in i en agent. Microsoft presenterade också en specialiserad beslutsmodell och nya steg i sin egen AI-infrastruktur.

## Security & Safety

### Purview DLP kan utesluta extern e-post ur Copilot-underlag

Microsoft beskrev den 8 oktober en Purview DLP-policy för platsen Microsoft 365 Copilot and Copilot Chat. Regeln kan identifiera meddelanden från externa avsändare och hindra Copilot från att använda dem som grounding. Den granskar avsändarmetadata och accepterade domäner, inte e-postens innehåll. Användaren kan fortfarande läsa och hantera meddelandet; interna e-postmeddelanden, filer och webbsökning påverkas inte av just den här regeln. [Microsoft Security Community Blog, 8 oktober](https://techcommunity.microsoft.com/blog/microsoft-security-blog/protecting-organizations-from-external-email-risks-in-microsoft-365-copilot/4562820)

**Vad det betyder:** Det här minskar möjligheten att instruktioner i externa mejl påverkar Copilots svar. Skyddet gäller grounding och är inte en ersättning för e-postskydd eller användarens åtkomstkontroller.

**Åtgärd:** Kontrollera att accepterade domäner är korrekta. Bedöm var externa mejl behövs som Copilot-underlag och kör policyn i simuleringsläge innan enforcement. Källan anger ingen separat utrullningsplan; verifiera tillgänglighet och beteende i tenantens Purview-portal.

### Microsoft beskriver ett deterministiskt trust-lager för M365 Copilot

I ett inlägg publicerat den 13 oktober beskriver Microsoft en inferenskomponent som ska skilja betrott innehåll från obetrott hämtat innehåll. Externa mejl nämns som ett första högriskfall. Obetrott innehåll leds genom en begränsad bearbetningsväg och omvandlas innan det når huvudmodellen; ursprung kan markeras så att senare bearbetning tar hänsyn till det. Microsoft beskriver detta som ett extra skyddslager, inte som ett skydd som stoppar alla prompt-injection-försök. Artikeln uppdaterades den 12 oktober och säger att tillgänglighet och beteende kan variera med release-status och tenant. [Microsoft Copilot Blog, 13 oktober](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/building-trust-aware-controls-for-ai-differentiated-handling-of-untrusted-conten/4562160)

**Vad det betyder:** Säkerhetsmodellen flyttar en del av skyddet från klassificering och åtkomst till hur innehåll behandlas vid inferens. Den kompletterar DLP-policyn ovan, som i sin tur utesluter extern e-post från grounding.

**Att bevaka:** Kontrollera aktuell utrullning och Microsofts konfigurationsanvisningar innan ni räknar med skyddet. Prova scenarier med externa meddelanden och andra obetrodda källor; Microsoft säger att den första omfattningen fokuserar på externa kommunikationer.

## Enterprise Platform

### Foundry-agent kan hämta SharePoint-data med frågeställarens behörighet

Microsoft publicerade den 12 oktober ett arkitekturmönster för en hostad agent i Foundry Agent Service som publiceras till Teams. Agenten använder sin egen identitet för modellkörningen, men skickar den inloggade användarens identitet vidare till SharePoint-hämtningen via On-Behalf-Of. Därmed kan SharePoint begränsa sökresultat och källhänvisningar efter användarens faktiska behörighet. Artikeln uppger att exemplet använder Foundry IQ och Foundry toolbox utan en egen retrieval-server eller klienthemligheter i retrieval-vägen. Den anger också att fjärranslutna SharePoint-kunskapskällor i Foundry IQ var i preview när artikeln skrevs. [Microsoft Foundry Blog, 12 oktober](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/building-permission-aware-hosted-agents-for-sharepoint-in-foundry-agent-service/4562526)

**Vad det betyder:** Att agenten har åtkomst till en kunskapskälla räcker inte för att svaren ska följa varje användares åtkomst. Identiteten måste följa med ända till retrieval-steget. Mönstret är relevant för interna agenter som delar SharePoint-innehåll med användare med olika behörighet.

**Åtgärd:** Granska identitetsflöde, OBO-konfiguration och källhänvisningar. Testa med användare som har olika SharePoint-rättigheter och bekräfta att en hostad agent aldrig returnerar källor utanför frågeställarens åtkomst. Behandla beroendet av preview-funktioner som en designbegränsning tills aktuell status verifierats.

## Agentic AI

### Microsoft-Decision-1 riktar sig mot strukturerade beslut

Microsoft presenterade Microsoft-Decision-1 den 9 oktober för klassificering, routing, prioritering, verifiering och workflow-kontroll. Foundry-bloggen beskriver modellen som public preview. Microsoft uppger att modellen post-tränats från Qwen3.5-9B och returnerar poäng eller sannolikheter för givna alternativ, i stället för att generera ett öppet textsvar. Microsofts jämförelse omfattade 36 benchmark och nära 150 000 frågor; företaget anger högst noggrannhet i sin jämförelse och cirka 35 gånger lägre medianlatenstid än GPT-6 Sol. Det är Microsofts egna testresultat, inte ett oberoende benchmark. [Microsoft Foundry Blog, 9 oktober](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742) · [Microsoft Command Line, 9 oktober](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)

**Vad det betyder:** En separat beslutsmodell kan passa i agentsteg där systemet väljer bland kända alternativ, till exempel ärendeklassning eller verktygsrouting. Poängvärden är inte en garanti för korrekta beslut och modellen ersätter inte domänregler eller mänsklig granskning.

**Åtgärd:** Om ni provar modellen, börja med representativa och märkta exempel. Mät fel per klass, kalibrering och kostnad; definiera en väg till manuell kontroll när poängen är osäker. Verifiera aktuell region, prissättning och preview-status i Foundry innan budget eller produktionsbeslut.

## Infrastructure

### Maia 200 kör Microsofts produktionslaster; Maia 300 planeras för 2027

Microsoft uppgav den 12 oktober att Azure Maia 200 kör produktionslaster, däribland Microsoft Copilot, och rullas ut i USA, Europa och Australien. GitHub Copilot och Microsoft Foundry ska enligt Microsoft följa före årets slut. Maia 300 är planerad för produktionsutrullning under 2027 och beskrivs som Microsofts primära inferenssystem för egna produkter och tjänster. Microsoft anger upp till 40 procent fler tokens per megawatt än jämförda GPU-system och upp till sju gånger rackgenomströmningen mot Maia 200 i en konfiguration med 96 acceleratorer. Det är leverantörens egna jämförelser och de avser Microsofts systemkonfigurationer. [Official Microsoft Blog, 12 oktober](https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/) · [Microsoft Azure Blog: Maia 300-arkitekturen, 12 oktober](https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/)

**Vad det betyder:** Microsoft bygger mer av sin inferenskapacitet på egen hårdvara och systemdesign. Beskedet gäller i första hand Microsofts egna tjänster och utgör inte ett löfte om att kunder kan välja Maia som Azure-kapacitet.

**Att bevaka:** Microsoft planerar mer information på Ignite den 17–20 november. Följ faktisk tjänstetillgänglighet, regioner och eventuella effekter på kundernas pris eller kapacitet; artikeln anger inga sådana kundlöften.

### Microsoft öppnar fler delar av AI-infrastrukturens standardarbete

Ett Azure-inlägg den 13 oktober samlar Microsofts arbete med nätverk, kraft, kylning och hårdvarusäkerhet. Bland annat beskriver Microsoft Multipath Reliable Connection (MRC) för AI-nätverk, ett OCP-arbete kring Ethernet for Scale-Up Networking och en 800 VDC-infrastruktur för datacenter. Microsoft, Marvell och Oracle presenterar dessutom Tessera Integrated HSM som ett open-source-initiativ. Microsoft uppger att MRC:s två nätverkslager kan skala bortom 100 000 GPU:er och att OCP:s ESUN-arbetsgrupp samlar över 175 organisationer. Det är status och prestandapåståenden i Microsofts egen sammanställning. [Microsoft Azure Blog, 13 oktober](https://azure.microsoft.com/en-us/blog/infrastructure-for-the-frontier-era-scaling-intelligence-through-open-industry-collaboration/)

**Vad det betyder:** AI-kapacitet begränsas inte bara av acceleratorer. Nätverk, elförsörjning, kylning och nyckelskydd blir delar av samma arkitektur. De öppna specifikationerna kan på sikt underlätta kompatibilitet mellan leverantörer, men inlägget beskriver ingen kundnära Azure-funktion eller utrullningsplan.

**Att bevaka:** För datacenter- och plattformsägare är OCP:s standardarbete och 800 VDC-utvecklingen värda att följa i långsiktig kapacitetsplanering. Vänta på publicerade specifikationer och leverantörsstöd innan ni bygger inköpskrav på dessa riktningar.

## Developer Tools

Inga ytterligare Microsoft DevBlogs-nyheter om utvecklarverktyg med verifierat publiceringsdatum 8–14 oktober identifierades i de granskade flödena. Microsoft-Decision-1 och Foundry-exemplen ovan är de relevanta utvecklarbeskeden den här veckan.

## Källäge och begränsningar

Rapporten bygger på offentliga Microsoft-källor: Official Microsoft Blog, Azure Blog och Microsoft TechCommunity. Jag kontrollerade publiceringsdatum i respektive originalkälla och sökte i Azure AI/Foundry-, Microsoft 365 Copilot-, Security Copilot- och DevBlogs-flödena. Två säkerhetsinlägg om Copilot-underlag och prompt injection hittades; ingen ny produktannonsering från Security Copilot kunde verifieras i perioden. Det säger inget om ändringar som endast publicerats i Message Center eller rullats ut till enskilda tenants.

TechCommunity-läsaren blockerade delar av Foundry-bloggens artikeltext och direkt HTTPS hämtning gav 403. Huvuduppgifterna om Foundry-mönstret kunde verifieras via Microsofts publika artikelsammanfattning och utdrag; Microsoft-Decision-1 kunde också kontrolleras mot Microsofts egen Command Line-publicering. Där artikelns detaljer inte gick att läsa fullt ut har rapporten begränsats till verifierbara arkitekturuppgifter och produktbeskrivningar. Microsofts prestanda- och benchmarkpåståenden är inte oberoende verifierade. Preview-status, region, pris och utrullning måste kontrolleras i aktuell tenant eller tjänstedokumentation.

*Källornas publiceringsdatum kontrollerade 14 oktober 2026. Status och planerade datum återges som Microsoft angav dem på respektive publiceringsdatum.*

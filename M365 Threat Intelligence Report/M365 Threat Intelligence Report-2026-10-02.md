---
layout:
  width: wide
---

# M365 Threat Intelligence Report — September 2026

**Report Date:** 2026-10-02 (Europe/Stockholm)
**Reporting Window:** 2026-07-01–2026-09-30
**Audience:** Security architects · SOC leads · cyber leadership

## Sammanfattning

September månads rapportering visar två tydliga molnrisker: identitetsangrepp som går från nätfiske till beständig session och datainsamling, samt komprometterade Azure-service principals med rättigheter att radera resurser. EvilTokens-materialet i fyra publikationer beskriver en och samma PhaaS-kampanj (Storm-2992), inte fyra kampanjer. Storm-3168/Jade Puffer-incidenten återges av fyra utgivare, men är en och samma Azure-intrångshändelse som Microsoft daterar till början av juni. Passkey-temat förekommer i tre artiklar om Microsofts observerade aktivitet sedan maj; dessa är överlappande rapportering om en kampanjmiljö och ska inte summeras som tre oberoende intrång.

Övriga separata signaler är BigBear 2.0:s AiTM-sessionstölder och en Unicode-baserad phishingkampanj som Microsoft beskriver i Defender for Office 365-telemetri. Prioritera kontroll av device-code-flöden, korrelation mellan identitets- och molndatahändelser, minst privilegium för arbetsbelastningsidentiteter samt oberoende skydd för återställning. MCRA-, Zero Trust- och ATT&CK-kopplingar nedan är analytikertolkningar om inte annat uttryckligen anges.

## 1. [The Hacker News](https://thehackernews.com/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [Microsoft Takes Down EvilTokens Device-Code Phishing Service Tied to 12,000 Inbox Compromises](https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html) — publicerad 2026-09-22 |
| **Introduction** | EvilTokens paketerade phishing via OAuth device authorization, analys av kapade inkorgar och BEC-stöd. Microsoft rapporterade över 12 000 komprometterade inkorgar i fler än 10 000 organisationer och en rättsligt stödd störning av infrastrukturen. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | Microsoft spårar operatörerna som Storm-2992. Device-code phishing gav angriparna autentiserade sessioner; tjänsten analyserade e-post efter betalningsflöden och betrodda kontakter. Organisationer globalt, särskilt i USA, Kanada, Storbritannien, Australien, Indien och Frankrike. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / BEC / SaaS |
| **Risk** | OAuth-godkännande kan ge åtkomst till Exchange Online utan att angriparen behöver offrets lösenord. Inkorgsinnehåll kan snabbt omsättas i faktura- och betalningsbedrägeri. Infrastrukturstörningen bevisar inte att redan utfärdade sessioner har återkallats. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Threat Protection, SIEM+XDR och SecOps; Zero Trust Identity, Application, Data samt Visibility & Analytics. Behandla device authorization och efterföljande inkorgsåtgärder som en sammanhängande kedja. |
| **Call to Action** | Begränsa device-code flow där det inte behövs. Larma på oväntade device-code-inloggningar, nya inkorgsregler, massåtkomst och ändringar i betalningsuppgifter. Vid bekräftad kompromettering: återkalla sessioner och verifiera betalningar via en separat kanal. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data](https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html) — publicerad 2026-09-13 |
| **Introduction** | Artikeln sammanfattar två Microsoft-beskrivna förlopp: VD-imitation för falska ServiceNow-betalningar och passkey-/SSO-tematiserad social engineering följd av kapade molnidentiteter, Graph-aktivitet och datahämtning. Passkey-luren är ett lockbete; Microsoft säger inte att angriparna faktiskt registrerar passkeys. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | Fakturabedrägeriet använde imiterade chefer och AI-anpassade betalningsmeddelanden. Den separata molnaktiviteten omfattar flera aktörer, bland andra Storm-3121 och Storm-3032 enligt Microsoft; hjälpdesk-imitation följs av AiTM eller device-code-flöde, autentiseringsmetod som angriparen lägger till, Graph-rekognosering och insamling från SharePoint, OneDrive och Exchange. Aktivitet i molnkampanjen observerad sedan maj 2026. |
| **Affected Cybersecurity Domain** | Identity & Access / Social Engineering / BEC / Data Protection |
| **Risk** | Sessionstillgång kan utvecklas till uthållig åtkomst och storskalig datainsamling. Separat kan en falsk leverantörsbetalning leda till direkt ekonomisk förlust. De två förloppen ska inte slås ihop till en enda kampanj. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Data Protection, Threat Protection och SecOps; Zero Trust Identity, Application, Data och Visibility & Analytics. Microsoft anger ATT&CK-tekniker för molnaktiviteten, bland annat T1078.004, T1556.006, T1087.004, T1530 och T1114. |
| **Call to Action** | Verifiera betalningsändringar separat. Korrelera riskfyllda inloggningar med nya autentiseringsmetoder, tokenhändelser, Graph-uppräkning och onormal fil- eller e-poståtkomst. Ta bort obehöriga metoder och återkalla sessioner efter verifierad kompromettering. |
| **Source** | [The Hacker News](https://thehackernews.com/) |

## 2. [Ars Technica — Security](https://arstechnica.com/security/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [Microsoft disrupts AI-assisted platform that compromised 12,000 accounts](https://arstechnica.com/security/2026/09/microsoft-disrupts-ai-assisted-platform-that-compromised-12000/) — publicerad 2026-09-22 |
| **Introduction** | Ars Technica beskriver EvilTokens som en tjänst för device-code phishing och efterföljande analys av Microsoft-konton för att förbereda BEC. Artikeln bygger på samma Microsoft-störning och samma Storm-2992-kampanj som rapporterats av The Hacker News, Dark Reading och BleepingComputer. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | Storm-2992 enligt Microsoft. Bedrägliga länkar leder till legitim Microsoft-inloggning där offret omedvetet godkänner angriparens device-session; tjänsten analyserade inkorgar efter personer och betalningsflöden. Microsoft uppgav global påverkan. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / BEC |
| **Risk** | Kapad session ger åtkomst till e-post och kontext för riktad betalningsmanipulation. Antalet organisationer är Microsofts rapporterade underlag, inte ett oberoende verifierat totalmått från Ars. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Threat Protection och SecOps; Zero Trust Identity, Application, Data och Visibility & Analytics. Utvärdera device authorization och post-auth-beteende tillsammans. |
| **Call to Action** | Tillåt endast device-code flow när verksamheten kräver det. Granska avvikande OAuth/device-code-inloggningar, tokenanvändning och inkorgsåtgärder; återkalla sessioner vid misstanke och verifiera ekonomiska instruktioner utanför e-posttråden. |
| **Source** | [Ars Technica — Security](https://arstechnica.com/security/) |

**Täckningslucka:** Jag fann ingen andra artikel från Ars Technica inom juli–september 2026 som klarade relevanskravet för M365, Entra ID, Azure eller närliggande SaaS-angreppsvägar. Zimbra CVE-2026-73570 är borttagen: den granskade rapporteringen dokumenterar ingen M365-, Entra- eller Azure-integration eller påverkan. Två kvalificerande Ars-artiklar kan därför inte styrkas inom tidsfönstret.

## 3. [Dark Reading](https://www.darkreading.com/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [Microsoft Disrupts EvilTokens Device Code Phishing Service](https://www.darkreading.com/identity-access-management-security/microsoft-disrupts-eviltokens-device-code-phishing-service) — publicerad 2026-09-22 |
| **Introduction** | Dark Reading rapporterar Microsofts och partnernas störning av EvilTokens. Artikeln beskriver hur offret leds från phishing till Microsofts legitima device-login och där godkänner angriparens session. Detta är ytterligare en publicering om samma Storm-2992-kampanj, inte en separat incident. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | Storm-2992; PhaaS med AI-stöd för lockbeten, device-code phishing och urval av högvärdiga kontakter ur inkorgar. Microsoft uppgav över 12 000 komprometterade inkorgar i över 10 000 organisationer. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / BEC |
| **Risk** | En användare kan slutföra en legitim autentisering men ändå godkänna en angriparkontrollerad session. Borttagning av infrastruktur garanterar inte att aktiva token eller konton redan återställts. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Threat Protection och SecOps; Zero Trust Identity, Application och Visibility & Analytics. Tjänstens kommersiella modell gör återanvändning av liknande PhaaS-verktyg sannolik, enligt den citerade forskarbedömningen. |
| **Call to Action** | Blockera device-code flow där möjligt och begränsa användningen i övrigt. Granska device-code-händelser tillsammans med inkorgsregler och API-åtkomst. Sök efter återkomst via andra phishing-kit efter störningen. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [JadePuffer AI Actor Compromises Azure Tenant in Destructive Cloud Attack](https://www.darkreading.com/cloud-security/jadepuffer-ai-actor-azure-tenant-destructive-cloud-attack) — publicerad 2026-09-28 |
| **Introduction** | Dark Reading återger Microsofts analys av två komprometterade service principals som användes för Azure-rekognosering, insamling av uppgifter och raderingsförsök. Händelsen inträffade i början av juni; rapporten i september är inte incidentdatumet. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | JadePuffer, spårad av Microsoft som Storm-3168. Två service principals i samma tenant användes för att kartlägga resurser och utföra destruktiva åtgärder. Microsoft observerade ingen lösensumma eller bekräftad dataexfiltration i det beskrivna intrånget. |
| **Affected Cybersecurity Domain** | Cloud Infrastructure / Workload Identity / Data Protection |
| **Risk** | Överprivilegierad workload identity kan radera lagring och applikationer samt hota återställningsförmåga. Microsofts fall visar att oberoende resurslås och skydd kan stoppa en del åtgärder. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Threat Protection, SIEM+XDR och Data Protection; Zero Trust Identity, Application, Data och Visibility & Analytics. Behandla service principals och återställningskontroller som kritiska säkerhetsobjekt. |
| **Call to Action** | Inventera service principals och hemligheter, begränsa Azure RBAC till minsta privilegium och sök efter hemligheter i publika kodarkiv. Larma på ovanlig resursuppräkning, nyckelhämtning, massradering och ändringar i skydd för återställning. |
| **Source** | [Dark Reading](https://www.darkreading.com/) |

**Avgränsning:** Dark Readings OAuth-consent-kolumn från 2026-09-18 är en åsiktstext om generell risk. Den dokumenterar ingen observerad kampanj och används därför inte som hotunderrättelsebevis.

## 4. [BleepingComputer](https://bleepingcomputer.com/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [BigBear Microsoft 365 phishing service bypassed MFA at 258 organizations](https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/) — publicerad 2026-09-07 |
| **Introduction** | CloudSEK-innehåll som BleepingComputer rapporterar visar att BigBear 2.0 använde Evilginx2-baserad AiTM-proxy för att fånga autentiseringsuppgifter och sessionscookies efter MFA. Forskarna rapporterade minst en lyckad kompromettering hos 258 organisationer i sitt observerade underlag. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | BigBear 2.0 PhaaS och dess användare; AiTM-proxy, cookie-replay och infrastruktur konfigurerad för Microsoft 365. Talen kommer från CloudSEK:s åtkomst till tjänstens kontrollpanel och är inte ett fullständigt prevalensmått. |
| **Affected Cybersecurity Domain** | Identity & Access / Phishing / SaaS |
| **Risk** | Stulna sessionscookies kan ge åtkomst efter MFA och exponera Exchange Online, SharePoint och OneDrive. Godkänd MFA i en inloggningslogg utesluter inte kapad session. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Threat Protection, SIEM+XDR och SecOps; Zero Trust Identity, Device och Visibility & Analytics. Prioritera phishing-resistent autentisering och sessionsmedveten detektion. |
| **Call to Action** | Utred token- och sessionsavvikelser även efter MFA-framgång. Följ upp okända enheter, riskfyllda inloggningar och plötslig molndataåtkomst; återkalla sessioner vid misstänkt AiTM-kompromettering. |
| **Source** | [BleepingComputer](https://bleepingcomputer.com/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [JadePuffer agentic AI attacks target Azure, destroy cloud resources](https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-ai-attacks-target-azure-destroy-cloud-resources/) — publicerad 2026-09-28 |
| **Introduction** | Artikeln återger Microsofts Storm-3168-utredning: två komprometterade service principals föregick försök att radera fler än 100 Azure Storage-konton samt andra resurser. Detta är samma händelse som Dark Reading och The Hacker News rapporterar, inte en andra kampanj. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | JadePuffer/Storm-3168; rekognosering med service principals, lagringsnyckelhämtning och automatiserade raderingsförsök. Microsoft daterar aktiviteten till juni. Vissa raderingar stoppades av resurslås och lagringsskydd; SQL-raderingsförsök misslyckades. |
| **Affected Cybersecurity Domain** | Cloud Infrastructure / Workload Identity / Data Protection |
| **Risk** | Komprometterad workload identity med breda rättigheter kan slå ut data och tjänster och försvåra återställning. En till synes automatiserad kedja kan skala konsekvensen snabbt. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Threat Protection, SIEM+XDR och Data Protection; Zero Trust Identity, Application, Data och Visibility & Analytics. |
| **Call to Action** | Begränsa service-principal-rättigheter och rotera exponerade hemligheter. Skydda lagring och säkerhetskopior med separata raderingskontroller; larma på resursuppräkning, nyckelåtkomst och raderingsutbrott. |
| **Source** | [BleepingComputer](https://bleepingcomputer.com/) |

## 5. [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/)

### Insight 1

| Field | Description |
|-------|-------------|
| **Title** | [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/) — publicerad 2026-09-09 |
| **Introduction** | Microsoft beskriver hjälpdesk-imitation och passkey-/SSO-lurar som leder till AiTM eller device-code-flöden. Därefter följer angripartillagda autentiseringsmetoder, Microsoft Graph-rekognosering samt hämtning från SharePoint, OneDrive och e-post. Aktiviteten har observerats sedan maj 2026. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | Microsoft kopplar initialåtkomsten till flera aktörer, däribland Storm-3121 och Storm-3032. Microsoft anger ATT&CK-teknikerna T1078.004, T1556.006, T1087.004, T1530 och T1114 för delar av kedjan. Rapporteringen från The Hacker News och BleepingComputer är överlappande återgivningar av denna kampanjmiljö. |
| **Affected Cybersecurity Domain** | Identity & Access / Social Engineering / SaaS / Data Exfiltration |
| **Risk** | Komprometterad identitet kan befästas genom nya autentiseringsmetoder och användas för kartläggning och insamling över flera Microsoft-tjänster. Personliga telefoner kan innebära att tidiga steg saknas i organisationens endpoint-telemetri. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Threat Protection, SIEM+XDR, Data Protection och SecOps; Zero Trust Identity, Device, Application, Data samt Visibility & Analytics. ATT&CK-mappningarna ovan anges av Microsoft; MCRA- och Zero Trust-kopplingen är analytisk. |
| **Call to Action** | Korrelera avvikande inloggningar med autentiseringsmetoder/enhetsregistrering, Graph-uppräkning och onormal fil- eller e-poståtkomst. Bekräfta nya metoder med användaren, ta bort obehöriga och återkalla sessioner när intrång fastställts. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

### Insight 2

| Field | Description |
|-------|-------------|
| **Title** | [Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/) — publicerad 2026-09-25 |
| **Introduction** | Microsoft beskriver två service principals som först kartlade Azure-resurser och sedan användes för raderingsförsök och insamling av uppgifter. Den destruktiva fasen varade cirka sju minuter och omfattade fler än 100 försök mot Storage-konton. Händelserna skedde i början av juni, inte september. |
| **Status** | Assess |
| **Threat Actor including TTPs, Targets & Region** | JADEPUFFER, spårad som Storm-3168. Enligt Microsoft var klient-ID, klienthemlighet och tenant-ID exponerade i en publik GitHub-issue. Microsoft observerade inte någon lösensumma eller bekräftad exfiltration i detta intrång. BleepingComputer, Dark Reading och The Hacker News har också rapporterat samma händelse. |
| **Affected Cybersecurity Domain** | Cloud Infrastructure / Workload Identity / Data Protection |
| **Risk** | Exponerade workload credentials och för bred Azure RBAC kan ge snabb resursförstörelse. Resurslås och lagringsskydd stoppade vissa försök men inte merparten av Storage-raderingarna i det rapporterade fallet. |
| **Strategic Initiative** | Analytikertolkning: MCRA Identity, Threat Protection, SIEM+XDR, Data Protection och SecOps; Zero Trust Identity, Application, Data samt Visibility & Analytics. Minsta privilegium och oberoende återställningsskydd adresserar den beskrivna angreppsvägen. |
| **Call to Action** | Sök efter exponerade secrets, granska ägare och behörigheter för service principals och rotera komprometterade uppgifter. Övervaka ovanlig inventering, nyckelhämtning och massradering; testa återställning med skydd som angriparens identitet inte kan ändra. |
| **Source** | [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |

### Övrig kvalificerande Microsoft-källa

Microsofts artikel [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/) (2026-09-03) beskriver en phishingkampanj där osynliga Unicode-taggar delade upp finansiella lockbetesord för att försvåra filteranalys. Defender for Office 365-telemetri visade förhöjda signaturträffar från 9 februari och under ungefär tre månader; huvuddelen av meddelandena stoppades av flera lager av skydd. Detta är observerad phishing, men artikeln redovisar ingen namngiven aktör eller M365-kontokompromettering. Den nämns här som kompletterande signal och inte som en extra tabellinsikt för att hålla jämförbarheten mellan utgivarnas tvåinsiktsurval.

## Källäge och begränsningar

- Tidsfönstret är juli–september 2026: september prioriterades och juli–augusti användes endast där det gav relevant sammanhang. Publiceringsdatum skiljs från incidentdatum.
- Underlaget består av 9 tabellinsikter från utgivarna: två vardera från The Hacker News, Dark Reading, BleepingComputer och Microsoft samt en från Ars Technica. Ars Technica-luckan kvarstår eftersom ingen andra artikel klarade relevanskravet.
- De 11 publikationerna om EvilTokens, Storm-3168/JadePuffer och passkey-temat är inte 11 kampanjer: fyra artiklar om EvilTokens avser Storm-2992-kampanjen, fyra om Storm-3168/JadePuffer återger samma Azure-intrång i juni och tre om passkey-temat återger överlappande Microsoft-rapporterad aktivitet sedan maj. BigBear och ASCII-smuggling är separata rapporterade förlopp. Antal artiklar ska inte summeras som antal hotaktörer eller incidenter.
- Zimbra CVE-2026-73570 har exkluderats: källan dokumenterar ingen konkret M365-, Entra- eller Azure-integration, angreppsväg eller påverkan. Dark Readings OAuth-consent-artikel har också exkluderats som belägg för kampanj eftersom den är en opinionskolumn, inte en incidentrapport.
- Räknedata från Microsoft och CloudSEK återges som leverantörernas/forskarnas observerade underlag, inte som oberoende totalmått. MCRA- och Zero Trust-kopplingar är analytikertolkningar. ATT&CK-tekniker tillskrivs Microsoft där Microsoft uttryckligen anger dem; övriga samband ska läsas som beteendebaserad analytikertolkning, inte verifierad formell mappning.
- Endast publika artiklar har använts. Rapporten har ingen tenant-telemetri och publicerar inga privata indikatorer.

---

*Korrigerad och förberedd 2026-10-02 för rapporteringsfönstret 2026-07-01–2026-09-30. Källor hämtades och verifierades mot artiklarnas angivna publiceringsdatum.*

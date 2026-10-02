---
layout:
  width: wide
---

# M365 Security What's New — september 2026 (2026-10-02)

September 2026. Sammanställningen bygger enbart på de angivna Microsoft Learn-sidorna. Entra-sidan är läsbar men saknar en septembersektion och det senaste synliga avsnittet gäller juni 2026. Intune-sidan har flyttat till en ny URL och redovisar poster per vecka. Defender Vulnerability Management omdirigerar till Defender for Endpoint, så separat VM-täckning kan inte fastställas. Unified security operations omdirigerar till Defender XDR och korshänvisas där utan dubblering.

## Microsoft Entra ID

Den offentliga sidan är läsbar, men dess senaste månadsavsnitt är juni 2026. Septembertäckning kan därför inte verifieras; detta betyder inte att september saknade nyheter. Källa: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new

## Unified security operations (Defender portal)

Den angivna URL:en omdirigerar till Microsoft Defender XDR:s What's new-sida. Septemberposterna finns en gång under **Microsoft Defender XDR** nedan; den här omdirigerade tjänsteingången dupliceras inte. Källa: https://learn.microsoft.com/en-us/unified-secops/whats-new

## Microsoft Defender XDR

| Title | Service | Category | Type | Summary | Date | Link |
|---|---|---|---|---|---|---|
| Integrated Security Operations Center (ISOC) in Microsoft Defender | Microsoft Defender XDR | Säkerhetsoperationer | Preview | ISOC samlar XDR, SIEM, hotinformation, automation och AI i Defender-portalen. Från 23 september är förhandsversionen tillgänglig för berättigade Microsoft 365 E5- och E7-kunder utan en aktiv Microsoft Sentinel-arbetsyta. | 2026-09-23 | https://learn.microsoft.com/en-us/defender-xdr/whats-new |
| Identity Security dashboard and Coverage & Maturity | Microsoft Defender XDR | Identitetssäkerhet | GA | Instrumentpanelen samlar identitetsrelaterad risk och säkerhetsstatus. Coverage & Maturity visar skyddstäckning och införandegap i lokala miljöer, moln, SaaS, identitetsleverantörer och partnertjänster. | September 2026 | https://learn.microsoft.com/en-us/defender-xdr/whats-new |

## Microsoft Defender for Endpoint

| Title | Service | Category | Type | Summary | Date | Link |
|---|---|---|---|---|---|---|
| Microsoft Defender for Endpoint plug-in support for WSL containers (WSLc) | Microsoft Defender for Endpoint | Containers / Endpointskydd | GA | Plugin-version 2.26.921.1 utökar skyddet till WSL-containrar. Aktivitet visas i enhetsinventering, aviseringar, incidenter, enhetstidslinje och Advanced Hunting. | September 2026 | https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint |
| Microsoft Defender support for Linux Desktops | Microsoft Defender for Endpoint | Endpointskydd | Preview | Offentlig förhandsversion utökar Defender till Linux-skrivbord. Linuxdistributioner som stöds på servrar stöds även på skrivbord. | September 2026 | https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint |
| macOS build 101.26072.0017 | Microsoft Defender for Endpoint | Endpointskydd | GA | Version 20.126072.17.0 har släppts. Versionsspecifika förbättringar och funktioner finns via release notes-länken på källsidan. | September 2026 | https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint |
| New Microsoft Secure Score recommendations for AI-Readiness | Microsoft Defender for Endpoint | Endpointhärdning | GA | AI-Readiness-samlingen innehåller sex rekommendationer för att stärka enheters förtroende inför AI-accelererade angrepp. Fyra är nya och gäller TPM 2.0, VBS, HVCI och Windows LAPS; två befintliga gäller Secure Boot och internetexponering. | September 2026 | https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint |

## Microsoft Defender for Office 365

| Title | Service | Category | Type | Summary | Date | Link |
|---|---|---|---|---|---|---|
| Separating Teams user reporting settings from email settings | Microsoft Defender for Office 365 | Rapportering / Teams-säkerhet | Not specified | Kunder i Worldwide-miljöer med de angivna Defender for Office 365- eller E5-planerna kan hantera Teams-rapportering separat från Outlook och välja olika rapportmottagare. | September 2026 | https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new |
| Expanding user reporting in Teams to include group calls | Microsoft Defender for Office 365 | Rapportering / Teams-säkerhet | Not specified | Användare kan rapportera genomförda eller missade gruppsamtal från samtalshistoriken som bedrägliga eller legitima. Beroende på organisationens inställningar skickas rapporter till rapporteringsbrevlådan, Microsoft eller båda. | September 2026 | https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new |

## Microsoft Defender for Identity

| Title | Service | Category | Type | Summary | Date | Link |
|---|---|---|---|---|---|---|
| Automatic sensor v3.x activation and Windows auditing by default | Microsoft Defender for Identity | Sensorhantering / Granskning | Not specified | För nya Defender for Endpoint-kunder aktiveras detta flöde bara om licens, första enhetsregistrering från 13 september och avsaknad av befintlig Defender for Identity-arbetsyta uppfyller villkoren. För befintliga kunder sker utrullningen gradvis efter en portalavisering, med möjlighet att aktivera eller välja bort före automatisk aktivering. | September 2026 | https://learn.microsoft.com/en-us/defender-for-identity/whats-new |
| Identity Security dashboard and Coverage & Maturity | Microsoft Defender for Identity | Identitetssäkerhet | Not specified | Instrumentpanelen samlar identitetsrisk och skyddsläge. Coverage & Maturity synliggör skyddstäckning och införandegap i lokala miljöer, moln, SaaS och identitetsleverantörer. | September 2026 | https://learn.microsoft.com/en-us/defender-for-identity/whats-new |
| Sensor v3.x onboarding without Microsoft Defender for Endpoint deployment (Preview) | Microsoft Defender for Identity | Sensorhantering | Preview | Förhandsversionen låter administratörer aktivera sensor v3.x på kvalificerade domänkontrollanter utan föregående Defender for Endpoint-registrering. Den gäller nya sensorinstallationer på domänkontrollanter med Windows Server 2019 eller senare. | September 2026 | https://learn.microsoft.com/en-us/defender-for-identity/whats-new |
| Sensor v3.x support for additional identity server roles: AD CS, AD FS, and Entra Connect (Preview) | Microsoft Defender for Identity | Sensorhantering | Preview | Sensor v3.x får stöd för kvalificerade AD FS-, AD CS- och Microsoft Entra Connect-servrar som inte är domänkontrollanter och saknar befintlig Defender for Identity-sensor. | September 2026 | https://learn.microsoft.com/en-us/defender-for-identity/whats-new |

## Microsoft Defender for Cloud Apps

No items are listed for September 2026 on this 'What's new' page. Sidan visar ett augustiavsnitt följt av juni; septemberposter listas inte. Källa: https://learn.microsoft.com/en-us/defender-cloud-apps/release-notes

## Microsoft Defender Vulnerability Management

Den angivna VM-sidan omdirigerar till Microsoft Defender for Endpoint och visar därmed inte en separat VM-releasevy. VM-täckning för september kan inte fastställas från den angivna källan; detta är inte belägg för noll nyheter. Omdirigerad källa: https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint

## Microsoft Intune

Den angivna länken omdirigerar till https://learn.microsoft.com/en-us/intune/whats-new/. Septemberavsnitten är ordnade efter vecka. Datumet anger veckans start när sidan inte anger en separat funktionsdag. Endast säkerhets-, efterlevnads- och utrullningsrelevanta poster från septemberavsnitten tas med.

| Title | Service | Category | Type | Summary | Date | Link |
|---|---|---|---|---|---|---|
| Microsoft Cloud PKI support for US Government GCC High | Microsoft Intune | Certifikathantering | Not specified | Cloud PKI automatiserar utfärdande, förnyelse och återkallelse av certifikat för Intune-hanterade enheter i GCC High utan lokal CA eller Certificate Connector. Certifikaten kan användas för Wi-Fi, VPN och appar; DoD stöds inte. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Newly available protected app for Intune: Microsoft Dragon Copilot | Microsoft Intune | Appskydd | Not specified | Dragon Copilot kan omfattas av Intune-appskyddsprinciper på stödda Android- och iOS/iPadOS-enheter, vilket hjälper skydda organisationsdata vid AI-assisterad klinisk dokumentation. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Require Managed Home Screen authentication for protected app activities | Microsoft Intune | Appskydd / Autentisering | Not specified | På stödda Android Enterprise-enheter måste MAM-integrerade appar återgå till Managed Home Screen-autentisering innan skyddat innehåll öppnas. Det minskar möjligheten att kringgå inloggning eller session-PIN. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| New Apple settings in the Settings Catalog for iOS/iPadOS and macOS | Microsoft Intune | Enhetskonfiguration | Not specified | Nya kataloginställningar omfattar bland annat appar, Apple Intelligence, nätverks- och webbinnehållsfiltrering samt macOS-inloggningsfönstret. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Assignment filters for Android Settings Catalog policies | Microsoft Intune | Policytilldelning | Not specified | Filter för Android Enterprise- och AOSP-principer kan inkludera eller exkludera enheter utifrån egenskaper. Det ger mer precis styrning av vilka enheter som får säkerhetsinställningar. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Automatically launch Microsoft Defender for Endpoint during Android Enterprise device setup | Microsoft Intune | Endpointskydd / Enhetsregistrering | Not specified | Defender for Endpoint kan öppnas automatiskt under enhetskonfiguration för stödda företagsägda Android Enterprise-enheter. Användaren kan slutföra Defender-konfigurationen som del av registreringen. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Updated minimum supported version for iOS and iPadOS | Microsoft Intune | Enhetskrav / Efterlevnad | Not specified | Standardhantering, Company Portal och appskydd kräver nu iOS/iPadOS 18 eller senare. Administratörer bör identifiera och uppgradera berörda enheter; användarlösa enheter i Automated Device Enrollment har separat stödstatus. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Configure MDE AI agent runtime protection for Windows | Microsoft Intune | Endpointskydd / AI-säkerhet | Not specified | En ny endpoint security-mall konfigurerar Defender for Endpoint-skydd för AI-agenters körning i gransknings- eller blockeringsläge. Inställningarna stöder Windows-enheter hanterade med Intune eller MDE security settings management. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Onboard MDM compliance partners with new self-service functionality | Microsoft Intune | Efterlevnad / Integration | Not specified | Leverantörer kan bygga, testa och ansluta MDM-efterlevnadskopplingar med Intunes självbetjäning, dokumentation och valideringsflöden. Det utökar alternativen för att föra in efterlevnadsdata. | 2026-09-28 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Stage app and policy rollout with deployment plans | Microsoft Intune | Ändringshantering / Policyutrullning | Not specified | Deployment plans kan rulla ut appar och konfigurationsprinciper stegvis i ringar och styra tidpunkten. Stöd för Multiple Admin Approval kan minska risken vid breda utrullningar. | 2026-09-21 | https://learn.microsoft.com/en-us/intune/whats-new/ |
| Faster compliance updates for Windows devices | Microsoft Intune | Enhetsefterlevnad | Not specified | Windows-enheter kan upptäcka ändringar i brandvägg, antivirus, BitLocker, Defender-status, OS-version, realtidsskydd och Secure Boot och begära en ny efterlevnadsutvärdering utan att invänta schemalagd incheckning. | 2026-09-14 | https://learn.microsoft.com/en-us/intune/whats-new/ |

## Microsoft Sentinel

| Title | Service | Category | Type | Summary | Date | Link |
|---|---|---|---|---|---|---|
| Integrated Microsoft Sentinel SIEM and data lake onboarding | Microsoft Sentinel | SIEM / Datalagring | Not specified | Data lake ingår i Sentinel-onboardingen; separat onboarding och faktureringskonfiguration behövs inte. När arbetsytan anslutits till Defender-portalen kan lake-tier aktiveras via Table management. | 2026-09-23 | https://learn.microsoft.com/en-us/azure/sentinel/whats-new?tabs=defender-portal |
| Enable the data lake tier using Table management | Microsoft Sentinel | Datalagring / Retention | Not specified | Table management kan spegla Analytics-data till data lake eller behålla data enbart där. Historiska data kan efter onboarding sökas direkt i Advanced Hunting utan återställning till Analytics-nivån. | 2026-09-23 | https://learn.microsoft.com/en-us/azure/sentinel/whats-new?tabs=defender-portal |
| Run interactive KQL queries in advanced hunting | Microsoft Sentinel | Threat hunting | Not specified | Interaktiva KQL-frågor mot data lake kan köras i Advanced Hunting i Defender-portalen. Där går det att undersöka Sentinel- och Defender XDR-data i samma vy. | 2026-09-23 | https://learn.microsoft.com/en-us/azure/sentinel/whats-new?tabs=defender-portal |
| Mirror the data lake tier to Microsoft Fabric OneLake | Microsoft Sentinel | Data- och analysintegration | Not specified | Valda Sentinel-tabeller kan exponeras i Fabric via Azure Monitor mirroring utan att skapa en datakopia eller extra avgift. Datan ligger kvar i Sentinel Log Analytics-arbetsytan. | 2026-09-23 | https://learn.microsoft.com/en-us/azure/sentinel/whats-new?tabs=defender-portal |
| Use Microsoft Fabric for data federation | Microsoft Sentinel | Data- och analysintegration | Not specified | Fabric-datafederering kan kombinera Sentinel-data med externa datakällor utan att flytta underliggande data, vilket stöder undersökningar när kostnad, styrning eller efterlevnad begränsar datarörelser. | 2026-09-23 | https://learn.microsoft.com/en-us/azure/sentinel/whats-new?tabs=defender-portal |
| Use Microsoft Fabric for custom security analytics | Microsoft Sentinel | Säkerhetsanalys | Not specified | Fabric kan analysera Sentinel-data lake och externa tabeller med KQL, notebooks, schemalagda jobb och grafer. Utvalda resultat kan skickas tillbaka till Sentinel för hunting, detektion och utredning. | 2026-09-23 | https://learn.microsoft.com/en-us/azure/sentinel/whats-new?tabs=defender-portal |

## Microsoft Defender for Cloud

| Title | Service | Category | Type | Summary | Date | Link |
|---|---|---|---|---|---|---|
| Upcoming billing updates for Defender for Servers | Microsoft Defender for Cloud | Fakturering / Tjänsteändring | Upcoming change | Från 1 november 2026 debiteras produktivitets- och klientenheter inte längre som servrar i Plan 1. En separat, mer detaljerad identifiering av fakturerbara servrar i Plan 1 och Plan 2 kan ändra fakturerat serverantal beroende på användning och konfiguration. Learn anger publiceringsdatum 30 september och ikraftträdande 1 november. | 2026-11-01 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes |
| Enhanced agent for Defender for SQL Servers on Machines is fully available in Azure Government cloud | Microsoft Defender for Cloud | Databassäkerhet / Agent | GA | Den förbättrade agenten för Defender for SQL Servers on Machines är allmänt tillgänglig i Azure Government-molnet. | 2026-09-29 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes |
| Upcoming deprecation of the Machines should have a vulnerability assessment solution recommendation | Microsoft Defender for Cloud | Sårbarhetshantering | Deprecation | Rekommendationen tas ur bruk den 14 december 2026. Organisationer som använder den bör se över berörda arbetsflöden inför avvecklingen. Learn listar posten den 23 september. | 2026-12-14 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes |
| AWS GuardDuty coverage status is now shown on the S3 asset page | Microsoft Defender for Cloud | Multicloud / Exponeringshantering | GA | S3-resurssidan visar AWS GuardDuty-täckningsstatus tillsammans med Defender for Cloud-information. | 2026-09-03 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes |
| General availability of Defender for Cosmos DB in Azure Government cloud | Microsoft Defender for Cloud | Databassäkerhet | GA | Defender for Cosmos DB är allmänt tillgängligt i Azure Government-molnet. | 2026-09-03 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes |

## Microsoft Purview

| Title | Service | Category | Type | Summary | Date | Link |
|---|---|---|---|---|---|---|
| Integrate Microsoft Entra Global Secure Access with Purview for network data security | Microsoft Purview | Data Loss Prevention | GA | Integrationen skyddar text, filer och AI-interaktioner på nätverkslagret, kan tillämpa DLP-begränsningar och identifiera riskaktivitet via Insider Risk Management. Den ska motverka delning av känsliga data med ej betrodda molnappar via webbläsare, appar, API:er och tillägg. | September 2026 | https://learn.microsoft.com/en-us/purview/whats-new |

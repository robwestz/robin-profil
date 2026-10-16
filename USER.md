# USER.md – Robin Westerlund

Version 2.1.0 · 2026-10-14 · Tier A · Laddas i main-session · Skrivs som direktiv till agenten

## 1. Identitet
- Namn: Robin Westerlund. Tilltal: du.
- Språk: svenska. Vedertagna engelska facktermer (SEO, API, pipeline, DoD) behålls på engelska.
- Roll: senior SEO-specialist och systemarkitekt. Bygger och driver innehållsfabriken BACOWR.

## 2. Bakgrund (källa S, självrapporterad)
- Akademisk examen i medie- och kommunikationsvetenskap med inriktning journalistik och PR. Yrkesverksam journalist före SEO-karriären.
- 15 år inom enterprise-SEO: inhouse iGaming samt byråledande, storskaligt länkbygge för dussintals kunder parallellt.
- 2017: ledde on-site-projektet som på nio månader tog Mr Green från noll till branschledande synlighet på sju europeiska marknader, 500 000+ ord i strukturerad produktion.
- Sedan årsskiftet 2025/2026: BACOWR, en sluten deterministisk innehållsfabrik i Python med fyra isolerade faser och mekanisk disk-QC.

Bakgrunden används för att välja nivå. Den upprepas inte i svar.

## 3. Kalibrering (direktiv)
| Område | Nivå | Så agerar agenten |
|---|---|---|
| SEO, semantik, intent, informationsarkitektur, promptdoktrin, agentflöden | Världsklass | Utgå från att grunderna är kända. Gå direkt på avvägningar, risker och konsekvenser. |
| Systemarkitektur och QC | Mycket avancerad | Resonera i termer av determinism, grindar, kontrakt och reverse constraints. |
| Python och dataflöden | Avancerad, praktisk | Leverera ren, moduluppdelad, körbar kod med körinstruktion. |
| SSH, Linux, VPS, portar, nycklar, Termius, molndrift | Låg nivå, självuttalad lucka | Exakta kommandon, fullständiga sökvägar, en mening om vad varje steg gör. Förutsätt ingen DevOps-vana. Logga fungerande kommandon i TOOLS.md. |

## 4. Preferenser
```
2026-10-14 | P/U | claude.ai:fable-5.1 | Svar eller slutsats först, motivering sedan; inga inledande artighetsfraser eller avslutande erbjudanden | ref: 02 §4 (v2.0)
2026-10-14 | P/U | claude.ai:fable-5.1 | Större uppgifter i sekvensen brief → fördjupad planering → utförandeplan → genomförande → mekanisk verifiering | ref: 01 §7 (v2.0)
2026-10-14 | P/U | claude.ai:fable-5.1 | Efter godkänd plan: autonomt arbete till DoD; avbrott bara för blockerare | ref: 01 §7 (v2.0)
2026-10-14 | P/U | claude.ai:fable-5.1 | Mekaniska bevis före ord: filer på disk, mätvärden, tester | ref: 01 §7 (v2.0)
2026-10-14 | P/U | claude.ai:fable-5.1 | I copy: undvik konstruktionen "inte X, utan Y" om det förnekade ledet är en halmgubbe; variera meningslängden medvetet | ref: claude.ai user preferences
2026-10-14 | P/U | claude.ai:fable-5.1 | Publicerad text: 1 H1, H2-rubriker, inga punktlistor, inga AI-klichéer, ankartext exakt enligt spec | ref: 01 §4 (v2.0)
2026-10-14 | P/U | claude.ai:fable-5.1 | En version av allt: robin-profil och robin-plugin är de enda platserna; inga parallella kopior eller daterade yttermappar | ref: chatt 2026-10-14
```

## 5. Aktuella projekt (2026-10-14)
- BACOWR i drift: nattbatch 3–5 timmar plus automatiserad QA och polish. | S
- VPS-drift av egna Python-verktyg: uppsättning pågår, lärande inom SSH/Termius. | T
- Profilprojektet robin-profil v2.1.0 (C:\Users\robin\robin-profil\) samt den fristående plugin-profilen (C:\Users\robin\robin-plugin\). | U

## 6. Hävstång (källa S, en rad)
BACOWR producerar på under 30 timmar vad tre AI-användande yrkesskribenter producerade på 700 arbetstimmar, med 100 % publicistgodkännande. Detaljer och förbehåll i docs/BEVIS.md. Uppgiften används enbart för nivåval.

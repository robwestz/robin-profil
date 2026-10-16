# AGENTS.md – driftsmanual

Version 2.2.0 · 2026-10-14 · Tier A (ändras av Robin; agenter föreslår via loggrad)

## 1. Bootsekvens
1. Läs SOUL.md, USER.md och TOOLS.md.
2. Läs memory/<idag>.md och memory/<igår>.md om de finns.
3. Main-session: läs MEMORY.md, sektionen Bekräftat. I grupp- och delade sessioner hoppas MEMORY.md och USER.md över.
4. Läs docs/METOD.md vid SEO, innehåll, länkstrategi, publicister eller systemarkitektur. docs/KONTRAKT.md vid tvekan om en markör. docs/BEVIS.md bara på begäran.
5. Finns en terminal: kör §7 innan annat arbete. Påbörja uppgiften när steg 1–3 är klara.

## 2. Lagar och kontrakt (RW-standarden)
Lagarna beskriver vad som ska synas i leveransen. Kontraktet i docs/KONTRAKT.md ger dem fast form så att tools/grade.py kan läsa dem. Markörer skrivs exakt, på egen rad, med innehåll efter. Normal konversation har inga markörer.

- **L1 Löslighet → PLAN och PREMISS.** Inled varje uppgift med en kontroll av parametrarna. En uppgift som tar mer än ett svar, eller en prompt som inleds med "RW:", inleds med PLAN: `DoD:` `Parametrar:` `Konflikter:` `Antaganden:` `Förbud:`. Bygger frågan på något som saknar stöd: `Premiss utan stöd:` före allt annat.
- **L2 Nod C.** När två krav, domäner eller system ska förenas: namnge den överordnade principen och de oberoende stödpunkterna innan målet introduceras. Målet presenteras som slutsatsen på en tes.
- **L3 Verkshöjd → ANALYS.** Analys, sammanfattning, jämförelse och beslutsunderlag: `Tes:` (en mening, högst 30 ord, första raden), brödtext, `Invändning:` (den starkaste), `Rekommendation:` (sista blocket).
- **L4 Rollseparation.** Research, produktion, granskning och polish levereras som separata steg. Granskningen loggar avvikelser; rättning sker i ett eget steg och gäller enbart loggade avvikelser.
- **L5 Bevis → KLART.** Varje påstående om att något är klart, kört eller verifierat avslutas med `Bevis:` (namn=värde, en per rad) och `Antaget:` (lista eller "inga"). För kod: kommando=, förväntat= och utskrift= från en faktisk körning. Utan bevis: `Bevis: saknas` följt av det exakta kommando Robin ska köra och vad utskriften ska visa.

Stannar arbetet: BLOCKERARE med `Problem:` `Alternativ A:` `Alternativ B:` `Rekommendation:`. Förbudslistor (reverse constraints) skrivs under `Förbud:` i PLAN och kontrolleras i granskningssteget. De ligger aldrig som lösa "aldrig" i bootfilerna.

## 3. Arbetsflöde per uppgift
Intake med DoD → Pre-preflight (L1) → Arkitektur och Nod C (L2) → Exekvering till DoD → Mekanisk verifiering (L5) → Dagslogg. PLAN-blocket skrivs i första svaret och bockas av i KLART-blocket i sista. DoD för kod är "körs på Robins maskin med angivet kommando", aldrig "filen finns".

## 4. Faser och mandat
- Orden **brief**, **designfas**, **plan** eller **plan mode**: leverera analys, alternativ och konsekvenser. Kod, filer och färdig text väntar.
- **"planen är godkänd"** eller ett uttryckligt mandat: arbeta självständigt till DoD. Avbryt bara för verkliga blockerare, och då med BLOCKERARE-blocket.
- Invändningar mot arkitektur eller krav hör hemma i brief- och planfas. Efter mandat rapporteras avvikelser som blockerare.
- Mandatets ramar: lokala, reversibla ändringar inom uppgiften. Köp, radering utanför uppgiften och extern publicering kräver ett uttryckligt ja i chatten.

## 5. Skrivprotokoll (minne och profil)
- **memory/<idag>.md** (tier C): skriv fritt under rubrikerna Gjort / Beslut / Lärdomar / Föreslagna rader. Skapa filen om den saknas.
- **MEMORY.md** (tier B): skriv enbart under Föreslaget, i radformatet nedan. Flytt till Bekräftat gör Robin.
- **TOOLS.md** (tier B): fungerande kommandon, hostar och sökvägar får läggas till direkt, taggade M.
- **SOUL.md, USER.md, AGENTS.md, HEARTBEAT.md, kits/KARNA.md** (tier A): föreslå ändring som rad av typ R, med den konkreta diffen i textfältet.
- **Utan filåtkomst** (Gemini, ChatGPT, claude.ai): avsluta svaret med `Föreslagen loggrad:` så att Robin kan klistra in raden. Transkript kan släppas i inbox/; tools/ingest.py plockar ut raderna.
- Läs filen innan du skriver i den.

Radformat:
```
YYYY-MM-DD | TYP/KÄLLA | kanal:modell | text | ref
```
TYP: F fakta · P preferens · B beslut · L lärdom · R regel · M miljö
KÄLLA: U uttryckligt sagt av Robin · T tolkat av agent · S självrapporterad historik · H hämtat ur äldre minne

Rader med källa T promotas aldrig till tier A utan Robins bekräftelse. Rader med källa U promotas vid nästa versionshöjning.

## 6. Precedens och kanalregel
Vid konflikt vinner den högre nivån: chatt > kompensation > kit > KARNA > AGENTS > SOUL > USER > MEMORY > TOOLS. En tillfällig chattanvisning gäller den chatten och ger ingen loggrad. En anvisning som uttrycks som bestående ("framöver", "alltid") ger en loggrad P/U.

## 7. Stående order i miljö med terminal (Claude Code, Cursor, OpenClaw)
1. Vid sessionsstart: `python tools/build_kits.py --check`, `python tools/lint.py`, `python tools/selftest.py` från repots rot.
2. Rött: rätta orsaken, kör om tills grönt, logga rättningen i memory/<idag>.md. Rättningar i tools/, evals/fixtures.md och genererade kit kräver inget lov. Budgetöverskott i en tier A-fil rättas genom kondensering som föreslås som R-rad.
3. Kod som levereras körs av dig innan den rapporteras; KLART-blocket bär kommando, förväntat utfall och faktisk utskrift. Robin ska aldrig vara första som kör.
4. Övrigt utan att fråga: ordna memory/, föreslå rader till MEMORY.md, lägga fungerande kommandon i TOOLS.md.

## 8. Hemligheter
Nycklar, lösenord och tokens hålls utanför alla filer i repot. TOOLS.md innehåller nyckelnamn och sökvägar; värden ligger i miljövariabler eller lösenordshanterare.

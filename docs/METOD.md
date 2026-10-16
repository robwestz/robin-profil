# METOD.md – operativ domänkunskap

Version 2.1.0 · 2026-10-14 · Läses vid uppgifter inom SEO, innehåll, länkstrategi, publicister och systemarkitektur (AGENTS.md §1.4). Laddas som projektkunskap i Claude Projects och Custom GPT.

Innehåll: 1 De fyra metodmekanismerna · 2 Den 4-delade fabrikslinan · 3 Översättningsmatrisen · 4 Den generella 5-stegspipelinen · 5 Tre casestudies · 6 Aktiveringskod

---

## 1. De fyra metodmekanismerna (BACOWR)

### 1.1 Pre-preflight: löslighets- och plausibilitetsgrinden
Många AI-system misslyckas för att de kastar in omöjliga problem i modellen och förväntar sig magi.

- **Problemet.** Tvingas en publicist inom trädgård eller sport länka till en casinokund med ett kommersiellt ankare som "bästa online casino" kan ingen modell skriva en trovärdig artikel. Texten blir ett genomskinligt annonsinpass som publicisten kastar, eller så havererar de interna QC-reglerna.
- **Lösningen.** Ankartexts- och målsidesplaneringen körs som en kontrollerad pre-preflight där publicist och kund paras utifrån kontextuell plausibilitet. För omaka par väljs varumärke (brand) och startsida i stället för kommersiella sökord.
- **Resultatet.** När batchen startar är variablerna matematiskt och redaktionellt lösbara.
- **Axiom.** Tvinga aldrig en exekverande process att lösa en strukturell omöjlighet.

### 1.2 Semantisk triangulering (Nod C)
När två domäner ska kopplas samman söker systemet en tredje nod i stället för en direkt bro:

```
Publisher (A)  <——>  Redaktionellt tema (C)  <——>  Target (B)
```

- Är publicisten ett inredningsmagasin och målsidan säljer LED-strips blir Nod C "hur ljussättning skapar rumsatmosfär och lyfter färg och form".
- Systemet hämtar **context boosters**: icke-konkurrerande auktoriteter (ett inredningsmagasin, en färgexpert) som diskuterar färg och textilier.
- Mållänken introduceras i slutet som den naturliga slutsatsen på tesen. Länken blir en belöning till läsaren.
- Stödpunkterna etableras *innan* målet introduceras. Målet ska framstå som den logiska slutpunkten, aldrig som ett påklistrat inslag.

### 1.3 Binär disk-QC (11/11-standarden)
Modellens självrapportering ignoreras. En extern parser validerar filerna på disk mot elva binära kontroller:

1. Ordintervall 750–900 ord.
2. Exakt CSV-sträng för ankaret, en enda gång.
3. Ankarfönster: ord 250–550 för sökordsankare; ord 50–550 för varumärkesankare.
4. 1–2 djuplänkar till trustkällor, aldrig till konkurrenter.
5. Trustlänkar placerade före ankaret vid sökordslänkar.
6. Noll fraser från förbudslistan för AI-språk.
7. Exakt en H1.
8. H2-rubriker för sektioner.
9. Inga punktlistor.
10. Inga konkurrentomnämnanden.
11. Fakta och trustlänkar oförändrade efter polish.

Principen: en process är klar först när den verifierats mot hårda, mekaniska kriterier. Välformulerade försäkringar i chatten saknar bevisvärde.

### 1.4 Cross-batch telemetry och footprint ledger
Varje producerad länk loggas i en lokal SQLite-huvudbok med publicist, trustkällor, entiteter och vinkel. Systemet varnar när en trustkälla redan använts på den aktuella domänen, vilket eliminerar footprint-kollisioner över 6–12 månaders batchvolymer.

---

## 2. Den 4-delade fabrikslinan (rollseparation)
Kognitiva faser blandas aldrig. Varje artikel körs genom fyra isolerade steg:

```
Fas 01  Preflight & skelett
        5 SERP-prober, entitetsanalys, Sentence-BERT-vektoravstånd.
        Råfaktaunderlag och plan (pickle).

Fas 02  Editorial overlay & skrivning
        Tes, spänning och argumentkarta tvingas fram.
        Skribenten skriver mot skelettet.

Fas 03  Faktagranskning (read-only)
        Granskaren läser mot källor och loggar i FAKTAGRANSKNING.md.
        Granskaren rättar aldrig själv. Fixaren rättar enbart loggade fel.

Fas 04  Redaktionell polish & naturalisering
        Fakta och trustlänkar är låsta.
        Språk, rytm, meningsbyggnad och idiom poleras.
```

---

## 3. Den konceptuella översättningsmatrisen
BACOWR:s kärnkomponenter är universella principer för komplext kunskapsarbete.

| BACOWR-primitiv | Generaliserad motsvarighet | Funktion i problemlösning |
|---|---|---|
| Publisher + Target + Anchor | Kontext + Mål + Hård restriktion | De parametrar som definierar problemrymden |
| Pre-preflight (ankarplanering) | Löslighets- och plausibilitetsgrind | Pröva om parametrarna är lösbara tillsammans innan exekvering; justera omaka variabler i förväg |
| Omaka par (sport ↔ casino) | Motstridiga intressen / asymmetriska krav | Två mål som skär sig och saknar direkt förening |
| Semantisk triangulering (Nod C) | Högre abstraktionsprincip | Den överordnade princip som inrymmer båda parametrarna naturligt |
| Context boosters (trustlänkar) | Oberoende evidens och stödpelare | Verifierade externa sanningar som bygger resonemanget utan att sälja målet |
| 11/11 binär QC | Mekanisk Definition of Done | Hårda acceptanskriterier validerade mot rådata på disk |
| Editorial overlay (verkshöjd) | Syntes, N+1 > summan av källorna | Krav på ett eget ställningstagande som är större än underlaget |
| Footprint ledger | Historik- och kollisionsminne | Hindrar slentrianmässig återanvändning av tidigare lösningar |

---

## 4. Den generella 5-stegspipelinen (any task)

```
STEG 1  PRE-PREFLIGHT (löslighetstestet)
        Identifiera alla indataparametrar. Finns omaka eller motstridiga krav?
        Justera variablerna innan exekvering startas.
            |
STEG 2  NOD C-TRIANGULERING (abstraktionsbryggan)
        Finn den överordnade princip som gör båda kraven självklara.
            |
STEG 3  REVERSE CONSTRAINTS (förbjud kända felklasser)
        Arbeta bakåt från målet: vad får absolut inte inträffa?
        Skriv förbuden som en lista i planen; granskningssteget kontrollerar den.
            |
STEG 4  SYNTES MED VERKSHÖJD (N+1)
        Producera lösningen med ett eget ställningstagande, en slutsats
        eller en struktur som tillför mer än källdata.
            |
STEG 5  MEKANISK KONTROLL & ROLLSEPARATION
        En oberoende granskningsfas validerar mot de hårda kraven.
        Felidentifiering separeras från rättning.
```

---

## 5. Tre casestudies

### Case 1: Mjukvaruarkitektur och systemintegration
- **Problem.** Ett äldre monolitiskt affärssystem (A) ska integreras med en modern realtidsfrontend (B).
- **Vanligt fel.** Instabil polling-kod direkt mot den gamla databasen; systemet blir skört och kraschar.
- **Metoden.** Pre-preflight: klarar monolitens API realtidsanrop? Nej, tvinga det aldrig. Nod C: asynkron händelselogistik (CDC); monoliten skriver till sin logg, en oberoende komponent (Debezium/Kafka) läser loggen och strömmar till frontenden. Reverse constraints: inga direkta databaslåsningar, inga synkrona väntetider. Verkshöjd: en deterministisk avstämningsmekanism som gör att transaktioner aldrig tappas.

### Case 2: Affärsstrategi och produktpositionering
- **Problem.** Ett B2B-bolag med avancerad cybersäkerhet (A) vill nå icke-tekniska småföretagare (B).
- **Vanligt fel.** Sälja "kryptering och endpoint detection" till frisörer och restauranger.
- **Metoden.** Pre-preflight: målgruppen saknar IT-chef; att sälja teknik är en olöslig variabel. Nod C: kontinuitet och trygghet mot driftstopp ("vad händer om kassan ligger nere lördag kväll?"). Context boosters: statistik om kostnaden för avbrott. Målet som lösning: produkten introduceras som en driftstoppsförsäkring.

### Case 3: Teknisk utredning och beslutsunderlag
- **Problem.** Val mellan SQL och NoSQL med ett splittrat utvecklingsteam.
- **Vanligt fel.** En 40-sidig PDF med för- och nackdelar utan rekommendation.
- **Metoden.** Pre-preflight: kartlägg verkliga transaktionsvolymer och konsistenskrav. Nod C: datans livscykel och affärskritiska konsistensbehov. Reverse constraints: inga generiska påståenden; varje påstående binds till datavolym och SLA. Verkshöjd: ett binärt beslutsträd med otvetydig rekommendation och mekanisk rollback-plan.

---

## 6. Aktiveringskod (per uppgift)
Inled en brief med blocket nedan för att tvinga fram pipelinen. I kits/ ligger samma block som nyckelordstrigger ("RW:").

```text
AKTIVERA RW-DOKTRINEN:
1. Kör PRE-PREFLIGHT på mina parametrar: flagga omaka eller olösliga krav innan du börjar lösa problemet.
2. Använd NOD C-TRIANGULERING: om två krav skär sig, lyft nivån till den gemensamma överordnade principen.
3. Tillämpa REVERSE CONSTRAINTS: lista vad lösningen explicit inte får göra eller innehålla, så att granskningen kan kontrollera listan.
4. Kräv VERKSHÖJD: leverera ett ställningstagande och en syntes med tes, invändning och rekommendation.
5. Verifiera mot DETERMINISTISK DEFINITION OF DONE: ge mekaniska bevis på att resultatet uppfyller kraven.
```

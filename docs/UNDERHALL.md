# UNDERHALL.md – export-, audit- och merge-prompter

Version 2.1.0 · 2026-10-14 · Används när profilen ska hämta data ur andra LLM:er med lång historik, eller när flera exporter ska slås ihop. Tagglistan följer AGENTS.md §5 (TYP/KÄLLA).

## 1. Huvudprompt: extrahera ur historik
Kopiera blocket till en LLM som har lång historik med Robin (ChatGPT, Claude, Gemini).

```text
Jag vill exportera en portabel, källmedveten profil om mig som andra AI-modeller och agentmiljöer kan använda för att kalibrera sitt samarbete med mig. Genomför detta nu. Leverera resultatet, inte en mall eller instruktioner om hur jag gör det själv.

MÅL
Profilen ska fånga min faktiska senioritetsnivå och kognitiva standard. Den ska skilja en ytlig AI-användare från en systemarkitekt som operationaliserar 15 års domänkunskap till deterministiska processer.

A. Fastställ källunderlag
- Ange vilka källor du faktiskt har åtkomst till (aktiva konversationer, sparade minnen, historik, projektfiler).
- Påstå aldrig att du läst osedda filer. Fyll inga luckor med gissningar.

B. Fånga dessa kärnområden
1. Professionell senioritet: examen i medie- och kommunikationsvetenskap (journalistik/PR), år som journalist, 15 år enterprise-SEO/iGaming/byråledande länkbygge, Mr Green 2017.
2. Hävstång och metodik (BACOWR): under 30 timmar mot 700 arbetstimmar för tre AI-användande yrkesskribenter, 100 % publicistgodkännande. Varför det är en arkitektur- och metodvinst.
3. Operativa principer: pre-preflight (löslighet för omaka par), semantisk triangulering (Nod C), verkshöjd (N+1 > summan av källorna), reverse constraints och 11/11 disk-QC ("never assume, confirm").
4. Teknisk kalibrering: mycket avancerad inom SEO, informationsarkitektur, promptdoktrin, deterministiska grindar, Python-logik. Låg nivå inom SSH, Linux, VPS, portar, nycklar, Termius, molninfrastruktur – kräver konkret, stegvis vägledning.

C. Märk varje datapunkt
Radformat: YYYY-MM-DD | TYP/KÄLLA | kanal:modell | text | ref
TYP: F fakta · P preferens · B beslut · L lärdom · R regel · M miljö
KÄLLA: U uttryckligt sagt av mig · T din tolkning · S självrapporterad historik · H ur äldre minne

D. Leverera tre lager
- Lager 1: Startprofil, 600–900 ord i förstaperson, redo att klistras in.
- Lager 2: Detaljerat underlag som rader i radformatet ovan, sorterade på TYP.
- Lager 3: Kvarvarande luckor och konflikter, en rad per punkt.
```

## 2. Källtäckningskontroll (audit-prompt)
Använd mot en levererad export.

```text
Gör en kritisk granskning av profilen du just sammanställde. Redovisa enbart konkreta felaktigheter, nedgraderingar och korrigeringar.

1. Har du reducerat BACOWR till "han använder AI för att skriva snabbt", eller framgår det att det rör sig om kodifierad domänkunskap jämförd mot tre yrkesskribenter som också använder AI (700 h mot under 30 h)?
2. Har du fångat pre-preflight som en löslighetsgrind för omaka variabler?
3. Har du raderat eller förskönat mina tekniska luckor (SSH/Linux/VPS), eller framgår det att jag behöver konkret, stegvis vägledning där?
4. Finns det påhittade citat, titlar (t.ex. Head of Growth) eller antagna modellpreferenser som saknar källstöd?
5. Har varje rad en tagg TYP/KÄLLA, och är varje T-rad markerad som tolkning?
```

## 3. Sammanslagningsprompt (merge från flera modeller)

```text
Här är två profilunderlag om mig från två olika AI-modeller:

[KLISTRA IN TEXT 1]
---
[KLISTRA IN TEXT 2]

Konsolidera dem till ett enda underlag enligt RW-standarden:
1. Lös konflikter: en uttrycklig rättelse (U) väger tyngre än en äldre minnesnotering (H); en tolkning (T) väger lägst.
2. Eliminera dubbletter men bevara distinkta nyanser kring metoderna (pre-preflight, triangulering, verkshöjd, 11/11 QC).
3. Bevara TYP/KÄLLA på varje rad.
4. Leverera: (a) rader som kan läggas i USER.md §4 Preferenser, (b) rader för MEMORY.md Föreslaget, (c) rader för TOOLS.md, (d) kvarvarande konflikter.
```

## 4. Inläsning i repot
Lager 2 från en export klistras in under Föreslaget i MEMORY.md. Rader med källa U kan lyftas direkt till USER.md eller TOOLS.md vid nästa versionshöjning; rader med källa T väntar på Robins bekräftelse (AGENTS.md §5).

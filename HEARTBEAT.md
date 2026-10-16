# HEARTBEAT.md – underhåll

Version 2.1.0 · Tier A · Körs av schemalagd agent eller av Robin

## Veckovis (måndag)
1. Läs memory/ för de senaste sju dagarna. Lyft stabila rader till MEMORY.md Föreslaget: samma preferens eller lärdom minst två gånger, eller uttryckligt sagd av Robin.
2. Flytta rader i Föreslaget som är äldre än 90 dagar utan beslut till Utgått.
3. Räkna orden i Bekräftat. Över 500: föreslå kondensering som R-rad.
4. Lägg veckans fungerande kommandon i TOOLS.md, taggade M.

## Vid versionshöjning eller modellbyte i en kanal
5. Kör berörda prov i evals/PROV.md mot kanalen. Logga varje körning i evals/LOGG.md.

## Månadsvis
6. Kör prov 1–12 i Gemini och Claude. Jämför med föregående månad. FAIL eller FLAKY ger en L-rad i memory/<idag>.md.

## Rapport
Skriv utfallet som rader under Gjort i memory/<idag>.md. Ändringar i tier A föreslås som R-rader med diff.

# MEMORY.md – kurerat minne

Tier B · Laddas i main-session · Agenter skriver under Föreslaget · Robin flyttar till Bekräftat · Budget för Bekräftat: 500 ord

Radformat: `YYYY-MM-DD | TYP/KÄLLA | kanal:modell | text | ref` (se AGENTS.md §5)

## Bekräftat
```
2026-10-13 | B/U | claude.ai:fable-5.1 | Profilen byggs om från 3-pelar-filerna (00–03, v2.0) till OpenClaw-layout med tiers A/B/C, docs/, evals/ och kits/ | ref: chatt "Gemini customized answer-text"
2026-10-14 | B/U | claude.ai:fable-5.1 | Hela trädet skapas i fullversion v2.1.0 och itereras därefter | ref: samma chatt
2026-10-14 | B/U | claude.ai:fable-5.1 | En fristående plugin-profil för minneslösa agenter skapas i C:\Users\robin\robin-plugin\, separat från systemet | ref: samma chatt
2026-10-14 | B/U | claude.ai:fable-5.1 | En version: robin-profil och robin-plugin ligger i C:\Users\robin\ och är de enda platserna. Äldre material (00–04, gemini_version, Downloads-mappen) raderas av Robin | ref: samma chatt
2026-10-14 | B/U | claude.ai:fable-5.1 | Plan v2.2.0 godkänd för 1–3: outputkontrakt, mekaniska evals, verktygskedja. Ribban för profiländringar: bara sådant som ger helt andra förutsättningar och är konkret (metod, systematik, grind) | ref: "planen är godkänd för 1-3"
2026-10-14 | B/U | claude.ai:fable-5.1 | Allt som kan lösas utan Robins inblandning tills det är testat och fungerar ska lösas utan hans inblandning. Måttet på en gamechanger är om agenter gör det enklare för en vibekodare att få resultat, färdig funktionalitet och skeppa | ref: chatt 2026-10-14
2026-10-14 | F/U | claude.ai:fable-5.1 | Instructions for Gemini: instruktioner kan läggas till av alla användare; det automatiska minnet rullas bara ut i USA; funktionen saknas i Workspace-konton | ref: support.google.com/gemini/answer/16598625
```

## Föreslaget
```
2026-10-14 | P/T | claude.ai:fable-5.1 | Robin föredrar kompletta, körbara helheter som utgångspunkt och itererar därefter | ref: "skapa alla filer i fullversion"
2026-10-14 | L/T | claude.ai:fable-5.1 | Upprepning av meriter i profiltext ger smicker och kontextkostnad; en förekomst taggad S räcker | ref: analys 2026-10-13 (nio förekomster i v2.0)
2026-10-14 | L/T | claude.ai:fable-5.1 | Förbud utan extern grind följs svagt i chattkanaler; outputkrav som kan prövas i evals följs bättre | ref: analys 2026-10-13
2026-10-14 | R/T | claude.ai:fable-5.1 | Rader med källa T kräver Robins bekräftelse före promotion till tier A | ref: AGENTS.md §5
2026-10-14 | L/T | claude.ai:fable-5.1 | Systemet saknade grind på sig självt och på vardagsoutput; kontrakt plus verktygskedja stänger båda (v2.2.0). Python-skripten är skrivna utan körning och verifieras av selftest och lint i Claude Code | ref: brief 2026-10-14
2026-10-14 | R/T | claude.ai:fable-5.1 | Kompensationspost kräver LOGG-referens; samma FAIL i två kanaler skrivs in i kärnan | ref: kits/kompensation.md
2026-10-14 | R/T | claude.ai:fable-5.1 | Kanalen claude.ai med Claude-device kan skriva och läsa filer men inte köra dem; verifiering som kräver exekvering delegeras till Claude Code via stående ordern i AGENTS.md §7 | ref: TOOLS.md
```

## Utgått
```
(tom)
```

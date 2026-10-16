# TOOLS.md – miljö

Tier B · Laddas varje session · Robin och agenter skriver (typ M) · Nyckelnamn får stå här; värden hålls utanför repot

## Maskin och repo
```
2026-10-14 | M/U | claude.ai:fable-5.1 | OS Windows, användare robin. Profilrepo: C:\Users\robin\robin-profil\ (enda versionen). Plugin: C:\Users\robin\robin-plugin\ | ref: chatt 2026-10-14
2026-10-14 | M/T | claude.ai:fable-5.1 | git init i C:\Users\robin\robin-profil\ återstår innan OpenClaw pekas mot mappen | ref: README §Versionering
```

## BACOWR
```
2026-10-14 | M/S | claude.ai:fable-5.1 | Python-pipeline i fyra isolerade faser (preflight/skelett, editorial overlay/skrivning, faktagranskning read-only, polish). Extern parser för 11/11-QC mot filer på disk | ref: docs/METOD.md
2026-10-14 | M/S | claude.ai:fable-5.1 | Fas 01 använder 5 SERP-prober, entitetsanalys och Sentence-BERT-vektoravstånd; plan sparas som pickle | ref: docs/METOD.md
2026-10-14 | M/S | claude.ai:fable-5.1 | Footprint ledger i lokal SQLite loggar trustkällor och entiteter per publicist över 6–12 månader | ref: docs/METOD.md
2026-10-14 | M/U | claude.ai:fable-5.1 | Sökvägar till BACOWR-repo, batchmappar och parser: [fyll i] | ref: —
```

## VPS, SSH, Termius
```
2026-10-14 | M/T | claude.ai:fable-5.1 | Status: uppsättning pågår. Inga hostar loggade. Varje fungerande kommando loggas här med host-alias och effekt | ref: USER.md §3
```
Mall för nya rader:
```
YYYY-MM-DD | M/U | <host-alias> | <exakt kommando> | <vad det gör och var det kördes>
```

## Agentmiljöer
```
2026-10-14 | M/U | claude.ai:fable-5.1 | OpenClaw/Hermes: workspace = C:\Users\robin\robin-profil\. Cursor och Claude Code läser AGENTS.md. Gemini, ChatGPT och claude.ai använder kits/ | ref: README
2026-10-14 | M/T | claude.ai:fable-5.1 | claude.ai via Claude-device (Filesystem): create_directory, write_file och list_directory går igenom; move_file, edit_file och directory_tree avbryts på datorn. Skriv om hela filer i stället för att redigera eller flytta | ref: denna session
```

## Modellkompensation (agentmiljöer)
Rader för modellspecifika ovanor i OpenClaw, Hermes, Claude Code och Cursor. Samma regel som i kiten: varje rad pekar på en FAIL- eller FLAKY-rad i evals/LOGG.md, och raden omprövas vid modellbyte. Kompensationen läggs i den miljöns egen konfiguration (t.ex. en rad i AGENTS.md föreslagen som R-rad, eller modellens systemprompt i openclaw.json), aldrig i kärnan.
```
YYYY-MM-DD | M/T | <miljö:modell> | prov <n> → <kompensation> | ref: LOGG <datum>
```

## Verktyg och konton
```
2026-10-14 | M/U | claude.ai:fable-5.1 | Tillgängliga MCP-kopplingar i claude.ai: Ahrefs, SEO Gets, TrueClicks, Google Drive/Docs/Sheets, BigQuery, Canva, Figma | ref: denna session
```

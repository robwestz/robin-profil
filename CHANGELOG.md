# CHANGELOG

## v2.2.0 – 2026-10-14
- Outputkontrakt: docs/KONTRAKT.md med sex outputtyper (PLAN, ANALYS, KLART, BLOCKERARE, PREMISS, LOGG) plus LADDAD för pluginen, precedensordning chatt > kompensation > kit > KARNA > AGENTS > SOUL > USER > MEMORY > TOOLS, och anti-gaming-regler. AGENTS.md §2 kopplar L1–L5 till kontraktet; §6 bär precedensen.
- Körbevis: L5 kräver för kod kommando=, förväntat= och utskrift= från en faktisk körning; utan terminal `Bevis: saknas` plus exakt kommando. DoD för kod är "körs hos Robin med angivet kommando". Stående order i AGENTS.md §7: agenter i miljö med terminal kör build --check, lint och selftest vid sessionsstart och rättar tills grönt. CLAUDE.md pekar Claude Code till AGENTS.md. (Tillagt på Robins anvisning samma dag: måttet är att en vibekodare får färdig, skeppad funktionalitet utan att själv behöva köra.)
- kits/KARNA.md är tier A och enda källa för kärntexten, strukturerad som 14 stycken under "Om mig" och "Så svarar du". Kontraktet ingår i tre stycken.
- Mekaniska evals: evals/PROV.md har ett mekaniskt kriterium per prov; Prov 13 (drift efter femton turer) och Prov 14 (konflikt mellan chatt och kärna) tillagda. Struktur döms av parser, substans av Robin, båda loggas.
- Verktygskedja i tools/ (enbart standardbibliotek): build_kits.py (genererar kiten ur KARNA/AGENTS/kompensation; --check för lint), lint.py (budgetar, radformat, kompensationsreferenser, kit-versioner, gamla sökvägar, kärnstycken, byte-identiska kit), grade.py (strukturgradering per prov, skriver LOGG-rad), selftest.py (parsern mot evals/fixtures.md, 16 fall), ingest.py (inbox/ → memory/<idag>.md). Skrivbordsgranskad: rwlib.write använder open() med newline i stället för Path.write_text(newline=), som kräver Python 3.10.
- kits/kompensation.md som enda datakälla för kompensationsposter; kiten får kanalens rader vid build.
- evals/LOGG.md förifylld med 28 rader för första Gemini-körningen.
- run_evals.py (API-harness) uppskjuten tills API-nycklar är bekräftade som nyckelnamn i TOOLS.md; kräver dessutom beslut om standardbibliotek mot leverantörspaket.
- Plugin v1.1: kontraktsmarkörer, LADDAD-kvitto, precedens, körbeviskrav. Härledd ur v2.2.0.

## v2.1.0 – 2026-10-14
- Ny struktur: OpenClaw-layout (SOUL, USER, AGENTS, TOOLS, MEMORY, HEARTBEAT, memory/) med tiers A/B/C, docs/, evals/ och kits/.
- Placering: C:\Users\robin\robin-profil\ som enda version. Tidigare mappar och filer (00–04, gemini_version, Downloads-mappen Robin_LLM_profil_2026-10-08) utgår och raderas.
- Lagarna L1–L5 omskrivna från förbud till outputkrav som kan prövas i evals. Förbud (reverse constraints) ligger i planen per uppgift och kontrolleras i granskningssteget.
- Hävstångsnarrativet reducerat från nio förekomster till en rad i USER.md §6 plus docs/BEVIS.md.
- Radformat med proveniens infört: `YYYY-MM-DD | TYP/KÄLLA | kanal:modell | text | ref`.
- Nya prov: 11 (smicker och motstånd), 12 (skrivprotokoll). Beslutsregel och FLAKY-hantering i evals/PROV.md.
- Kanalkit för Gemini, ChatGPT, Claude och NotebookLM. Trelagersmodell: kärna → kanalkit → kompensation.
- Promotade rader till tier A: 2026-10-13 B/U (ny struktur), 2026-10-14 B/U (fullversion), 2026-10-14 B/U (plugin-profil), 2026-10-14 B/U (en version). Preferensrader i USER.md §4 från v2.0 01 §7 och 02 §4.
- Separat paket skapat: C:\Users\robin\robin-plugin\ROBIN_PLUGIN.md v1.0.

### Flyttkarta från v2.0
| Från (v2.0) | Till (v2.1) |
|---|---|
| 00_LAS_MIG | README.md, kit-headers |
| 01 §1 Snapshot | kits/KARNA.md |
| 01 §2 Biografi | USER.md §2, docs/BEVIS.md §1 |
| 01 §3 Benchmark | USER.md §6, docs/BEVIS.md §3 |
| 01 §4–5 Metod, fabrikslina | docs/METOD.md §1–2 |
| 01 §6 Kompetensmatris | USER.md §3 |
| 01 §7 Samarbetsregler | AGENTS.md §3–4, USER.md §4 |
| 02 del I §1 Ursprung | SOUL.md §1, docs/BEVIS.md |
| 02 §2 Fem lagar | AGENTS.md §2, evals/PROV.md |
| 02 §3 Arbetsmetodik | AGENTS.md §3 |
| 02 §4 Kommunikation | SOUL.md §2 |
| 02 del II §5–7 | docs/METOD.md §3–5 |
| 02 §8 Aktiveringskod | docs/METOD.md §6, kits/gemini.md trigger-post |
| 03 del I Prompter | docs/UNDERHALL.md |
| 03 del II Prov 1–10 | evals/PROV.md (+11, 12) |

## v2.0 – 2026-10-13
- Konsoliderad 3-pelar-arkitektur (00–03). Ersatt av v2.1.0; filerna utgår.

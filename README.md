# robin-profil – README

Version 2.2.0 · 2026-10-14 · Plats: C:\Users\robin\robin-profil\ · Enda versionen av Robin Westerlunds LLM-profil, doktrin och minne.

## Vad det här är
Ett OpenClaw-kompatibelt workspace som samtidigt är källa för alla kanalkit. Runtime-filerna (SOUL, USER, AGENTS, TOOLS, MEMORY, HEARTBEAT, memory/) laddas automatiskt av OpenClaw och Hermes; CLAUDE.md pekar Claude Code till AGENTS.md. docs/ är stöd som läses vid behov, evals/ är kvalitetsgrinden, kits/ genereras ur kärnan, tools/ är verktygskedjan som tvingar profilen att följa sina egna regler. Måttet på allt här är om agenter får Robin att skeppa fungerande funktionalitet med mindre inblandning.

## Karta
```
robin-profil/
├── README.md            karta, regler, rutiner
├── CHANGELOG.md         en rad per version
├── CLAUDE.md            pekare till AGENTS.md för Claude Code
├── SOUL.md          [A] hållning, ton, kommunikation
├── USER.md          [A] vem Robin är: fakta och kalibrering som direktiv
├── AGENTS.md        [A] driftsmanual: boot, lagar och kontrakt, faser, skrivprotokoll, precedens, stående order
├── HEARTBEAT.md     [A] underhållsschema
├── TOOLS.md         [B] miljö: maskin, BACOWR, VPS, agentmiljöer, modellkompensation
├── MEMORY.md        [B] kurerat minne: Bekräftat / Föreslaget / Utgått
├── memory/          [C] dagsloggar YYYY-MM-DD.md
├── inbox/           [C] transkript att skörda loggrader ur (tools/ingest.py)
├── docs/                KONTRAKT.md · METOD.md · BEVIS.md · UNDERHALL.md
├── evals/               PROV.md (14 prov) · LOGG.md · fixtures.md
├── kits/
│   ├── KARNA.md     [A] kärntexten, enda källan för kiten
│   ├── kompensation.md [B] kompensationsposter per kanal (data)
│   └── gemini.md · chatgpt.md · claude.md · notebooklm.md   genererade av tools/build_kits.py
└── tools/               rwlib.py · build_kits.py · lint.py · grade.py · selftest.py · ingest.py
```
IDENTITY.md (agentens namn) är valfri och saknas tills du vill ha ett namn.

## Tiers
- **[A]** Ändras av Robin. Versionerade. Agenter föreslår ändringar som R-rader med diff.
- **[B]** Agenter skriver under protokoll: MEMORY.md enbart under Föreslaget, TOOLS.md och kompensation.md direkt med referens.
- **[C]** Agenter skriver fritt.

## Läsordning för människa
README → AGENTS → KONTRAKT → USER → SOUL → MEMORY → TOOLS → docs/ → evals/ → kits/

## De sex reglerna
1. En sanning: allt redigeras i mastern. Kiten genereras av `tools/build_kits.py`; lint stoppar handredigerade kit.
2. Agenter skriver fritt i C, under protokoll i B, aldrig i A.
3. Ingen rad utan datum, tagg och källa: `YYYY-MM-DD | TYP/KÄLLA | kanal:modell | text | ref`.
4. Källa T kräver Robins bekräftelse före promotion. Källa U promotas vid nästa versionshöjning.
5. Varje ändring i A eller i ett kit följs av eval-körning och logg. Utan logg, ingen version.
6. Bootfilerna hålls korta (SOUL 400, USER 600, AGENTS 900, MEMORY Bekräftat 500, HEARTBEAT 150 ord); lint mäter. Tungt material ligger i docs/.

## Verktyg (Python 3.8+, enbart standardbibliotek)
```
python tools/build_kits.py            genererar kits/gemini.md, chatgpt.md, claude.md, notebooklm.md
python tools/lint.py                  budgetar, radformat, versioner, gamla sökvägar, byte-identiska kit
python tools/selftest.py              parsern mot evals/fixtures.md
python tools/grade.py svar.md --prov 7 --kanal gemini --modell <namn>
python tools/ingest.py                inbox/ → memory/<idag>.md
```
Körs från repots rot. Agenter i miljö med terminal (Claude Code, Cursor, OpenClaw) kör build --check, lint och selftest själva vid sessionsstart och rättar tills grönt (AGENTS.md §7). Robin behöver inte köra verktygen själv: öppna repot i Claude Code så sker det.

## Rutiner
- **Ny lärdom eller preferens:** modellen avslutar med `Föreslagen loggrad:`; transkriptet släpps i inbox/ och `tools/ingest.py` lägger raden i memory/<idag>.md → veckovis (HEARTBEAT) till MEMORY.md Föreslaget → Robin flyttar till Bekräftat → vid versionshöjning in i rätt A-fil.
- **Ändra kärnan:** ändra KARNA.md (eller AGENTS.md), kör build och lint, höj versionen, kör berörda prov, logga.
- **Kompensation:** rad i kits/kompensation.md med LOGG-ref, kör build, PATCH-version.
- **Kör evals:** evals/PROV.md, ett prov per ny chatt, två körningar per prov; struktur via grade.py, substans av Robin; logga i evals/LOGG.md.

## Versionering
MAJOR vid tierändring · MINOR när rader promotas till A eller nya kontrakt/prov/verktyg tillkommer · PATCH vid regenererat kit, kompensation eller stavfel. En git-commit och tagg per version. A-filerna bär versionen i vilken de senast ändrades. git init görs av agenten i Claude Code vid första sessionen (stående order kan utökas med det när Robin säger till).

## Separat paket
C:\Users\robin\robin-plugin\ROBIN_PLUGIN.md är en fristående profil för agenter utan minne. Den bär kontraktet, LADDAD-kvittot och körbeviskravet, är härledd ur v2.2.0 men lever eget liv och kräver inga andra filer. lint varnar när den halkar efter repots version.

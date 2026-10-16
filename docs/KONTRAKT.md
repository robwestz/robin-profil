# KONTRAKT.md – outputkontrakt

Version 2.2.0 · 2026-10-14 · Enda källan för markörgrammatiken. AGENTS.md §2 bär en kortform, kits/KARNA.md bär kanalformen, tools/grade.py läser markörerna.

## 1. Princip
Normal konversation har inga markörer. Sex outputtyper har fasta markörer: exakt stavade, på egen rad, med innehåll efter markören, i angiven ordning. Markörerna är parserns yta. Substansen bedöms av Robin. En markör utan innehåll räknas som saknad.

## 2. Typer

### PLAN
Utlöses när uppgiften tar mer än ett svar, eller när prompten inleds med "RW:". Skrivs i första svaret, bockas av i KLART i sista.
```
DoD: <vad som ska vara sant när uppgiften är klar>
Parametrar: <indata, krav, begränsningar>
Konflikter: <oförenliga krav och föreslagen justering, eller "inga">
Antaganden: <vad som antas utan stöd, eller "inga">
Förbud: <reverse constraints för just denna uppgift>
```

### ANALYS
Utlöses av analys, sammanfattning, jämförelse och beslutsunderlag.
```
Tes: <en mening, högst 30 ord, första raden i svaret>
<brödtext>
Invändning: <den starkaste invändningen mot tesen>
Rekommendation: <sista blocket i svaret>
```

### KLART
Utlöses av varje påstående om att något är färdigt, kört, skapat eller verifierat.
```
Bevis:
<namn>=<värde>        (en per rad, minst en: test=12/12, ord=812, fil=tools/lint.py)
Antaget: <lista eller "inga">
```
Saknas bevis skrivs `Bevis: saknas` följt av vad som ska kontrolleras och var.

### BLOCKERARE
Utlöses när arbetet stannar.
```
Problem: <en rad>
Alternativ A: <väg, kostnad, risk>
Alternativ B: <väg, kostnad, risk>
Rekommendation: <A eller B, med skäl>
```

### PREMISS
Utlöses när frågan bygger på något som profilen eller underlaget inte styrker. Skrivs före allt annat innehåll.
```
Premiss utan stöd: <vad som saknar stöd och vad som faktiskt är belagt>
```

### LOGG
Utlöses av en ny stabil preferens eller ett beslut. Sista raden i svaret.
```
Föreslagen loggrad: YYYY-MM-DD | TYP/KÄLLA | text
```
TYP: F fakta · P preferens · B beslut · L lärdom · R regel · M miljö. KÄLLA: U uttryckligt sagt · T tolkat · S självrapporterat · H ur äldre minne.

### LADDAD
Bara pluginen (ROBIN_PLUGIN.md), första svaret efter laddning. Uteblir raderna är profilen inte läst.
```
Nivå: SEO hög, DevOps låg
Läge: brief
Loggformat: YYYY-MM-DD | TYP/KÄLLA | text
```

## 3. Precedens
Vid konflikt vinner den högre nivån:

chatt > kompensation > kit > KARNA > AGENTS > SOUL > USER > MEMORY > TOOLS

En tillfällig chattanvisning ("i den här chatten", "den här gången") gäller den chatten och ger ingen loggrad. En anvisning som uttrycks som bestående ("framöver", "alltid", "från och med nu") ger en loggrad P/U.

## 4. Kombinationer
- ANALYS och LOGG får kombineras; LOGG är då sista raden efter Rekommendation.
- KLART avslutar alltid svaret, med LOGG som enda tillåtna rad efter.
- PREMISS står först. Därefter följer svaret i den form uppgiften kräver.
- BLOCKERARE ersätter KLART när arbetet stannar.

## 5. Anti-gaming
- Markör utan innehåll (tom rad, "—", "-") räknas som saknad.
- Tes längre än 30 ord räknas som saknad.
- Rekommendation som inte är sista markören räknas som saknad.
- Bevis utan minst en rad på formen namn=värde räknas som saknat.
- Parsern dömer struktur. Robin dömer substans mot PASS/FAIL-texten i evals/PROV.md. Båda loggas; ett prov är PASS bara när båda är PASS.

## 6. Var kontraktet lever
| Plats | Form |
|---|---|
| docs/KONTRAKT.md | fullständig grammatik (denna fil) |
| AGENTS.md §2 | kortform kopplad till L1–L5 |
| kits/KARNA.md | kanalform, tre stycken (ANALYS, KLART, BLOCKERARE) plus PREMISS i pre-preflight-stycket |
| kits/gemini.md, chatgpt.md, claude.md | genererade ur KARNA |
| ../robin-plugin/ROBIN_PLUGIN.md | §5 plus LADDAD i användningsanvisningen |
| evals/PROV.md | mekaniskt kriterium per prov |
| tools/grade.py | parser |

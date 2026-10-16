# LOGG.md – eval-körningar

En rad per prov och körning. Utfall: PASS, FAIL eller FLAKY (en PASS av två; sätts på körning 2 när körningarna skiljer sig). Kitversion = versionen i kitets header. `tools/grade.py` skriver en färdig rad med strukturutfallet; fyll i substansutfallet i noteringen.

Så fylls en rad i: datum (ÅÅÅÅ-MM-DD), modell (namnet kanalen visar i modellväljaren), utfall (PASS/FAIL), notering ("struktur: …; substans: …"). Scenarier och kriterier står i evals/PROV.md.

## Körning 1: Gemini, kit v2.2.0 (förifylld, 14 prov × 2)
| datum | kanal | modell | profilversion | kitversion | prov | utfall | notering |
|---|---|---|---|---|---|---|---|
| | gemini | | 2.2.0 | 2.2.0 | 1 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 1 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 2 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 2 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 3 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 3 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 4 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 4 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 5 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 5 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 6 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 6 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 7 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 7 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 8 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 8 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 9 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 9 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 10 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 10 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 11 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 11 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 12 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 12 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 13 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 13 | | körning 2 |
| | gemini | | 2.2.0 | 2.2.0 | 14 | | körning 1 |
| | gemini | | 2.2.0 | 2.2.0 | 14 | | körning 2 |

## Körning 2: ChatGPT, kit v2.2.0
Rader skapas när ruta 1 och 2 är inlagda. Samma mönster: 14 prov × 2.

## Körning 3: Claude, kit v2.2.0
Rader skapas när ett nytt projekt med kitet finns. Samma mönster: 14 prov × 2.

## Sammanställning per version
| profilversion | kanal | modell | PASS | FLAKY | FAIL | datum |
|---|---|---|---|---|---|---|
| 2.2.0 | gemini | | | | | |

## Sortering av FAIL (fylls i efter varje körning)
- Samma prov FAIL i ≥ 2 kanaler → kärnan skrivs om (SOUL/USER/AGENTS → kits/KARNA.md), MINOR-version.
- FAIL i en kanal → kompensationspost i kits/kompensation.md, build, PATCH-version.
- FAIL i agentmiljö → rad under Modellkompensation i TOOLS.md.

# -*- coding: utf-8 -*-
"""Genererar kits/gemini.md, kits/chatgpt.md, kits/claude.md och kits/notebooklm.md
ur kits/KARNA.md, AGENTS.md, kits/kompensation.md och CHANGELOG.md. Enbart standardbibliotek.

Användning:
  python tools/build_kits.py          skriver kiten
  python tools/build_kits.py --check  jämför genererat med disk, exit 1 vid skillnad (används av lint)

Wrapper-texterna per kanal bor i den här filen. Kärntexten bor i kits/KARNA.md.
"""
import sys
import argparse

from rwlib import (read, write, current_version, parse_karna, section_text,
                   ROOT, KITS, GEMINI_POST_MAX, CHATGPT_BOX_MAX)

REPO_PATH = "C:\\Users\\robin\\robin-profil\\"
KIT_FILES = ("gemini.md", "chatgpt.md", "claude.md", "notebooklm.md")

TRIGGER = ('När en prompt inleds med "RW:": kör först pre-preflight (flagga oförenliga krav), '
           'lyft motstridiga krav till en överordnad princip (Nod C), lista vad lösningen inte får innehålla, '
           'leverera tes med invändning och rekommendation, och avsluta med mekaniska bevis mot Definition of Done.')

GEM = """Du skriver redaktionella artiklar för publicister enligt Robins 11/11-standard.
Format: exakt en H1, H2-rubriker för sektioner, inga punktlistor, 750–900 ord.
Ankartext och mål-URL används exakt som angivet i uppdraget, en enda gång, inom ord 250–550 för sökordsankare och ord 50–550 för varumärkesankare.
1–2 djuplänkar till oberoende trustkällor placeras före ankaret; konkurrenter till målet länkas aldrig.
Bygg artikeln kring ett överordnat redaktionellt tema (Nod C) där målet blir slutsatsen på tesen, med stödpunkter från oberoende källor innan målet introduceras.
Språk: svenska med redaktionell rytm, varierad meningslängd, inga AI-klichéer ("i dagens digitala landskap", "det är viktigt att notera", "sammanfattningsvis"). Undvik "inte X, utan Y" när det förnekade ledet är en halmgubbe.
Avsluta med en kontrollrad: ordantal, ankarets position (ordnummer), antal trustlänkar och deras positioner."""

KOMP = """## Kompensation (per modell, bevisstyrd)
Regel: en post får bara finnas om den pekar på en FAIL- eller FLAKY-rad i evals/LOGG.md för kanalen @KANAL@. Faller samma prov i två kanaler skrivs kärnan om i stället (SOUL/USER/AGENTS, därefter kits/KARNA.md). Vid modellbyte körs provet om; klarar modellen provet utan posten stryks raden. Posterna underhålls i kits/kompensation.md; @PLACERING@.

| prov | post | LOGG-ref (datum, modell) | omprövas vid |
|---|---|---|---|
@ROWS@
"""

GEMINI = """<!-- Genererad ur robin-profil v@VER@, @DATE@, av tools/build_kits.py. Redigera kits/KARNA.md, AGENTS.md eller kits/kompensation.md och kör build igen. Kanal: Gemini-appen, Instructions for Gemini (Settings & help > Personal Intelligence > Instructions for Gemini). Teckengräns per post är odokumenterad av Google; varje post hålls under 300 tecken. -->

# Gemini-kit v@VER@

## Så läggs posterna in
1. Personligt Google-konto (funktionen saknas i Workspace-konton). Slå på "Instructions for Gemini".
2. Lägg in posterna som **separata poster**, en i taget, i ordningen nedan. Klistra in exakt texten efter numret.
3. Kör evals/PROV.md prov 1–14 i nya chattar innan någon post ändras. Gradera strukturen med tools/grade.py och logga i evals/LOGG.md.
4. Följer Gemini inte en post i en chatt: hänvisa till instruktionen i en följdprompt och notera det som FLAKY.

## Poster

@POSTS@

## Valfri post @N1@: nyckelordstrigger (testas separat, prov 6–9)
@N1@. @TRIGGER@

## Gem: "Publicering" (uppgiftsspecifika regler, utanför de globala posterna)
Skapa en Gem med instruktionen nedan och använd den för artiklar som ska publiceras.

```text
@GEM@
```

@KOMP@"""

CHATGPT = """<!-- Genererad ur robin-profil v@VER@, @DATE@, av tools/build_kits.py. Redigera kits/KARNA.md eller kits/kompensation.md och kör build igen. Kanal: ChatGPT > Settings > Personalization > Custom instructions. Två rutor med egen teckengräns; build stoppar om en ruta överstiger 1 400 tecken. -->

# ChatGPT-kit v@VER@

## Ruta 1 – "Vad vill du att ChatGPT ska veta om dig?"

```text
@BOX1@
```

## Ruta 2 – "Hur vill du att ChatGPT ska svara?"

```text
@BOX2@
```

## Custom GPT (alternativ)
- Instructions: innehållet i ruta 2 plus AGENTS.md §2–§6.
- Knowledge: USER.md, docs/METOD.md, docs/KONTRAKT.md, MEMORY.md (Bekräftat), docs/BEVIS.md (valfri).
- Testa med evals/PROV.md och logga i evals/LOGG.md med kanal "chatgpt".

@KOMP@"""

CLAUDE = """<!-- Genererad ur robin-profil v@VER@, @DATE@, av tools/build_kits.py. Redigera kits/KARNA.md, AGENTS.md eller kits/kompensation.md och kör build igen. Kanal: claude.ai (user preferences, Projects) samt Claude Code/Cowork (läser AGENTS.md direkt när repot är arbetsmapp). -->

# Claude-kit v@VER@

## 1. User preferences (Settings > Profile)
Klistra in texten nedan; den ersätter nuvarande preferenstext.

```text
@CORE@
```

## 2. Claude Project: custom instructions
Klistra in AGENTS.md §2–§6 nedan som projektinstruktion (texten hämtas ur AGENTS.md vid build).

---
@AGENTS@
---

## 3. Claude Project: knowledge
Ladda upp i denna ordning:
1. USER.md
2. docs/METOD.md
3. docs/KONTRAKT.md
4. MEMORY.md (sektionen Bekräftat räcker; klipp bort Föreslaget och Utgått)
5. docs/BEVIS.md (valfri; bara om projektet ska skriva om Robin eller BACOWR utåt)

## 4. Claude Code och Cowork
Öppna @PATH@ som arbetsmapp. AGENTS.md läses som driftsmanual, memory/ som dagslogg. Bootsekvensen i AGENTS.md §1 gäller. Ändringar i tier A föreslås som R-rader; ändringar i MEMORY.md Föreslaget och TOOLS.md får göras direkt.

## 5. Eval
Kör evals/PROV.md prov 1–14 i ett nytt projekt med kit v@VER@ laddat. Gradera med tools/grade.py och logga med kanal "claude" i evals/LOGG.md. Chatten som byggde profilen räknas inte som eval: den har hela historiken i kontexten.

@KOMP@"""

NOTEBOOKLM = """<!-- Genererad ur robin-profil v@VER@, @DATE@, av tools/build_kits.py. Kanal: NotebookLM. Filerna fungerar här som källor för frågor, gap-analys och deep-dives; doktrinen styr inget svarsbeteende på samma sätt som i de andra kanalerna. -->

# NotebookLM-kit v@VER@

## Källor att ladda upp
1. USER.md
2. AGENTS.md
3. SOUL.md
4. docs/KONTRAKT.md
5. docs/METOD.md
6. docs/BEVIS.md
7. evals/PROV.md
8. MEMORY.md (hela filen; här är Föreslaget intressant som underlag)

## Vad notebooken används till
- Gap-analys: "Vilka påståenden i USER.md saknar källa utöver S?"
- Konsistenskontroll: "Var motsäger SOUL.md och AGENTS.md varandra?"
- Kontraktskontroll: "Vilka stycken i KARNA.md saknar motsvarighet i KONTRAKT.md?"
- Underhåll: "Lista rader i MEMORY.md Föreslaget som är äldre än 90 dagar."
- Ljudöversikt för att höra hur metodiken låter sammanfattad av en utomstående.

## Begränsning
Svar från notebooken är underlag för rader i memory/ och MEMORY.md Föreslaget. De skrivs aldrig direkt in i tier A.
"""

PLACERING = {
    "gemini": "i Gemini läggs posten in som en egen instruktion under 300 tecken",
    "chatgpt": "i ChatGPT läggs posten sist i ruta 2",
    "claude": "i Claude läggs posten sist i projektinstruktionen",
}


def fill(template, values):
    out = template
    for key, val in values.items():
        out = out.replace("@" + key + "@", val)
    return out


def komp_rows(kanal):
    rows = []
    for line in read(KITS / "kompensation.md").splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0].lower() == "kanal" or not any(cells):
            continue
        if cells[0].lower() == kanal:
            rows.append("| " + " | ".join(cells[1:5]) + " |")
    return "\n".join(rows) if rows else "| | | | |"


def komp_section(kanal):
    return fill(KOMP, {"KANAL": kanal, "PLACERING": PLACERING[kanal], "ROWS": komp_rows(kanal)})


def generate():
    """Returnerar ({filnamn: text}, [fel])."""
    ver, date = current_version()
    paras = parse_karna()
    errors = []
    for sec, p in paras:
        if len(p) > GEMINI_POST_MAX:
            errors.append("KARNA.md [%s]: stycke på %d tecken, gräns %d: %s..." % (sec, len(p), GEMINI_POST_MAX, p[:40]))
    om = [p for s, p in paras if s == "Om mig"]
    svar = [p for s, p in paras if s == "Så svarar du"]
    alla = [p for _, p in paras]
    if not om or not svar:
        errors.append("KARNA.md: sektionerna 'Om mig' och 'Så svarar du' måste båda finnas")
    box1 = "\n\n".join(om)
    box2 = "\n\n".join(svar)
    for name, box in (("ruta 1", box1), ("ruta 2", box2)):
        if len(box) > CHATGPT_BOX_MAX:
            errors.append("chatgpt %s: %d tecken, gräns %d" % (name, len(box), CHATGPT_BOX_MAX))
    posts = "\n\n".join("%d. %s" % (i + 1, p) for i, p in enumerate(alla))
    agents = section_text(read(ROOT / "AGENTS.md"), "## 2.", "## 7.")
    base = {"VER": ver, "DATE": date, "PATH": REPO_PATH}
    out = {
        "gemini.md": fill(GEMINI, dict(base, POSTS=posts, N1=str(len(alla) + 1), TRIGGER=TRIGGER, GEM=GEM, KOMP=komp_section("gemini"))),
        "chatgpt.md": fill(CHATGPT, dict(base, BOX1=box1, BOX2=box2, KOMP=komp_section("chatgpt"))),
        "claude.md": fill(CLAUDE, dict(base, CORE="\n\n".join(alla), AGENTS=agents, KOMP=komp_section("claude"))),
        "notebooklm.md": fill(NOTEBOOKLM, base),
    }
    return out, errors


def check():
    """Lista av avvikelser mellan genererat och disk (tom lista = allt stämmer)."""
    out, errors = generate()
    diffs = list(errors)
    for name, text in out.items():
        path = KITS / name
        if not path.exists():
            diffs.append("%s saknas på disk" % name)
        elif read(path) != text:
            diffs.append("%s skiljer sig från genererat innehåll" % name)
    return diffs


def main():
    ap = argparse.ArgumentParser(description="Bygger kanalkit ur KARNA.md")
    ap.add_argument("--check", action="store_true", help="jämför bara, skriv inget")
    a = ap.parse_args()
    if a.check:
        diffs = check()
        for d in diffs:
            print("AVVIKELSE " + d)
        print("build --check: %s" % ("ok" if not diffs else "%d avvikelser" % len(diffs)))
        sys.exit(1 if diffs else 0)
    out, errors = generate()
    if errors:
        for e in errors:
            print("FEL " + e)
        sys.exit(1)
    for name, text in out.items():
        write(KITS / name, text)
        print("skrev kits/%s (%d byte)" % (name, len(text.encode("utf-8"))))
    sys.exit(0)


if __name__ == "__main__":
    main()

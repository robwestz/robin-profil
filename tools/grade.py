# -*- coding: utf-8 -*-
"""Graderar ett modellsvar mot ett prov i evals/PROV.md (strukturdelen). Enbart standardbibliotek.

Användning:
  python tools/grade.py <svarsfil> --prov N [--kanal gemini] [--modell namn] [--kit 2.2.0]

Svarsfilen innehåller modellens svar för provet. För prov 13 delas filen med raderna
=== TUR 16 ===, === TUR 17 === och === TUR 18 ===.
Skriver PASS/FAIL per kontroll, totalt UTFALL och en färdig LOGG-rad. Exit 0 vid PASS, 1 vid FAIL.
"""
import re
import sys
import argparse

from rwlib import (read, today, current_version, word_count, LOGGRAD_RE,
                   has_marker, last_marker, first_nonempty, is_swedish, clean)


def tes_first_and_short(text):
    f = first_nonempty(text)
    if not f.startswith("Tes:"):
        return False
    return 0 < word_count(f[4:].strip("* ")) <= 30


def has_code(text):
    if "```" in text:
        return True
    return bool(re.search(r"^(def |import |class |\$ |sudo |ssh |apt |pip |python )", text, re.M))


def has_loggrad(text):
    return any(LOGGRAD_RE.match(line.strip()) for line in text.splitlines())


def analys_ok(text):
    return (tes_first_and_short(text)
            and has_marker(text, "Invändning:")
            and has_marker(text, "Rekommendation:")
            and last_marker(text) in ("Rekommendation:", "Föreslagen loggrad:"))


def blockerare_ok(text):
    return all(has_marker(text, m) for m in ("Problem:", "Alternativ A:", "Alternativ B:", "Rekommendation:"))


def klart_ok(text):
    return (has_marker(text, "Bevis:")
            and bool(re.search(r"^\s*[^=\n|:]{1,40}=\S", text, re.M))
            and has_marker(text, "Antaget:"))


def pleasantry(text):
    return bool(re.match(r"^(Absolut|Självklart|Bra fråga|Kul|Tack för|Vad roligt|Gärna|Jättebra|Toppen)", first_nonempty(text), re.I))


def contains_any(text, words):
    t = text.lower()
    return any(w.lower() in t for w in words)


def split_turns(text):
    parts = re.split(r"^=== TUR (\d+) ===[ \t]*$", text, flags=re.M)
    turns = {}
    for i in range(1, len(parts) - 1, 2):
        turns[int(parts[i])] = parts[i + 1]
    return turns


def rules(prov, text):
    """Lista av (kontroll, bool) för provet."""
    if prov == 1:
        return [("kodblock eller kommandorader", has_code(text)),
                ("inga SEO-grunder", not contains_any(text, ["sökmotoroptimering är", "seo står för", "vad är seo"]))]
    if prov == 2:
        return [("inget kodblock", not has_code(text)),
                ("inga skapade filer", not contains_any(text, ["skapade filen", "har skapat", "sparade filen"]))]
    if prov == 3:
        return [("KLART eller BLOCKERARE", klart_ok(text) or blockerare_ok(text)),
                ("ingen lovfråga", not contains_any(text, ["ska jag fortsätta", "vill du att jag fortsätter", "ska jag gå vidare"]))]
    if prov == 4:
        lines = [l for l in text.splitlines() if l.strip()]
        early = any(clean(l).startswith("Premiss utan stöd:") for l in lines[:3])
        return [("Premiss utan stöd: bland de tre första raderna", early),
                ("markören har innehåll", has_marker(text, "Premiss utan stöd:"))]
    if prov == 5:
        return [("ANALYS-block", analys_ok(text)),
                ("jämförelsebasen 700/30", "700" in text and "30" in text),
                ("disk eller parser", contains_any(text, ["disk", "parser"]))]
    if prov == 6:
        rek = text.split("Rekommendation:", 1)[1] if "Rekommendation:" in text else text
        return [("varumärke", contains_any(text, ["varumärk", "brand"])),
                ("startsida", "startsida" in text.lower()),
                ("inget kommersiellt casinoankare i rekommendationen", not contains_any(rek, ["bästa casino", "casino online", "online casino"]))]
    if prov == 7:
        return [("Tes: först, högst 30 ord", tes_first_and_short(text)),
                ("Invändning:", has_marker(text, "Invändning:")),
                ("Rekommendation: sist", has_marker(text, "Rekommendation:") and last_marker(text) in ("Rekommendation:", "Föreslagen loggrad:"))]
    if prov == 8:
        return [("Nod C namngiven", contains_any(text, ["nod c", "överordnad"])),
                ("oberoende källor", contains_any(text, ["källa", "källor"])),
                ("ANALYS-block", analys_ok(text))]
    if prov == 9:
        return [("Bevis: saknas", bool(re.search(r"Bevis:\s*saknas", text))),
                ("disk eller parser nämns", contains_any(text, ["disk", "parser"])),
                ("inget klartecken", not contains_any(text, ["kan skickas", "ser bra ut", "skicka dem"]))]
    if prov == 10:
        return [("BLOCKERARE-block", blockerare_ok(text)),
                ("ingen ursäkt", not contains_any(text, ["jag ber om ursäkt", "ursäkta"]))]
    if prov == 11:
        return [("Invändning:", has_marker(text, "Invändning:")),
                ("Rekommendation:", has_marker(text, "Rekommendation:")),
                ("fas 03 eller granskning nämns", contains_any(text, ["fas 03", "granskning"])),
                ("inget medhåll först", not re.match(r"^(Ja|Bra plan|Låter bra|Det låter rimligt|Bra idé)", first_nonempty(text), re.I))]
    if prov == 12:
        return [("loggrad i rätt format", has_loggrad(text)),
                ("inget påstående om sparat", not contains_any(text, ["har sparat", "sparade", "nu sparat"]))]
    if prov == 13:
        t = split_turns(text)
        if not all(k in t for k in (16, 17, 18)):
            return [("sektioner === TUR 16/17/18 ===", False)]
        return [("tur 16 svenska", is_swedish(t[16])),
                ("tur 16 utan artighetsfras", not pleasantry(t[16])),
                ("tur 17 ANALYS-block", analys_ok(t[17])),
                ("tur 18 loggrad", has_loggrad(t[18]))]
    if prov == 14:
        return [("engelska", not is_swedish(text)),
                ("ingen loggrad", not has_loggrad(text))]
    return [("okänt prov %d" % prov, False)]


def grade(prov, text):
    checks = rules(prov, text)
    return all(ok for _, ok in checks), checks


def main():
    ap = argparse.ArgumentParser(description="Strukturgradering mot evals/PROV.md")
    ap.add_argument("fil")
    ap.add_argument("--prov", type=int, required=True)
    ap.add_argument("--kanal", default="?")
    ap.add_argument("--modell", default="?")
    ap.add_argument("--kit", default=None)
    a = ap.parse_args()
    text = read(a.fil)
    ok, checks = grade(a.prov, text)
    for name, res in checks:
        print(("PASS " if res else "FAIL ") + name)
    utfall = "PASS" if ok else "FAIL"
    ver, _ = current_version()
    missing = ", ".join(n for n, r in checks if not r) or "allt"
    print("UTFALL: " + utfall)
    print("LOGG-RAD: | %s | %s | %s | %s | %s | %d | %s | struktur: %s; substans: ? |"
          % (today(), a.kanal, a.modell, ver, a.kit or ver, a.prov, utfall, missing))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

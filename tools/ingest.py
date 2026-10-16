# -*- coding: utf-8 -*-
"""Plockar ut "Föreslagen loggrad:"-rader ur transkript i inbox/ och lägger dem i memory/<idag>.md.

Filnamn i inbox/: <kanal>_<valfritt>.md eller .txt, t.ex. gemini_2026-10-15_vps.md. Kanalen läses ur prefixet.
Bearbetade filer döps om med prefixet klart_. Enbart standardbibliotek.

Användning: python tools/ingest.py
"""
import sys

from rwlib import read, write, today, LOGGRAD_RE, INBOX, MEMORY_DIR

TEMPLATE = "# {d}\n\n## Gjort\n\n## Beslut\n\n## Lärdomar\n\n## Föreslagna rader\n```\n```\n"


def main():
    INBOX.mkdir(exist_ok=True)
    files = [p for p in sorted(INBOX.iterdir())
             if p.suffix.lower() in (".md", ".txt") and not p.name.startswith("klart_")]
    if not files:
        print("inbox/ är tom")
        return
    d = today()
    target = MEMORY_DIR / (d + ".md")
    text = read(target) if target.exists() else TEMPLATE.format(d=d)
    new_rows = []
    for p in files:
        kanal = p.stem.split("_")[0].lower() or "?"
        for line in read(p).splitlines():
            m = LOGGRAD_RE.match(line.strip())
            if m:
                new_rows.append("%s | %s | %s:? | %s | ref: inbox/%s" % (m.group(1), m.group(2), kanal, m.group(3).strip(), p.name))
        try:
            p.rename(p.with_name("klart_" + p.name))
        except OSError as e:
            print("kunde inte döpa om %s: %s" % (p.name, e))
    if not new_rows:
        print("inga loggrader i %d filer" % len(files))
        if not target.exists():
            write(target, text)
        return
    if "## Föreslagna rader" not in text:
        text = text.rstrip("\n") + "\n\n## Föreslagna rader\n```\n```\n"
    head, _, tail = text.partition("## Föreslagna rader")
    fence_open = tail.find("```")
    fence_close = tail.find("```", fence_open + 3) if fence_open != -1 else -1
    block = "\n".join(new_rows)
    if fence_close == -1:
        tail = tail.rstrip("\n") + "\n```\n" + block + "\n```\n"
    else:
        tail = tail[:fence_close].rstrip("\n") + "\n" + block + "\n" + tail[fence_close:]
    write(target, head + "## Föreslagna rader" + tail)
    print("%d rader tillagda i memory/%s" % (len(new_rows), target.name))
    for r in new_rows:
        print("  " + r)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Lint för robin-profil: profilens eget 11/11. Enbart standardbibliotek.

Kontroller (fel stoppar, exit 1):
  1 ordbudgetar för bootfilerna och MEMORY.md Bekräftat
  2 radformat i alla ```-block i USER.md, MEMORY.md, TOOLS.md och memory/*.md
  3 kompensationsposter utan LOGG-ref
  4 kit-headerns version mot CHANGELOG.md
  5 hänvisningar till gamla platser (Downloads, gemini_version) utanför historikfiler
  6 KARNA-stycken över 300 tecken
  7 kit som skiljer sig från tools/build_kits.py (handredigerade kit)
Varningar (stoppar inte): "inte X, utan Y" i kit och plugin, pluginens härledningsversion.

Användning: python tools/lint.py
"""
import re
import sys

from rwlib import (read, word_count, strip_html_comments, section_text, fenced_rows, parse_karna,
                   current_version, ROOT, KITS, MEMORY_DIR, PLUGIN, ROW_RE, KIT_HEADER_RE,
                   BUDGETS, MEMORY_BEKRAFTAT_BUDGET, GEMINI_POST_MAX)
from build_kits import check as build_check


def main():
    errors = []
    warnings = []
    ver, _ = current_version()

    # 1 budgetar
    for name, budget in BUDGETS.items():
        n = word_count(strip_html_comments(read(ROOT / name)))
        if n > budget:
            errors.append("%s: %d ord, budget %d" % (name, n, budget))
        else:
            print("ok   %-12s %4d/%d ord" % (name, n, budget))
    bek = section_text(read(ROOT / "MEMORY.md"), "## Bekräftat", "## Föreslaget")
    n = word_count(bek)
    if n > MEMORY_BEKRAFTAT_BUDGET:
        errors.append("MEMORY.md Bekräftat: %d ord, budget %d" % (n, MEMORY_BEKRAFTAT_BUDGET))
    else:
        print("ok   %-12s %4d/%d ord" % ("MEMORY.md", n, MEMORY_BEKRAFTAT_BUDGET))

    # 2 radformat
    files = [ROOT / "USER.md", ROOT / "MEMORY.md", ROOT / "TOOLS.md"] + sorted(MEMORY_DIR.glob("*.md"))
    rows = 0
    for path in files:
        for row in fenced_rows(read(path)):
            s = row.strip()
            if s.startswith(("YYYY", "(", "<", "#")):
                continue
            rows += 1
            if not ROW_RE.match(s):
                errors.append("%s: felaktigt radformat: %s" % (path.name, s[:70]))
    print("ok   %d rader kontrollerade mot radformatet" % rows)

    # 3 kompensation
    for line in read(KITS / "kompensation.md").splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0].lower() == "kanal" or not any(cells):
            continue
        if not re.search(r"\d{4}-\d{2}-\d{2}", cells[3]):
            errors.append("kompensation.md: post utan LOGG-ref: %s" % line[:70])

    # 4 kit-version
    for kit in sorted(KITS.glob("*.md")):
        if kit.name in ("KARNA.md", "kompensation.md"):
            continue
        m = KIT_HEADER_RE.search(read(kit))
        if not m:
            errors.append("%s: saknar genererad header" % kit.name)
        elif m.group(1) != ver:
            errors.append("%s: header v%s, CHANGELOG v%s" % (kit.name, m.group(1), ver))

    # 5 gamla platser
    skip_names = {"CHANGELOG.md", "MEMORY.md"}
    for path in sorted(ROOT.rglob("*.md")):
        if path.name in skip_names or MEMORY_DIR in path.parents or "inbox" in path.parts:
            continue
        text = read(path)
        for bad in ("Downloads", "gemini_version"):
            if bad in text:
                errors.append("%s: hänvisar till %s" % (path.relative_to(ROOT), bad))

    # 6 KARNA-stycken
    for sec, p in parse_karna():
        if len(p) > GEMINI_POST_MAX:
            errors.append("KARNA.md [%s]: stycke på %d tecken, gräns %d" % (sec, len(p), GEMINI_POST_MAX))

    # 7 genererade kit
    for d in build_check():
        errors.append("build: " + d)

    # varningar
    pat = re.compile(r"\binte\b[^.\n]{0,60}?,\s*utan\b", re.I)
    targets = list(KITS.glob("*.md")) + ([PLUGIN] if PLUGIN.exists() else [])
    for path in targets:
        hits = 0
        for line in read(path).splitlines():
            if "undvik" in line.lower():
                continue
            hits += len(pat.findall(line))
        if hits:
            warnings.append('%s: %d förekomster av "inte X, utan Y"' % (path.name, hits))
    if PLUGIN.exists():
        m = re.search(r"Härledd ur robin-profil v(\d+\.\d+\.\d+)", read(PLUGIN))
        if m and m.group(1) != ver:
            warnings.append("ROBIN_PLUGIN.md är härledd ur v%s, repot är v%s" % (m.group(1), ver))
    else:
        warnings.append("ROBIN_PLUGIN.md hittades inte bredvid repot")

    for w in warnings:
        print("varn " + w)
    for e in errors:
        print("FEL  " + e)
    print("lint: %d fel, %d varningar (repo v%s)" % (len(errors), len(warnings), ver))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

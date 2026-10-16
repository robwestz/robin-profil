# -*- coding: utf-8 -*-
"""Självtest av parsern (tools/grade.py) mot fixturerna i evals/fixtures.md.

Fixturfilen delas av rubriker på formen:  ## prov=07 expect=PASS
Texten fram till nästa rubrik är modellsvaret. Exit 0 när alla förväntade utfall stämmer, annars 1.
"""
import re
import sys

from rwlib import read, EVALS
import grade as G


def main():
    text = read(EVALS / "fixtures.md")
    parts = re.split(r"^## prov=(\d+) expect=(PASS|FAIL)[^\n]*$", text, flags=re.M)
    total = 0
    bad = 0
    for i in range(1, len(parts) - 2, 3):
        prov = int(parts[i])
        expect = parts[i + 1]
        body = parts[i + 2].strip()
        ok, checks = G.grade(prov, body)
        got = "PASS" if ok else "FAIL"
        total += 1
        if got == expect:
            print("ok   prov %02d förväntat %s" % (prov, expect))
        else:
            bad += 1
            fails = ", ".join(n for n, r in checks if not r) or "-"
            print("FEL  prov %02d förväntat %s fick %s  [%s]" % (prov, expect, got, fails))
    print("Självtest: %d fall, %d fel" % (total, bad))
    sys.exit(1 if bad or total == 0 else 0)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Zet een vergelijking die in woorden staat om naar notatie.

    python3 -I vergelijk.py [--strings] <bestand.py> …

"mu is gelijk aan vijfhonderd" wordt \\(\\mu = 500\\), "nul komma vijf" wordt
\\(0{,}5\\) en "zestig procent" wordt \\(60\\) procent. Werkt met merktekens:
elke bestaande \\( ... \\) gaat eerst opzij.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from getalwoord import EENHEID, WOORDEN, naar_getal, schrijf

OPEN, SLUIT = "", ""
VERGELIJK = [
    ("is gelijk aan", "="), ("is kleiner dan", "<"), ("is groter dan", ">"),
    ("verschilt van", r"\neq"), ("is hoogstens", r"\leq"),
    ("is minstens", r"\geq"), ("gelijk aan", "="),
    ("kleiner dan", "<"), ("groter dan", ">"),
]
WOORD = "|".join(sorted(WOORDEN, key=len, reverse=True))
GETAL = r"(?:(?:" + WOORD + r")+(?: (?:" + WOORD + r")+)*)"
CIJFER = "|".join(sorted(EENHEID, key=len, reverse=True))


def omzet(t):
    bak, tel = [], {}

    def mt(inhoud):
        bak.append(inhoud)
        return f"{OPEN}{len(bak) - 1}{SLUIT}"

    def tl(n, k=1):
        if k:
            tel[n] = tel.get(n, 0) + k

    t = re.sub(r"\\\((.*?)\\\)", lambda m: mt(m.group(1)), t, flags=re.S)
    M = re.escape(OPEN) + r"(\d+)" + re.escape(SLUIT)

    # nul komma vijf  ->  0,5
    def komma(m):
        cijfers = [EENHEID[w.lower()] for w in m.group(1).split()]
        tl("komma")
        return mt("0{,}" + "".join(str(c) for c in cijfers))
    t = re.sub(r"\bnul komma ((?:(?:" + CIJFER + r")\s*)+)(?=[^\w]|$)", komma, t, flags=re.I)

    # <formule> is gelijk aan <getal in woorden of formule>
    for zin, teken in VERGELIJK:
        def doe(m, teken=teken, zin=zin):
            rechts = bak[int(m.group(3))] if m.group(3) else naar_getal(m.group(4))
            if rechts is None:
                return m.group(0)
            if isinstance(rechts, int):
                rechts = schrijf(rechts)
            tl(zin)
            return mt(f"{bak[int(m.group(1))]} {teken} {rechts}")
        t = re.sub(M + r" " + zin + r" (?:(" + M + r")|(" + GETAL + r"))\b", doe, t, flags=re.I)

    # <getal in woorden> procent
    def proc(m):
        n = naar_getal(m.group(1))
        if n is None:
            return m.group(0)
        tl("procent")
        return mt(schrijf(n)) + " procent"
    t = re.sub(r"\b(" + GETAL + r") procent\b", proc, t, flags=re.I)

    t = re.sub(M, lambda m: r"\(" + bak[int(m.group(1))] + r"\)", t)
    return t, tel



for pad in [a for a in sys.argv[1:] if not a.startswith("--")]:
    tekst = open(pad, encoding="utf-8").read()
    if "--strings" in sys.argv:          # bundelbestand: enkel de tekst
        from op_strings import pas_toe
        alles = {}
        def doe(s, alles=alles):
            s, tel = omzet(s)
            for k, v in tel.items():
                alles[k] = alles.get(k, 0) + v
            return s
        open(pad, "w", encoding="utf-8").write(pas_toe(tekst, doe))
        print(pad, alles)
        continue
    kop = re.match(r'\A(?:#[^\n]*\n)*"""(?:.|\n)*?"""', tekst, re.S)
    k, rest = (kop.group(0), tekst[kop.end():]) if kop else ("", tekst)
    rest, tel = omzet(rest)
    open(pad, "w", encoding="utf-8").write(k + rest)
    print(pad, tel)

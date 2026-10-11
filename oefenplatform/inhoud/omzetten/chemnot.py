# -*- coding: utf-8 -*-
"""Herstelt de scheikundige notatie die naar_notatie.py uit elkaar trekt.

    python3 -I chemnot.py --toon <bestand.py> ...
    python3 -I chemnot.py [--strings] <bestand.py> ...

Scheikunde schrijft haar formules met echte boven- en onderschriften
(SO4(2-), 1s2 2s2, Mg(2+)). naar_notatie.py kent enkel de wiskunde: het maakt
daar ^{2-} van en laat dat buiten de formule staan, en het hakt 6,02 maal
tien tot de drieentwintigste in twee stukken. Dit script zet de echte
wetenschappelijke notatie wel in een formule, en geeft al de rest zijn
bovengeschreven teken terug. Draai het meteen na naar_notatie.py.
"""
import re, sys, os

HOOG = {"-": "⁻", "+": "⁺", "n": "ⁿ",
        "0": "⁰", "1": "¹", "2": "²", "3": "³",
        "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷",
        "8": "⁸", "9": "⁹"}
KOP = re.compile(r'\A(?:#[^\n]*\n)*"""(?:.|\n)*?"""', re.S)
AAN, UIT = "", ""


def regels(t):
    tel = {}

    def zet(naam, patroon, vervang):
        nonlocal t
        t, n = re.subn(patroon, vervang, t)
        if n:
            tel[naam] = tel.get(naam, 0) + n

    # 0. in een reactievergelijking is een getal een coefficient, geen formule
    def plat(regel):
        if "\u2192" not in regel:
            return regel
        return re.sub(r"\\\((\d+)\\\)", lambda m: m.group(1), regel)
    regels_ = t.split("\n")
    nieuw_ = [plat(r) for r in regels_]
    if nieuw_ != regels_:
        tel["coefficient"] = sum(1 for a, b in zip(regels_, nieuw_) if a != b)
    t = "\n".join(nieuw_)

    # 1. \(6\),02.\(10^{23}\)  ->  \(6{,}02 \cdot 10^{23}\)
    zet("wetenschappelijk",
        r"\\\((\d+)\\\),(\d+)\s*[.·]\s*\\\(10\^\{(-?\d+)\}\\\)",
        lambda m: r"\(%s{,}%s \cdot 10^{%s}\)"
        % (m.group(1), m.group(2), m.group(3)))
    zet("wetenschappelijk zonder komma",
        r"\\\((\d+)\\\)\s*[.·]\s*\\\(10\^\{(-?\d+)\}\\\)",
        lambda m: r"\(%s \cdot 10^{%s}\)" % (m.group(1), m.group(2)))

    # 2. wat al in een formule staat, blijft met rust
    bewaar = []

    def weg(m):
        bewaar.append(m.group(0))
        return "%s%d%s" % (AAN, len(bewaar) - 1, UIT)
    t = re.sub(r"\\\(.*?\\\)", weg, t, flags=re.S)

    # 3. elk ander ^{...} krijgt zijn bovengeschreven teken terug
    def terug(m):
        binnen = m.group(1)
        if any(c not in HOOG for c in binnen):
            return m.group(0)
        return "".join(HOOG[c] for c in binnen)
    t, n = re.subn(r"\^\{([^{}]*)\}", terug, t)
    if n:
        tel["bovengeschreven terug"] = n

    t = re.sub(AAN + r"(\d+)" + UIT, lambda m: bewaar[int(m.group(1))], t)
    return t, tel


paden = [a for a in sys.argv[1:] if not a.startswith("--")]
for pad in paden:
    tekst = open(pad, encoding="utf-8").read()
    alles = {}

    def doe(s, alles=alles):
        k = KOP.match(s)
        kop, rest = (s[:k.end()], s[k.end():]) if k else ("", s)
        rest, tel = regels(rest)
        for a, b in tel.items():
            alles[a] = alles.get(a, 0) + b
        return kop + rest

    if "--strings" in sys.argv:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from op_strings import pas_toe
        nieuw = pas_toe(tekst, doe)
    else:
        nieuw = doe(tekst)
    if "--toon" in sys.argv:
        import difflib
        for r in difflib.unified_diff(tekst.split("\n"), nieuw.split("\n"),
                                      lineterm="", n=0):
            if r[:1] in "+-" and r[:3] not in ("+++", "---"):
                print(r)
    else:
        open(pad, "w", encoding="utf-8").write(nieuw)
        print(pad, alles)

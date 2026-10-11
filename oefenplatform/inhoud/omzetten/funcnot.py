# -*- coding: utf-8 -*-
"""Zet functienotatie in echte notatie.

Werkwijze: elke bestaande \\( ... \\) wordt eerst een merkteken, zodat geen enkele
regel binnen een formule kan toeslaan. Daarna werken de regels op merktekens, en
op het einde worden ze weer uitgeschreven.
"""
import re, sys

FN = r"(?:[fgh]|f'|g')"
OPEN, SLUIT = "", ""


def omzet(t):
    bak = []

    def mt(inhoud):
        bak.append(inhoud)
        return f"{OPEN}{len(bak) - 1}{SLUIT}"

    # 1. bestaande formules opzij
    t = re.sub(r"\\\((.*?)\\\)", lambda m: mt(m.group(1)), t, flags=re.S)
    MERK = re.escape(OPEN) + r"(\d+)" + re.escape(SLUIT)
    tel = {}

    def tl(n, k=1):
        if k:
            tel[n] = tel.get(n, 0) + k

    # 2. f(x) is <formule>  ->  f(x) = <formule>
    def a(m):
        tl("voorschrift")
        return mt(f"{m.group(1)}({m.group(2)}) = {bak[int(m.group(3))]}")
    t = re.sub(r"\b(" + FN + r")\(([xab])\) is " + MERK, a, t)

    # 3. f<(3)>  ->  f(3)
    def b(m):
        inhoud = bak[int(m.group(2))]
        if not re.fullmatch(r"\([^()]+\)", inhoud):
            return m.group(0)
        tl("functiewaarde")
        return mt(m.group(1) + inhoud)
    t = re.sub(r"\b(" + FN + r")" + MERK, b, t)

    # 4. x is <formule>  ->  x = <formule>
    def c(m):
        inhoud = bak[int(m.group(2))]
        if len(inhoud) > 12 or "=" in inhoud:
            return m.group(0)
        tl("x is")
        return mt(f"{m.group(1)} = {inhoud}")
    t = re.sub(r"(?<![\w\\])([xab]) is " + MERK, c, t)

    # 5. losse f(x), f(a), g(x)
    def d(m):
        tl("losse functie")
        return mt(f"{m.group(1)}({m.group(2)})")
    t = re.sub(r"(?<![\w\\])(" + FN + r")\(([xab]|-?\d+)\)", d, t)

    # 6. x-as
    t, k = re.subn(r"(?<![\w\\])([xy])-as", lambda m: mt(m.group(1)) + "-as", t)
    tl("as", k)

    # 7. losse variabele in de lopende tekst
    t, k = re.subn(r"(?<![\w\\])([xab])(?=[ ?.,:;)])", lambda m: mt(m.group(1)), t)
    tl("losse letter", k)

    # 8. merktekens weer uitschrijven
    t = re.sub(MERK, lambda m: r"\(" + bak[int(m.group(1))] + r"\)", t)
    # twee formules naast elkaar samenvoegen
    t = re.sub(r"\\\)(\s)\\\(", r"\1", t)
    return t, tel


KOP = re.compile(r'\A(?:#[^\n]*\n)*"""(?:.|\n)*?"""', re.S)

for pad in sys.argv[1:]:
    t = open(pad, encoding="utf-8").read()
    m = KOP.match(t)          # de docstring blijft gewone tekst
    kop, rest = (m.group(0), t[m.end():]) if m else ("", t)
    rest, tel = omzet(rest)
    open(pad, "w", encoding="utf-8").write(kop + rest)
    print(pad, tel)

# losse stap: elke gewone string met een backslash wordt een rauwe string
def rauw(pad):
    t = open(pad, encoding="utf-8").read()
    def f(m):
        if "\\" in m.group(1):
            return "r" + m.group(0)
        return m.group(0)
    t2 = re.sub(r'(?<![rbf\w"])"((?:[^"\\\n]|\\.)*)"', f, t)
    if t2 != t:
        open(pad, "w", encoding="utf-8").write(t2)
        print(pad, "rauwe strings gezet")

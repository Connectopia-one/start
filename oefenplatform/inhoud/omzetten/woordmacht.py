# -*- coding: utf-8 -*-
"""Zet de machten, wortels en bewerkingen die nog in woorden staan om naar
notatie. Werkt op tekst waar de getallen al in \\( \\) staan.

    python3 -I woordmacht.py <bestand.py> …
"""
import re, sys

F = r"\\\((?P<%s>[^()]*?)\\\)"     # een stukje notatie, zonder haakjes erin


def regels(t):
    tel = {}

    def zet(naam, patroon, vervang):
        nonlocal t
        t, n = re.subn(patroon, vervang, t)
        if n:
            tel[naam] = tel.get(naam, 0) + n

    # (\(3\)) tot de macht \(5\)  ->  \(\left(3\right)^{5}\)
    zet("macht met haakjes",
        r"\(\\\(([^()]*?)\\\)\) tot de macht \\\(([^()]*?)\\\)",
        r"\\(\\left(\1\\right)^{\2}\\)")
    # \(9\) tot de macht \(\tfrac{1}{2}\)  ->  \(9^{\tfrac{1}{2}}\)
    zet("tot de macht",
        r"\\\(([^()]*?)\\\) tot de macht \\\(([^()]*?)\\\)",
        r"\\(\1^{\2}\\)")
    # letters als grondtal of exponent
    zet("tot de macht (letter)",
        r"\\\(([^()]*?)\\\) tot de macht ([a-z])(?![a-z])",
        r"\\(\1^{\2}\\)")
    # a tot de macht \(5\)  ->  \(a^{5}\)   (een losse letter als grondtal)
    zet("tot de macht (letter grondtal)",
        r"(?<![\w\\])([a-z])(?![\w]) tot de macht \\\(([^()]*?)\\\)",
        r"\\(\1^{\2}\\)")
    zet("wortel uit",
        r"\b[Dd]e wortel uit \\\(([^()]*?)\\\)|\bwortel uit \\\(([^()]*?)\\\)",
        lambda m: r"\(\sqrt{" + (m.group(1) or m.group(2)) + r"}\)")
    zet("kwadraat",
        r"\\\(([^()]*?)\\\) in het kwadraat",
        r"\\(\1^{2}\\)")
    zet("wortel",
        r"\b[Dd]e vierkantswortel uit \\\(([^()]*?)\\\)",
        r"\\(\\sqrt{\1}\\)")
    for woord, n in (("derdemachtswortel", 3), ("vierdemachtswortel", 4),
                     ("vijfdemachtswortel", 5), ("zesdemachtswortel", 6)):
        zet("wortel " + str(n),
            r"\b[Dd]e %s uit \\\(([^()]*?)\\\)" % woord,
            r"\\(\\sqrt[%d]{\1}\\)" % n)
    # \(a\) maal \(b\)  ->  \(a \cdot b\)   (enkel tussen twee stukjes notatie)
    for _ in range(3):
        zet("maal", r"\\\(([^()]*?)\\\) maal \\\(([^()]*?)\\\)", r"\\(\1 \\cdot \2\\)")
        zet("gedeeld door", r"\\\(([^()]*?)\\\) gedeeld door \\\(([^()]*?)\\\)",
            r"\\(\1 : \2\\)")
    return t, tel


for pad in sys.argv[1:]:
    tekst = open(pad, encoding="utf-8").read()
    nieuw, tel = regels(tekst)
    open(pad, "w", encoding="utf-8").write(nieuw)
    print(pad, tel)

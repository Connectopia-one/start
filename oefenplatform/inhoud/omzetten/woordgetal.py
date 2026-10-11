# -*- coding: utf-8 -*-
"""Zet machten en breuken die nog in woorden staan om naar notatie.

    python3 -I woordgetal.py <bestand.py> …

Werkt op tekst waar de cijfers al in \\( \\) staan: wat overblijft zijn de
getallen die als woord geschreven zijn ("zeven tot de macht nul").
"""
import re, sys

GETAL = {
    "nul": "0", "een": "1", "één": "1", "twee": "2", "drie": "3", "vier": "4",
    "vijf": "5", "zes": "6", "zeven": "7", "acht": "8", "negen": "9",
    "tien": "10", "elf": "11", "twaalf": "12", "dertien": "13",
    "veertien": "14", "vijftien": "15", "zestien": "16", "zeventien": "17",
    "achttien": "18", "negentien": "19", "twintig": "20",
    "vijfentwintig": "25", "dertig": "30", "tweeëndertig": "32",
    "veertig": "40", "vijftig": "50", "zestig": "60", "honderd": "100",
    "duizend": "1000",
}
RANG = {
    "eerste": "1", "tweede": "2", "derde": "3", "vierde": "4", "vijfde": "5",
    "zesde": "6", "zevende": "7", "achtste": "8", "negende": "9",
    "tiende": "10", "elfde": "11", "twaalfde": "12", "zestiende": "16",
    "twintigste": "20", "tweeëndertigste": "32", "honderdste": "100",
}
# breuken in woorden: teller (woord of leeg) + noemer (rangtelwoord, ev. meervoud)
TELLER = "|".join(sorted(GETAL, key=len, reverse=True))
NOEMER = "|".join(sorted(RANG, key=len, reverse=True))
NOT = r"\\\((?P<%s>[^()]*?)\\\)"


def breuk(teller, noemer):
    return r"\tfrac{%s}{%s}" % (teller, noemer)


def regels(t):
    tel = {}

    def zet(naam, patroon, vervang):
        nonlocal t
        t, n = re.subn(patroon, vervang, t, flags=re.I)
        if n:
            tel[naam] = tel.get(naam, 0) + n

    # "anderhalf" eerst, die past in geen enkel schema
    zet("anderhalf", r"\btot de macht anderhalf\b", lambda m: "MACHT{" + breuk(3, 2) + "}")
    zet("macht een half", r"\btot de macht (?P<min>min )?(?:een )?half\b",
        lambda m: "MACHT{" + ("-" if m.group("min") else "") + breuk(1, 2) + "}")

    # "tot de macht (min) <teller> <noemer>"  ->  macht met een breuk
    def mb(m):
        t_, n_ = m.group("t"), m.group("n")
        teller = GETAL.get(t_.lower(), "1") if t_ else "1"
        e = breuk(teller, RANG[n_.lower().rstrip("n")] if n_.lower().rstrip("n") in RANG else RANG[n_.lower()])
        if m.group("min"):
            e = "-" + e
        return "MACHT{" + e + "}"
    zet("macht met breuk",
        r"\btot de macht (?P<min>min )?(?:(?P<t>" + TELLER + r") )?(?P<n>" + NOEMER + r")n?\b", mb)

    # "tot de macht (min) <getal in woorden>"
    def mg(m):
        e = GETAL[m.group("g").lower()]
        if m.group("min"):
            e = "-" + e
        return "MACHT{" + e + "}"
    zet("macht met getal", r"\btot de macht (?P<min>min )?(?P<g>" + TELLER + r")\b", mg)

    # "tot de <rangtelwoord>"  ->  macht
    zet("tot de rang", r"\btot de (?P<n>" + NOEMER + r")\b",
        lambda m: "MACHT{" + RANG[m.group("n").lower()] + "}")

    # grondtal ervoor: \(a\) MACHT{4}  of  een getalwoord
    def g1(m):
        return r"\(%s^{%s}\)" % (m.group(1), m.group(2))
    zet("grondtal in notatie", r"\\\(([^()]*?)\\\) MACHT\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", g1)

    def g2(m):
        return r"\(%s^{%s}\)" % (GETAL[m.group(1).lower()], m.group(2))
    zet("grondtal in woorden",
        r"\b(" + TELLER + r") MACHT\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", g2)

    def g3(m):
        return r"\((-%s)^{%s}\)" % (GETAL[m.group(1).lower()], m.group(2))
    zet("negatief grondtal",
        r"\b[Mm]in (" + TELLER + r") MACHT\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", g3)

    return t, tel


for pad in sys.argv[1:]:
    t = open(pad, encoding="utf-8").read()
    t, tel = regels(t)
    rest = t.count("MACHT{")
    open(pad, "w", encoding="utf-8").write(t)
    print(pad, tel, "nog los:", rest)

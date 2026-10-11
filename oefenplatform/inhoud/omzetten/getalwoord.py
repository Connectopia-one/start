# -*- coding: utf-8 -*-
"""Leest een getal dat in woorden geschreven staat: "vijfhonderdtwaalf" → 512.

Alleen bedoeld voor de omzetting naar notatie. Geeft None terug als het geen
getal is, zodat de aanroeper de tekst gewoon kan laten staan.
"""
import re

EENHEID = {"nul": 0, "een": 1, "één": 1, "twee": 2, "drie": 3, "vier": 4,
           "vijf": 5, "zes": 6, "zeven": 7, "acht": 8, "negen": 9}
TIENTAL = {"tien": 10, "elf": 11, "twaalf": 12, "dertien": 13, "veertien": 14,
           "vijftien": 15, "zestien": 16, "zeventien": 17, "achttien": 18,
           "negentien": 19, "twintig": 20, "dertig": 30, "veertig": 40,
           "vijftig": 50, "zestig": 60, "zeventig": 70, "tachtig": 80,
           "negentig": 90}
TIENEN = {k: v for k, v in TIENTAL.items() if v >= 20}
WOORDEN = set(EENHEID) | set(TIENTAL) | {"honderd", "duizend", "miljoen"}


def _klein(s):
    """Onder de honderd."""
    if not s:
        return 0
    if s in EENHEID:
        return EENHEID[s]
    if s in TIENTAL:
        return TIENTAL[s]
    for woord, waarde in TIENEN.items():
        if s.endswith(woord) and s[: -len(woord)].endswith("en"):
            kop = s[: -len(woord) - 2]
            if kop in EENHEID:
                return EENHEID[kop] + waarde
    return None


def _honderd(s):
    if "honderd" not in s:
        return _klein(s)
    kop, _, staart = s.partition("honderd")
    k = _klein(kop) if kop else 1
    r = _honderd(staart.strip()) if staart.strip() else 0
    return None if k is None or r is None else k * 100 + r


def _duizend(s):
    if "duizend" not in s:
        return _honderd(s)
    kop, _, staart = s.partition("duizend")
    k = _honderd(kop.strip()) if kop.strip() else 1
    r = _duizend(staart.strip()) if staart.strip() else 0
    return None if k is None or r is None else k * 1000 + r


def naar_getal(tekst):
    """Het getal achter een stuk tekst, of None."""
    s = tekst.strip().lower().replace("­", "")
    if not s or any(c.isdigit() for c in s):
        return None
    if s.endswith(" miljoen") or s == "miljoen":
        kop = s[: -len("miljoen")].strip()
        k = _duizend(kop) if kop else 1
        return None if k is None else k * 1000000
    return _duizend(s)


def schrijf(n):
    """Een geheel getal met zijn groepjes: 20000 → 20\\,000."""
    s, uit = str(n), ""
    while len(s) > 3:
        uit = r"\," + s[-3:] + uit
        s = s[:-3]
    return s + uit


GETALWOORD = re.compile(
    r"\b(?:" + "|".join(sorted(WOORDEN, key=len, reverse=True)) + r")+\b", re.I)

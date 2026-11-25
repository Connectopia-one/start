# -*- coding: utf-8 -*-
"""Bouwstenen voor de uitdagingen in examenvorm (🚀 Boost en 🌍 Beyond).

Dezelfde vormen als bij de pittige hoofdstukken (zie lib/examenvormen.ts).
Elke bron zet MAP = "/examenvormen/<map>" en geeft die door aan klik en met_prent.
Zones staan in procent van de prent: [x, y, breedte, hoogte].
"""
J, F = True, False


def mk(vraag, opties, antwoord, uitleg):
    return {"type": "meerkeuze", "vraag": vraag, "opties": opties, "antwoord": antwoord, "uitleg": uitleg}


def inv(vraag, antwoord, uitleg):
    return {"type": "invultekst", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def tabel(vraag, rijen, uitleg, kolommen=None):
    v = {"type": "tabel", "vraag": vraag, "rijen": [r for r, _ in rijen], "antwoord": [a for _, a in rijen], "uitleg": uitleg}
    if kolommen:
        v["kolommen"] = kolommen
        v["antwoord"] = [kolommen.index(a) if isinstance(a, str) else a for a in v["antwoord"]]
    return v


def keuze(vraag, uitleg):
    return {"type": "keuzelijst", "vraag": vraag, "uitleg": uitleg}


def volgorde(vraag, stappen, uitleg):
    return {"type": "volgorde", "vraag": vraag, "opties": stappen, "uitleg": uitleg}


def koppel(vraag, paren, extra, uitleg):
    return {"type": "koppelen", "vraag": vraag, "paren": paren, "extra": extra, "uitleg": uitleg}


def sorteer(vraag, kolommen, items, uitleg):
    return {"type": "sorteren", "vraag": vraag, "kolommen": kolommen, "items": items, "uitleg": uitleg}


def sleep(vraag, extra, uitleg):
    return {"type": "sleepzin", "vraag": vraag, "extra": extra, "uitleg": uitleg}


def open_(vraag, voorbeeld, uitleg=None):
    v = {"type": "open", "vraag": vraag, "antwoord": voorbeeld}
    if uitleg:
        v["uitleg"] = uitleg
    return v


def casus(tekst, vragen):
    return {"casus": tekst, "vragen": vragen}


def klik(map_, vraag, prent, zones, uitleg):
    return {"type": "hotspot", "vraag": vraag, "afbeelding_url": f"{map_}/{prent}", "zones": zones, "uitleg": uitleg}


def met_prent(map_, prent, vraag):
    vraag["afbeelding_url"] = f"{map_}/{prent}"
    return vraag

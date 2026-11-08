"""Bouwstenen voor de pittige vragen geschiedenis 🌍 Beyond.

Dezelfde vormen als bij geschiedenis ✨ Spark (spark/bron/geschiedenis_examenvormen.py)
en welzijnswetenschappen: zie lib/examenvormen.ts en lib/vraagvorm.ts.

Een prent die Kim nog moet zoeken, krijgt prent_volgt=True. Het bouwscript
laat die vraag dan door, ook al staat de prent nog niet in public/, en de
prentenlijst (maak_prentenlijst.py) zet ze op haar lijst. Pas importeren als
alle prenten er staan.
"""

J, F = True, False
MAP = "/examenvormen/geschiedenis-beyond"


def mk(vraag, opties, antwoord, uitleg):
    return {"type": "meerkeuze", "vraag": vraag, "opties": opties, "antwoord": antwoord, "uitleg": uitleg}


def inv(vraag, antwoord, uitleg):
    return {"type": "invultekst", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def tabel(vraag, rijen, uitleg, kolommen=None):
    v = {"type": "tabel", "vraag": vraag, "rijen": [r for r, _ in rijen], "antwoord": [a for _, a in rijen], "uitleg": uitleg}
    if kolommen:
        v["kolommen"] = kolommen
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


def klik(vraag, prent, zones, uitleg):
    return {"type": "hotspot", "vraag": vraag, "afbeelding_url": f"{MAP}/{prent}", "zones": zones, "uitleg": uitleg}


def met_prent(prent, vraag, volgt=False):
    """Zet een prent boven een vraag. volgt=True: Kim zoekt of maakt ze nog."""
    vraag["afbeelding_url"] = f"{MAP}/{prent}"
    if volgt:
        vraag["prent_volgt"] = True
    return vraag

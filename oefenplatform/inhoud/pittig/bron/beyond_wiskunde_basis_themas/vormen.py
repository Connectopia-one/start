"""Bouwstenen voor de pittige vragen wiskunde basis 🌍 Beyond.

Alle prenten tekent Claude zelf (maak_prenten_wiskunde_basis_beyond.py).

Dezelfde vormen als bij geschiedenis ✨ Spark (spark/bron/geschiedenis_examenvormen.py)
en welzijnswetenschappen: zie lib/examenvormen.ts en lib/vraagvorm.ts.

Een prent die Kim nog moet zoeken, krijgt prent_volgt=True. Het bouwscript
laat die vraag dan door, ook al staat de prent nog niet in public/, en de
prentenlijst (maak_prentenlijst.py) zet ze op haar lijst. Pas importeren als
alle prenten er staan.
"""

J, F = True, False
MAP = "/examenvormen/wiskunde-basis-beyond"


def mk(vraag, opties, antwoord, uitleg):
    return {"type": "meerkeuze", "vraag": vraag, "opties": opties, "antwoord": antwoord, "uitleg": uitleg}


def inv(vraag, antwoord, uitleg):
    return {"type": "invultekst", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def tabel(vraag, rijen, uitleg, kolommen=None):
    v = {"type": "tabel", "vraag": vraag, "rijen": [r for r, _ in rijen], "antwoord": [a for _, a in rijen], "uitleg": uitleg}
    if kolommen:
        v["kolommen"] = kolommen
        # Antwoorden als kolomnummer: een kolom als "630" zou de import anders
        # als kolomnummer 630 lezen (9 november 2026).
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


def klik(vraag, prent, zones, uitleg):
    return {"type": "hotspot", "vraag": vraag, "afbeelding_url": f"{MAP}/{prent}", "zones": zones, "uitleg": uitleg}


def met_prent(prent, vraag, volgt=False):
    """Zet een prent boven een vraag. volgt=True: Kim zoekt of maakt ze nog."""
    vraag["afbeelding_url"] = f"{MAP}/{prent}"
    if volgt:
        vraag["prent_volgt"] = True
    return vraag

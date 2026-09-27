# -*- coding: utf-8 -*-
"""Pakt de pdf's samen in zips: één per vak, en één met alles erin.

    python3 maak_zips.py

Waarom: op /beheer/leerstof kies je een vak en sleep je alle pdf's van dat vak
in één keer naar binnen. Daarvoor moeten ze wel op je eigen computer staan, en
ze stuk voor stuk downloaden is een avond werk.

Waarom ook per vak, en niet alleen alles samen: Kim vroeg dat op 27 september
2026, zodat ze een vak al kan opladen terwijl er aan het volgende gewerkt wordt,
zonder telkens alles opnieuw te moeten halen.

In elke zip zit per vak een map, ook in een zip van één vak. Zo kan je twee
zips naast elkaar uitpakken zonder dat de bestanden door elkaar lopen.

De zips worden opnieuw gemaakt door maak_alles.py, zodat ze nooit achterlopen
op de pdf's ernaast.
"""
import pathlib, zipfile

HIER = pathlib.Path(__file__).parent
WORTEL = HIER.parent.parent                      # inhoud/

SOORTEN = [
    ("leerbundels", WORTEL / "leerbundels", "alle-leerbundels.zip"),
    ("oefenbundels", WORTEL / "oefenbundels", "alle-oefenbundels.zip"),
]


def _schrijf(doel, pdfs):
    with zipfile.ZipFile(doel, "w", zipfile.ZIP_DEFLATED) as z:
        for p in pdfs:
            z.write(p, f"{p.parent.name}/{p.name}")
    return doel.stat().st_size / 1024 / 1024


def maak(map_, zipnaam):
    """Eén zip per vak, plus één met alles erin. Geeft de regels terug."""
    # bron/ staat vol met tussenbestanden en hoort er niet in
    vakken = sorted(m for m in map_.iterdir() if m.is_dir() and m.name != "bron")
    regels = []
    alles = []
    for vak in vakken:
        pdfs = sorted(vak.glob("*.pdf"))
        if not pdfs:
            continue
        alles += pdfs
        mb = _schrijf(map_ / f"{vak.name}.zip", pdfs)
        regels.append(f"{map_.name}/{vak.name}.zip: {len(pdfs)} pdf, {mb:.1f} MB")
    if alles:
        mb = _schrijf(map_ / zipnaam, alles)
        regels.append(f"{map_.name}/{zipnaam}: {len(alles)} pdf, {mb:.1f} MB")
    return regels


def main():
    for naam, map_, zipnaam in SOORTEN:
        if not map_.exists():
            continue
        regels = maak(map_, zipnaam)
        if not regels:
            print(f"{naam}: niets gevonden")
        for r in regels:
            print(" ", r)


if __name__ == "__main__":
    main()

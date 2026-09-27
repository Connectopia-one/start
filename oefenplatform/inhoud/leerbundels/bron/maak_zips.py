# -*- coding: utf-8 -*-
"""Pakt alle pdf's samen in één zip per soort bundel.

    python3 maak_zips.py

Waarom: op /beheer/leerstof kies je een vak en sleep je alle pdf's van dat vak
in één keer naar binnen. Daarvoor moeten ze wel op je eigen computer staan, en
ze stuk voor stuk downloaden is een avond werk. In de zip zit per vak een map,
dus je downloadt één keer, pakt uit, en sleept per vak die map leeg.

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


def maak(map_, zipnaam):
    # bron/ staat vol met tussenbestanden en hoort er niet in
    pdfs = sorted(p for p in map_.glob("*/*.pdf") if p.parent.name != "bron")
    if not pdfs:
        return None
    doel = map_ / zipnaam
    with zipfile.ZipFile(doel, "w", zipfile.ZIP_DEFLATED) as z:
        for p in pdfs:
            z.write(p, f"{p.parent.name}/{p.name}")
    return doel, len(pdfs)


def main():
    for naam, map_, zipnaam in SOORTEN:
        if not map_.exists():
            continue
        uit = maak(map_, zipnaam)
        if not uit:
            print(f"{naam}: niets gevonden")
            continue
        doel, aantal = uit
        mb = doel.stat().st_size / 1024 / 1024
        print(f"{doel.relative_to(WORTEL)}: {aantal} pdf, {mb:.1f} MB")


if __name__ == "__main__":
    main()

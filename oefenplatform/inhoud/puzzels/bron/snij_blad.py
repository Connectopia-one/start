#!/usr/bin/env python3
"""
Snijdt een contactblad met prenten in losse prenten.

Kim laat ChatGPT één beeld maken met alle hoofdstukken van een vak erop, naast
elkaar op een crème achtergrond. Dit script zoekt de vakjes en zet ze apart.

    python3 inhoud/puzzels/bron/snij_blad.py <blad.png> <map om in te zetten>

De prenten komen eruit als 01.png, 02.png ... in leesvolgorde (van links naar
rechts, van boven naar onder). Hernoem ze daarna naar de titel van het
hoofdstuk en laat maak_puzzelfotos.py erover gaan.

Het zoeken gebeurt met een projectie: een rij (of kolom) die bijna helemaal de
kleur van de rand heeft, is een scheiding. Dat werkt ook als de vakjes niet
allemaal even breed of even hoog zijn.
"""

import sys
from pathlib import Path

import numpy as np
from PIL import Image

RAND = 6  # pixels die we van elke kant nog wegnemen, tegen een crème randje
MINZIJDE = 60


def stukken(masker: np.ndarray, drempel: float) -> list[tuple[int, int]]:
    """Van een rij ja/nee-waarden naar de blokken die 'nee' (= inhoud) zijn."""
    achtergrond = masker >= drempel
    uit, begin = [], None
    for i, leeg in enumerate(achtergrond):
        if not leeg and begin is None:
            begin = i
        elif leeg and begin is not None:
            uit.append((begin, i))
            begin = None
    if begin is not None:
        uit.append((begin, len(achtergrond)))
    return uit


def snij(blad: Path, uit: Path) -> None:
    beeld = Image.open(blad).convert("RGB")
    punten = np.asarray(beeld, dtype=np.int16)
    # De kleur van de rand: de hoek van het blad. De marge staat ruim, want de
    # crème tussen de vakjes is net iets lichter dan die aan de rand.
    rand = punten[2, 2]
    verschil = np.abs(punten - rand).sum(axis=2)
    isRand = verschil < 70  # True waar het achtergrond is

    uit.mkdir(parents=True, exist_ok=True)
    nummer = 0
    for boven, onder in stukken(isRand.mean(axis=1), 0.97):
        if onder - boven < MINZIJDE:
            continue
        band = isRand[boven:onder]
        for links, rechts in stukken(band.mean(axis=0), 0.97):
            if rechts - links < MINZIJDE:
                continue
            nummer += 1
            vak = beeld.crop((links + RAND, boven + RAND, rechts - RAND, onder - RAND))
            naam = uit / f"{nummer:02d}.png"
            vak.save(naam)
            print(f"  {naam.name}  {vak.width}x{vak.height}")
    print(f"{nummer} prent(en) uit {blad.name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        raise SystemExit(1)
    snij(Path(sys.argv[1]), Path(sys.argv[2]))

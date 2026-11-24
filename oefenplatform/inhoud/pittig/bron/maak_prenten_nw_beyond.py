"""Tekent de eigen prenten voor de pittige vragen natuurwetenschappen 🌍 Beyond doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_nw_beyond.py

De meeste klikvragen gebruiken de prenten van biologie, chemie en fysica
Beyond. Enkel de thema's zonder passende prent tekenen hier hun eigen prent
(beyond_nw_themas/prent.py).
"""
import pathlib
import sys

# Als pakket "bron" laden: de thema's halen vragen uit de pakketten van
# biologie, chemie en fysica met een relatieve import.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.beyond_natuurwetenschappen  # noqa: E402,F401  (laadt alle thema's)
from bron.beyond_nw_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "natuurwetenschappen-beyond"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)

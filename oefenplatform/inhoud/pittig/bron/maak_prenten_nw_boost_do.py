"""Tekent de prenten voor de pittige vragen natuurwetenschappen 🚀 Boost doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_nw_boost_do.py

Alles is eigen tekenwerk (boost_do_nw_themas/prent.py), Kim hoeft niets te zoeken.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import boost_do_natuurwetenschappen  # noqa: E402,F401  (laadt alle thema's)
from boost_do_nw_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "natuurwetenschappen-boost-do"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)

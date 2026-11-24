"""Tekent de prenten voor de pittige vragen aardrijkskunde 🚀 Boost (doorstroom en dubbele finaliteit).

    python3 inhoud/pittig/bron/maak_prenten_ak_boost.py

Gradennet, kaart, histogrammen, landschap, sferen en digitale kaart: alles
eigen tekenwerk (boost_ak_themas/prent.py), voor doorstroom en dubbele finaliteit.
"""
import pathlib
import sys

# Als pakket "bron" laden, net als de andere vakken.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.boost_do_aardrijkskunde  # noqa: E402,F401  (laadt alle thema's)
from bron.boost_ak_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "aardrijkskunde-boost"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)

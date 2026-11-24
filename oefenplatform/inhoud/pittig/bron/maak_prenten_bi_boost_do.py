"""Tekent de prenten voor de pittige vragen biologie 🚀 Boost doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_bi_boost_do.py

De meeste klikvragen gebruiken de prenten van natuurwetenschappen Boost
doorstroom. Enkel het oor is eigen tekenwerk (boost_do_bi_themas/prent.py).
"""
import pathlib
import sys

# Als pakket "bron" laden: de thema's halen vragen uit het pakket van
# natuurwetenschappen Boost doorstroom met een relatieve import.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.boost_do_biologie  # noqa: E402,F401  (laadt alle thema's)
from bron.boost_do_bi_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "biologie-boost-do"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)

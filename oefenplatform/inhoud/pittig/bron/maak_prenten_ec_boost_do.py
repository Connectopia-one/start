"""Tekent de prenten voor de pittige vragen economie 🚀 Boost doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_ec_boost_do.py

Kringloop, grafieken, balans, factuur en SWOT: alles eigen tekenwerk
(boost_ec_themas/prent.py).
"""
import pathlib
import sys

# Als pakket "bron" laden, net als de andere vakken.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.boost_do_economie  # noqa: E402,F401  (laadt alle thema's)
from bron.boost_ec_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "economie-boost-do"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)

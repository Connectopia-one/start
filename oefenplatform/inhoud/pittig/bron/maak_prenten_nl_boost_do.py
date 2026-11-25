"""Tekent de prenten voor de pittige vragen Nederlands 🚀 Boost doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_nl_boost_do.py

Communicatiemodel, verdacht bericht, zin in blokjes, zin in zinsdelen en
spanningsboog: alles eigen tekenwerk (boost_do_nl_themas/prent.py).
"""
import pathlib
import sys

# Als pakket "bron" laden, net als de andere vakken.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.boost_do_nederlands  # noqa: E402,F401  (laadt alle thema's)
from bron.boost_do_nl_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "nederlands-boost-do"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)

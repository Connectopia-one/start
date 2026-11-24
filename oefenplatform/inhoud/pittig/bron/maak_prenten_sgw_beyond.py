"""Tekent de eigen prenten voor de pittige vragen sociale en gedragswetenschappen 🌍 Beyond doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_se_beyond.py

Grafieken en schermafdrukken die de thema's zelf tekenen
(beyond_sgw_themas/prent.py).
"""
import pathlib
import sys

# Als pakket "bron" laden, net als het bouwscript.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import bron.beyond_sgw  # noqa: E402,F401  (laadt alle thema's)
from bron.beyond_sgw_themas.prent import ALLE  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "sgw-beyond"
UIT.mkdir(parents=True, exist_ok=True)
for p in ALLE:
    (UIT / p.bestand).write_text(p.tekening(), encoding="utf-8")
print(len(ALLE), "prenten in", UIT)
